# Summarization

Summarization is the task of producing a shorter version of a document that preserves most of the
original document's meaning.

### CNN / Daily Mail

The [CNN / Daily Mail dataset](https://arxiv.org/abs/1506.03340) as processed by 
[Nallapati et al. (2016)](http://www.aclweb.org/anthology/K16-1028) has been used
for evaluating summarization. The dataset contains online news articles (781 tokens 
on average) paired with multi-sentence summaries (3.75 sentences or 56 tokens on average).
The processed version contains 287,226 training pairs, 13,368 validation pairs and 11,490 test pairs.
Models are evaluated based on ROUGE-1, ROUGE-2, ROUGE-L, and METEOR (optional). * indicates that models
were trained and evaluated on the anonymized version of the dataset.

| Model           | ROUGE-1 | ROUGE-2 | ROUGE-L | METEOR | Paper / Source | Code |
| --------------- | :-----: | :-----: | :-----: | :----: | -------------- | ---- |
| Fast-ABS-RL (Chen and Bansal, 2018) | 41.20 | 18.18 | 38.79 | 20.55 | [Fast Abstractive Summarization with Reinforce-Selected Sentence Rewriting](https://arxiv.org/abs/1805.11080) | [Official](https://github.com/chenrocks/fast_abs_rl) |
| DCA (Celikyilmaz et al., 2018) | 41.69| 19.47 | 37.92 | | [Deep Communicating Agents for Abstractive Summarization](https://arxiv.org/abs/1803.10357) | |
| REFRESH - Extractive model (Narayan et al., 2018) | 40.0 | 18.2 | 36.6 | | [Ranking Sentences for Extractive Summarization with Reinforcement Learning](https://arxiv.org/pdf/1802.08636.pdf) | [Official](https://github.com/EdinburghNLP/Refresh) |
| Pointer-generator + coverage (See et al., 2017) | 39.53| 17.28 | 36.38 | 18.72 | [Get To The Point: Summarization with Pointer-Generator Networks](https://arxiv.org/abs/1704.04368) | [Official](https://github.com/abisee/pointer-generator) |
| Extractive model (Nallapati et al., 2017)* | ﻿39.6 | 16.2 | 35.3 | | [SummaRuNNer: A Recurrent Neural Network based Sequence Model for Extractive Summarization of Documents](https://arxiv.org/abs/1611.04230) | |
| Abstractive model (Nallapti et al., 2016)* | 35.46 | 13.30 | 32.65 | | [Abstractive Text Summarization using Sequence-to-sequence RNNs and Beyond](http://www.aclweb.org/anthology/K16-1028) | |

## Sentence Compression

Sentence compression produces a shorter sentence by removing redundant information,
preserving the grammatically and the important content of the original sentence. 

### Google Dataset

The [Google Dataset](https://github.com/google-research-datasets/sentence-compression) was built by Filippova et al., 2013([Overcoming the Lack of Parallel Data in Sentence Compression](https://www.aclweb.org/anthology/D/D13/D13-1155.pdf)). The first dataset released contained only 10,000 sentence-compression pairs, but last year was released an additional 200,000 pairs. 

Example of a sentence-compression pair:
> Sentence: Floyd Mayweather is open to fighting Amir Khan in the future, despite snubbing the Bolton-born boxer in favour of a May bout with Argentine Marcos Maidana, according to promoters Golden Boy

> Compression: Floyd Mayweather is open to fighting Amir Khan in the future. 

In short, this is a deletion-based task where the compression is a subsequence from the original sentence. From the 10,000 pairs of the eval portion([repository](https://github.com/google-research-datasets/sentence-compression/tree/master/data)) it is used the very first 1,000 sentence for automatic evaluation and the 200,000 pairs for training.

Models are evaluated using the following metrics:
* F1 - compute the recall and precision in terms of tokens kept in the golden and the generated compressions.
* Compression rate (CR) - the length of the compression in characters divided over the sentence length. 

| Model           | F1 | CR |Paper / Source | Code |
| -------------   | :-----:| --- | --- | --- |
| LSTM (Filippova et al., 2015) | 0.82 | 0.38 | [Sentence Compression by Deletion with LSTMs](https://research.google.com/pubs/archive/43852.pdf) | |
| BiLSTM (Wang et al., 2017) | 0.8 | 0.43 | [Can Syntax Help? Improving an LSTM-based Sentence Compression Model for New Domains](http://www.aclweb.org/anthology/P17-1127) |  |

[Go back to the README](README.md)
