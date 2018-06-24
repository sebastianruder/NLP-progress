## Dependency parsing

Dependency parsing is the task of extracting a dependency parse of a sentence that represents its grammatical
structure and defines the relationships between "head" words and words, which modify those heads.

Example:

```
     root
      |
      | +-------dobj---------+
      | |                    |
nsubj | |   +------det-----+ | +-----nmod------+
+--+  | |   |              | | |               |
|  |  | |   |      +-nmod-+| | |      +-case-+ |
+  |  + |   +      +      || + |      +      | |
I  prefer  the  morning   flight  through  Denver
```

Relations among the words are illustrated above the sentence with directed, labeled
arcs from heads to dependents (+ indicates the dependent).

### Penn Treebank&mdash;dependency parsing

Models are evaluated on the [Stanford Dependency](https://nlp.stanford.edu/software/dependencies_manual.pdf)
conversion of the Penn Treebank with predicted POS-tags. Punctuation symbols
are excluded from the evaluation. Evaluation metrics are unlabeled attachment score (UAS) and
labeled attachment score (LAS).

| Model           | UAS | LAS | Paper / Source |
| ------------- | :-----:| :-----:| --- |
| Stack-only RNNG (Kuncoro et al., 2017) | 95.8 | 94.6 | [What Do Recurrent Neural Network Grammars Learn About Syntax?](https://arxiv.org/abs/1611.05774) |
| Semi-supervised LSTM-LM (Choe and Charniak, 2016) | 95.9 | 94.1 | [Parsing as Language Modeling](http://www.aclweb.org/anthology/D16-1257) | 
| Deep Biaffine (Dozat and Manning, 2017) | 95.66 | 94.03 | [Deep Biaffine Attention for Neural Dependency Parsing](https://arxiv.org/abs/1611.01734) | 
| Andor et al. (2016) | 94.61 | 92.79 | [Globally Normalized Transition-Based Neural Networks](https://www.aclweb.org/anthology/P16-1231) |
| Distilled neural FOG (Kuncoro et al., 2016) | 94.26 | 92.06 | [Distilling an Ensemble of Greedy Dependency Parsers into One MST Parser](https://arxiv.org/abs/1609.07561) | 
| Weiss et al. (2015) | 94.0 | 92.0 | [Structured Training for Neural Network Transition-Based Parsing](http://anthology.aclweb.org/P/P15/P15-1032.pdf) |
| Arc-hybrid (Ballesteros et al., 2016) | 93.56 | 91.42 | [Training with Exploration Improves a Greedy Stack-LSTM Parser](https://arxiv.org/abs/1603.03793) |
| BIST parser (Kiperwasser and Goldberg, 2016) | 93.2 | 91.2 | [Simple and Accurate Dependency Parsing Using Bidirectional LSTM Feature Representations](https://aclweb.org/anthology/Q16-1023) |

[Go back to the README](README.md)
