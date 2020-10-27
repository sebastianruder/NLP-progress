# Discourse Parsing



## RST discourse treebank (RST-DT)

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


