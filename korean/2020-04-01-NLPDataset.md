---
layout: post
title: "Korean Dataset "
excerpt: "Github Blog Tuto"

categories:
  - NLP
tags:
  - NLP, Dataset

last_modified_at : 2020-04-06T00:00:00
---
### Naver sentiment movie corpus

The [NSMC dataset](https://ai.stanford.edu/~ang/papers/acl11-WordVectorsSentimentAnalysis.pdf) is a is a movie review dataset in the Korean language. Reviews were scraped from [Naver Movies](http://movie.naver.com/movie/point/af/list.nhn). The dataset construction is based on the method noted in [Large movie review dataset](http://ai.stanford.edu/~amaas/data/sentiment/) from Maas et al., 2011.

### Chatbot_data

Chatbot_data_for_Korean v1.0

### Petitions_data

Collect expired petition data from the Blue House National Petition Site.

### Korean Parallel corpora

Neural Machine Translation(NMT) Dataset for **Korean to Franch** & **Korean to English**

### KorQuAD

KorQuAD 1.0 is a large-scale question-and-answer dataset constructed for Korean machine reading comprehension, and investigate the dataset to understand the distribution of answers and the types of reasoning required to answer the question. This dataset benchmarks the data generating process of SQuAD v1.0 to meet the standard.

KorQuAD 2.1 is a Korean machine readable understanding dataset consisting of 100K+ pairs, including 20K+ question and answers from KorQuAD 1.0. Unlike KorQuAD 1.0, you should find the answer in the whole Wikipedia source, not in paragraph 1-2. You need to consider the search time, because of long document. Also, since it contains tables and lists, you need to understand the structure of the document through HTML tags. With this dataset, documents of various shapes and lengths can be machine-readable.

| Dataset           | Label  |  Source |
| ------------- | :-----:| --- |
| Naver sentiment movie corpus v1.0 | 0, 1</br>(Neg, Pos) | [Naver sentiment movie corpus v1.0](https://github.com/e9t/nsmc) |
| Chatbot_data_for_Korean v1.0 | 0, 1, 2</br>(Normal, Neg, Pos) | [Chatbot_data](https://github.com/songys/Chatbot_data)
| Petitions_data | Raw | [Petitions_data](https://github.com/akngs/petitions)
|Korean NER Corpus| POS tag & NER tag | [KoreanNERCorpus](https://github.com/machinereading/KoreanNERCorpus)
|Korean Parallel corpora | Franch </br> English | [Korean Parallel corpora](https://github.com/j-min/korean-parallel-corpora)
| KorQuAD v1.0 | | [KorQuAD v1.0](https://korquad.github.io/category/1.0_KOR.html)
| KorQuAD v2.1 | | [KorQuAD v2.1](https://sosomemo.tistory.com/21)
