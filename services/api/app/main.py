import sys
from contextlib import asynccontextmanager
from pathlib import Path
from uuid import uuid4

# Ensure services/api directory is on sys.path for app module imports
_api_dir = str(Path(__file__).resolve().parent.parent)
if _api_dir not in sys.path:
    sys.path.insert(0, _api_dir)

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import text

from app.auth.router import router as auth_router
from app.core.config import get_settings
from app.db.session import engine
from app.organizations.router import router as organizations_router

settings = get_settings()


@asynccontextmanager
async def lifespan(_: FastAPI):
    yield
    await engine.dispose()


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="Enterprise knowledge intelligence and controlled agentic workflows.",
    lifespan=lifespan,
    docs_url="/docs" if not settings.is_production else None,
    redoc_url=None,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["Authorization", "Content-Type", "X-Request-ID"],
)


@app.middleware("http")
async def request_context(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID") or str(uuid4())
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return response


@app.exception_handler(Exception)
async def unexpected_error_handler(_: Request, exc: Exception):
    # Detailed exception data belongs in protected server logs, never in API responses.
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})


@app.get("/health/live", tags=["health"])
async def liveness() -> dict[str, str]:
    return {"status": "alive"}


@app.get("/health/ready", tags=["health"])
async def readiness() -> dict[str, str]:
    async with engine.connect() as connection:
        await connection.execute(text("SELECT 1"))
    return {"status": "ready", "database": "connected"}


app.include_router(auth_router, prefix=settings.api_v1_prefix)
app.include_router(organizations_router, prefix=settings.api_v1_prefix)
