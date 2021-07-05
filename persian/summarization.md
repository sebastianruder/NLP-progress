# Summarization

Summarization is the task of producing a shorter version of one or several documents that preserves most of the input's meaning.

### Warning: Evaluation Metrics

For summarization, automatic metrics such as ROUGE and METEOR have serious limitations:
1. They only assess content selection and do not account for other quality aspects, such as fluency, grammaticality, coherence, etc. 
2. To assess content selection, they rely mostly on the lexical overlap, although an abstractive summary could express the same content as a reference without any lexical overlap.
3. Given the subjectiveness of summarization and the correspondingly low agreement between annotators, the metrics were designed to be used with multiple reference summaries per input. However, recent datasets such as `pn_summary` provide only a single reference.

Therefore, tracking progress and claiming state-of-the-art based only on these metrics is questionable. Most papers carry out additional manual comparisons of alternative summaries. Unfortunately, such experiments are difficult to compare across papers. If you have an idea on how to do that, feel free to contribute.

There are a few resources for the abstractive/extractive tasks in Persian, while some are not available online, or there are no curators for them. While surfing the academic papers, you might see some of them like **Pasokh**. Of course, thanks to some researchers' efforts in this field, a dataset called Persian News Summarization (known as `pn_summary`) has been prepared for both Persian summarization tasks and made available online.


### Persian News Summary (known as pn_summary)

The [Persian News Summary (known as pn_summary)](https://github.com/hooshvare/pn-summary) is a well-structured summarization dataset for the Persian language that consists of 93,207 online news articles (from 200,000 crawled news) from 6 different news agencies in 18 different news categories from economy to tourism. Each document (article) includes the long original text as well as a human-generated summary. Models are evaluated with full-length F1-scores of ROUGE-1, ROUGE-2, ROUGE-L, and METEOR (optional).

#### Abstractive Models & Mixed Models

| Model           | ROUGE-1 | ROUGE-2 | ROUGE-L | METEOR | Paper / Source | Code |
| --------------- | :-----: | :-----: | :-----: | :----: | -------------- | ---- |
| BERT2BERT (ParsBERT) + mT5 (Farahani et al., 2020) |  44.01  |  25.07  |  37.76  |    -   | [Leveraging ParsBERT and Pretrained mT5 for Persian Abstractive Text Summarization](https://arxiv.org/abs/2012.11204) | [Official](https://github.com/hooshvare/pn-summary) |


### Pasokh
[Pasokh](https://ieeexplore.ieee.org/document/6682873/) is a summarization dataset covering 6 news categories from 7 news agencies in two forms: **Single-Document (SD)** and **Multi-Document (MD)** with 100, 1000 records. Each document covers 5 samples for extractive and abstractive example.

#### Extractive Models & Mixed Models

| Model           | ROUGE-1 | ROUGE-2 | ROUGE-L | METEOR | Paper / Source | Code |
| --------------- | :-----: | :-----: | :-----: | :----: | -------------- | ---- |
| Based on NER (SD) (Khademi, Fakhredanesh, 2020) | 47.20 | 33.40 | - | - | [Persian Automatic Text Summarization Based on Named Entity Recognition](https://link.springer.com/article/10.1007%2Fs40998-020-00352-2) | - |
| Based on NER (SD) (Khademi et al., 2020) | 45.40 | 30.10 | - | - | [Conceptual Text Summarizer: A new model in continuous vector space](http://iajit.org/index.php?option=com_content&task=view&id=1935&Itemid=488) | - |
| Feature Extraction (SD) (Rezaei et al., 2019) | 78.00 | 71.00 | 74.00 | - | [Features in Extractive Supervised Single-document Summarization: Case of Persian News](https://arxiv.org/abs/1909.02776) | [Official](https://github.com/Hrezaei/SummBot) |
| Multi-Feature Extraction (SD) (Kermani, Ghanbari, 2019) | 48.70 | 42.60 | - | - | [Extractive Persian Summarizer for News Websites](https://ieeexplore.ieee.org/document/8765279) | - |
