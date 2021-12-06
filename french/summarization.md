# Summarization

Summarization is the task of producing a shorter version of one or several documents that preserves most of the
input's meaning.

### Warning: Evaluation Metrics

For summarization, automatic metrics such as ROUGE and METEOR have serious limitations:
1. They only assess content selection and do not account for other quality aspects, such as fluency, grammaticality, coherence, etc. 
2. To assess content selection, they rely mostly on lexical overlap, although an abstractive summary could express they same content as a reference without any lexical overlap.
3. Given the subjectiveness of summarization and the correspondingly low agreement between annotators, the metrics were designed to be used with multiple reference summaries per input. However, recent datasets such as MLSUM provide only a single reference.

Therefore, tracking progress and claiming state-of-the-art based only on these metrics is questionable. Most papers carry out additional manual comparisons of alternative summaries. Unfortunately, such experiments are difficult to compare across papers. If you have an idea on how to do that, feel free to contribute.


### MLSUM

We present [MLSUM](https://www.aclweb.org/anthology/2020.emnlp-main.647/), the first large-scale MultiLingual SUMmarization dataset. 
Obtained from online newspapers, it contains 1.5M+ article/summary pairs in five different languages -- namely, [French](../french/summarization.md#mlsum), [German](../german/summarization.md#mlsum), [Spanish](../spanish/summarization.md#mlsum), [Russian](../russian/summarization.md#mlsum), [Turkish](../turkish/summarization.md#mlsum). Together with [English](../english/summarization.md#cnn--daily-mail) newspapers from the popular CNN / Daily Mail dataset, 
the collected data form a large scale multilingual dataset which can enable new research directions for the text summarization community. 
We report cross-lingual comparative analyses based on state-of-the-art systems. 
These highlight existing biases which motivate the use of a multi-lingual dataset.

Below results are ranked by chronological order.

| Model | ROUGE-1 | ROUGE-2 | ROUGE-L | METEOR | Paper / Source | Code |
| --------------- | :-----: | :-----: | :-----: | :-----: | -------------- | ---- |
| Lead_3 | 28.74 | 9.84 | 19.7 | 12.6 | [MLSUM](https://www.aclweb.org/anthology/2020.emnlp-main.647/) | [Official](https://github.com/recitalAI/MLSUM) |
| Pointer-Generator | 31.08 | 10.12 | 23.6 | 14.1 | [MLSUM](https://www.aclweb.org/anthology/2020.emnlp-main.647/) | [Official](https://github.com/recitalAI/MLSUM) |
| M-BERT (Scialom et al., 2020) | 31.59 | 10.61 | 25.1 | 15.1 | [MLSUM](https://www.aclweb.org/anthology/2020.emnlp-main.647/) | [Official](https://github.com/recitalAI/MLSUM) |
| Oracle | 47.32 | 25.95 | 37.7 | 24.7 | [MLSUM](https://www.aclweb.org/anthology/2020.emnlp-main.647/) | [Official](https://github.com/recitalAI/MLSUM) |
| MARGE-NEWS (Train All) (Lewis et al., 2020) | - | - | 25.79 | - | [Pre-training via Paraphrasing](https://arxiv.org/abs/2006.15020) | [Official](https://github.com/lucidrains/marge-pytorch) |

### OrangeSum

The OrangeSum dataset was introduced in ["BARThez: a Skilled Pretrained French Sequence-to-Sequence Model"](https://aclanthology.org/2021.emnlp-main.740/). It was created by scraping the "Orange Actu" website: https://actu.orange.fr/. Orange S.A. is a large French multinational telecommunications corporation, with 266M customers worldwide. Scraped pages cover almost a decade from Feb 2011 to Sep 2020. They belong to five main categories: France, world, politics, automotive, and society. The society category is itself divided into 8 subcategories: health, environment, people, culture, media, high-tech, unsual ("insolite" in French), and miscellaneous.

Each article featured a single-sentence title as well as a very brief abstract, both professionally written by the author of the article. These two fields were extracted from each page, thus creating two summarization tasks: OrangeSum Title and OrangeSum Abstract.

The dataset can be found [here](https://huggingface.co/datasets/orange_sum).
   

#### OrangeSum-abstract

| Model | ROUGE-1 | ROUGE-2 | ROUGE-L | METEOR | Paper / Source | Code |
| --------------- | :-----: | :-----: | :-----: | :-----: | -------------- | ---- |
| BARThez | 31.44 | 12.77 | 22.23 | - | [BARThez](https://aclanthology.org/2021.emnlp-main.740/) | [Official](https://github.com/moussaKam/BARThez) |
| mBARThez | 32.67 | 13.73 | 23.18 | - | [BARThez](https://aclanthology.org/2021.emnlp-main.740/) | [Official](https://github.com/moussaKam/BARThez) |
| CamemBERT2CamemBERT (Martin, Louis, et al.) | 29.23 | 09.79 | 19.95 | - | [BARThez](https://aclanthology.org/2021.emnlp-main.740/) | [Official](https://github.com/moussaKam/BARThez) |
| mBART (Liu, Yinhan, et al.) | 31.85 | 13.10 | 22.35 | - | [BARThez](https://aclanthology.org/2021.emnlp-main.740/) | [Official](https://github.com/moussaKam/BARThez) |
| PAGnol-S | 24.54 | 8.98 | 18.45 | - | [PAGnol](https://arxiv.org/pdf/2110.08554.pdf) | [Official](https://github.com/lightonai/lairgpt) |
| PAGnol-M | 27.80 | 10.56 | 20.29 | - | [PAGnol](https://arxiv.org/pdf/2110.08554.pdf) | [Official](https://github.com/lightonai/lairgpt) |
| PAGnol-L | 28.25 | 11.05 | 21.03 | - | [PAGnol](https://arxiv.org/pdf/2110.08554.pdf) | [Official](https://github.com/lightonai/lairgpt) |
| PAGnol-XL | 28.72 | 11.08 | 20.89 | - | [PAGnol](https://arxiv.org/pdf/2110.08554.pdf) | [Official](https://github.com/lightonai/lairgpt) |

#### OrangeSum-title

| Model | ROUGE-1 | ROUGE-2 | ROUGE-L | METEOR | Paper / Source | Code |
| --------------- | :-----: | :-----: | :-----: | :-----: | -------------- | ---- |
| BARThez | 40.86 | 23.68 | 36.03 | - | [BARThez](https://aclanthology.org/2021.emnlp-main.740/) | [Official](https://github.com/moussaKam/BARThez) |
| mBARThez | 41.08 | 24.11 | 36.41 | - | [BARThez](https://aclanthology.org/2021.emnlp-main.740/) | [Official](https://github.com/moussaKam/BARThez) |
| CamemBERT2CamemBERT (Martin, Louis, et al.) | 34.92 | 18.04 | 30.83 | - | [BARThez](https://aclanthology.org/2021.emnlp-main.740/) | [Official](https://github.com/moussaKam/BARThez) |
| mBART (Liu, Yinhan, et al.) | 40.74 | 23.70 | 36.04 | - | [BARThez](https://aclanthology.org/2021.emnlp-main.740/) | [Official](https://github.com/moussaKam/BARThez) |

