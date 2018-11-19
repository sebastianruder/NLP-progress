# Relationship Extraction

Relationship extraction is the task of extracting semantic relationships from a text. Extracted relationships usually
occur between two or more entities of a certain type (e.g. Person, Organisation, Location) and fall into a number of
semantic categories (e.g. married to, employed by, lives in).

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
| Entity Attention Bi-LSTM (Lee and Seo, 2018) | **85.2** | [Semantic Relation Classification via Bidirectional LSTM Networks with Entity-aware Attention using Latent Entity Typing]() |
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


# FewRel

The Few-Shot Relation Classification Dataset (FewRel) is a different setting from the previous datasets. This dataset consists of 70K sentences expressing 100 relations annotated by crowdworkers on Wikipedia corpus. The few-shot learning task follows the N-way K-shot meta learning setting. It is both the largest supervised relation classification dataset as well as the largest few-shot learning dataset till now. 

The public leaderboard is available on the [FewRel website](http://zhuhao.me/fewrel).

[Go back to the README](../README.md)
