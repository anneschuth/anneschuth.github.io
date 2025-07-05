---
title: "An architect after all?"
date: '2025-06-23T10:00:00+01:00'
author: Anne
layout: post
week_number: 99
tags:
  - '2025'
  - 'weeknotes'
  - 'ai'
  - 'development'
---

Something special happens when you type [`claude --dangerously-skip-permissions`](https://docs.anthropic.com/en/docs/claude-code) into your terminal, give it a task, and go for a run. You return to an assistant that has simply continued working while you were busy. I even tell [Claude Code](https://docs.anthropic.com/en/docs/claude-code): "I'm going away for an hour now. Use the Unix clock to see how much time you have left and make sure you use the time well." And it does.

## More than just code

I asked Claude Code to improve this website. To implement some missing features. Claude Code itself thought that dark mode and search functionality would be good features, and as you can see, they are now there. Of course, these are indispensable and fantastic features that no website can do without. But it went even further than that. It found missing PDFs and publications on websites of other universities in other countries, with co-authors. It ensures that my website is up-to-date again and that there are almost no broken links left.

This goes beyond just executing code. It *thinks* along about what needs to be done.

## Clean code, no fuss

When I look at the code that comes out, it's just neat. Neat markdown, neat HTML, neat CSS—separation between content and formatting as it should be. Claude Code writes very neat Git commit messages and creates pull requests with descriptions. It uses the right libraries and frameworks that are already in your project. It follows conventions without you having to explain them.

Claude Code even added conventions that I didn't have yet. Pre-commit hooks, for example, to clean markdown and straighten other things out. It not only improves what's there but makes the codebase better than I had left it.

## An architect after all?

This is where it gets ironic. I notice that I'm becoming more of an architect and less of a programmer. In [previous posts](/2025/04/11/maken-over-schrijven.html) I was quite critical of architects who are detached from the actual building—and now I'm saying this? Apparently, I'm becoming that architect I used to be so critical of after all.

But perhaps this is a different kind of architect. This is an architect who is not just an architect, but also the entire development team attached to it. Architect, product manager, back-end engineer, front-end engineer, UX designer—all in one. It's not a handover; there's no such thing as an architect detached from the developers. No, this is an architect who is also the developer. There is suddenly no longer a separation, but this covers the entire spectrum.

This is not new—[others](https://simonwillison.net/2025/Mar/19/vibe-coding/) [say](https://www.youtube.com/watch?v=LCEmiRjPEtQ) [exactly](https://brainhub.eu/library/software-developer-age-of-ai) [the same](https://newsletter.pragmaticengineer.com/p/vibe-coding-as-a-software-engineer). But the difference is that I am now truly experiencing it.

## Trust

What's special about Claude Code is that I can trust it. I can go for a run for an hour and know that it will get to work. That it makes a to-do list and systematically works through it. That it not only does what I asked but also thinks about what I meant.

I don't have that trust with other development tools. With other tools, you constantly have to check, adjust, repair. With Claude Code, you come back and think: "Yes, this is exactly what I wanted." It understands context, it makes sensible choices, it leaves behind code you would have wanted to write yourself.

## The future is now

I think this will change the world. That we will become entire development teams instead of just programmers. The power lies not only in the speed with which code is written but also in the way you can think about problems. You can focus on *what* needs to be done instead of *how* it needs to be done.

If you want to try this: start small, be specific about what you want, and provide context. And if you leave for an hour—say so. Claude Code uses the time well.

That `--dangerously-skip-permissions` flag sounds more dramatic than it is. It means that Claude Code can read and write files without asking for permission every time. For my own projects, I think that's fine—commits and pull requests just happen. I only check before merging to main.

## One step further

It goes even further than just Claude Code. I also use [Wispr Flow](https://wispr.ai/) to dictate instructions to Claude Code. Talking out loud to your computer while your hands are full or leaning back, and exactly those thoughts you have are converted into text and sent to Claude Code. The combination of speech-to-text and AI-driven development makes the boundary between thinking and implementing even thinner.

During my leave, I was mainly busy with the baby, her sisters, and the mother, of course. But occasionally, in between, I would come to my computer to give it an instruction, and then the computer would get to work. I'll be back at work next week, but precisely because I use Wispr Flow, I can also program hands-free with a baby quite easily. The future of development is not only more efficient but also more adaptable to life.

The future of software development is no longer science fiction. It's happening now, on your terminal, while you're out for a run.

*By the way, you no longer have to pay separately for Claude Code or have a developer account with separate billing for the API—it's part of the Claude Pro subscription.*
