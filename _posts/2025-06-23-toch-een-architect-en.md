---
title: "An Architect After All?"
date: '2025-06-23T10:00:00+01:00'
author: Anne
layout: post
lang: en
lang_ref: toch-een-architect
tags:
  - '2025'
  - 'weeknotes'
  - 'ai'
  - 'development'
---

Something special happens when you type [`claude --dangerously-skip-permissions`](https://docs.anthropic.com/en/docs/claude-code) into your terminal, give it a task, and go for a run. You come back to an assistant that has simply continued working while you were away. I even tell [Claude Code](https://docs.anthropic.com/en/docs/claude-code): "I'm going away for an hour now. Use the Unix clock to see how much time you have left and make good use of the time." And it does.

## More than just code

I asked Claude Code to improve this website. To implement some missing features. Claude Code figured out by itself that dark mode and search functionality would be good features, and as you can see, they're here now. Of course, these are indispensable and fantastic features that every website really can't do without. But it went even further than that. It found missing PDFs and publications on websites of other universities in other countries, from fellow co-authors. It ensures that my website is up-to-date again and that there are almost no broken links left.

This goes beyond just executing code. It *thinks* along about what needs to happen.

## Clean code, no frills

When I look at the code that comes out, it's just neat. Clean markdown, clean HTML, clean CSS—separation between content and layout as it should be. Claude Code writes very clean Git commit messages and creates pull requests with descriptions. It uses the right libraries and frameworks that are already in your project. It follows conventions without you having to explain them.

Claude Code has even added conventions I didn't have yet. Pre-commit hooks for example to clean up markdown and straighten out other things. It not only improves what's there, but makes the codebase better than I had left it.

## An architect after all?

This is where it becomes ironic. I notice that I'm becoming more of an architect and less of a programmer. In [earlier posts](/2025/04/11/maken-over-schrijven.html) I was quite critical of architects who are disconnected from the actual building—and now I'm saying this? Apparently I'm becoming that architect I used to be so critical of.

But maybe this is a different kind of architect. This is an architect who isn't just an architect, but also the entire development team attached to it. Architect, product manager, back-end engineer, front-end engineer, UX designer—all in one. It's not a handover; there's no such thing as an architect who stands apart from the developers. No, this is an architect who is also the developer. Suddenly there's no separation anymore, but this covers the entire spectrum.

This isn't new—[others](https://simonwillison.net/2025/Mar/19/vibe-coding/) [say](https://www.youtube.com/watch?v=LCEmiRjPEtQ) [exactly](https://brainhub.eu/library/software-developer-age-of-ai) [the same](https://newsletter.pragmaticengineer.com/p/vibe-coding-as-a-software-engineer). But the difference is that I'm now really experiencing it.

## Trust

What's special about Claude Code is that I can trust it. I can go for an hour-long run and know that it will get to work. That it makes a todo list and works through it systematically. That it not only does what I asked, but also thinks about what I meant.

I don't have that trust with other development tools. With other tools you have to constantly check, adjust, repair. With Claude Code you come back and think: "Yes, this is exactly what I wanted." It understands context, it makes sensible choices, it leaves behind code that you would have wanted to write yourself.

## The future is now

I think this is going to change the world. That we become entire development teams instead of just programmers. The power lies not only in the speed with which code is written, but also in the way you can think about problems. You can focus on *what* needs to happen instead of *how* it needs to happen.

If you want to try this: start small, be specific about what you want, and give context. And if you go away for an hour—say so. Claude Code uses the time well.

That `--dangerously-skip-permissions` flag sounds more dramatic than it is. It means that Claude Code can read and write files without asking permission every time. For my own projects I'm fine with that—commits and pull requests just happen. I only check before I merge to main.

## One step further

It goes even further than just Claude Code. I also use [Wispr Flow](https://wispr.ai/) to dictate instructions to Claude Code. Talking out loud to your computer while your hands are full or you're leaning back, and exactly those thoughts you have are converted to text and sent to Claude Code. The combination of speech-to-text and AI-driven development makes the boundary between thinking and implementation even thinner.

During my leave I was of course mainly busy with the baby, her sisters and the mother. But occasionally, in between, I would come to my computer to give it an instruction, and then the computer would get to work nicely. Starting next week I'll be back at work, but precisely because I use Wispr Flow, I can also continue programming hands-free with a baby quite easily. The future of development is not only more efficient, but also better integrated into life.

The future of software development is no longer science fiction. It's happening now, on your terminal, while you're out running.

*By the way, you no longer need to pay separately for Claude Code or have a developer account with separate billing for the API—it's part of the Claude Pro subscription.*
