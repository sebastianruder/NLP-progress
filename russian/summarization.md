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
| Lead_3 | 9.29 | 1.54 | 5.9 | 5.8 | [MLSUM](https://www.aclweb.org/anthology/2020.emnlp-main.647/) | [Official](https://github.com/recitalAI/MLSUM) |
| Pointer-Generator | 9.19 | 1.18 | 5.7 | 5.7 | [MLSUM](https://www.aclweb.org/anthology/2020.emnlp-main.647/) | [Official](https://github.com/recitalAI/MLSUM) |
| M-BERT (Scialom et al., 2020) | 10.94 | 1.75 | 9.5 | 6.8 | [MLSUM](https://www.aclweb.org/anthology/2020.emnlp-main.647/) | [Official](https://github.com/recitalAI/MLSUM) |
| Oracle | 36.14 | 19.88 | 29.8 | 20.3 | [MLSUM](https://www.aclweb.org/anthology/2020.emnlp-main.647/) | [Official](https://github.com/recitalAI/MLSUM) |
| MARGE-NEWS (Train All) (Lewis et al., 2020) | - | - | 11.03 | - | [Pre-training via Paraphrasing](https://arxiv.org/abs/2006.15020) | [Official](https://github.com/lucidrains/marge-pytorch) |
