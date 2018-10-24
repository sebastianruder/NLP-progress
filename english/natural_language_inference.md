# Natural language inference

Natural language inference is the task of determining whether a "hypothesis" is 
true (entailment), false (contradiction), or undetermined (neutral) given a "premise".

Example:

| Premise | Label | Hypothesis |
| --- | ---| --- |
| A man inspects the uniform of a figure in some East Asian country. | contradiction | The man is sleeping. |
| An older and younger man smiling. | neutral  | Two men are smiling and laughing at the cats playing on the floor. |
| A soccer game with multiple males playing. | entailment | Some men are playing a sport. |

### SNLI

The [Stanford Natural Language Inference (SNLI) Corpus](https://arxiv.org/abs/1508.05326)
contains around 550k hypothesis/premise pairs. Models are evaluated based on accuracy.

State-of-the-art results can be seen on the [SNLI website](https://nlp.stanford.edu/projects/snli/).

### MultiNLI

The [Multi-Genre Natural Language Inference (MultiNLI) corpus](https://arxiv.org/abs/1704.05426)
contains around 433k hypothesis/premise pairs. It is similar to the SNLI corpus, but
covers a range of genres of spoken and written text and supports cross-genre evaluation. The data
can be downloaded from the [MultiNLI](https://www.nyu.edu/projects/bowman/multinli/) website.

Public leaderboards for [in-genre (matched)](https://www.kaggle.com/c/multinli-matched-open-evaluation/leaderboard) 
and [cross-genre (mismatched)](https://www.kaggle.com/c/multinli-mismatched-open-evaluation/leaderboard)
evaluation are available, but entries do not correspond to published models.

| Model           | Matched  | Mismatched | Paper / Source |
| ------------- | :-----:| :-----:| --- |
| Finetuned Transformer LM (Radford et al., 2018) | 82.1 | 81.4 | [Improving Language Understanding by Generative Pre-Training](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf) |
| Multi-task BiLSTM + Attn (Wang et al., 2018) | 72.2 | 72.1 | [GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding](https://arxiv.org/abs/1804.07461) |
| GenSen (Subramanian et al., 2018) | 71.4 | 71.3 | [Learning General Purpose Distributed Sentence Representations via Large Scale Multi-task Learning](https://arxiv.org/abs/1804.00079) | |

### SciTail

The [SciTail](http://ai2-website.s3.amazonaws.com/publications/scitail-aaai-2018_cameraready.pdf)
entailment dataset consists of 27k. In contrast to the SNLI and MultiNLI, it was not crowd-sourced
but created from sentences that already exist "in the wild". Hypotheses were created from
science questions and the corresponding answer candidates, while relevant web sentences from a large
corpus were used as premises. Models are evaluated based on accuracy.

| Model           | Accuracy  |  Paper / Source |
| ------------- | :-----:| --- |
| Finetuned Transformer LM (Radford et al., 2018) | 88.3 | [Improving Language Understanding by Generative Pre-Training](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf) 
| Hierarchical BiLSTM Max Pooling (Talman et al., 2018) | 86.0 | [Natural Language Inference with Hierarchical BiLSTM Max Pooling](https://arxiv.org/abs/1808.08762)
| CAFE (Tay et al., 2018) | 83.3 | [A Compare-Propagate Architecture with Alignment Factorization for Natural Language Inference](https://arxiv.org/abs/1801.00102) |

[Go back to the README](../README.md)
