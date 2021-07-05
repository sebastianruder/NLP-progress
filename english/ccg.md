# Combinatory Categorical Grammar

Combinatory Categorical Grammar (CCG; [Steedman, 2000](http://www.citeulike.org/group/14833/article/8971002)) is a
highly lexicalized formalism. The standard parsing model of [Clark and Curran (2007)](https://www.mitpressjournals.org/doi/abs/10.1162/coli.2007.33.4.493)
uses over 400 lexical categories (or _supertags_), compared to about 50 part-of-speech tags for typical parsers.

Example:

| Vinken | , | 61 | years | old |
| --- | ---| --- | --- | --- |
| N| , | N/N | N | (S[adj]\ NP)\ NP |

## Parsing

CCG parsing is evaluated in terms of labeled dependency F-score, which "take\[s\] into account the lexical category containing the dependency relation, the argument slot, the word associated with the lexical category, and the argument head word: All four must be correct to score a point" ([Clark & Curran, 2007](https://doi.org/10.1162/coli.2007.33.4.493)).
Besides the word forms, some popular parsers (like the C&C parser) take POS tags as input. For fair comparison, systems should use automatically obtained POS as input, though some papers additionally report performance with oracle gold-standard POS features.

### CCGBank

The CCGBank is a corpus of CCG derivations and dependency structures extracted from the Penn Treebank by
[Hockenmaier and Steedman (2007)](http://www.aclweb.org/anthology/J07-3004). Sections 2-21 are used for training,
section 00 for development, and section 23 as in-domain test set.

| Model           | Labeled F-score |  Paper / Source |
| ------------- | :-----:| --- |
| Prange et al. (2021), non-constructive | 90.91 | [Supertagging the Long Tail with Tree-Structured Decoding of Complex Categories](https://doi.org/10.1162/tacl_a_00364) |
| Bhargava and Penn (2020), constructive | 90.9 | [Supertagging with CCG primitives](https://www.aclweb.org/anthology/2020.repl4nlp-1.23/) |
| Prange et al. (2021), constructive | 90.79 | [Supertagging the Long Tail with Tree-Structured Decoding of Complex Categories](https://doi.org/10.1162/tacl_a_00364) |
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

To mitigate sparsity, CCG supertaggers have traditionally been trained only on categories that occur 10 times or more in the CCGBank training data, which amounts to the 425 most frequent categories. In more recent work, using this threshold is becoming less common. In any case, supertagging evaluation is always measured for all supertags occurring in the test set. Models are evaluated based on token accuracy.

### Constructive supertagging

A constructive tagger models the internal structure of supertags rather than treating each supertag type as opaque ([Kogkalidis et al., 2019](https://www.aclweb.org/anthology/W19-4314/)). Supertags are constructed from minimal pieces (which for CCG are slashes and atomic categories) and there is no frequency cutoff.

### CCGBank

Like for parsing, sections 2-21 are used for training, section 00 for development, and section 23 as in-domain test set.

| Model           | Accuracy |  Paper / Source |
| ----------------- | :-----:| --- |
| Prange et al. (2021), non-constructive | 96.22 | [Supertagging the Long Tail with Tree-Structured Decoding of Complex Categories](https://doi.org/10.1162/tacl_a_00364) |
| Prange et al. (2021), constructive | 96.09 | [Supertagging the Long Tail with Tree-Structured Decoding of Complex Categories](https://doi.org/10.1162/tacl_a_00364) |
| Clark et al. (2018) | 96.05 | [Semi-Supervised Sequence Modeling with Cross-View Training](https://arxiv.org/abs/1809.08370) |
| Bhargava and Penn (2020), constructive | 96.00 | [Supertagging with CCG primitives](https://www.aclweb.org/anthology/2020.repl4nlp-1.23/) |
| Lewis et al. (2016) | 94.7 | [LSTM CCG Parsing](https://aclweb.org/anthology/N/N16/N16-1026.pdf) |
| Vaswani et al. (2016) | 94.24 | [Supertagging with LSTMs](https://aclweb.org/anthology/N/N16/N16-1027.pdf) |
| Low supervision (Søgaard and Goldberg, 2016) | 93.26 | [Deep multi-task learning with low level tasks supervised at lower layers](http://anthology.aclweb.org/P16-2038) |
| Xu et al. (2015) | 93.00 | [CCG Supertagging with a Recurrent Neural Network](http://www.aclweb.org/anthology/P15-2041) |
| Clark and Curran (2004) | 92.00 | [The Importance of Supertagging for Wide-Coverage CCG Parsing](https://aclweb.org/anthology/papers/C/C04/C04-1041/) (result from Lewis et al. (2016)) |

#### Rare and unseen supertags

| Model           | Acc on tags seen 1-9 times | Acc on unseen tags |  Paper / Source |
| ------------- | :-----: | :-----: | --- |
| Bhargava and Penn (2020), constructive | - | 5.00 | [Supertagging with CCG primitives](https://www.aclweb.org/anthology/2020.repl4nlp-1.23/) |
| Prange et al. (2021), constructive | 37.40 | 3.03 | [Supertagging the Long Tail with Tree-Structured Decoding of Complex Categories](https://doi.org/10.1162/tacl_a_00364) |
| Prange et al. (2021), non-constructive | 23.17 | 0.00 | [Supertagging the Long Tail with Tree-Structured Decoding of Complex Categories](https://doi.org/10.1162/tacl_a_00364) |

### Wikipedia

| Model           | Accuracy |  Paper / Source |
| ------------- | :-----: | --- |
| Prange et al. (2021), non-constructive | 92.54 | [Supertagging the Long Tail with Tree-Structured Decoding of Complex Categories](https://doi.org/10.1162/tacl_a_00364) |
| Prange et al. (2021), constructive | 92.46 | [Supertagging the Long Tail with Tree-Structured Decoding of Complex Categories](https://doi.org/10.1162/tacl_a_00364) |
| Xu et al. (2015) | 90.00 | [CCG Supertagging with a Recurrent Neural Network](http://www.aclweb.org/anthology/P15-2041) |

## Conversion to PTB

There has been interest in converting CCG derivations to phrase structure parses for comparison with phrase structure parsers (since CCGBank is based on the PTB).

| Model           | Accuracy |  Paper / Source |
| ------------- | :-----:| --- |
| Kummerfeld et al. (2012) | 96.30 | [Robust Conversion of CCG Derivations to Phrase Structure Trees](https://www.aclweb.org/anthology/P12-2021) |
| Zhang et al. (2012) | 95.71 | [A Machine Learning Approach to Convert CCGbank to Penn Treebank](https://www.aclweb.org/anthology/C12-3067)
| Clark and Curran (2009) | 94.64 | [Comparing the Accuracy of CCG and Penn Treebank Parsers](https://aclweb.org/anthology/papers/P/P09/P09-2014/) |

[Go back to the README](../README.md)
