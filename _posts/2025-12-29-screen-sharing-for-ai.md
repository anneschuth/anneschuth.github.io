---
title: "Screen-sharing for AI"
date: '2025-12-29T10:00:00+01:00'
author: Anne
layout: post
tags:
  - '2025'
  - 'weeknotes'
---

I built [claude-threads](https://github.com/anneschuth/claude-threads). It's a tool that brings Claude Code into Mattermost.

The tagline: "Think of it as screen-sharing for AI pair programming, but everyone can type."

## How it works

You @mention a bot in your team chat. It spawns a Claude Code session on your machine. Everything streams live to a thread—Claude's responses, code diffs, task lists, permission requests.

Colleagues can watch the session. They can ask questions. They can `!invite` others to participate. Multiple people can run their own sessions simultaneously in different threads.

When Claude wants to do something—write a file, run a command—you see a permission prompt in the thread. React with 👍 to approve, 👎 to deny, or ✅ to approve everything this session.

Code changes appear as diffs. Tasks show their status: ⬜ pending, 🔄 in progress, ✅ completed. The conversation is visible. The context stays shared.

## Why build this

Claude Code sessions are normally invisible. You're having a conversation with AI on your machine. Your colleague asks "what are you working on?" You paste some output. They lose context.

This makes it transparent. Not as a recording, but in real-time.

The problem with traditional pair programming: only one person drives. Screen-sharing is better, but still passive—the driver drives, everyone else watches.

This is different. Everyone can participate. The session owner controls access, but anyone invited can contribute. The knowledge stays in the thread.

## What people use it for

- Debugging together—everyone sees the investigation unfold
- Onboarding—new people watch how experienced developers work with Claude
- Architecture exploration—spawn a session, try different approaches, see what works
- Office hours—a senior developer runs a public session where anyone can ask questions
- Cross-team coordination—multiple teams watch and contribute to shared components

These use cases emerged from sharing the tool. I didn't design for all of them.

## Building it with Claude

I built claude-threads _with_ Claude Code. A tool to make Claude collaborative, built by collaborating with Claude.

About 3,000 lines of TypeScript. Managing concurrent sessions, WebSocket connections, permission prompts via emoji reactions, git worktree isolation, streaming diffs.

I don't know Node.js particularly well. Haven't written a Mattermost bot before. Never built an MCP server.

But I knew what I wanted. Claude Code helped figure out the rest.

[Same as I wrote in October](/2025/10/21/praten.html) about building 38,000 lines of mobile app code by talking to my computer. The [erosion effect](/2025/12/27/ai-erodeert.html)—rugged terrain becoming navigable.

## Working open

The code is on [GitHub](https://github.com/anneschuth/claude-threads). Published on npm. MIT licensed.

I could have kept it private. Built it for my own use.

Instead: open from day one.

Why? Because [making over talking](/2025/04/11/maken-over-schrijven.html). I write about how government should build prototypes and share them. This is that principle in practice.

Because tools for collaboration should be built collaboratively. Others can contribute, fork, improve.

Because [1 cloud is no cloud](/2025/11/28/makelaar-of-maker.html). Vendor lock-in applies to AI tools too. Open tools create options.

## Try it

If your team works with AI and the collaboration feels awkward, try it:

```bash
npm install -g claude-threads
```

The [README](https://github.com/anneschuth/claude-threads#readme) has setup instructions. You'll need Claude Code and a Mattermost bot account.

If it doesn't work for your use case, open an issue. If it almost works, fork it. If it works well, tell someone else who might need it.

And if you build something better—please share it.
