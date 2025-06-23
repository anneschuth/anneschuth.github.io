---
title: "Experiments with Machine Law"
date: '2025-01-25T07:00:00+01:00'
author: Anne
layout: post
tags:
  - '2025'
  - 'weeknotes'
lang: en
---

[Last week](/2025/01/16/starting-bureau-architecture.html), I wrote about joining Bureau Architecture and the energy I
found there. This week, I want to share what I've been experimenting with: what I've been calling "Machine Law."

## The Experiment

I've been exploring what happens when we treat laws and regulations as interconnected systems rather than isolated
implementations. Take a citizen applying for childcare benefits - this seemingly straightforward request touches
multiple government organizations, each with their own rules, computations, and data requirements.

Currently, each organization typically implements these rules in their own way, creating silos and complexity. My
experiments involve modeling how these different pieces could work together in a machine-readable format.

If you're interested, my experiments live
here: [https://github.com/MinBZK/poc-machine-law](https://github.com/MinBZK/poc-machine-law).

## Why This Matters

Many Dutch laws are essentially mechanical processes. Think about pension calculations, rent subsidies, or cost-sharing
norms - they're algorithms disguised as text. But today, we face three key problems:

1. These algorithms are interpreted and implemented by programmers who often lack legal backgrounds
2. The implementations lack transparency - both citizens and civil servants face "computer says no" situations
3. Quality control of these implementations is difficult across different government organizations
4. And, importantly, a single underlying standard makes a _true_ single-government portal much more attainable.

When a citizen requests a benefit, they shouldn't need to understand our organizational structure or navigate between
different departments. My experiments with Machine Law explore what happens when we lift these implementations out of
isolated codebases into a shared, machine-readable representation. What changes when we make the connections between
different regulations explicit and executable?

## Moving to Delivery

"The strategy is delivery" isn't just a motto - it's a necessity. These experiments aren't just theoretical exercises.
They're about understanding what we need to actually implement this approach:

- What technical infrastructure would we need?
- Which stakeholders need to be involved?
- How do we start small while keeping the bigger picture in mind?

## Next Steps

The implications of this approach are significant, and I'm still uncovering new ones. But the focus now is on moving
toward delivery. I'm looking for opportunities to test these ideas in real, albeit small, contexts.

We need to bring the right people on board - not just engineers and architects, but policy makers, legal experts, and
most importantly, the civil servants who work directly with citizens. And, importantly, a UX designer, I think.

The experiment continues, but with an eye toward making it real.

---

**Related:** See also my follow-up post on [Rules as Code Europe](/2025/03/21/rules-as-code-europe.html) and my talks on [machine-executable legislation](/talks/automated-extraction-of-machine-executable-legislation-2025.html) and [prediction in the public sector](/talks/prediction-is-power-also-in-the-public-sector-2025.html).
