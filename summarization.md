# Summarization

Summarization is the task of producing a shorter version of a document that preserves most of the
original document's meaning.

### CNN / Daily Mail

The [CNN / Daily Mail dataset](https://arxiv.org/abs/1506.03340) as processed by 
[Nallapati et al. (2016)](http://www.aclweb.org/anthology/K16-1028) has been used
for evaluating summarization. The dataset contains online news articles (781 tokens 
on average) paired with multi-sentence summaries (3.75 sentences or 56 tokens on average).
The processed version contains 287,226 training pairs, 13,368 validation pairs and 11,490 test pairs.
Models are evaluated based on ROUGE-1, ROUGE-2, and ROUGE-L. * indicates that models
were trained and evaluated on the anonymized version of the dataset.

| Model           | ROUGE-1  | ROUGE-2  | ROUGE-L  |  Paper / Source |
| ------------- | :-----:| :-----:| :-----:| --- |
| DCA (Celikyilmaz et al., 2018) | 41.69| 19.47 | 37.92 | [Deep Communicating Agents for Abstractive Summarization](https://arxiv.org/abs/1803.10357) |
| Pointer-generator + coverage (See et al., 2017) | 39.53| 17.28 | 36.38 | [Get To The Point: Summarization with Pointer-Generator Networks](https://arxiv.org/abs/1704.04368) |
| Extractive model (Nallapati et al., 2017)* | ﻿39.6 | 16.2 | 35.3 | [SummaRuNNer: A Recurrent Neural Network based Sequence Model for Extractive Summarization of Documents](https://arxiv.org/abs/1611.04230) |
| Abstractive model (Nallapti et al., 2016)* | 35.46 | 13.30 | 32.65 | [Abstractive Text Summarization using Sequence-to-sequence RNNs and Beyond](http://www.aclweb.org/anthology/K16-1028) |

[Go back to the README](README.md)
