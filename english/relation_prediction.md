# Relation Prediction

## Task

Relation Prediction is the task of recognizing a named relation between two named semantic entities. The common test setup is to hide one entity from the relation triplet, asking the system to recover it based on the other entity and the relation type.

For example, given the triple \<*Roman Jakobson*, *born-in-city*, *?*\>, the system is required to replace the question mark with *Moscow*.

Relation Prediction datasets are typically extracted from two types of resources: 
* *Knowledge Bases*: KBs such as [FreeBase](https://developers.google.com/freebase/) contain hundreds or thousands of relation types pertaining to world-knowledge obtained automatically or semi-automatically from various resources on millions of entities. These relations include *born-in*, *nationality*, *is-in* (for geographical entities), *part-of* (for organizations, among others), and more.
* *Semantic Graphs*: SGs such as [WordNet](https://wordnet.princeton.edu/) are often manually-curated resources of semantic concepts, restricted to more "linguistic" relations compared to free real-world knowledge. The most common semantic relation is *hypernym*, also known as the *is-a* relation (example: \<*cat*, *hypernym*, *feline*\>).

## Evaluation

Evaluation in Relation Prediction hinges on a list of ranked candidates given by the system to the test instance. The metrics below are derived from the location of correct candidate(s) in that list.

A common action performed before evaluation on a given list is *filtering*, where the list is cleaned of entities whose corresponding triples exist in the knowledge graph. Unless specified otherwise, results here are from filtered lists.

### Metrics

#### Mean Reciprocal Rank (MRR):

The mean of all reciprocal ranks for the true candidates over the test set (1/rank).

#### Hits at k (H@k):

The rate of correct entities appearing in the top *k* entries for each instance list. This number may exceed 1.00 if the average *k*-truncated list contains more than one true entity.

### Datasets

#### Freebase-15K-237 (FB15K-237)
The FB15K dataset was introduced in [Bordes et al., 2013](http://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data.pdf). It is a subset of Freebase which contains about 14,951 entities with 1,345 different relations. This dataset was found to suffer from major test leakage through inverse relations and a large number of test triples can be obtained simply by inverting triples in the training set initially by [Toutanova et al.](http://aclweb.org/anthology/D15-1174). To create a dataset without this property, [Toutanova et al.](http://aclweb.org/anthology/D15-1174) introduced FB15k-237 – a subset of FB15k where inverse relations are removed.

#### WordNet-18-RR (WN18RR)

The WN18 dataset was also introduced in [Bordes et al., 2013](http://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data.pdf). It included the full 18 relations scraped from WordNet for roughly 41,000 synsets. Similar to FB15K, This dataset was found to suffer from test leakage by [Dettmers et al. (2018)](https://arxiv.org/abs/1707.01476) introduced the [WN18RR](https://github.com/villmow/datasets_knowledge_embedding). 

As a way to overcome this problem, [Dettmers et al. (2018)](https://arxiv.org/abs/1707.01476) introduced the [WN18RR](https://github.com/villmow/datasets_knowledge_embedding) dataset, derived from WN18, which features 11 relations only, no pair of which is reciprocal (but still include four internally-symmetric relations like *verb_group*, allowing the rule-based system to reach 35 on all three metrics).

### Experimental Results

#### WN18RR

The test set is composed of triplets, each used to create two test instances, one for each entity to be predicted. Since each instance is associated with a single true entity, the maximum value for all metrics is 1.00.
   
| Model           | H@10 | H@1 | MRR | Paper / Source | Code | 
| ------------- | :-----:| :-----:| :-----:| --- | --- | 
| Max-Margin Markov Graph Models (Pinter & Eisenstein, 2018) | 59.02 | 45.37 | 49.83 | [Predicting Semantic Relations using Global Graph Properties](https://arxiv.org/abs/1808.08644) | [Official](http://www.github.com/yuvalpinter/m3gm) |
| TransE (reimplementation by Pinter & Eisenstein, 2018) | 55.55 | 42.26 | 46.59 | [Translating Embeddings for Modeling Multi-relational Data. ](http://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data.pdf) | [OpenKE](https://github.com/thunlp/OpenKE) |
| ConvKB (Nguyen et al., 2018) | 52.50 | - | 24.80 | [A Novel Embedding Model for Knowledge Base Completion Based on Convolutional Neural Network](http://www.aclweb.org/anthology/N18-2053) | [Official](https://github.com/daiquocnguyen/ConvKB) |
| ConvE (v6; Dettmers et al., 2018) | 52.00 | 40.00 | 43.00 | [Convolutional 2D Knowledge Graph Embeddings](https://arxiv.org/abs/1707.01476) | [Official](https://github.com/TimDettmers/ConvE) |
| ComplEx (Trouillon et al., 2016) | 51.00 | 41.00 | 44.00 | [Complex Embeddings for Simple Link Prediction](http://www.jmlr.org/proceedings/papers/v48/trouillon16.pdf) | [Official](https://github.com/ttrouill/complex) | 
| DistMult (reimplementation by Dettmers et al., 2018) | 49.00 | 40.00 | 43.00 | [Embedding Entities and Relations for Learning and Inference in Knowledge Bases.](https://arxiv.org/pdf/1412.6575) | [Link](https://github.com/thunlp/OpenKE) |

#### FB15K-237

| Model           | H@10 | H@1 | MRR | Paper / Source | Code | 
| ------------- | :-----:| :-----:| :-----:| --- | --- | 
| TransE (reimplementation by Han et al., 2018) | 47.09 | 19.87 | 29.04 | [Translating Embeddings for Modeling Multi-relational Data. ](http://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data.pdf) | [OpenKE](https://github.com/thunlp/OpenKE) |
| TransH (reimplementation by Han et al., 2018) | 41.32 | 5.79 | 17.66 | [Knowledge Graph Embedding by Translating on Hyperplanes.](http://www.aaai.org/ocs/index.php/AAAI/AAAI14/paper/viewFile/8531/8546) | [OpenKE](https://github.com/thunlp/OpenKE) |
| TransR (reimplementation by Han et al., 2018) | 40.67 | 16.35 | 24.44 | [ Learning Entity and Relation Embeddings for Knowledge Graph Completion.](http://www.aaai.org/ocs/index.php/AAAI/AAAI15/paper/download/9571/9523/) | [OpenKE](https://github.com/thunlp/OpenKE) |
| TransD (reimplementation by Han et al., 2018) | 46.05 | 14.83 | 25.27 | [Knowledge Graph Embedding via Dynamic Mapping Matrix.](http://anthology.aclweb.org/P/P15/P15-1067.pdf) | [OpenKE](https://github.com/thunlp/OpenKE) |
| ConvKB (Nguyen et al., 2018) | 51.70 | - | 39.60 | [A Novel Embedding Model for Knowledge Base Completion Based on Convolutional Neural Network](http://www.aclweb.org/anthology/N18-2053) | [Official](https://github.com/daiquocnguyen/ConvKB) |
| ConvE (v6; Dettmers et al., 2018) | 50.10 | 23.70 | 32.50 | [Convolutional 2D Knowledge Graph Embeddings](https://arxiv.org/abs/1707.01476) | [Official](https://github.com/TimDettmers/ConvE) |
| ComplEx (reimplementation by Dettmers et al., 2018) | 42.80 | 15.80 | 24.70 | [Complex Embeddings for Simple Link Prediction](http://www.jmlr.org/proceedings/papers/v48/trouillon16.pdf) | [Official](https://github.com/ttrouill/complex) | 
| DistMult (reimplementation by Dettmers et al., 2018) | 41.90 | 15.50 | 24.10 | [Embedding Entities and Relations for Learning and Inference in Knowledge Bases.](https://arxiv.org/pdf/1412.6575) | [Link](https://github.com/thunlp/OpenKE) |

## Resources
[OpenKE](http://aclweb.org/anthology/D18-2024) is an open toolkit for relational learning which provides a standard training and testing framework. Currently, the implemented models in OpenKE include TransE, TransH, TransR, TransD, RESCAL, DistMult, ComplEx and HolE.

[KRLPapers](https://github.com/thunlp/KRLPapers) is a must-read paper list for relational learning.

[Back to README](../README.md)
