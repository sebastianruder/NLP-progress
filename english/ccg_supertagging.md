# CCG supertagging

Combinatory Categorical Grammar (CCG; [Steedman, 2000](http://www.citeulike.org/group/14833/article/8971002)) is a
highly lexicalized formalism. The standard parsing model of [Clark and Curran (2007)](https://www.mitpressjournals.org/doi/abs/10.1162/coli.2007.33.4.493)
uses over 400 lexical categories (or _supertags_), compared to about 50 part-of-speech tags for typical parsers.

Example:

| Vinken | , | 61 | years | old |
| --- | ---| --- | --- | --- |
| N| , | N/N | N | (S[adj]\ NP)\ NP |

### CCGBank

The CCGBank is a corpus of CCG derivations and dependency structures extracted from the Penn Treebank by
[Hockenmaier and Steedman (2007)](http://www.aclweb.org/anthology/J07-3004). Sections 2-21 are used for training,
section 00 for development, and section 23 as in-domain test set.
Performance is only calculated on the 425 most frequent labels. Models are evaluated based on accuracy.

| Model           | Accuracy |  Paper / Source |
| ------------- | :-----:| --- |
| Clark et al. (2018) | 96.1 | [Semi-Supervised Sequence Modeling with Cross-View Training](https://arxiv.org/abs/1809.08370) |
| Lewis et al. (2016) | 94.7 | [LSTM CCG Parsing](https://aclweb.org/anthology/N/N16/N16-1026.pdf) |
| Vaswani et al. (2016) | 94.24 | [Supertagging with LSTMs](https://aclweb.org/anthology/N/N16/N16-1027.pdf) |
| Low supervision (Søgaard and Goldberg, 2016) | 93.26 | [Deep multi-task learning with low level tasks supervised at lower layers](http://anthology.aclweb.org/P16-2038) |
| Xu et al. (2015) | 93.00 | [CCG Supertagging with a Recurrent Neural Network](http://www.aclweb.org/anthology/P15-2041) |

[Go back to the README](../README.md)
