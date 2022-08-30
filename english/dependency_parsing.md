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

| Model                                                                        |  POS  |  UAS  |  LAS  | Paper / Source                                                                                                                    | Code                                                                           |
| ---------------------------------------------------------------------------- | :---: | :---: | :---: | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Label Attention Layer + HPSG + XLNet (Mrini et al., 2019)                    | 97.3  | 97.42 | 96.26 | [Rethinking Self-Attention: Towards Interpretability for Neural Parsing](https://khalilmrini.github.io/Label_Attention_Layer.pdf) | [Official](https://github.com/KhalilMrini/LAL-Parser)                          |
| ACE + fine-tune (Wang et al., 2020) | - | 97.20 | 95.80 | [Automated Concatenation of Embeddings for Structured Prediction](https://arxiv.org/pdf/2010.05006.pdf) | [Official](https://github.com/Alibaba-NLP/ACE)|
| HPSG Parser (Joint) + XLNet (Zhou et al, 2020)                            | 97.3  | 97.20 | 95.72 | [Head-Driven Phrase Structure Grammar Parsing on Penn Treebank](https://www.aclweb.org/anthology/2020.findings-emnlp.398.pdf)                        | [Official](https://github.com/DoodleJZ/HPSG-Neural-Parser)                     |
| Second-Order MFVI + BERT (Wang et al., 2020) | - | 96.91 | 95.34 | [Second-Order Neural Dependency Parsing with Message Passing and End-to-End Training](https://arxiv.org/pdf/2010.05003.pdf) | [Official](https://github.com/wangxinyu0922/Second_Order_Parsing)|
| CVT + Multi-Task (Clark et al., 2018)                                        | 97.74 | 96.61 | 95.02 | [Semi-Supervised Sequence Modeling with Cross-View Training](https://arxiv.org/abs/1809.08370)                                    | [Official](https://github.com/tensorflow/models/tree/master/research/cvt_text) |
| CRF Parser (Zhang et al., 2020)                                              |   -   | 96.14 | 94.49 | [Efficient Second-Order TreeCRF for Neural Dependency Parsing](https://www.aclweb.org/anthology/2020.acl-main.302)                | [Official](https://github.com/yzhangcs/crfpar)                                 |
| Second-Order MFVI (Wang et al., 2020) | - | 96.12 | 94.47 | [Second-Order Neural Dependency Parsing with Message Passing and End-to-End Training](https://arxiv.org/pdf/2010.05003.pdf) | [Official](https://github.com/wangxinyu0922/Second_Order_Parsing)|
| Left-to-Right Pointer Network (Fernández-González and Gómez-Rodríguez, 2019) | 97.3  | 96.04 | 94.43 | [Left-to-Right Dependency Parsing with Pointer Networks](https://www.aclweb.org/anthology/N19-1076)                               | [Official](https://github.com/danifg/Left2Right-Pointer-Parser)                |
| Graph-based parser with GNNs (Ji et al., 2019)                               | 97.3  | 95.97 | 94.31 | [Graph-based Dependency Parsing with Graph Neural Networks](https://www.aclweb.org/anthology/P19-1237)                            |                                                                                |
| Deep Biaffine (Dozat and Manning, 2017)                                      | 97.3  | 95.74 | 94.08 | [Deep Biaffine Attention for Neural Dependency Parsing](https://arxiv.org/abs/1611.01734)                                         | [Official](https://github.com/tdozat/Parser-v1)                                |
| jPTDP (Nguyen and Verspoor, 2018)                                            | 97.97 | 94.51 | 92.87 | [An improved neural network model for joint POS tagging and dependency parsing](https://arxiv.org/abs/1807.03955)                 | [Official](https://github.com/datquocnguyen/jPTDP)                             |
| Andor et al. (2016)                                                          | 97.44 | 94.61 | 92.79 | [Globally Normalized Transition-Based Neural Networks](https://www.aclweb.org/anthology/P16-1231)                                 |                                                                                |
| Distilled neural FOG (Kuncoro et al., 2016)                                  | 97.3  | 94.26 | 92.06 | [Distilling an Ensemble of Greedy Dependency Parsers into One MST Parser](https://arxiv.org/abs/1609.07561)                       |                                                                                |
| Distilled transition-based parser (Liu et al., 2018)                         | 97.3  | 94.05 | 92.14 | [Distilling Knowledge for Search-based Structured Prediction](http://aclweb.org/anthology/P18-1129)                               | [Official](https://github.com/Oneplus/twpipe)                                  |
| Weiss et al. (2015)                                                          | 97.44 | 93.99 | 92.05 | [Structured Training for Neural Network Transition-Based Parsing](http://anthology.aclweb.org/P/P15/P15-1032.pdf)                 |                                                                                |
| BIST transition-based parser (Kiperwasser and Goldberg, 2016)                | 97.3  | 93.9  | 91.9  | [Simple and Accurate Dependency Parsing Using Bidirectional LSTM Feature Representations](https://aclweb.org/anthology/Q16-1023)  | [Official](https://github.com/elikip/bist-parser/tree/master/barchybrid/src)   |
| Arc-hybrid (Ballesteros et al., 2016)                                        | 97.3  | 93.56 | 91.42 | [Training with Exploration Improves a Greedy Stack-LSTM Parser](https://arxiv.org/abs/1603.03793)                                 |                                                                                |
| BIST graph-based parser (Kiperwasser and Goldberg, 2016)                     | 97.3  | 93.1  | 91.0  | [Simple and Accurate Dependency Parsing Using Bidirectional LSTM Feature Representations](https://aclweb.org/anthology/Q16-1023)  | [Official](https://github.com/elikip/bist-parser/tree/master/bmstparser/src)   |

### Universal Dependencies

The focus of the task is learning syntactic dependency parsers that can work in a real-world setting, starting from raw text, and that can work over many typologically different languages, even low-resource languages for which there is little or no training data, by exploiting a common syntactic annotation standard. This task has been made possible by the Universal Dependencies initiative (UD, http://universaldependencies.org), which has developed treebanks for 60+ languages with cross-linguistically consistent annotation and recoverability of the original raw texts.

Participating systems will have to find labeled syntactic dependencies between words, i.e. a syntactic head for each word, and a label classifying the type of the dependency relation. In addition to syntactic dependencies, prediction of morphology and lemmatization will be evaluated. There will be multiple test sets in various languages but all data sets will adhere to the common annotation style of UD. Participants will be asked to parse raw text where no gold-standard pre-processing (tokenization, lemmas, morphology) is available. Data preprocessed by a baseline system (UDPipe, https://ufal.mff.cuni.cz/udpipe) was provided so that the participants could focus on improving just one part of the processing pipeline. The organizers believed that this made the task reasonably accessible for everyone.

| Model                     |  LAS  | MLAS  | BLEX  | Paper / Source                                                                                                                                              | Code                                                                 |
| ------------------------- | :---: | :---: | :---: | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Stanford (Qi et al.)      | 74.16 | 62.08 | 65.28 | [Universal Dependency Parsing from Scratch](https://arxiv.org/pdf/1901.10457.pdf)                                                                           | [Official](https://github.com/stanfordnlp/stanfordnlp)               |
| UDPipe Future (Straka)    | 73.11 | 61.25 | 64.49 | [UDPipe 2.0 Prototype at CoNLL 2018 UD Shared Task](https://www.aclweb.org/anthology/K18-2020)                                                              | [Official](https://github.com/CoNLL-UD-2018/UDPipe-Future)           |
| HIT-SCIR (Che et al.)     | 75.84 | 59.78 | 65.33 | [Towards Better UD Parsing: Deep Contextualized Word Embeddings, Ensemble, and Treebank Concatenation](https://arxiv.org/abs/1807.03121)                    |                                                                      |
| TurkuNLP (Kanerva et al.) | 73.28 | 60.99 | 66.09 | [Turku Neural Parser Pipeline: An End-to-End System for the CoNLL 2018 Shared Task](https://universaldependencies.org/conll18/proceedings/pdf/K18-2013.pdf) | [Official](https://github.com/TurkuNLP/Turku-neural-parser-pipeline) |

The following results are just for references:

| Model                                                                  |  UAS  |  LAS  | Note                           | Paper / Source                                                                                    |
| ---------------------------------------------------------------------- | :---: | :---: | ------------------------------ | ------------------------------------------------------------------------------------------------- |
| Stack-only RNNG (Kuncoro et al., 2017)                                 | 95.8  | 94.6  | Constituent parser             | [What Do Recurrent Neural Network Grammars Learn About Syntax?](https://arxiv.org/abs/1611.05774) |
| Deep Biaffine (Dozat and Manning, 2017)                                | 95.75 | 94.22 | Stanford conversion **v3.5.0** | [Deep Biaffine Attention for Neural Dependency Parsing](https://arxiv.org/abs/1611.01734)         |
| Semi-supervised LSTM-LM (Choe and Charniak, 2016) (Constituent parser) | 95.9  | 94.1  | Constituent parser             | [Parsing as Language Modeling](http://www.aclweb.org/anthology/D16-1257)                          |

# Cross-lingual zero-shot dependency parsing

Cross-lingual zero-shot parsing is the task of inferring the dependency parse of sentences from one language without any labeled training trees for that language.

## Universal Dependency Treebank

Models are evaluated against the [Universal Dependency Treebank v2.0](https://github.com/ryanmcd/uni-dep-tb). For each of the 6 target languages, models can use the trees of all other languages and English and are evaluated by the UAS and LAS on the target. The final score is the average score across the 6 target languages. The most common evaluation setup is to use
gold POS-tags.

| Model                                      |  UAS  |  LAS  | Paper / Source                                                                                                                               | Code                                                          |
| ------------------------------------------ | :---: | :---: | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| XLM-R + SubDP (Shi et al., 2022) | --- | 79.6* | [Substructure Distribution Projection for Zero-Shot Cross-Lingual Dependency Parsing](https://aclanthology.org/2022.acl-long.452/) | [Official](https://aclanthology.org/attachments/2022.acl-long.452.software.zip)
| Cross-Lingual ELMo (Schuster et al., 2019) | 84.2  | 77.3  | [Cross-Lingual Alignment of Contextual Word Embeddings, with Applications to Zero-shot Dependency Parsing](https://arxiv.org/abs/1902.09492) | [Official](https://github.com/TalSchuster/CrossLingualELMo)   |
| MALOPA (Ammar et al., 2016)                |       | 70.5  | [Many Languages, One Parser](https://www.transacl.org/ojs/index.php/tacl/article/view/892)                                                   | [Official](https://github.com/clab/language-universal-parser) |
| Guo et al. (2016)                          | 76.7  | 69.9  | [A representation learning framework for multi-source transfer parsing](https://dl.acm.org/citation.cfm?id=3016100.3016284)                  |

*: Evaluated on four target languages.

# Unsupervised dependency parsing

Unsupervised dependency parsing is the task of inferring the dependency parse of sentences without any labeled training data.

## Penn Treebank

As with supervised parsing, models are evaluated against the Penn Treebank. The most common evaluation setup is to use
gold POS-tags as input and to evaluate systems using the unlabeled attachment score (also called 'directed dependency
accuracy').

| Model                                                |  UAS  | Paper / Source                                                                                                                                        |
| ---------------------------------------------------- | :---: | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Iterative reranking (Le & Zuidema, 2015)             | 66.2  | [Unsupervised Dependency Parsing - Let’s Use Supervised Parsers](http://www.aclweb.org/anthology/N15-1067)                                            |
| Combined System (Spitkovsky et al., 2013)            | 64.4  | [Breaking Out of Local Optima with Count Transforms and Model Recombination - A Study in Grammar Induction](http://www.aclweb.org/anthology/D13-1204) |
| Tree Substitution Grammar DMV (Blunsom & Cohn, 2010) | 55.7  | [Unsupervised Induction of Tree Substitution Grammars for Dependency Parsing](http://www.aclweb.org/anthology/D10-1117)                               |
| Shared Logistic Normal DMV (Cohen & Smith, 2009)     | 41.4  | [Shared Logistic Normal Distributions for Soft Parameter Tying in Unsupervised Grammar Induction](http://www.aclweb.org/anthology/N09-1009)           |
| DMV (Klein & Manning, 2004)                          | 35.9  | [Corpus-Based Induction of Syntactic Structure - Models of Dependency and Constituency](http://www.aclweb.org/anthology/P04-1061)                     |

[Go back to the README](../README.md)
