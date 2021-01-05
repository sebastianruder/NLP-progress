# Coreference resolution

Coreference resolution is the task of clustering mentions in text that refer to the same underlying real world entities.

Example:

```
               +-----------+
               |           |
I voted for Obama because he was most aligned with my values", she said.
 |                                                 |            |
 +-------------------------------------------------+------------+
```

"I", "my", and "she" belong to the same cluster and "Obama" and "he" belong to the same cluster.

### CoNLL 2012

Experiments are conducted on the data of the [CoNLL-2012 shared task](http://www.aclweb.org/anthology/W12-4501), which
uses OntoNotes coreference annotations. Papers
report the precision, recall, and F1 of the MUC, B3, and CEAFφ4 metrics using the official
CoNLL-2012 evaluation scripts. The main evaluation metric is the average F1 of the three metrics.

| Model           | Avg F1 |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| Xu et al. (2020) | 80.2 | [Revealing the Myth of Higher-Order Inference in Coreference Resolution](https://arxiv.org/abs/2009.12013) |[Official](https://github.com/emorynlp/coref-hoi) |
| Joshi et al. (2019)<sup>[1](#myfootnote1)</sup> | 79.6 | [SpanBERT: Improving Pre-training by Representing and Predicting Spans](https://arxiv.org/pdf/1907.10529) |[Official](https://github.com/facebookresearch/SpanBERT) |
| Joshi et al. (2019)<sup>[2](#myfootnote2)</sup> | 76.9 | [BERT for Coreference Resolution: Baselines and Analysis](https://arxiv.org/abs/1908.09091) | [Official](https://github.com/mandarjoshi90/coref) |
| Kantor and Globerson (2019) | 76.6 | [Coreference Resolution with Entity Equalization](https://www.aclweb.org/anthology/P19-1066/) | [Official](https://github.com/kkjawz/coref-ee) |
| Fei et al. (2019) | 73.8 | [End-to-end Deep Reinforcement Learning Based Coreference Resolution](https://www.aclweb.org/anthology/P19-1064/) | |
| (Lee et al., 2017)+ELMo (Peters et al., 2018)+coarse-to-fine & second-order inference (Lee et al., 2018) | 73.0 | [Higher-order Coreference Resolution with Coarse-to-fine Inference](http://aclweb.org/anthology/N18-2108) | [Official](https://github.com/kentonl/e2e-coref) |
| (Lee et al., 2017)+ELMo (Peters et al., 2018) | 70.4 | [Deep contextualized word representations](https://arxiv.org/abs/1802.05365) | |
| Lee et al. (2017) | 67.2 | [End-to-end Neural Coreference Resolution](https://arxiv.org/abs/1707.07045) | |

<a name="myfootnote1">[1]</a> Joshi et al. (2019): (Lee et al., 2017)+coarse-to-fine & second-order inference (Lee et al., 2018)+SpanBERT (Joshi et al., 2019)

<a name="myfootnote2">[2]</a> Joshi et al. (2019): (Lee et al., 2017)+coarse-to-fine & second-order inference (Lee et al., 2018)+BERT (Devlin et al., 2019)

### Gendered Ambiguous Pronoun Resolution

Experiments are conducted on [GAP dataset](https://github.com/google-research-datasets/gap-coreference). 
Metrics used are F1 score on Masculine (M) and Feminine (F) examples, Overall, and a Bias factor calculated as F / M.

| Model           | Overall F1 | Masculine F1 (M) | Feminine F1 (F) | Bias (F/M) | Paper / Source | Code |
| ------------- | :-----:| :-----:| :-----:| :-----:| --- | --- |
| Attree et al. (2019) | 92.5 | 94.0 | 91.1 | 0.97 | [Gendered Ambiguous Pronouns Shared Task: Boosting Model Confidence by Evidence Pooling](https://arxiv.org/abs/1906.00839) | [GREP](https://github.com/sattree/gap) |
| Chada et al. (2019) | 90.2 | 90.9 | 89.5 | 0.98 | [Gendered Pronoun Resolution using BERT and an extractive question answering formulation](https://arxiv.org/abs/1906.03695) | [CorefQA](https://github.com/rakeshchada/corefqa) |


[Go back to the README](../README.md)
