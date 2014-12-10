---
title: "主题模型及LSI、PLSI、LDA简介"
date: 2014-07-16 17:12
categories:
slug: topic-model
---

如何从大量文档中自动归纳出每篇文章的主题，是一个很有意思的任务。
1998年，Papadimitriou等人在[一篇论文](http://www.ingentaconnect.com/content/ap/ss/2000/00000061/00000002/art01711)
中提出了LSI的概念，这是一种主题模型（topic model），
[维基百科上面的主题模型词条](http://zh.wikipedia.org/wiki/%E4%B8%BB%E9%A2%98%E6%A8%A1%E5%9E%8B)。

在这篇文章中提出了LSI（潜在语义索引），维基百科词条
[潜在语义索引](http://zh.wikipedia.org/wiki/%E4%B8%BB%E9%A2%98%E6%A8%A1%E5%9E%8B)

PLSI指的是概率性潜在语义索引。跟PLSA是同义语，维基百科上面这两个词也指向同一个页面。
[论文下载](http://cs.brown.edu/~th/papers/Hofmann-SIGIR99.pdf)

LSI从那里来的呢？从LSA而来。
[Latent semantic analysis](http://en.wikipedia.org/wiki/Latent_semantic_analysis)，
[LSA主页](http://lsa.colorado.edu/)，
[论文下载](http://lsa.colorado.edu/papers/JASIS.lsi.90.pdf)，
还有一个概念是PLSA，
[Probabilistic latent semantic analysis](http://en.wikipedia.org/wiki/Probabilistic_latent_semantic_analysis)，
它来自于[这篇论文](http://cs.brown.edu/people/th/papers/Hofmann-UAI99.pdf)。
PLSI和PLSA的两篇论文都是hofmann所发表。

2003年，Blei等人提出LDA，这是一种一般化的PLSI，之后其他的主题模型一般是在LDA的基础上改进的。
维基百科[隐含狄利克雷分布](http://zh.wikipedia.org/wiki/%E9%9A%90%E5%90%AB%E7%8B%84%E5%88%A9%E5%85%8B%E9%9B%B7%E5%88%86%E9%85%8D)。
论文地址：[Latent Dirichlet Allocation](http://jmlr.org/papers/v3/blei03a.html)
现任百度公司首席科学家的[吴恩达](http://zh.wikipedia.org/wiki/%E5%90%B4%E6%81%A9%E8%BE%BE)是论文的作者之一。

中文方面，丕子网有一个[关于主题模型](http://www.zhizhihu.com/html/ytag/%E4%B8%BB%E9%A2%98%E6%A8%A1%E5%9E%8B)的系列文章，介绍了不少有价值的信息来源。
比如，这一篇[收集下2010之前的“基于LDA的Topic Model变形”的论文](http://www.zhizhihu.com/html/y2011/3226.html)就介绍了不少这方面的论文。

[八灵九霖的博客](http://blog.sina.com.cn/s/blog_9d7bca9f01015580.html)里的一篇文章，虽然篇幅较短，却是最容易理解的一篇文章。

[统计之都](http://cos.name/)上面也有一些此方面的论文，搜索一下LDA等词即可搜到，比如[这篇文章](http://cos.name/2013/03/lda-math-text-modeling/)。

我们要提倡创新精神、创造性思维、创造性劳动。比如，上面这许多中文博客，内容都有一定价值，但是没有原创内容，属于对大牛的原创内容的介绍与二次传播。
我们虽然要写博客记录、介绍和学习大牛的成果，自己也要做一个生产者，通过自己的实践和思考，产生高质量的原创性成果。

如果想要学习这个领域的最新成果，可以找一下上面几篇大牛论文所发表的期刊和会议，然后看一下这些期刊和会议的最新几期的论文，应该能够了解到该领域最新
前沿成果。
