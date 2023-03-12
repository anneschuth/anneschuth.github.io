---
author: "Joris Baan and Maartje ter Hoeve and Marlies van der Wees and Anne Schuth and Maarten de Rijke"
booktitle: "arXiv"
date: "2019-11-10"
key: baan2019b
keywords: "deep learning, explainability"
layout: publication
pdf: /assets/1911.03898.pdf
title: "Understanding Multi-Head Attention in Abstractive Summarization"
type: article
year: "2019"
---

Attention mechanisms in deep learning architectures have often been used as a means of transparency and, as such, to shed light on the inner workings of the architectures. Recently, there has been a growing interest in whether or not this assumption is correct. In this paper we investigate the interpretability of multihead attention in abstractive summarization, a sequence-to-sequence task for which attention does not have an intuitive alignment role, such as in machine translation. We first introduce three metrics to gain insight in the focus of attention heads and observe that these heads specialize towards relative positions, specific part-of-speech tags, and named entities. However, we also find that ablating and pruning these heads does not lead to a significant drop in performance, indicating redundancy. By replacing the softmax activation functions with sparsemax activation functions, we find that attention heads behave seemingly more transparent: we can ablate fewer heads and heads score higher on our interpretability metrics. However, if we apply pruning to the sparsemax model we find that we can prune even more heads, raising the question whether enforced sparsity actually improves transparency. Finally, we find that relative positions heads seem integral to summarization performance and persistently remain after pruning.

