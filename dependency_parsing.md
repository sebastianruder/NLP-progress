# Dependency parsing

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

### Penn Treebank

Models are evaluated on the [Stanford Dependency](https://nlp.stanford.edu/software/dependencies_manual.pdf)
conversion (**v3.3.0**) of the Penn Treebank with __predicted__ POS-tags. Punctuation symbols
are excluded from the evaluation. Evaluation metrics are unlabeled attachment score (UAS) and
labeled attachment score (LAS). Here, we also mention the predicted POS tagging accuracy.

| Model           | POS | UAS | LAS | Paper / Source | Code |
| ------------- | :-----: | :-----:| :-----:| --- | --- |
| Deep Biaffine (Dozat and Manning, 2017) | 97.3 | 95.44 | 93.76 | [Deep Biaffine Attention for Neural Dependency Parsing](https://arxiv.org/abs/1611.01734) | [Official](https://github.com/tdozat/Parser-v1) |
| jPTDP (Nguyen and Verspoor, 2018) | 97.97 | 94.51 | 92.87  | [An improved neural network model for joint POS tagging and dependency parsing](https://arxiv.org/abs/1807.03955) | [Official](https://github.com/datquocnguyen/jPTDP) |
| Andor et al. (2016) | 97.44 | 94.61 | 92.79 | [Globally Normalized Transition-Based Neural Networks](https://www.aclweb.org/anthology/P16-1231) | |
| Distilled neural FOG (Kuncoro et al., 2016) | 97.3 | 94.26 | 92.06 | [Distilling an Ensemble of Greedy Dependency Parsers into One MST Parser](https://arxiv.org/abs/1609.07561) | |
| Weiss et al. (2015) | 97.44 | 93.99 | 92.05 | [Structured Training for Neural Network Transition-Based Parsing](http://anthology.aclweb.org/P/P15/P15-1032.pdf) | |
| BIST transition-based parser (Kiperwasser and Goldberg, 2016) | 97.3 | 93.9 | 91.9 | [Simple and Accurate Dependency Parsing Using Bidirectional LSTM Feature Representations](https://aclweb.org/anthology/Q16-1023) | [Official](https://github.com/elikip/bist-parser/tree/master/barchybrid/src) | 
| Arc-hybrid (Ballesteros et al., 2016) | 97.3 | 93.56 | 91.42 | [Training with Exploration Improves a Greedy Stack-LSTM Parser](https://arxiv.org/abs/1603.03793) | |
| BIST graph-based parser (Kiperwasser and Goldberg, 2016) | 97.3 | 93.1 | 91.0 | [Simple and Accurate Dependency Parsing Using Bidirectional LSTM Feature Representations](https://aclweb.org/anthology/Q16-1023) | [Official](https://github.com/elikip/bist-parser/tree/master/bmstparser/src) | 

The following results are just for references:

| Model           | UAS | LAS | Paper / Source | Note | 
| ------------- | :-----:| :-----:| --- | --- | 
| Stack-only RNNG (Kuncoro et al., 2017) | 95.8 | 94.6 | [What Do Recurrent Neural Network Grammars Learn About Syntax?](https://arxiv.org/abs/1611.05774) | Constituent parser |
| Semi-supervised LSTM-LM (Choe and Charniak, 2016) (Constituent parser) | 95.9 | 94.1 | [Parsing as Language Modeling](http://www.aclweb.org/anthology/D16-1257) | Constituent parser |
| Deep Biaffine (Dozat and Manning, 2017)   | 95.66 | 94.03 | [Deep Biaffine Attention for Neural Dependency Parsing](https://arxiv.org/abs/1611.01734) | Stanford conversion **v3.5.0** |

[Go back to the README](README.md)
