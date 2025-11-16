# How I Actually Use MCP Servers Every Day

In this post, I’ll walk through:

- **Which clients I use MCP with** and what each is good at.
- **My favorite MCP servers** and how they actually help with code, research, and knowledge work.

Think of this as an opinionated field guide: not the theory of MCP, but how it actually fits into a working developer’s stack.

---

## How MCP Fits Into My Daily Workflow

Once I configure a server, it becomes part of my **personal AI toolkit**. The same tools are available in multiple places, so I choose the client based on the kind of work I’m doing—not on which model happens to support what.

Here’s how that breaks down.

### GitHub Copilot: My Coding Cockpit

Most of my hands‑on work happens in VS Code and **GitHub Copilot** is my main MCP client.

Github Copilot allows me to:

- Combine multiple models (ChatGPT, Claude, Gemini, Grok, etc.) for different tasks.
- Pair with vibe-coding archetypes (will dive into this in a future post) and MCP tools.
- Perform a variety of coding related tasks, from planning features, to writing and fixing code, generating tests, and updating documentation, drafting commit messages, and more.
- I often find myself usign Github Copilot for non-coding tasks as well, mainly through its MCP integrations - for example, I use it to organize my folders and apply naming conventions [TODO](add 1-2 more trivial examples) more on this in the next section.

### Claude: Wide‑Angle Reasoning and Longform Work

On desktop, **Claude** is my go‑to for broader thinking:

- **Research and synthesis** across multiple sources.
- **Documentation passes**, like rewriting README files or crafting design docs.
- **Higher‑level reasoning**, where I want narrative, structure, and tradeoff analysis.

The free tier is limited, but when I do use it with MCP, I get the same sources and tools I use in VS Code—just through a wider, more narrative‑friendly lens.

### ChatGPT: Generalist Workhorse, Now with MCP

I’ve been a paid **ChatGPT** user since the early days, and it still handles a lot of my generic workflows:

- Writing and editing emails.
- Quick coding tasks and experiments.
- Brainstorming, planning, and outlining.

For a while, it lagged behind Claude in MCP support. With the more recent MCP integration, it’s finally catching up:

- I can **tap into the same MCP servers** I use elsewhere.
- I can **pull in code, docs, and research sources** instead of manually copy‑pasting.

It still has some rough edges on the MCP side, but it’s gotten to the point where it’s genuinely useful instead of experimental.

### Warp Terminal: MCP for Shell‑Centric Workflows

Sometimes I want to stay close to the command line. **Warp Terminal** with MCP lets me:

- Use AI to **reason about shell commands**, scripts, and logs.
- Ask questions about **project files and outputs** right where they’re generated.
- Keep the same MCP servers available in a terminal‑first environment.

This is especially handy for debugging sessions, log spelunking, or quick data transformations where bouncing back and forth between a browser and terminal would be annoying.

---

## The MCP Servers I Rely on Most

Now let’s talk about the servers themselves. While there are countless MCP servers out there, I keep coming back to two broad categories:

1. **Documentation & Codebase Assistance**
2. **Research & Knowledge Work**

These cover most of my day‑to‑day needs as a developer who also spends a lot of time reading, writing, and synthesizing information.

---

## 1. Documentation & Codebase Assistance

The core idea here: I want the model to **really understand my project**, not just the one file I pasted in. MCP servers that expose files, docs, and structure turn the AI into a collaborator instead of a snippet generator.

### Filesystem / Repo Browsers

These servers give the AI a window into the repo:

- Let the model **inspect your project structure**, not just one file.
- Answer questions about **how modules connect**, where things live, and how data flows.
- Propose and generate **refactors that touch multiple files**.

In practice, I use them to:

- Ask things like "Where is the real entrypoint for this feature?" or "What code handles authentication?".
- Get **mermaid diagrams** or architectural overviews for large, unfamiliar codebases.
- Navigate and explore whole projects quickly when I’m onboarding or context‑switching.

### Docs Servers

Docs servers index local Markdown, API docs, or wikis and make them queryable via MCP:

- **README and architecture docs** sitting in the repo.
- **API references** or protocol specs.
- Internal **runbooks** or onboarding documentation.

They’re invaluable for:

- Turning "tribal knowledge" into something the AI can surface.
- Cross‑linking **code and documentation**—"Show me docs relevant to this function".
- Generating **new docs** that match the tone and structure of existing ones.

### What I Actually Do with These Servers

Once the model can see both code and docs, a lot of workflows become natural:

- **Improve code documentation**
  - Walk through files and add or refine docstrings.
  - Add function signatures and type hints where they’re missing.
  - Add short module summaries at the top of important files.

- **Refactor code with confidence**
  - Suggest and implement code improvements and optimizations.
  - Restructure modules based on best practices.
  - Keep style consistent across the repo.

- **Explain complex logic and architectures**
  - Have the AI explain **entire subsystems**, not just a function.
  - Ask it to **identify entrypoints and dependencies**.
  - Generate **sequence diagrams or mermaid flows** to visualize control paths.

- **Boost onboarding and knowledge transfer**
  - Use the AI to create **guided tours of the codebase**.
  - Generate concise summaries for new team members.
  - Capture Q&A into docs so the next person doesn’t have to ask.

- **Generate tests and confidence**
  - Create unit tests, integration tests, and end‑to‑end tests.
  - Focus first on **edge cases and failure scenarios** uncovered during refactors.

- **Generate and maintain documentation**
  - Draft or update READMEs, API docs, and user guides.
  - Keep narrative docs in sync with fast‑moving code.

Some specialized helpers I like in this space:

- **Context7** – for rich project‑wide context and documentation workflows.
- **Sequential Thinking MCP** – to force deeper, step‑by‑step reasoning on complex problems instead of shallow answers.

---

## 2. Research & Knowledge Work

Beyond code, MCP shines when you treat your research stack as just another set of servers. Instead of forcing everything into a single app, you **bring your tools into the agent**.

### Zotero MCP: Turning a Library into a Knowledge Base

**ZoteroMCP** connects my Zotero library directly to my AI assistants. This is a big upgrade over clunky "AI inside Zotero" experiments.

What it gives me:

- Access to my **entire Zotero library** from any MCP‑aware client.
- The ability to:
  - Summarize papers.
  - Extract key points and arguments.
  - Compare articles or perspectives.
  - Generate citations and bibliographies.

The key shift is architectural: instead of dragging the agent **into** Zotero, I bring **Zotero into the agent**. That means I can:

- Combine paper summaries with **code analysis** in the same session.
- Feed insights into **documentation, design docs, or blog posts**.
- Chain Zotero with other servers (like Notion or NotebookLM) for downstream workflows.

### NotebookLM MCP: Structured AI Workspaces as a Service

With **NotebookLM MCP** (see the implementation at `https://github.com/PleasePrompto/notebooklm-mcp`), NotebookLM becomes another node in the workflow rather than a separate island.

Some things this enables:

- Extract certain items or highlights from sources and **automatically upload them to NotebookLM**.
- Have the AI **create structured documents** in NotebookLM based on research sessions.
- Use GitHub Copilot or other clients to **generate code that preprocesses research data**, then push the results to NotebookLM via MCP.

This is where the "orchestrate multiple tools" side of MCP really starts to shine.

### Notion MCP: The Meta‑Layer for Ideas and Planning

My **Notion MCP** setup is the meta‑layer over everything else:

- Track **papers I’ve reviewed** and what I thought about them.
- Maintain **project notes, ideas, and next actions**.
- Keep a living log of experiments and decisions.

Because it’s exposed via MCP, I can:

- Turn YouTube/video summaries into Notion pages.
- Tie research notes to **specific code changes or experiments**.
- Ask the AI to surface "What did I say last time about this topic?".

### YouTube MCP: Taming the Firehose

YouTube is one of the most important learning channels today—and also one of the messiest.

A **YouTube MCP server** helps me:

- **Manage playlists** more sanely:
  - Add, remove, and reorder items.
  - Keep a clean, up‑to‑date library of learning resources.

- **Extract real knowledge from videos**:
  - Pull transcripts or key points.
  - Summarize long videos into digestible notes.
  - Combine video summaries with other tools:
    - Create Notion pages with key takeaways.
    - Generate PDF summaries.
    - Push structured content into NotebookLM, ChatGPT, or Claude.

Again, the pattern repeats: bring YouTube **to the agent**, don’t move your entire workflow into YouTube.

### PDF MCP: Building Meta‑Documents

Finally, **PDF MCP** servers are my glue layer when I need to compile or synthesize across sources:

- Combine information from **multiple PDFs** (papers, specs, reports).
- Create **meta‑documents** that weave together insights from different places.
- Export clean, sharable outputs for colleagues or future me.

This is especially useful when I’m:

- Comparing competing proposals or standards.
- Distilling a messy set of resources into a single narrative.
- Preparing teaching material, talks, or blog posts.

---

## Why MCP Changed How I Think About AI Tools

The main shift MCP brought to my workflow is this:

> I no longer think in terms of "which AI app should I use?" but **"which clients and servers make sense for this task?"**

- Clients (Copilot, Claude, ChatGPT, Warp) are just **different frontends** tuned for different contexts: coding, longform writing, quick chats, or terminal work.
- Servers (filesystem, docs, Zotero, NotebookLM, Notion, YouTube, PDF, etc.) are **reusable capabilities** I can wire into any of those frontends.

When you set things up this way, your AI experience stops feeling like isolated assistants and starts feeling like one coherent system:

- Your **code and docs** are always available.
- Your **research library** is never more than a prompt away.
- Your **notes, playlists, and PDFs** can actually talk to each other.

That’s the real power of MCP in my daily workflow—not a single killer feature, but a quiet unification of all the tools I was already using.
