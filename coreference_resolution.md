## Coreference resolution

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

| Model           | Avg F1 |  Paper / Source |
| ------------- | :-----:| --- |
| (Lee et al., 2017)+ELMo (Peters et al., 2018)+coarse-to-fine & second-order inference (Lee et al., 2018) | 73.0 | [Higher-order Coreference Resolution with Coarse-to-fine Inference](http://aclweb.org/anthology/N18-2108) |
| (Lee et al., 2017)+ELMo (Peters et al., 2018) | 70.4 | [Deep contextualized word representatIions](https://arxiv.org/abs/1802.05365) |
| Lee et al. (2017) | 67.2 | [End-to-end Neural Coreference Resolution](https://arxiv.org/abs/1707.07045) |

[Go back to the README](README.md)
