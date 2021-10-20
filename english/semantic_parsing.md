# Semantic parsing

### Table of contents

- [AMR parsing](#amr-parsing)
  - [LDC2014T12](#ldc2014t12)
  - [LDC2015E86](#ldc2015e86)
  - [LDC2016E25](#ldc2016e25)
- [DRS parsing](#drs-parsing)
  - [PMB 2.2.0](#pmb-220)
  - [PMB 3.0.0](#pmb-300)
  - [RST-DT](#rst-dt)
- [UCCA parsing](#ucca-parsing)
  - [SemEval 2019 Task 1](semeval-2019-task-1)
  - [CoNLL 2019](conll-2019)
- [Semantic Dependency Parsing](#semantic-dependency-parsing)
  - [SemEval 2015 Task 18](#semeval-2015-task-18)
- [SQL parsing](#sql-parsing)
  - [ATIS](#atis)
  - [Advising](#advising)
  - [GeoQuery](#geoquery)
  - [Scholar](#scholar)
  - [Spider](#spider)
  - [WikiSQL](#wikisql)
  - [Smaller datasets](#smaller-datasets)

Semantic parsing is the task of translating natural language into a formal meaning
representation on which a machine can act. Representations may be an executable language
such as SQL or more abstract representations such as [Abstract Meaning Representation (AMR)](https://en.wikipedia.org/wiki/Abstract_Meaning_Representation)
and [Universal Conceptual Cognitive Annotation (UCCA)](http://www.cs.huji.ac.il/~oabend/ucca.html).

## AMR parsing

Each AMR is a single rooted, directed graph. AMRs include PropBank semantic roles, within-sentence coreference, named entities and types, modality, negation, questions, quantities, and so on. [See](https://amr.isi.edu/index.html).
In the following tables, systems marked with &hearts; are pipeline systems that require POS as input,
&spades; is for those require NER,
&diams; is for those require syntax parsing,
and &clubs; is for those require SRL.

### LDC2014T12:
The dataset contains 13,051 AMRs split across training, dev, and test partitions.

Models are evaluated on the newswire section and the full dataset based on [smatch](https://amr.isi.edu/smatch-13.pdf).

| Model           | F1 Newswire  | F1 Full |  Paper / Source |
| ------------- | :-----:| :-----:| --- |
| APT (Action-Pointer Transformer, Zhou et al., 2021) | -- | 79.8 | [AMR Parsing with Action-Pointer Transformer](https://aclanthology.org/2021.naacl-main.443/) |
| Pushing the Limits of AMR Parsing with Self-Learning (Young-Suk Lee et al., 2020) | -- | 78.2 | [Pushing the Limits of AMR Parsing with Self-Learning](https://arxiv.org/abs/2010.10673) |
| AMR Parsing via Graph-Sequence Iterative Inference (Cai and Lam , 2020)&hearts;&spades; | -- | 75.4 | [AMR Parsing via Graph-Sequence Iterative Inference](https://arxiv.org/pdf/2004.05572.pdf) |
| Broad-Coverage Semantic Parsing as Transduction (Zhang et al., 2019)&hearts; | -- | 71.3 | [Broad-Coverage Semantic Parsing as Transduction](https://www.aclweb.org/anthology/D19-1392.pdf) |
| Two-stage Sequence-to-Graph Transducer (Zhang et al., 2019)&hearts; | -- | 70.2 | [AMR Parsing as Sequence-to-Graph Transduction](https://www.aclweb.org/anthology/P19-1009.pdf) |
| Transition-based+improved aligner+ensemble (Liu et al. 2018)&hearts; | 73.3 | 68.4 | [An AMR Aligner Tuned by Transition-based Parser](http://aclweb.org/anthology/D18-1264) |
| Improved CAMR (Wang and Xue, 2017)&spades;&diams; | --| 68.1| [Getting the Most out of AMR Parsing](http://aclweb.org/anthology/D17-1129) |
| Incremental joint model (Zhou et al., 2016)&hearts;&spades; | 71 | 66 | [AMR Parsing with an Incremental Joint Model](https://aclweb.org/anthology/D16-1065) |
| Transition-based transducer (Wang et al., 2015)&hearts;&diams;&clubs; | 70 | 66 | [Boosting Transition-based AMR Parsing with Refined Actions and Auxiliary Analyzers](http://www.aclweb.org/anthology/P15-2141) |
| Imitation learning  (Goodman et al., 2016)&hearts;&spades; | 70 |  -- | [Noise reduction and targeted exploration in imitation learning for Abstract Meaning Representation parsing](http://www.aclweb.org/anthology/P16-1001) |
| MT-Based (Pust et al., 2015)&spades; | -- | 66 | [Parsing English into Abstract Meaning Representation Using Syntax-Based Machine Translation ](http://www.aclweb.org/anthology/D15-1136)
| Transition-based parser-Stack-LSTM (Ballesteros and Al-Onaizan, 2017)&hearts;&diams; | 69 | 64  | [AMR Parsing using Stack-LSTMs](http://www.aclweb.org/anthology/D17-1130) |
| Transition-based parser-Stack-LSTM (Ballesteros and Al-Onaizan, 2017) | 68 | 63  | [AMR Parsing using Stack-LSTMs](http://www.aclweb.org/anthology/D17-1130) |

### LDC2015E86:
The dataset contains 19,572 AMRs split across training, dev, and test partitions.

Models are evaluated based on [smatch](https://amr.isi.edu/smatch-13.pdf).

| Model           | Smatch  |  Paper / Source |
| ------------- | :-----:| --- |
| Joint model (Lyu and Titov, 2018)&hearts;&spades; | 73.7 | [AMR Parsing as Graph Prediction with Latent Alignment](https://arxiv.org/abs/1805.05286) |
| Mul-BiLSTM (Foland and Martin, 2017)&spades; | 70.7 | [Abstract Meaning Representation Parsing using LSTM Recurrent Neural Networks](http://aclweb.org/anthology/P17-1043) |
| JAMR (Flanigan et al., 2016)&hearts;&diams;&clubs; | 67.0 | [CMU at SemEval-2016 Task 8: Graph-based AMR Parsing with Infinite Ramp Loss](http://www.aclweb.org/anthology/S16-1186) |
| CAMR (Wang et al., 2016)&hearts;&diams;&clubs; | 66.5 | [CAMR at SemEval-2016 Task 8: An Extended Transition-based AMR Parser](http://www.aclweb.org/anthology/S16-1181) |
| AMREager (Damonte et al., 2017)&hearts;&spades;&diams; | 64.0 | [An Incremental Parser for Abstract Meaning Representation](http://www.aclweb.org/anthology/E17-1051) |
| SEQ2SEQ + 20M (Konstas et al., 2017)&spades; | 62.1 | [Neural AMR: Sequence-to-Sequence Models for Parsing and Generation](https://arxiv.org/abs/1704.08381) |

### LDC2017T10 (LDC2016E25):
The dataset contains 39,260 AMRs split across training, dev, and test partitions.

Models are evaluated based on [smatch](https://amr.isi.edu/smatch-13.pdf).

| Model           | Smatch  |  Paper / Source |
| ------------- | :-----:| --- |
| One SPRING to Rule Them Both: Symmetric AMR Semantic Parsing and Generation without a Complex Pipeline (Bevilacqua et al., 2020) | 84.5 | [One SPRING to Rule Them Both: Symmetric AMR Semantic Parsing and Generation without a Complex Pipeline](https://ojs.aaai.org/index.php/AAAI/article/view/17489) |
| APT (Action-Pointer Transformer, Zhou et al., 2021) | 83.4 | [AMR Parsing with Action-Pointer Transformer](https://aclanthology.org/2021.naacl-main.443/) |
| AMR Parsing with Sequence-to-Sequence Pre-training (Xu, et al., 2020) | 81.4 | [Improving AMR Parsing with Sequence-to-Sequence Pre-training](https://arxiv.org/pdf/2010.01771.pdf) |
| Pushing the Limits of AMR Parsing with Self-Learning (Young-Suk Lee et al., 2020) | 81.3 | [Pushing the Limits of AMR Parsing with Self-Learning](https://arxiv.org/abs/2010.10673) |
| AMR Parsing via Graph-Sequence Iterative Inference (Cai and Lam, 2020)&hearts;&spades; | 80.2 | [AMR Parsing via Graph-Sequence Iterative Inference](https://arxiv.org/pdf/2004.05572.pdf) |
| Broad-Coverage Semantic Parsing as Transduction (Zhang et al., 2019)&hearts; | 77.0 | [Broad-Coverage Semantic Parsing as Transduction](https://www.aclweb.org/anthology/D19-1392.pdf) |
| Two-stage Sequence-to-Graph Transducer (Zhang et al., 2019)&hearts; | 76.3 | [AMR Parsing as Sequence-to-Graph Transduction](https://www.aclweb.org/anthology/P19-1009.pdf) |
| Rewarding Smatch: Transition-Based AMR Parsing with Reinforcement Learning (Naseem et al., 2019)&hearts;&spades;&diams; | 75.5 | [Rewarding Smatch: Transition-Based AMR Parsing with Reinforcement Learning](https://arxiv.org/pdf/1905.13370) |
| Joint model (Lyu and Titov, 2018)&hearts;&spades; | 74.4 | [AMR Parsing as Graph Prediction with Latent Alignment](https://arxiv.org/abs/1805.05286) |
| Rewarding Smatch: Transition-Based AMR Parsing with Reinforcement Learning (Naseem et al., 2019); | 73.4 | [Rewarding Smatch: Transition-Based AMR Parsing with Reinforcement Learning](https://arxiv.org/pdf/1905.13370) |
| Core Semantic First: A Top-down Approach for AMR Parsing (Cai and Lam, 2019)&hearts;&spades; | 73.2 | [Core Semantic First: A Top-down Approach for AMR Parsing](https://www.aclweb.org/anthology/D19-1393.pdf) |
| ChSeq + 100K (van Noord and Bos, 2017)&hearts; | 71.0 | [Neural Semantic Parsing by Character-based Translation: Experiments with Abstract Meaning Representations](https://clinjournal.org/clinj/article/view/72/64) |
| Neural-Pointer (Buys and Blunsom, 2017)&hearts;&spades; | 61.9 | [Oxford at SemEval-2017 Task 9: Neural AMR Parsing with Pointer-Augmented Attention](http://aclweb.org/anthology/S17-2157) |

### LDC2020T02
The dataset contains 59,255 AMRs split across training, dev, and test partitions.

Models are evaluated based on [smatch](https://amr.isi.edu/smatch-13.pdf).

| Model           | Smatch  |  Paper / Source |
| ------------- | :-----:| --- |
| One SPRING to Rule Them Both: Symmetric AMR Semantic Parsing and Generation without a Complex Pipeline (Bevilacqua et al., 2020) | 83.0 | [One SPRING to Rule Them Both: Symmetric AMR Semantic Parsing and Generation without a Complex Pipeline](https://ojs.aaai.org/index.php/AAAI/article/view/17489) |
| APT (Action-Pointer Transformer, Zhou et al., 2021) | 81.2 | [AMR Parsing with Action-Pointer Transformer](https://aclanthology.org/2021.naacl-main.443/) |


## DRS parsing

Discourse Representation Structures (DRS) are formal meaning representations introduced by [Discourse Representation Theory](https://en.wikipedia.org/wiki/Discourse_representation_theory). DRS parsing is a complex task, comprising other NLP tasks, such as semantic role labeling, word sense disambiguation, co-reference resolution and named entity tagging. Also, DRSs show explicit scope for certain operators, which allows for a more principled and linguistically motivated treatment of negation, modals and quantification, as has been advocated in formal semantics. Moreover, DRSs can be translated to formal logic, which allows for automatic forms of inference by third parties.

### Parallel Meaning Bank (PMB)

The results listed here are from annotated English DRSs released by the [Parallel Meaning Bank](pmb.let.rug.nl). An introduction of the PMB and the annotation process is described in [this paper](https://www.aclweb.org/anthology/E17-2039.pdf). A DRS consists of a list of clauses. Each clause contains a number of variables, which are matched during evaluation using the evaluation tool Counter ([paper](https://www.aclweb.org/anthology/L18-1267.pdf), [code](https://github.com/RikVN/DRS_parsing)). Counter calculates an F-score over the matching clauses for each DRS-pair and micro-averages these to calculate a final F-score, similar to the Smatch procedure of AMR parsing.

The scores listed here are for PMB release [2.2.0](https://pmb.let.rug.nl/data.php) and [3.0.0](https://pmb.let.rug.nl/data.php), specifically. The development and test sets differ per release, but have a considerable overlap. The results listed here are on the test set. The data sets can be downloaded on the official [PMB webpage](https://pmb.let.rug.nl/data.php), but note that a more user-friendly format can be downloaded by following the steps in the [Neural_DRS repository](https://github.com/RikVN/Neural_DRS).

#### PMB-2.2.0

The gold standard train, dev and test sets contain 4,597, 682 and 650 documents, respectively.

| Model         | Authors | F1  |  Paper / Source |
| ------------- |------- | :-----:| --- |
| Bi-LSTM seq2seq: BERT + characters in 1 encoder | Van Noord et al. (2020) | 88.3 | [Character-level Representations Improve DRS-based Semantic Parsing Even in the Age of BERT](https://www.aclweb.org/anthology/2020.emnlp-main.371.pdf) |
| Transformer seq2seq | Liu et al. (2019) | 87.1 | [Discourse Representation Structure Parsing with Recurrent Neural Networks and the Transformer Model](https://www.aclweb.org/anthology/W19-1203.pdf)
| Character-level bi-LSTM seq2seq + linguistic features | Van Noord et al. (2019) | 86.8 | [Linguistic Information in Neural Semantic Parsing with Multiple Encoders](https://www.aclweb.org/anthology/W19-0504.pdf)|
| Character-level bi-LSTM seq2seq | Van Noord et al. (2018) | 83.3 | [Exploring Neural Methods for Parsing Discourse Representation Structures](https://www.aclweb.org/anthology/Q18-1043.pdf)|
| Neural graph-based system using DAG-grammars | Fancellu et al. (2019) | 76.4 | [Semantic graph parsing with recurrent neural network DAG grammars](https://www.aclweb.org/anthology/D19-1278.pdf) |
| Transition-based Stack-LSTM | Evang (2019) | 74.4 | [Transition-based DRS Parsing Using Stack-LSTMs](https://www.aclweb.org/anthology/W19-1202.pdf) |

#### PMB-3.0.0

The gold standard train, dev and test sets contain 6,620, 885 and 898 documents, respectively.

| Model         | Authors | F1  |  Paper / Source |
| ------------- |------- | :-----:| --- |
| Bi-LSTM seq2seq: BERT + characters in 1 encoder | Van Noord et al. (2020) | 89.3 | [Character-level Representations Improve DRS-based Semantic Parsing Even in the Age of BERT](https://www.aclweb.org/anthology/2020.emnlp-main.371.pdf) |
| Character-level bi-LSTM seq2seq + linguistic features | Van Noord et al. (2019) | 87.7 | [Linguistic Information in Neural Semantic Parsing with Multiple Encoders](https://www.aclweb.org/anthology/W19-0504.pdf)|
| Character-level bi-LSTM seq2seq | Van Noord et al. (2018) | 84.9 | [Exploring Neural Methods for Parsing Discourse Representation Structures](https://www.aclweb.org/anthology/Q18-1043.pdf)|

### RST-DT

RST-DT [(Carlson et al., 2001)](https://www.aclweb.org/anthology/W01-1605.pdf) contains 385 documents of American English selected from the Penn Treebank (Marcus et al., 1993), annotated in the framework of Rhetorical Structure Theory.
The dataset was officially divided into 347 documents as the training dataset and 38 documents as the test dataset. Note that there is no officially available development dataset.
In the evaluation, micro-averaged F1 scores of unlabeled spans (Span), those of nuclearity labeled spans (Nuclearity), those of rhetorical relation labeled spans (Relation), and those of both nuclearity and rhetorical relation labeled spans (Full) based on RST-Parseval [(Marcu 2000)](https://mitpress.mit.edu/books/theory-and-practice-discourse-parsing-and-summarization) are used. An implementation of the standard evaluation metrics is [here](http://alt.qcri.org/tools/discourse-eval/).

| Model    | Span     | Nuclearity | Relation | Full     | Paper / Source | Code |
| -------- | -------- | -------- | -------- | -------- | -------------- | ---- |
| Span-based Top-down Parser (ensemble) (Kobayashi et al., 2020)  | 87.0 | 74.6 | 60.0 | -- | [Top-Down RST Parsing Utilizing Granularity Levels in Documents](https://doi.org/10.1609/aaai.v34i05.6321) | [Official](https://github.com/nttcslab-nlp/Top-Down-RST-Parser) |
| Two-stage Parsing (Wang et al., 2017)  | 86.0 | 72.4 | 59.7 | -- | [A Two-Stage Parsing Method for Text-Level Discourse Analysis](https://www.aclweb.org/anthology/P17-2029.pdf) | [Official](https://github.com/yizhongw/StageDP)    |
| Bottom-up Linear-chain CRF-based Parser (Feng and Hirst, 2014) | 85.7 | 71.0 | 58.2 | -- | [A Linear-Time Bottom-Up Discourse Parser with Constraints and Post-Editing](https://www.aclweb.org/anthology/P14-1048.pdf) | [Official](http://www.cs.toronto.edu/~weifeng/software.html) |
| Transition-based Parser with Implicit Syntax Features (Yu et al., 2018)  | 85.5 | 73.1 | 60.2 | 59.9 | [Transition-based Neural RST Parsing with Implicit Syntax Features](https://www.aclweb.org/anthology/C18-1047.pdf) | [Official](https://github.com/fajri91/NeuralRST) |
| Two-stage Discourse Parser with a Sliding Window (Joty et al., 2015) | 83.84 | 68.90 | 55.87 | -- | [CODRA: A Novel Discriminative Framework for Rhetorical Analysis](https://www.aclweb.org/anthology/J15-3002.pdf) | [Official](http://alt.qcri.org/tools/discourse-parser/) |
|  HILDA Parser (Hernault et al., 2010) | 83.0 | 68.4 | 55.3 | 54.8 | [HILDA: a discourse parser using support vector machine classification](http://journals.linguisticsociety.org/elanguage/dad/article/download/591/591-2300-1-PB.pdf) |  |
| Greedy Bottom-up Parser with Syntactic Features (Surdeanu et al., 2015) | 82.6* | 67.1* | 55.4* | 54.9* | [Two Practical Rhetorical Structure Theory Parsers](https://www.aclweb.org/anthology/N15-3001.pdf) | [Official](https://github.com/clulab/processors) |
| Re-implemented HILDA RST parser (Hayashi et al., 2016)| 82.6* | 66.6* | 54.6* | 54.3* |[Empirical comparison of dependency conversions for RST discourse trees](https://www.aclweb.org/anthology/W16-3616.pdf) | -- |
| Discourse Parser with Hierarchical Attention (Li et al., 2016) | 82.2* | 66.5* | 51.4* | 50.6* | [Discourse Parsing with Attention-based Hierarchical Neural Networks](https://www.aclweb.org/anthology/D16-1035.pdf) | -- |
| Discourse Parsing from Linear Projection (Ji et al., 2014) | 82.0* | 68.2* | 57.8* | 57.6* | [Representation Learning for Text-level Discourse Parsing](https://www.aclweb.org/anthology/P14-1002.pdf) | [Official](https://github.com/jiyfeng/DPLP) |
| Transition-Based Parser Trained on Cross-Lingual Corpus (Braud et al., 2017) | 81.3* | 68.1* | 56.3* | 56.0* | [Cross-lingual RST Discourse Parsing](https://www.aclweb.org/anthology/E17-1028.pdf) | [Official](https://bitbucket.org/) |
|  LSTM Sequential Discourse Parser (Braud et al., 2016) | 79.7* | 63.6* | 47.7* | 47.5* | [Multi-view and multi-task training of RST discourse parsers](https://www.aclweb.org/anthology/C16-1179.pdf) | [Official](http://bitbucket.org/chloebt/discourse) |

*: The score is reported in [Morey et al.2017](https://www.aclweb.org/anthology/D17-1136.pdf).

## UCCA parsing

UCCA ([Abend and Rappoport, 2013](https://www.aclweb.org/anthology/P13-1023.pdf))
is a semantic representation whose main design principles
are ease of annotation, cross-linguistic applicability, and a modular architecture. UCCA represents
the semantics of linguistic utterances as directed acyclic graphs (DAGs), where terminal (childless)
nodes correspond to the text tokens, and non-terminal nodes to semantic units that participate in
some super-ordinate relation. Edges are labeled,
indicating the role of a child in the relation the parent represents.
UCCA's foundational layer mostly covers predicate-argument structure,
semantic heads and inter-Scene relations.
UCCA distinguishes primary edges, corresponding to explicit relations, from remote edges
that allow for a unit to participate in several super-ordinate relations.
Primary edges form a tree in each layer, whereas remote edges enable reentrancy, forming a DAG.

Evaluation is done by labeled F1 on the graph edges, matched by child terminal yield.

### [SemEval 2019 Task 1](https://www.aclweb.org/anthology/S19-2001.pdf)

Open and closed tracks on English, French and German [UCCA corpora](https://github.com/UniversalConceptualCognitiveAnnotation) from Wikipedia and *Twenty Thousand Leagues Under the Sea*.
Results for the English open track data are given here, with 5,141 training sentences.

| Model | English-Wiki (open) F1 | English-20K (open) F1 | Paper / Source | Code |
| ------| :--------------------: | :-------------------: | -------------- | ---- |
| Constituent Tree Parsing + BERT (Jiang et al., 2019) | 80.5 | 76.7 | [HLT@SUDA at SemEval-2019 Task 1: UCCA Graph Parsing as Constituent Tree Parsing](https://www.aclweb.org/anthology/S19-2002/) | https://github.com/SUDA-LA/ucca-parser |
| Neural Transducer (Zhang et al., 2019) | 76.6 | -- | [Broad-Coverage Semantic Parsing as Transduction](https://www.aclweb.org/anthology/D19-1392.pdf) | https://github.com/sheng-z/stog |
| Transition-based + MTL (Hershcovich et al., 2018) | 73.5 | 68.4 | [Multitask Parsing Across Semantic Representations](https://www.aclweb.org/anthology/P18-1035.pdf) | https://github.com/danielhers/tupa |
| Transition-based (Hershcovich et al., 2017) | 72.8 | 67.2 | [A Transition-Based Directed Acyclic Graph Parser for UCCA](https://www.aclweb.org/anthology/P17-1104.pdf) | https://github.com/danielhers/tupa |

### [CoNLL 2019](https://www.aclweb.org/anthology/K19-2001.pdf)

The CoNLL 2019 shared task included parsing to AMR, UCCA, DM, PSD, and EDS.
The [UCCA training data](http://svn.nlpl.eu/mrp/2019/public/ucca.tgz) is freely available.

UCCA evaluation is done both by UCCA F1 (as in SemEval 2019) and by the MRP metric, which is similar to smatch.
The training data contains 6,572 sentences from web reviews and Wikipedia.
There are two evaluation sets: one with 1,131, from the same domains (Full), and one with 87 sentences, from *The Little Prince* (LPP). Note that due to an error, 535 of the 1,131 Full Evaluation sentences were included in the training data, and therefore the full evaluation scores are an overestimate. The LPP scores are unaffected by this.

| Model | Full UCCA F1 | Full MRP F1 | LPP UCCA F1 | LPP MRP F1 | Paper / Source | Code |
| ------| :----------: | :---------: | :---------: | :--------: | -------------- | ---- |
| Transition-based + BERT + Efficient Training + Effective Encoding (Che et al., 2019) | 66.7 | 81.7 | 64.4 | 82.6 | [HIT-SCIR at MRP 2019: A Unified Pipeline for Meaning Representation Parsing via Efficient Training and Effective Encoding](https://www.aclweb.org/anthology/K19-2007.pdf) | https://github.com/DreamerDeo/HIT-SCIR-CoNLL2019 |
| Transition-based + BERT (Hershcovich and Arviv, 2019) | 57.4 | 77.7 |  65.9 | 82.2 | [TUPA at MRP 2019: A Multi-Task Baseline System](https://www.aclweb.org/anthology/K19-2002.pdf) | https://github.com/danielhers/tupa/tree/mrp |
| Transition-based + BERT + MTL (Hershcovich and Arviv, 2019) | 35.6 | 64.1 |  50.3 | 73.1 | [TUPA at MRP 2019: A Multi-Task Baseline System](https://www.aclweb.org/anthology/K19-2002.pdf) | https://github.com/danielhers/tupa/tree/mrp |

## Semantic Dependency Parsing

Broad-coverage semantic dependency parsing (SDP) [(Oepen et al., 2014)](aclweb.org/anthology/S14-2008) is defined as the task of recovering sentence-internal predicate–argument relationships for all content words, i.e. the semantic structure constituting the relational core of sentence meaning.  Target representations, thus, are semantic dependency graphs, as shown in our running example for the (Wall Street Journal) sentence:

```
A similar technique is almost impossible to apply to other crops, such as cotton, soybeans, and rice.
```
 Here, ‘technique’ for example, is the argument of at least the determiner (as the quantificational locus), the intersective modifier ‘similar’, and the predicate ‘apply’.  Conversely, the predicative copula, infinitival ‘to’, and the vacuous preposition marking the deep object of ‘apply’ arguably have no semantic contribution of their own.  For general background on the 2014 variant and an overview of participating systems (and results), please see the [(Oepen et al., 2014)](aclweb.org/anthology/S14-2008).
 
 ### [SemEval 2015 Task 18](http://alt.qcri.org/semeval2015/task18/)
 
 This Task is a re-run with some extensions of [Task 8 at SemEval 2014](http://alt.qcri.org/semeval2014/task8/). The task has three distinct target representations, dubbed DM, PAS, and PSD (renamed from what was PCEDT at SemEval 2014), representing different traditions of semantic annotation. More detail on the linguistic ‘pedigree’ of these formats is available in the [summary](http://alt.qcri.org/semeval2015/task18/index.php?id=representations) of target representations, and there is also an [on-line search](http://wesearch.delph-in.net/sdp/) interface available to interactively explore these representations (like the initial release of the training data, this interface in early August 2014 still lacks semantic dependency graphs for languages other than English).

In each dataset, there is a in-domain (ID) and out-of-domain (OOD) test set. The evaluation metric is the labeled F1 score.

| Model           | DM ID | DM OOD | PAS ID | PAS OOD | PSD ID | PSD OOD | Paper / Source | Code |
| --------------- | :-----: |  :-----:|:-----: |  :-----:|:-----: |  :-----:| --------------- | ---- |
| ACE + fine-tune (Wang et al., 2020) | 95.6 | 92.6 | 95.8 | 94.6 | 83.8 | 83.4| [Automated Concatenation of Embeddings for Structured Prediction](https://arxiv.org/pdf/2010.05006.pdf) | [Official](https://github.com/Alibaba-NLP/ACE)|
|Transition-based Pointer Network+Char+Lemma+BERT (Fernández-González & Gómez-Rodríguez, 2020)|94.4|91.0|95.1|93.4|82.6|82.0|[Transition-based Semantic Dependency Parsing with Pointer Networks](https://www.aclweb.org/anthology/2020.acl-main.629/)|[Official](https://github.com/danifg/SemanticPointer)|
|Second-Order+Biaffine+Char+Lemma (Wang et al., 2019)|94.0|89.7|94.1|91.3|81.4|79.6|[Second-Order Semantic Dependency Parsing with End-to-End Neural Networks](https://www.aclweb.org/anthology/P19-1454/)|[Official](https://github.com/wangxinyu0922/Second_Order_SDP)|
|Biaffine+Char+Lemma (Dozat and Manning, 2018)|93.7|88.9|93.9|90.6|81.0|79.4|[Simpler but More Accurate Semantic Dependency Parsing](https://www.aclweb.org/anthology/P18-2077/)|[Official](https://github.com/tdozat/Parser-v3)|



## SQL parsing

### ATIS

5,280 user questions for a flight-booking task:

- Collected and manually annotated with SQL [Dahl et al., (1994)](http://dl.acm.org/citation.cfm?id=1075823)
- Modified by [Iyer et al., (2017)](http://www.aclweb.org/anthology/P17-1089) to reduce nesting
- Bugfixes and changes to a canonical style by [Finegan-Dollak et al., (2018)](http://arxiv.org/abs/1806.09029)


Example:

| Question | SQL query |
| ------------- |  --- |
| what flights from any city land at MKE | `SELECT DISTINCT FLIGHTalias0.FLIGHT_ID FROM AIRPORT AS AIRPORTalias0 , AIRPORT_SERVICE AS AIRPORT_SERVICEalias0 , CITY AS CITYalias0 , FLIGHT AS FLIGHTalias0 WHERE AIRPORTalias0.AIRPORT_CODE = "MKE" AND CITYalias0.CITY_CODE = AIRPORT_SERVICEalias0.CITY_CODE AND FLIGHTalias0.FROM_AIRPORT = AIRPORT_SERVICEalias0.AIRPORT_CODE AND FLIGHTalias0.TO_AIRPORT = AIRPORTalias0.AIRPORT_CODE ;` |

| Model           | Question Split | Query Split |  Paper / Source | Code |
| --------------- | ----- |  :-----:| --------------- | ---- |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | 51 | 32 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |
| Iyer et al., (2017) | 45 | 17 | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) | [System](https://github.com/sriniiyer/nl2sql) |
| Template Baseline (Finegan-Dollak et al., 2018) | 45 | 0 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |

### Advising

4,570 user questions about university course advising, with manually annotated SQL [Finegan-Dollak et al., (2018)](http://arxiv.org/abs/1806.09029).

Example:

| Question | SQL query |
| ------------- |  --- |
| Can undergrads take 550 ? | `SELECT DISTINCT COURSEalias0.ADVISORY_REQUIREMENT , COURSEalias0.ENFORCED_REQUIREMENT , COURSEalias0.NAME FROM COURSE AS COURSEalias0 WHERE COURSEalias0.DEPARTMENT = \"department0\" AND COURSEalias0.NUMBER = 550 ;` |

| Model           | Question Split | Query Split |  Paper / Source | Code |
| --------------- | ----- |  :-----:| --------------- | ---- |
| Template Baseline (Finegan-Dollak et al., 2018) | 80 | 0 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | 70 | 0  | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |
| Iyer et al., (2017) | 41 | 1 | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) | [System](https://github.com/sriniiyer/nl2sql) |

### GeoQuery

877 user questions about US geography:

- Collected and manually annotated with Prolog [Zelle and Mooney (1996)](http://dl.acm.org/citation.cfm?id=1864519.1864543)
- Most questions were converted to SQL by [Popescu et al., (2003)](http://doi.acm.org/10.1145/604045.604070)
- Remaining question converted to SQL by [Giordani and Moschitti (2012)](https://doi.org/10.1007/978-3-642-45260-4_5), and independently by [Iyer et al., (2017)](http://www.aclweb.org/anthology/P17-1089)
- Bugfixes and changes to a canonical style by [Finegan-Dollak et al., (2018)](http://arxiv.org/abs/1806.09029)

Example:

| Question | SQL query |
| ------------- |  --- |
| what is the biggest city in arizona | `SELECT CITYalias0.CITY_NAME FROM CITY AS CITYalias0 WHERE CITYalias0.POPULATION = ( SELECT MAX( CITYalias1.POPULATION ) FROM CITY AS CITYalias1 WHERE CITYalias1.STATE_NAME = "arizona" ) AND CITYalias0.STATE_NAME = "arizona"` |

| Model           | Question Split | Query Split |  Paper / Source | Code |
| --------------- | ----- |  :-----:| --------------- | ---- |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | 71 | 20 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |
| Iyer et al., (2017) | 66 | 40 | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) | [System](https://github.com/sriniiyer/nl2sql) |
| Template Baseline (Finegan-Dollak et al., 2018) | 66 | 0  | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |

### Scholar

817 user questions about academic publications, with automatically generated SQL that was checked by asking the user if the output was correct.

- Collected by [Iyer et al., (2017)](http://www.aclweb.org/anthology/P17-1089)
- Bugfixes and changes to a canonical style by [Finegan-Dollak et al., (2018)](http://arxiv.org/abs/1806.09029)

Example:

| Question | SQL query |
| ------------- |  --- |
| What papers has sharon goldwater written ? | `SELECT DISTINCT WRITESalias0.PAPERID FROM AUTHOR AS AUTHORalias0 , WRITES AS WRITESalias0 WHERE AUTHORalias0.AUTHORNAME = "sharon goldwater" AND WRITESalias0.AUTHORID = AUTHORalias0.AUTHORID ;` |

| Model           | Question Split | Query Split |  Paper / Source | Code |
| --------------- | ----- |  :-----:| --------------- | ---- |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | 59 | 5 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |
| Template Baseline (Finegan-Dollak et al., 2018) | 52 | 0   | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |
| Iyer et al., (2017) | 44 | 3 | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) | [System](https://github.com/sriniiyer/nl2sql) |

### Spider

Spider is a large-scale complex and cross-domain semantic parsing and text-to-SQL
dataset. It consists of 10,181 questions and 5,693 unique complex SQL queries on
200 databases with multiple tables covering 138 different domains. In Spider 1.0,
different complex SQL queries and databases appear in train and test sets.

The Spider dataset can be accessed and leaderboard can be accessed [here](https://yale-lily.github.io/spider).

### WikiSQL

The [WikiSQL dataset](https://arxiv.org/abs/1709.00103) consists of 87,673
examples of questions, SQL queries, and database tables built from 26,521 tables.
Train/dev/test splits are provided so that each table is only in one split.
Models are evaluated based on accuracy on execute result matches.

Example:

| Question | SQL query |
| ------------- |  --- |
| How many engine types did Val Musetti use? | `SELECT COUNT Engine WHERE Driver = Val Musetti` |

The WikiSQL dataset and leaderboard can be accessed [here](https://github.com/salesforce/WikiSQL).

### Smaller Datasets

Restaurants - 378 questions about restaurants, their cuisine and locations, collected by [Tang and Mooney (2000)](http://www.aclweb.org/anthology/W/W00/W00-1317.pdf), converted to SQL by [Popescu et al., (2003)]((http://doi.acm.org/10.1145/604045.604070) and [Giordani and Moschitti (2012)](https://doi.org/10.1007/978-3-642-45260-4_5), improved and converted to canonical style by [Finegan-Dollak et al., (2018)](http://arxiv.org/abs/1806.09029)

Example:

| Question | SQL query |
| ------------- |  --- |
| where is a restaurant in alameda ? | `SELECT LOCATIONalias0.HOUSE_NUMBER , RESTAURANTalias0.NAME FROM LOCATION AS LOCATIONalias0 , RESTAURANT AS RESTAURANTalias0 WHERE LOCATIONalias0.CITY_NAME = "alameda" AND RESTAURANTalias0.ID = LOCATIONalias0.RESTAURANT_ID ;` |

| Model           | Question Split | Query Split |  Paper / Source | Code |
| --------------- | ----- |  :-----:| --------------- | ---- |
| Iyer et al., (2017) | 100 | 8 | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) | [System](https://github.com/sriniiyer/nl2sql) |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | 100 | 4 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |
| Template Baseline (Finegan-Dollak et al., 2018) | 95 | 0  | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |

Academic - 196 questions about publications generated by enumerating all of the different queries possible with the Microsoft Academic Search interface, then writing questions for each query [Li and Jagadish (2014)](http://dx.doi.org/10.14778/2735461.2735468). Improved and converted to a cononical style by [Finegan-Dollak et al., (2018)](http://arxiv.org/abs/1806.09029).

Example:

| Question | SQL query |
| ------------- |  --- |
| return me the homepage of PVLDB | `SELECT JOURNALalias0.HOMEPAGE FROM JOURNAL AS JOURNALalias0 WHERE JOURNALalias0.NAME = "PVLDB" ;` |

| Model           | Question Split | Query Split |  Paper / Source | Code |
| --------------- | ----- |  :-----:| --------------- | ---- |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | 81 | 74 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |
| Iyer et al., (2017) | 76 | 70 | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) | [System](https://github.com/sriniiyer/nl2sql) |
| Template Baseline (Finegan-Dollak et al., 2018) | 0 | 0 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |

Yelp - 128 user questions about the Yelp website [Yaghmazadeh et al., 2017](http://doi.org/10.1145/3133887). Improved and converted to a cononical style by [Finegan-Dollak et al., (2018)](http://arxiv.org/abs/1806.09029).

Example:

| Question | SQL query |
| ------------- |  --- |
| List all businesses with rating 3.5 | `SELECT BUSINESSalias0.NAME FROM BUSINESS AS BUSINESSalias0 WHERE BUSINESSalias0.RATING = 3.5 ;` |

| Model           | Question Split | Query Split |  Paper / Source | Code |
| --------------- | ----- |  :-----:| --------------- | ---- |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | 12 | 4 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |
| Iyer et al., (2017) | 6 | 6 | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) | [System](https://github.com/sriniiyer/nl2sql) |
| Template Baseline (Finegan-Dollak et al., 2018) | 1 | 0 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |

IMDB - 131 user questions about the Internet Movie Database [Yaghmazadeh et al., 2017](http://doi.org/10.1145/3133887). Improved and converted to a cononical style by [Finegan-Dollak et al., (2018)](http://arxiv.org/abs/1806.09029).

Example:

| Question | SQL query |
| ------------- |  --- |
| What year was the movie " The Imitation Game " produced | `SELECT MOVIEalias0.RELEASE_YEAR FROM MOVIE AS MOVIEalias0 WHERE MOVIEalias0.TITLE = "The Imitation Game" ;` |

| Model           | Question Split | Query Split |  Paper / Source | Code |
| --------------- | ----- |  :-----:| --------------- | ---- |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | 26 | 9 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |
| Iyer et al., (2017) | 10 | 4 | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) | [System](https://github.com/sriniiyer/nl2sql) |
| Template Baseline (Finegan-Dollak et al., 2018) | 0 | 0 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |

[Go back to the README](../README.md)

