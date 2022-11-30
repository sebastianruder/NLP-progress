# Semantic role labeling

Semantic role labeling aims to model the predicate-argument structure of a sentence
and is often described as answering "Who did what to whom". BIO notation is typically
used for semantic role labeling.

Example:

| Housing | starts | are | expected | to | quicken | a | bit | from | August’s | pace | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| B-ARG1 | I-ARG1 | O |  O  |  O  |   V  | B-ARG2 | I-ARG2 | B-ARG3 | I-ARG3 | I-ARG3 |    

### OntoNotes

Models are typically evaluated on the [OntoNotes benchmark](http://www.aclweb.org/anthology/W13-3516) based on F1.

| Model           | F1  |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| Tian et al., (2022) + XLNet | 87.67 | [Syntax-driven Approach for Semantic Role Labeling](https://aclanthology.org/2022.lrec-1.772/) | [Official](https://github.com/synlp/SRL-MM) |
| He et al., (2018) + ELMO | 85.5 | [Jointly Predicting Predicates and Arguments in Neural Semantic Role Labeling](http://aclweb.org/anthology/P18-2058) |
| (He et al., 2017) + ELMo (Peters et al., 2018) | 84.6 | [Deep contextualized word representations](https://arxiv.org/abs/1802.05365) |
| Tan et al. (2018) | 82.7 | [Deep Semantic Role Labeling with Self-Attention](https://arxiv.org/abs/1712.01586) |
| He et al. (2018) | 82.1 | [Jointly Predicting Predicates and Arguments in Neural Semantic Role Labeling](http://aclweb.org/anthology/P18-2058) | 
| He et al. (2017) | 81.7 | [Deep Semantic Role Labeling: What Works and What’s Next](http://aclweb.org/anthology/P17-1044) |

### CoNLL-2005

Models are typically evaluated on the [CoNLL-2005 dataset](https://www.cs.upc.edu/~srlconll/soft.html) based on F1.

| Model           | F1 |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| Tian et al., (2022) + XLNet | 89.80 | [Syntax-driven Approach for Semantic Role Labeling](https://aclanthology.org/2022.lrec-1.772/) | [Official](https://github.com/synlp/SRL-MM) |
| He et al., (2018) + ELMO | 87.4 | [Jointly Predicting Predicates and Arguments in Neural Semantic Role Labeling](http://aclweb.org/anthology/P18-2058) |
| He et al. (2018) | 83.9 | [Jointly Predicting Predicates and Arguments in Neural Semantic Role Labeling](http://aclweb.org/anthology/P18-2058) |
| Tan et al. (2018) | 82.9 | [Deep Semantic Role Labeling with Self-Attention](https://arxiv.org/abs/1712.01586) | 
| He et al. (2017) | 81.5 | [Deep Semantic Role Labeling: What Works and What’s Next](http://aclweb.org/anthology/P17-1044) |

[Go back to the README](../README.md)
