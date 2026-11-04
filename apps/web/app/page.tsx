import { Activity, ArrowUpRight, BookOpen, Bot, Database, FileSearch, Files, Gauge, LockKeyhole, Network, Plus, Search, ShieldCheck, Sparkles } from "lucide-react";

const nav = [
  { label: "Overview", icon: Gauge, active: true },
  { label: "Knowledge library", icon: BookOpen },
  { label: "AI workspace", icon: Sparkles },
  { label: "Agent runs", icon: Network },
  { label: "Analytics", icon: Activity },
  { label: "Evaluations", icon: ShieldCheck },
];

function Metric({ label, value, detail, icon: Icon }: { label: string; value: string; detail: string; icon: typeof Files }) {
  return <div className="rounded-xl border border-[var(--line)] bg-[var(--panel)] p-5">
    <div className="flex items-center justify-between text-sm text-[#9ba9ba]"><span>{label}</span><Icon size={17} /></div>
    <div className="mt-4 text-3xl font-semibold tracking-tight">{value}</div>
    <div className="mt-2 text-xs text-[#8290a2]">{detail}</div>
  </div>;
}

export default function Home() {
  return <div className="min-h-screen md:flex">
    <aside className="flex w-full flex-col border-b border-[var(--line)] bg-[#0c121c] md:min-h-screen md:w-[248px] md:border-r md:border-b-0">
      <div className="flex items-center gap-3 px-6 py-6"><div className="flex h-9 w-9 items-center justify-center rounded-xl border border-[#31445e] bg-[#17263a]"><Network size={19} className="text-[#a7c7ff]" /></div><div><div className="font-semibold tracking-[.16em]">NEXUS<span className="text-[#a7c7ff]"> AI</span></div><div className="text-[10px] tracking-[.18em] text-[#8290a2]">KNOWLEDGE SYSTEMS</div></div></div>
      <div className="mx-4 rounded-lg border border-[var(--line)] bg-[#111a27] px-3 py-3"><div className="text-xs text-[#8290a2]">WORKSPACE</div><div className="mt-1 flex items-center justify-between text-sm">Local development <span className="text-[#8290a2]">⌄</span></div></div>
      <nav className="flex gap-1 overflow-x-auto px-3 py-5 md:flex-col">{nav.map(({ label, icon: Icon, active }) => <div key={label} aria-current={active ? "page" : undefined} className={`flex shrink-0 items-center gap-3 rounded-lg px-3 py-2.5 text-sm ${active ? "border border-[#293b53] bg-[#17263a] text-[#dbe8fa]" : "text-[#98a5b5]"}`}><Icon size={17} />{label}</div>)}</nav>
      <div className="mt-auto hidden p-4 md:block"><div className="rounded-xl border border-[var(--line)] bg-[#101722] p-4"><div className="flex items-center gap-2 text-xs font-medium"><LockKeyhole size={14} className="text-[#a7c7ff]" /> PRIVATE WORKSPACE</div><p className="mt-2 text-xs leading-5 text-[#8290a2]">Organization-scoped access controls are enforced by the API.</p></div></div>
    </aside>
    <main className="min-w-0 flex-1">
      <header className="flex flex-wrap items-center justify-between gap-4 border-b border-[var(--line)] px-6 py-5 md:px-9"><div><div className="text-xs text-[#8290a2]">WORKSPACE / OVERVIEW</div><h1 className="mt-1 text-xl font-semibold">Enterprise intelligence</h1></div><div className="flex items-center gap-3"><div className="hidden items-center gap-2 rounded-lg border border-[var(--line)] px-3 py-2 text-xs text-[#8290a2] sm:flex"><Search size={14} /> Search workspace <span className="ml-5">⌘ K</span></div><div className="rounded-lg border border-[var(--line)] px-3 py-2 text-xs text-[#aeb9c7]">Local · Not connected</div></div></header>
      <div className="mx-auto max-w-[1400px] space-y-7 p-6 md:p-9">
        <section className="flex flex-wrap items-end justify-between gap-4"><div><div className="text-sm text-[#a7c7ff]">SYSTEM INITIALIZATION</div><h2 className="mt-2 text-2xl font-semibold tracking-tight md:text-3xl">Your knowledge, connected.</h2><p className="mt-2 max-w-2xl text-sm leading-6 text-[#98a5b5]">A controlled intelligence layer for enterprise documents, structured data and agentic workflows. Start by configuring the platform and adding a knowledge source.</p></div><a href="#setup" className="inline-flex items-center gap-2 rounded-lg bg-[#dce9fb] px-4 py-2.5 text-sm font-semibold text-[#142033] hover:bg-white"><Plus size={16} /> Configure workspace</a></section>
        <section className="grid gap-4 sm:grid-cols-2 xl:grid-cols-4"><Metric label="Indexed documents" value="—" detail="No documents ingested yet" icon={Files} /><Metric label="Knowledge chunks" value="—" detail="Available after indexing" icon={Database} /><Metric label="Agent executions" value="—" detail="No workflow runs recorded" icon={Bot} /><Metric label="System health" value="Unverified" detail="Connect the API and database" icon={Activity} /></section>
        <section className="grid gap-5 xl:grid-cols-[1.4fr_1fr]">
          <div className="rounded-xl border border-[var(--line)] bg-[var(--panel)] p-6"><div className="flex items-center justify-between"><div><h3 className="font-semibold">Knowledge workspace</h3><p className="mt-1 text-xs text-[#8290a2]">Document ingestion and evidence retrieval</p></div><FileSearch size={19} className="text-[#a7c7ff]" /></div><div className="mt-6 rounded-xl border border-dashed border-[#344357] bg-[#0c131e] px-5 py-12 text-center"><div className="mx-auto flex h-11 w-11 items-center justify-center rounded-xl bg-[#19283b]"><Files size={20} className="text-[#a7c7ff]" /></div><p className="mt-4 text-sm font-medium">No knowledge sources yet</p><p className="mx-auto mt-2 max-w-sm text-xs leading-5 text-[#8290a2]">Your documents will appear here after secure upload, parsing, chunking, embedding and indexing are implemented.</p><span className="mt-4 inline-flex rounded-lg border border-[var(--line)] px-3 py-2 text-xs text-[#aeb9c7]">Ingestion module · Planned</span></div></div>
          <div className="rounded-xl border border-[var(--line)] bg-[var(--panel)] p-6"><div className="flex items-center justify-between"><div><h3 className="font-semibold">Platform readiness</h3><p className="mt-1 text-xs text-[#8290a2]">Initial foundation checklist</p></div><ShieldCheck size={19} className="text-[#a7c7ff]" /></div><div className="mt-6 space-y-4">{[{name:"Application structure",state:"Created"},{name:"Authentication foundation",state:"Implemented"},{name:"Tenant membership checks",state:"Implemented"},{name:"Database migrations",state:"Pending"},{name:"Gemini provider",state:"Not configured"},{name:"Advanced RAG pipeline",state:"Planned"}].map((item) => <div key={item.name} className="flex items-center justify-between gap-3 border-b border-[var(--line)] pb-3 last:border-0"><span className="text-sm text-[#c7d0dc]">{item.name}</span><span className={`text-[11px] ${item.state === "Implemented" || item.state === "Created" ? "text-[#9bc6a7]" : "text-[#9aa6b5]"}`}>{item.state}</span></div>)}</div></div>
        </section>
        <section id="setup" className="rounded-xl border border-[var(--line)] bg-[#101722] p-6"><div className="flex items-center gap-2 text-sm font-semibold"><ArrowUpRight size={16} className="text-[#a7c7ff]" /> Next engineering milestone</div><p className="mt-2 text-sm leading-6 text-[#98a5b5]">Complete database migrations and integration tests, then implement secure document ingestion as the first end-to-end AI workflow. No demo metrics or generated answers are presented as real data.</p></section>
        <footer className="flex flex-wrap items-center justify-between gap-2 border-t border-[var(--line)] pt-5 text-[11px] text-[#6f7e90]"><span>NEXUS AI · Engineering preview · v0.1.0</span><span>Evidence first. Permissions always.</span></footer>
      </div>
    </main>
  </div>;
}
