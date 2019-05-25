# Relationship Extraction

Relationship extraction is the task of extracting semantic relationships from a text. Extracted relationships usually
occur between two or more entities of a certain type (e.g. Person, Organisation, Location) and fall into a number of
semantic categories (e.g. married to, employed by, lives in).

## Extraction of entities and their semantic relations

The task involves two sub-tasks of named entity recognition (NER) and relation classification (RC). 


### CoNLL04 corpus

The benchmark "entity and relation recognition" dataset CoNLL04 is available from [HERE](https://cogcomp.org/page/resource_view/43) by Dan Roth and Wen-tau Yih.  

On this corpus, two evaluation setup scenarios are : (1) NER & RC: A realistic scenario where entity boundaries are not given. (2) EC & RC: A less realistic scenario where the entity boundaries are given. Thus the NER task which identifies both entity boundaries and classes reduces to the entity classification (EC) task. 

Metric: macro-averaged F1.


| Model | (1) NER | (1) RC | (2) EC | (2) RC | Paper | Code  |    train/dev/test | 
| ------| ------- | ------- | ------- | ------- | ------- | ------- | ------ | 
|  Nguyen and  Verspoor (2019) [+++] | 86.2 |  64.4 |  93.8 |  69.6 | [End-to-end neural relation extraction using deep biaffine attention](https://arxiv.org/abs/1812.11275) | [Official](https://github.com/datquocnguyen/jointRE) | 64/16/20 |
| Bekoulis et al. (2018) [+++]|  83.9 | 62.0 |  93.3 |  67.0 | [Joint entity recognition and relation extraction as a multi-head selection problem](https://arxiv.org/abs/1804.07847) | [Official](https://github.com/bekou/multihead_joint_entity_relation_extraction) | 64/16/20 |
| Bekoulis et al. (2018) [+++]  |  83.6 | 62.0 | 93.0 | 68.0 | [Adversarial training for multi-context joint entity and relation extraction](https://arxiv.org/abs/1808.06876) | [Official](https://github.com/bekou/multihead_joint_entity_relation_extraction) | 64/16/20 |
| Adel and Schutze (2017) [+++] |  n/a  |  n/a | 82.1 | 62.5 | [Global Normalization of Convolutional Neural Networks for Joint Entity and Relation Classification](https://www.aclweb.org/anthology/D17-1181) | [Official](http://cistern.cis.lmu.de/globalNormalization/) | 64/16/20 |
| Gupta et al. (2016) [+++]  |  n/a  |  n/a | 92.4 | 69.9 | [Table Filling Multi-Task Recurrent Neural Network for Joint Entity and Relation Extraction](https://aclweb.org/anthology/papers/C/C16/C16-1239/) | [Official](https://github.com/pgcool/TF-MTRNN) |  80/0/20 |
| Miwa and Sasaki (2014) [---] | 80.7 | 61.0 | 92.3 | 71.0 | [Modeling Joint Entity and Relation Extraction with Table Representation](https://www.aclweb.org/anthology/D14-1200)|   |   80/0/20 |
|Zhang et al. (2017) [---]| 85.6 | 67.8| n/a|n/a | [End-to-End Neural Relation Extraction with Global Optimization](https://www.aclweb.org/anthology/D17-1182)|    |   72/8/20 |

* [+++] denotes that those models used the same test set. Although using the same test set, Gupta
et al. (2016)  reported results on a 80/0/20 training/development/test split, instead of a 64/16/20 split used in Nguyen and  Verspoor (2019), Bekoulis et al. (2018)  and Adel and Schutze (2017).

* [---] denotes that results are just for reference, **not for comparison**, due to a random sampling of the test set. In particular, Miwa and Sasaki (2014) used the 80/0/20 split for Setup 1 and performed 5-fold cross validation (i.e. sort of equivalent to 80/0/20) for Setup 2, while Zhang et al. (2017) used a 72/8/20 split.













## Relation prediction/classification

In cases where (gold standard) entity mentions were already given, the task reduces to predicting a relation type for a given entity pair.

### New York Times Corpus

The standard corpus for distantly supervised relationship extraction is the New York Times (NYT) corpus, published in
[Riedel et al, 2010](http://www.riedelcastro.org//publications/papers/riedel10modeling.pdf).

This contains text from the [New York Times Annotated Corpus](https://catalog.ldc.upenn.edu/ldc2008t19) with named
entities extracted from the text using the Stanford NER system and automatically linked to entities in the Freebase
knowledge base. Pairs of named entities are labelled with relationship types by aligning them against facts in the
Freebase knowledge base. (The process of using a separate database to provide label is known as 'distant supervision')

Example:
 > **Elevation Partners**, the $1.9 billion private equity group that was founded by **Roger McNamee**

 `(founded_by, Elevation_Partners, Roger_McNamee)`

Different papers have reported various metrics since the release of the dataset, making it difficult to compare systems
directly. The main metrics used are either precision at N results or plots of the precision-recall. The range of recall
has increased over the years as systems improve, with earlier systems having very low precision at 30% recall.


| Model                               | P@10% | P@30% | Paper / Source | Code           |
| ----------------------------------- | ----- | ----- | --------------- | -------------- |
| Intra- and Inter-Bag (Ye and Ling, 2019)         | 78.9   | 62.4   | [Distant Supervision Relation Extraction with Intra-Bag and Inter-Bag Attentions](https://arxiv.org/pdf/1904.00143.pdf) | [Code](https://github.com/ZhixiuYe/Intra-Bag-and-Inter-Bag-Attentions) |
| RESIDE (Vashishth et al., 2018)         | 73.6   | 59.5   | [RESIDE: Improving Distantly-Supervised Neural Relation Extraction using Side Information](http://malllabiisc.github.io/publications/papers/reside_emnlp18.pdf) | [RESIDE](https://github.com/malllabiisc/RESIDE) |
| PCNN+ATT (Lin et al., 2016)         | 69.4   | 51.8   | [Neural Relation Extraction with Selective Attention over Instances](http://www.aclweb.org/anthology/P16-1200) | [OpenNRE](https://github.com/thunlp/OpenNRE/) |
| MIML-RE (Surdeneau et al., 2012)    | 60.7+  |   -   | [Multi-instance Multi-label Learning for Relation Extraction](http://www.aclweb.org/anthology/D12-1042) | [Mimlre](https://nlp.stanford.edu/software/mimlre.shtml) |
| MultiR (Hoffman et al., 2011)       | 60.9+  |   -   | [Knowledge-Based Weak Supervision for Information Extraction of Overlapping Relations](http://www.aclweb.org/anthology/P11-1055) | [MultiR](http://aiweb.cs.washington.edu/ai/raphaelh/mr/) |
| (Mintz et al., 2009)                | 39.9+  |   -   | [Distant supervision for relation extraction without labeled data](http://www.aclweb.org/anthology/P09-1113) | |


(+) Obtained from results in the paper "Neural Relation Extraction with Selective Attention over Instances"


### SemEval-2010 Task 8

[SemEval-2010](http://www.aclweb.org/anthology/S10-1006) introduced 'Task 8 - Multi-Way Classification of Semantic
Relations Between Pairs of Nominals'. The task is, given a sentence and two tagged nominals, to predict the relation
between those nominals *and* the direction of the relation. The dataset contains nine general semantic relations
together with a tenth 'OTHER' relation.

Example:
 > There were apples, **pears** and oranges in the **bowl**.

 `(content-container, pears, bowl)`

The main evaluation metric used is macro-averaged F1, averaged across the nine proper relationships (i.e. excluding the
OTHER relation), taking directionality of the relation into account.

Several papers have used additional data (e.g. pre-trained word embeddings, WordNet) to improve performance. The figures
reported here are the highest achieved by the model using any external resources.

#### End-to-End Models

| Model                                  | F1    | Paper / Source  | Code           |
| -------------------------------------- | ----- | --------------- | -------------- |
| *CNN-based Models* |
| Multi-Attention CNN (Wang et al. 2016) | **88.0** | [Relation Classification via Multi-Level Attention CNNs](http://aclweb.org/anthology/P16-1123) | [lawlietAi's Reimplementation](https://github.com/lawlietAi/relation-classification-via-attention-model) |
| Attention CNN (Huang and Y Shen, 2016) | 84.3<br>85.9<sup>[\*](#footnote)</sup> | [Attention-Based Convolutional Neural Network for Semantic Relation Extraction](http://www.aclweb.org/anthology/C16-1238) |
| CR-CNN (dos Santos et al., 2015)       | 84.1  | [Classifying Relations by Ranking with Convolutional Neural Network](https://www.aclweb.org/anthology/P15-1061) | [pratapbhanu's Reimplementation](https://github.com/pratapbhanu/CRCNN) |
| CNN (Zeng et al., 2014)                | 82.7  | [Relation Classification via Convolutional Deep Neural Network](http://www.aclweb.org/anthology/C14-1220) | [roomylee's Reimplementation](https://github.com/roomylee/cnn-relation-extraction) |
| *RNN-based Models* |
| Entity Attention Bi-LSTM (Lee et al., 2019) | **85.2** | [Semantic Relation Classification via Bidirectional LSTM Networks with Entity-aware Attention using Latent Entity Typing](https://arxiv.org/abs/1901.08163) | [Official](https://github.com/roomylee/entity-aware-relation-classification) |
| Hierarchical Attention Bi-LSTM (Xiao and C Liu, 2016) | 84.3 | [Semantic Relation Classification via Hierarchical Recurrent Neural Network with Attention](http://www.aclweb.org/anthology/C16-1119) |
| Attention Bi-LSTM (Zhou et al., 2016)  | 84.0 | [Attention-Based Bidirectional Long Short-Term Memory Networks for Relation Classification](http://www.aclweb.org/anthology/P16-2034) | [SeoSangwoo's Reimplementation](https://github.com/SeoSangwoo/Attention-Based-BiLSTM-relation-extraction) |
| Bi-LSTM (Zhang et al., 2015)           | 82.7<br>84.3<sup>[\*](#footnote)</sup> | [Bidirectional long short-term memory networks for relation classification](http://www.aclweb.org/anthology/Y15-1009) |

<a name="footnote">*</a>: It uses external lexical resources, such as WordNet, part-of-speech tags, dependency tags, and named entity tags.


#### Dependency Models

| Model                               | F1    | Paper / Source  | Code           |
| ----------------------------------- | ----- | --------------- | -------------- |
| BRCNN (Cai et al., 2016)            | **86.3**  | [Bidirectional Recurrent Convolutional Neural Network for Relation Classification](http://www.aclweb.org/anthology/P16-1072) |
| DRNNs (Xu et al., 2016)             | 86.1  | [Improved Relation Classification by Deep Recurrent Neural Networks with Data Augmentation](https://arxiv.org/abs/1601.03651) |
| depLCNN + NS (Xu et al., 2015a)     | 85.6 | [Semantic Relation Classification via Convolutional Neural Networks with Simple Negative Sampling](https://www.aclweb.org/anthology/D/D15/D15-1062.pdf) |
| SDP-LSTM (Xu et al., 2015b)         | 83.7  | [Classifying Relations via Long Short Term Memory Networks along Shortest Dependency Path](https://arxiv.org/abs/1508.03720) | [Sshanu's Reimplementation](https://github.com/Sshanu/Relation-Classification) |
| DepNN (Liu et al., 2015)            | 83.6  | [A Dependency-Based Neural Network for Relation Classification](http://www.aclweb.org/anthology/P15-2047) |
| FCN (Yu et al., 2014)               | 83.0  | [Factor-based compositional embedding models](https://www.cs.cmu.edu/~mgormley/papers/yu+gormley+dredze.nipsw.2014.pdf) |
| MVRNN (Socher et al., 2012)         | 82.4  | [Semantic Compositionality through Recursive Matrix-Vector Spaces](http://aclweb.org/anthology/D12-1110) | [pratapbhanu's Reimplementation](https://github.com/pratapbhanu/MVRNN) |


### TACRED

[TACRED](https://nlp.stanford.edu/projects/tacred/) is a large-scale relation extraction dataset with 106,264 examples built over newswire and web text from the [corpus](https://catalog.ldc.upenn.edu/LDC2018T03) used in the yearly [TAC Knowledge Base Population (TAC KBP) challenges](https://tac.nist.gov/2017/KBP/index.html). Examples in TACRED cover 41 relation types as used in the TAC KBP challenges (e.g., _per:schools_attended_ and _org:members_) or are labeled as _no_relation_ if no defined relation is held. These examples are created by combining available human annotations from the TAC KBP challenges and crowdsourcing.

Example:
 > *Billy Mays*, the bearded, boisterious pitchman who, as the undisputed king of TV yell and sell, became an inlikely pop culture icon, died at his home in *Tampa*, Fla, on Sunday. 

 `(per:city_of_death, Billy Mays, Tampa)`

The main evaluation metric used is micro-averaged F1 over instances with proper relationships (i.e. excluding the
_no_relation_ type).

| Model                                  | F1    | Paper / Source  | Code           |
| -------------------------------------- | ----- | --------------- | -------------- |
| C-GCN + PA-LSTM (Zhang et al. 2018) | **68.2** | [Graph Convolution over Pruned Dependency Trees Improves Relation Extraction](http://aclweb.org/anthology/D18-1244) | [Offical](https://github.com/qipeng/gcn-over-pruned-trees) |
| PA-LSTM (Zhang et al, 2017) | 65.1 | [Position-aware Attention and Supervised Data Improve Slot Filling](http://aclweb.org/anthology/D17-1004) | [Official](https://github.com/yuhaozhang/tacred-relation) |



# FewRel

The Few-Shot Relation Classification Dataset (FewRel) is a different setting from the previous datasets. This dataset consists of 70K sentences expressing 100 relations annotated by crowdworkers on Wikipedia corpus. The few-shot learning task follows the N-way K-shot meta learning setting. It is both the largest supervised relation classification dataset as well as the largest few-shot learning dataset till now. 

The public leaderboard is available on the [FewRel website](http://www.zhuhao.me/fewrel/).

[Go back to the README](../README.md)
