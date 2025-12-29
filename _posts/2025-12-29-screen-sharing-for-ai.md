---
title: "Screen-sharing for AI"
date: '2025-12-29T10:00:00+01:00'
author: Anne
layout: post
tags:
  - '2025'
  - 'weeknotes'
---

A few weeks ago I built [claude-threads](https://github.com/anneschuth/claude-threads), a tool that bridges Claude Code and Mattermost. The tagline: "Think of it as screen-sharing for AI pair programming, but everyone can type."

You @mention a bot in a chat channel. It spawns a Claude Code session on your machine. Everything streams live to a Mattermost thread—Claude's responses, code diffs, task lists, permission requests. Colleagues can watch. They can jump in. They can run their own sessions in parallel.

It's published on npm. The code is on GitHub. MIT licensed. Anyone can use it.

This post is about what I learned building it, why I'm sharing it openly, and what it means for how we work with AI.

## Building with AI to collaborate with AI

The irony isn't lost on me: I built this tool _with_ Claude Code. A tool to make Claude Code collaborative, built by collaborating with Claude Code.

[In October](/2025/10/21/praten.html) I wrote about building an app by talking to my computer. 38,000 lines of code I didn't write myself. This was similar, but different. About 3,000 lines of TypeScript. Not a mobile app this time, but a bot that manages concurrent sessions, handles WebSocket connections, formats diffs, streams responses, manages git worktrees.

I don't know Node.js particularly well. I haven't written a Mattermost bot before. I've never built an MCP server. But I know what I wanted: transparent AI collaboration that feels like everyone's in the room together, even when they're not.

Claude Code and I figured out the rest.

## The mechanics of transparency

Traditional pair programming has a problem: only one person drives. The other watches, comments, occasionally takes the keyboard. It's intimate but exclusive.

Screen-sharing scales this up—multiple people can watch. But it's still one-way. The driver drives. Everyone else is passive.

Claude Code sessions have a different problem: they're invisible. You're having a conversation with an AI on your machine. Your colleague asks "what are you working on?" You paste some output in Slack. They lose context. The conversation fragments.

claude-threads changes this. The bot becomes the shared screen. Every message, every code change, every task update appears in real-time. Not as a recording or summary, but as it happens.

But unlike screen-sharing, it's not passive. Anyone in the thread can see exactly what Claude is doing. They can ask questions. They can suggest different approaches. They can fork the conversation into their own session.

The session owner can `!invite` specific people. Others can request permission to participate. Everything is visible, but controlled.

## What it actually looks like

A colleague @mentions the bot: "help me add authentication to the user service"

A new thread appears. Claude starts exploring the codebase. The thread updates:
- Reading `src/services/user.ts`
- Searching for existing auth patterns
- Creating a task list

The tasks show up in the thread:
- 🔄 Analyzing current authentication approach
- ⬜ Implementing JWT token generation
- ⬜ Adding middleware for route protection
- ⬜ Writing tests

Code changes appear as diffs—red lines removed, green lines added. Not full files, just what changed.

When Claude wants to run a command, a permission prompt appears: "⚠️ Permission requested: Run `npm test`"

React with 👍 to approve. Or ✅ to approve everything this session. Or 👎 to deny.

Another colleague watching the thread notices a problem: "wait, we're using refresh tokens too"

The session owner invites them: `!invite @colleague`

Now they can participate directly. The knowledge stays in the thread. The context is shared.

## Working open as default

I could have kept this private. Built it for my own use. Maybe shared it with a few colleagues.

Instead it's on GitHub. Public from day one.

Why?

First, because [making over talking](/2025/04/11/maken-over-schrijven.html). I write about how government should build prototypes, share demos, work transparently. This is that principle in practice. Not just describing what could be built, but building it and sharing how.

Second, because tools for collaboration should themselves be collaborative. If claude-threads helps teams work together with AI, it should be built in a way that others can contribute to, learn from, fork, improve.

Third, because working in the open creates accountability. The code is there. The decisions are visible. The trade-offs are documented. Anyone can see not just what it does, but how it does it and why.

Fourth, because [digital sovereignty](/2025/11/28/makelaar-of-maker.html) matters. When I wrote about "1 cloud is no cloud," I was talking about vendor lock-in. The same principle applies to AI tools. If your entire workflow depends on one vendor's chat interface, you're stuck. Open tools create options.

## The fear of rough edges

There's a hesitation around sharing unfinished work. Especially in government contexts, where I spend most of my time.

Everything must be polished. Documented. Approved. Presented as complete.

But this creates a paradox: by the time something is "ready to share," it's often too late to incorporate feedback. The decisions are made. The architecture is set. The abstraction is locked in.

claude-threads has rough edges. The error handling could be better. Some features are half-implemented. The documentation makes assumptions about what you already know.

But it works. People use it. They file issues. They suggest improvements. Some have contributed code.

The rough edges are where collaboration happens. Polish can come later.

## What's possible when AI becomes transparent

[Earlier I wrote](/2025/05/02/demo.html) about how demos speak louder than documents. A working prototype changes conversations from "what if" to "what now."

But there's another shift happening: from solo prototyping to collaborative exploration.

When I build something with Claude Code privately, I'm exploring a possibility space. Trying ideas. Hitting dead ends. Finding what works.

When that exploration is visible—when others can watch, suggest, participate—the possibility space expands.

Someone watching my session might notice: "actually, we tried that approach last month and hit a scaling issue." Another might suggest: "what if you used this library instead?" A third might fork a different direction entirely.

The AI amplifies this. It can explore paths faster than I can. But the judgment—which paths are worth exploring, which trade-offs matter—that still requires human context. Multiple humans, with different perspectives, different experiences, different priorities.

Making AI collaboration transparent doesn't just help us work faster. It helps us work smarter.

## The paradox of AI tools

Here's something I keep thinking about: we're building tools to make AI more useful, while AI makes building those tools easier.

It's a feedback loop. AI helps me build claude-threads. claude-threads makes AI more collaborative. Better collaboration means better use of AI. Better use means we discover what other tools we need. AI helps us build those too.

This accelerates. Not in a scary singularity way. In a practical "wait, we could just build that" way.

The [erosion effect](/2025/12/27/ai-erodeert.html) I wrote about—AI making rugged terrain navigable—applies to building AI tools themselves.

Five years ago, building a Mattermost bot that manages concurrent Claude sessions, each with its own MCP server, handling permission prompts via emoji reactions, streaming diffs in real-time... that would have been a substantial project.

Last month it took a few days. Most of that time was figuring out what I actually wanted, not how to implement it.

## Why this matters for government

I keep coming back to government because that's where I work. But also because that's where this matters most.

Government technology is often built behind closed doors. Large contracts. Waterfall processes. Long specifications. Implementations that take years.

What if instead:
- Policy teams could watch engineers explore solutions in real-time
- Engineers could see policymakers refine requirements as prototypes emerge
- Different departments could learn from each other's sessions
- Citizens could see how their government actually builds things

Not all of it—some things need privacy. But the default could shift. From closed by default to open where possible.

claude-threads is a small tool. It doesn't solve these big problems. But it demonstrates a possibility: making AI collaboration transparent, participatory, and open.

The technology exists. The question is whether we choose to use it this way.

## The maintenance question

One concern people raise: "what happens when you move on?"

Fair question. Open source has a sustainability problem. Maintainers burn out. Projects get abandoned. Dependencies break.

I don't have a perfect answer. But I have a few thoughts:

First, the tool is small enough that anyone who knows TypeScript can understand it. The [CLAUDE.md](https://github.com/anneschuth/claude-threads/blob/main/CLAUDE.md) file explains the architecture. The code is straightforward.

Second, it's designed to be forkable. MIT license. No proprietary dependencies. If someone wants to take it in a different direction, they can.

Third, and maybe most important: it solves a real problem for me. I use it daily. As long as that's true, I'll maintain it. When it's not true anymore, that's probably when someone else should take over anyway.

The alternative—building everything behind closed doors, never sharing, keeping the knowledge locked up—doesn't solve the maintenance problem. It just makes it invisible.

## What you can build with this

Some things people have used claude-threads for:

- Debugging production issues collaboratively—everyone sees the investigation in real-time
- Onboarding new team members—they watch experienced developers work with Claude
- Architecture discussions—spawn a session, explore different approaches, see what actually works
- Code review prep—use Claude to check a branch, share the session with reviewers
- Learning new technologies—work with Claude to build something, invite others to learn along

One team uses it for "office hours"—a senior developer runs a public session where anyone can ask questions, suggest tasks, watch how problems get solved.

Another uses it for cross-team coordination—when multiple teams need to understand a shared component, they watch a session together, all contributing ideas.

These aren't use cases I designed for. They emerged from making the tool and sharing it.

## The limits of transparency

Not everything should be transparent. Not every collaboration should be open.

Security-sensitive work. Personal data. Competitive strategy. Early-stage ideas that need space to be bad before they get good.

claude-threads has access controls. You can restrict who can start sessions. Who can participate. Who can see which threads.

But the default design assumes transparency is good. You have to actively choose privacy, not the other way around.

This is a choice. A different tool might make the opposite choice—private by default, open by exception.

I chose this way because I think we need more transparency in how we build with AI, not less.

## What's next

The repository has a roadmap of sorts. File upload support. Better diff rendering. Rate limiting for busy channels.

But mostly I'm waiting to see what people actually need. Issues on GitHub tell me more than any roadmap I could write.

Some features emerge from use. Someone asks "can it do X?" I think "no, but it could." Then either I build it or they do.

That's the point of working open. The conversation continues beyond what I can imagine alone.

## The invitation

If you're working with AI—in government, in companies, in open source projects—and you're finding the collaboration model awkward, give claude-threads a try.

It's not perfect. It won't solve every problem. But it might change how your team works together.

The code is at [github.com/anneschuth/claude-threads](https://github.com/anneschuth/claude-threads). Install it with `npm install -g claude-threads`. The README has setup instructions.

If it doesn't work for you, open an issue. If it almost works but needs changes, fork it. If it works great, tell someone else who might need it.

And if you build something better, please share it. This space needs more experiments, more tools, more ways of working together.

## The real point

This post is ostensibly about a tool I built. But really it's about a few things I keep coming back to:

[Making speaks louder than writing](/2025/04/11/maken-over-schrijven.html). Building a collaboration tool teaches you more about collaboration than any amount of theorizing.

[Demos change conversations](/2025/05/02/demo.html). Before claude-threads existed, "AI pair programming collaboration" was abstract. Now it's "have you tried @mentioning the bot?"

[Working open creates options](/2025/11/28/makelaar-of-maker.html). Closed tools create vendor lock-in. Open tools create possibilities.

[AI is eroding the barriers](/2025/12/27/ai-erodeert.html) to building what we need. The rugged terrain of "I don't know Node.js well enough to build this" becomes navigable. Not flat, but climbable.

The question isn't whether you can build tools like this. You can. The question is what you'll build, how you'll share it, and who you'll build it with.

I'm curious what happens next.
