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
| PCNN+ATT (Lin et al., 2016)         | 69*   | 51*   | [Neural Relation Extraction with Selective Attention over Instances](http://www.aclweb.org/anthology/P16-1200) | [OpenNRE](https://github.com/thunlp/OpenNRE/) |
| MIML-RE (Surdeneau et al., 2012)    | 61*+  |   -   | [Multi-instance Multi-label Learning for Relation Extraction](http://www.aclweb.org/anthology/D12-1042) | [Mimlre](https://nlp.stanford.edu/software/mimlre.shtml) |
| MultiR (Hoffman et al., 2011)       | 60*+  |   -   | [Knowledge-Based Weak Supervision for Information Extraction of Overlapping Relations](http://www.aclweb.org/anthology/P11-1055) | [MultiR](http://aiweb.cs.washington.edu/ai/raphaelh/mr/) |
| (Mintz et al., 2009)                | 40*+  |   -   | [Distant supervision for relation extraction without labeled data](http://www.aclweb.org/anthology/P09-1113) | |


(*) Estimated from plots using [WebplotDigitizer](https://apps.automeris.io/wpd/). These are reported to two significant digits due to the low accuracy when extracting from graphs.

(+) Estimated from results in the paper "Neural Relation Extraction with Selective Attention over Instances"

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

| Model                               | F1    | Paper / Source  | Code           |
| ----------------------------------- | ----- | --------------- | -------------- |
| BRCNN (Cai et al., 2016)            | 86.3  | [Bidirectional Recurrent Convolutional Neural Network for Relation Classification](http://www.aclweb.org/anthology/P16-1072) | [Reimplementation](https://github.com/roomylee/rcnn-relation-extraction) |
| DepLCNN (Xu et al., 2015)           | 85.6  | [Semantic Relation Classification via Convolutional Neural Networks with Simple Negative Sampling](https://www.aclweb.org/anthology/D/D15/D15-1062.pdf) ||
| CR-CNN (dos Santos et al., 2015)    | 84.1  | [Classifying Relations by Ranking with Convolutional Neural Network](https://www.aclweb.org/anthology/P15-1061)
| UTD (Rink and Harabagiu, 2010)      | 82.2  | [UTD: Classifying Semantic Relations by Combining Lexical and Semantic Resources](http://www.aclweb.org/anthology/S10-1057) ||


[Go back to the README](README.md)
