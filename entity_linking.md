# Entity Linking

## Task

Entity Linking (EL) is the task of recognizing (cf. [Named Entity Recognition](named_entity_recognition.md)) and disambiguating (Named Entity Disambiguation) named entities to a knowledge base (e.g. Wikidata, DBpedia, or YAGO). It is sometimes also simply known as Named Entity Recognition and Disambiguation.

EL can be split into two classes of approaches:
* *End-to-End*: processing a piece of text to extract the entities (i.e. Named Entity Recognition) and then disambiguate these extracted entities to the correct entry in a given knowledge base (e.g. Wikidata, DBpedia, YAGO).
* *Disambiguation-Only*: contrary to the first approach, this one directly takes gold standard named entities as input and only disambiguates them to the correct entry in a given knowledge base.

Example:

| Barack | Obama | was | born | in | Hawaï |
| --- | ---| --- | --- | --- | --- |
| https://en.wikipedia.org/wiki/Barack_Obama | https://en.wikipedia.org/wiki/Barack_Obama | O | O | O | https://en.wikipedia.org/wiki/Hawaii |

More in details can be found in this [survey](http://dbgroup.cs.tsinghua.edu.cn/wangjy/papers/TKDE14-entitylinking.pdf).

## Evaluation

### Metrics for Disambiguation-Only Approach

* Micro-Precision: Fraction of correctly disambiguated named entities in the full corpus.
* Macro-Precision: Fraction of correctly disambiguated named entities, averaged by document.

## Datasets

### AIDA CoNLL-YAGO Dataset

The [AIDA CoNLL-YAGO](https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/yago-naga/aida/downloads/) Dataset [1] contains assignments of entities to the mentions of named entities annotated for the original [CoNLL 2003 NER task](http://www.aclweb.org/anthology/W03-0419.pdf) [2]. The entities are identified by [YAGO2](http://yago-knowledge.org/) entity identifier, by [Wikipedia URL](https://en.wikipedia.org/), or by [Freebase mid](http://wiki.freebase.com/wiki/Machine_ID).

| Approach | Micro-Precision | Macro-Precision  |  Paper / Source |
| ------------- | :-----:| :----: | --- |
| Radhakrishnan et al. (2018) | 93.0 | 93.7 | [ELDEN: Improved Entity Linking using Densified Knowledge Graphs](http://aclweb.org/anthology/N18-1167) |
| Le et al. (2018) | 93.07 | - | [Improving Entity Linking by Modeling Latent Relations between Mentions](https://arxiv.org/abs/1804.10637) |
| Hoffart at al. (2011) | 82.29 | 82.02 | [Robust Disambiguation of Named Entities in Text](http://www.aclweb.org/anthology/D11-1072)

## References

[1] Johannes Hoffart, Mohamed Amir Yosef, Ilaria Bordino, Hagen Fürstenau, Manfred Pinkal, Marc Spaniol, Bilyana Taneva, Stefan Thater, and Gerhard Weikum. Robust Disambiguation of Named Entities in Text. In Proceedings of the 2011 Conference on Empirical Methods in Natural Language Processing, EMNLP 2011, Edinburgh, Scotland, pages 782–792, 2011.

[2] Erik F Tjong Kim Sang and Fien De Meulder. Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition. In Proceedings of the 7th Conference on Natural Language Learning, CoNLL 2003, Edmonton, Canada, 2003.

[Go back to the README](README.md)