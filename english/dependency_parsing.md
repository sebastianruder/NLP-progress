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
are excluded from the evaluation. Evaluation metrics are unlabeled attachment score (UAS) and labeled attachment score (LAS). UAS does not consider the semantic relation (e.g. Subj) used to label the attachment between the head and the child, while LAS requires a semantic correct label for each attachment.Here, we also mention the predicted POS tagging accuracy.

| Model           | POS | UAS | LAS | Paper / Source | Code |
| ------------- | :-----: | :-----:| :-----:| --- | --- |
| CVT + Multi-Task (Clark et al., 2018) | ---  | 96.61 | 95.02 | [Semi-Supervised Sequence Modeling with Cross-View Training](https://arxiv.org/abs/1809.08370) | [Official](https://github.com/tensorflow/models/tree/master/research/cvt_text) |
| Deep Biaffine (Dozat and Manning, 2017) | 97.3 | 95.44 | 93.76 | [Deep Biaffine Attention for Neural Dependency Parsing](https://arxiv.org/abs/1611.01734) | [Official](https://github.com/tdozat/Parser-v1) |
| jPTDP (Nguyen and Verspoor, 2018) | 97.97 | 94.51 | 92.87  | [An improved neural network model for joint POS tagging and dependency parsing](https://arxiv.org/abs/1807.03955) | [Official](https://github.com/datquocnguyen/jPTDP) |
| Andor et al. (2016) | 97.44 | 94.61 | 92.79 | [Globally Normalized Transition-Based Neural Networks](https://www.aclweb.org/anthology/P16-1231) | |
| Distilled neural FOG (Kuncoro et al., 2016) | 97.3 | 94.26 | 92.06 | [Distilling an Ensemble of Greedy Dependency Parsers into One MST Parser](https://arxiv.org/abs/1609.07561) | |
| Distilled transition-based parser (Liu et al., 2018) | 97.3 | 94.05 | 92.14 | [Distilling Knowledge for Search-based Structured Prediction](http://aclweb.org/anthology/P18-1129) | [Official](https://github.com/Oneplus/twpipe) |
| Weiss et al. (2015) | 97.44 | 93.99 | 92.05 | [Structured Training for Neural Network Transition-Based Parsing](http://anthology.aclweb.org/P/P15/P15-1032.pdf) | |
| BIST transition-based parser (Kiperwasser and Goldberg, 2016) | 97.3 | 93.9 | 91.9 | [Simple and Accurate Dependency Parsing Using Bidirectional LSTM Feature Representations](https://aclweb.org/anthology/Q16-1023) | [Official](https://github.com/elikip/bist-parser/tree/master/barchybrid/src) | 
| Arc-hybrid (Ballesteros et al., 2016) | 97.3 | 93.56 | 91.42 | [Training with Exploration Improves a Greedy Stack-LSTM Parser](https://arxiv.org/abs/1603.03793) | |
| BIST graph-based parser (Kiperwasser and Goldberg, 2016) | 97.3 | 93.1 | 91.0 | [Simple and Accurate Dependency Parsing Using Bidirectional LSTM Feature Representations](https://aclweb.org/anthology/Q16-1023) | [Official](https://github.com/elikip/bist-parser/tree/master/bmstparser/src) | 

The following results are just for references:

| Model           | UAS | LAS | Note | Paper / Source |  
| ------------- | :-----:| :-----:| --- | --- | 
| Stack-only RNNG (Kuncoro et al., 2017) | 95.8 | 94.6 | Constituent parser |[What Do Recurrent Neural Network Grammars Learn About Syntax?](https://arxiv.org/abs/1611.05774) |
| Semi-supervised LSTM-LM (Choe and Charniak, 2016) (Constituent parser) | 95.9 | 94.1 | Constituent parser |[Parsing as Language Modeling](http://www.aclweb.org/anthology/D16-1257) | 
| Deep Biaffine (Dozat and Manning, 2017)   | 95.66 | 94.03 | Stanford conversion **v3.5.0** | [Deep Biaffine Attention for Neural Dependency Parsing](https://arxiv.org/abs/1611.01734) | 

# Unsupervised dependency parsing

Unsupervised dependency parsing is the task of inferring the dependency parse of sentences without any labeled training data.

## Penn Treebank

As with supervised parsing, models are evaluated against the Penn Treebank. The most common evaluation setup is to use
gold POS-tags as input and to evaluate systems using the unlabeled attachment score (also called 'directed dependency
accuracy').
  
| Model           | UAS | Paper / Source |  
| ------------- | :-----:| ---- | 
| Iterative reranking (Le & Zuidema, 2015) | 66.2 | [Unsupervised Dependency Parsing - Let’s Use Supervised Parsers](http://www.aclweb.org/anthology/N15-1067) |
| Combined System (Spitkovsky et al., 2013) | 64.4 | [Breaking Out of Local Optima with Count Transforms and Model Recombination - A Study in Grammar Induction](http://www.aclweb.org/anthology/D13-1204) |
| Tree Substitution Grammar DMV (Blunsom & Cohn, 2010) | 55.7 | [Unsupervised Induction of Tree Substitution Grammars for Dependency Parsing](http://www.aclweb.org/anthology/D10-1117) |
| Shared Logistic Normal DMV (Cohen & Smith, 2009) | 41.4 | [Shared Logistic Normal Distributions for Soft Parameter Tying in Unsupervised Grammar Induction](http://www.aclweb.org/anthology/N09-1009) |
| DMV (Klein & Manning, 2004) | 35.9 | [Corpus-Based Induction of Syntactic Structure - Models of Dependency and Constituency](http://www.aclweb.org/anthology/P04-1061) |

[Go back to the README](../README.md)
