# Relation Prediction

## Task

Relation Prediction is the task of recognizing a named relation between two named semantic entities. The common test setup is to hide one entity from the relation triplet, asking the system to recover it based on the other entity and the relation type.

For example, given the triple \<*Roman Jakobson*, *born-in-city*, *?*\>, the system is required to replace the question mark with *Moscow*.

Relation Prediction datasets are typically extracted from two types of resources: 
* *Knowledge Bases*: KBs such as [FreeBase](https://developers.google.com/freebase/) contain hundreds or thousands of relation types pertaining to world-knowledge obtained autmoatically or semi-automatically from various resources on millions of entities. These relations include *born-in*, *nationality*, *is-in* (for geographical entities), *part-of* (for organizations, among others), and more.
* *Semantic Graphs*: SGs such as [WordNet](https://wordnet.princeton.edu/) are often manually-curated resources of semantic concepts, restricted to more "linguistic" relations compared to free real-world knowledge. The most common semantic relation is *hypernym*, also known as the *is-a* relation (example: \<*cat*, *hypernym*, *feline*\>).

## Evaluation

Evaluation in Relation Prediction hinges on a list of ranked candidates given by the system to the test instance. The metrics below are derived from the location of correct candidate(s) in that list.

A common action performed before evaluation on a given list is *filtering*, where the list is cleaned of entities known to mismatch the type of expected entity to the relation. Unless specified otherwise, results here are from filtered lists.

### Metrics

#### Mean Reciprocal Rank (MRR):

The mean of all reciprocal ranks for the true candidates over the test set (1/rank).

#### Hits at k (H@k):

The rate of correct entities appearing in the top *k* entries for each instance list. This number may exceed 1.00 if the average *k*-truncated list contains more than one true entity.

### Datasets

#### WordNet-18-RR (WN18RR)

The WN18 dataset was introduced in Bordes et al., 2013. It included the full 18 relations scraped from WordNet for roughly 41,000 synsets. This dataset was found to suffer from major training set leakage, initially by Socher et al. 2013. This means reciprocal edges from symmetric relations (e.g. *hypernym*-*hyponym*) appear in one form in the training or dev set, and in the other in the test set. A trivial rule-based system recovering these regularities surpasses 90% performance on the test set.

As a way to overcome this problem, Dettmers et al. (2018) introduced the WN18RR dataset, derived from WN18, which features 11 relations only, no pair of which is reciprocal (but still include four internally-symmetric relations like *verb_group*, allowing the rule-based system to reach 35 on all three metrics).

The test set is composed of triplets, each used to create two test instances, one for each entity to be predicted. Since each instance is associated with a single true entity, the maximum value for all metrics is 1.00.

{% include table.html
   results=site.data.relation_prediction.WN18RR
   scores='H@10,H@1,MRR' %}

[Back to README](README.md)
