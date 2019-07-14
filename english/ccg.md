# Combinatory Categorical Grammar

Combinatory Categorical Grammar (CCG; [Steedman, 2000](http://www.citeulike.org/group/14833/article/8971002)) is a
highly lexicalized formalism. The standard parsing model of [Clark and Curran (2007)](https://www.mitpressjournals.org/doi/abs/10.1162/coli.2007.33.4.493)
uses over 400 lexical categories (or _supertags_), compared to about 50 part-of-speech tags for typical parsers.

Example:

| Vinken | , | 61 | years | old |
| --- | ---| --- | --- | --- |
| N| , | N/N | N | (S[adj]\ NP)\ NP |

## Parsing

### CCGBank

The CCGBank is a corpus of CCG derivations and dependency structures extracted from the Penn Treebank by
[Hockenmaier and Steedman (2007)](http://www.aclweb.org/anthology/J07-3004). Sections 2-21 are used for training,
section 00 for development, and section 23 as in-domain test set. Some work

| Model           | Accuracy |  Paper / Source |
| ------------- | :-----:| --- |
| Vaswani et al. (2016) | 88.32 | [Supertagging with LSTMs](https://aclweb.org/anthology/N/N16/N16-1027.pdf) |
| Lewis et al. (2016) | 88.1 | [LSTM CCG Parsing](https://aclweb.org/anthology/N/N16/N16-1026.pdf) |
| Xu et al. (2015) | 87.04 | [CCG Supertagging with a Recurrent Neural Network](http://www.aclweb.org/anthology/P15-2041) |
| Kummerfeld et al. (2010), with additional unlabeled data | 85.95 | [Faster Parsing by Supertagger Adaptation](https://www.aclweb.org/anthology/papers/P/P10/P10-1036/) |
| Clark and Curran (2007) | 85.45 | [Wide-Coverage Efficient Statistical Parsing with CCG and Log-Linear Models](https://www.aclweb.org/anthology/J07-4004) |

### Wikipedia

| Model           | Accuracy |  Paper / Source |
| ------------- | :-----:| --- |
| Xu et al. (2015) | 82.49 | [CCG Supertagging with a Recurrent Neural Network](http://www.aclweb.org/anthology/P15-2041) |
| Kummerfeld et al. (2010), with additional unlabeled data | 81.7 | [Faster Parsing by Supertagger Adaptation](https://www.aclweb.org/anthology/papers/P/P10/P10-1036/) |

### Bioinfer

| Model         | Bio specifc taggers? | Accuracy |  Paper / Source |
| ------------- | -------------------- | :-------:| --- |
| Kummerfeld et al. (2010), with additional unlabeled data | Yes | 82.3 | [Faster Parsing by Supertagger Adaptation](https://www.aclweb.org/anthology/papers/P/P10/P10-1036/) |
| Rimell and Clark (2008) | Yes | 81.5 | [Adapting a Lexicalized-Grammar Parser to Contrasting Domains](https://aclweb.org/anthology/papers/D/D08/D08-1050/) |
| Xu et al. (2015) | No | 77.74 | [CCG Supertagging with a Recurrent Neural Network](http://www.aclweb.org/anthology/P15-2041) |
| Kummerfeld et al. (2010), with additional unlabeled data | No | 76.1 | [Faster Parsing by Supertagger Adaptation](https://www.aclweb.org/anthology/papers/P/P10/P10-1036/) |
| Rimell and Clark (2008) | No | 76.0 | [Adapting a Lexicalized-Grammar Parser to Contrasting Domains](https://aclweb.org/anthology/papers/D/D08/D08-1050/) |

## Supertagging

### CCGBank

For Supertagging evaluation on CCGBank, performance is only calculated over the 425 most frequent labels. Models are evaluated based on accuracy.

| Model           | Accuracy |  Paper / Source |
| ------------- | :-----:| --- |
| Clark et al. (2018) | 96.1 | [Semi-Supervised Sequence Modeling with Cross-View Training](https://arxiv.org/abs/1809.08370) |
| Lewis et al. (2016) | 94.7 | [LSTM CCG Parsing](https://aclweb.org/anthology/N/N16/N16-1026.pdf) |
| Vaswani et al. (2016) | 94.24 | [Supertagging with LSTMs](https://aclweb.org/anthology/N/N16/N16-1027.pdf) |
| Low supervision (Søgaard and Goldberg, 2016) | 93.26 | [Deep multi-task learning with low level tasks supervised at lower layers](http://anthology.aclweb.org/P16-2038) |
| Xu et al. (2015) | 93.00 | [CCG Supertagging with a Recurrent Neural Network](http://www.aclweb.org/anthology/P15-2041) |
| Clark and Curran (2004) | 92.00 | [The Importance of Supertagging for Wide-Coverage CCG Parsing](https://aclweb.org/anthology/papers/C/C04/C04-1041/) (result from Lewis et al. (2016)) |

## Conversion to PTB

There has been interest in converting CCG derivations to phrase structure parses for comparison with phrase structure parsers (since CCGBank is based on the PTB).

| Model           | Accuracy |  Paper / Source |
| ------------- | :-----:| --- |
| Kummerfeld et al. (2012) | 96.30 | [Robust Conversion of CCG Derivations to Phrase Structure Trees](https://www.aclweb.org/anthology/P12-2021) |
| Zhang et al. (2012) | 95.71 | [A Machine Learning Approach to Convert CCGbank to Penn Treebank](https://www.aclweb.org/anthology/C12-3067)
| Clark and Curran (2009) | 94.64 | [Comparing the Accuracy of CCG and Penn Treebank Parsers](https://aclweb.org/anthology/papers/P/P09/P09-2014/) |

[Go back to the README](../README.md)
