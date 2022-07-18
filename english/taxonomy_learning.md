# Taxonomy Learning

Taxonomy learning is the task of hierarchically classifying concepts in an automatic manner from text corpora. The process of building taxonomies is usually divided into two main steps: (1) extracting hypernyms for concepts, which may constitute a field of research in itself (see Hypernym Discovery below) and (2) refining the structure into a taxonomy.

## Hypernym Discovery

Given a corpus and a target term (hyponym), the task of hypernym discovery consists of extracting a set of its most appropriate hypernyms from the corpus. For example, for the input word “dog”, some valid hypernyms would be “canine”, “mammal” or “animal”.

### SemEval 2018

The SemEval-2018 hypernym discovery evaluation benchmark ([Camacho-Collados et al. 2018](http://aclweb.org/anthology/S18-1115)), which can be freely downloaded [here](https://competitions.codalab.org/competitions/17119), contains three domains (general, medical and music) and is also available in Italian and Spanish (not in this repository). For each domain a target corpus and vocabulary (i.e. hypernym search space) are provided. The dataset contains both concepts (e.g. dog) and entities (e.g. Manchester United) up to trigrams. The following table lists the number of hyponym-hypernym pairs for each dataset: 

| Partition           | General | Medical | Music |
| ------------- | :-----:|:-----:|:-----:|
|Trial | 200 | 101 | 355 |
|Training |  11779 | 3256 | 5455 |
|Test | 7048 | 4116 | 5233 |

The results for each model and dataset (general, medical and music) are presented below (MFH stands for “Most Frequent Hypernyms” and is used as a baseline).

**General:**

| Model           | MAP | MRR | P@5 |  Paper / Source |
| ------------- | :-----:|:-----:|:-----:| --- |
|CRIM (Bernier-Colborne and Barrière, 2018) | 19.78 | 36.10 | 19.03 | [A Hybrid Approach to Hypernym Discovery](http://aclweb.org/anthology/S18-1116) |
|vTE (Espinosa-Anke et al., 2016) | 10.60 | 23.83 | 9.91 |  [Supervised Distributional Hypernym Discovery via Domain Adaptation](https://aclweb.org/anthology/D16-1041) |
|NLP_HZ (Qui et al., 2018) | 9.37 | 17.29 | 9.19 |  [A Nearest Neighbor Approach](http://aclweb.org/anthology/S18-1148) |
|300-sparsans (Berend et al., 2018) | 8.95 | 19.44 | 8.63 |  [Hypernymy as interaction of sparse attributes ](http://aclweb.org/anthology/S18-1152) |
|MFH | 8.77 | 21.39 | 7.81 |  -- |
|SJTU BCMI (Zhang et al., 2018) | 5.77 | 10.56 | 5.96 |  [Neural Hypernym Discovery with Term Embeddings](http://aclweb.org/anthology/S18-1147) |
|Apollo (Onofrei et al., 2018) | 2.68 | 6.01 | 2.69 |  [Detecting Hypernymy Relations Using Syntactic Dependencies ](http://aclweb.org/anthology/S18-1146) |
|balAPInc (Shwartz et al., 2017) | 1.36 | 3.18 | 1.30 |  [Hypernyms under Siege: Linguistically-motivated Artillery for Hypernymy Detection](http://www.aclweb.org/anthology/E17-1007) |


**Medical domain:**

| Model           | MAP | MRR | P@5 |  Paper / Source |
| ------------- | :-----:|:-----:|:-----:| --- |
|CRIM (Bernier-Colborne and Barrière, 2018) | 34.05 | 54.64 | 36.77 | [A Hybrid Approach to Hypernym Discovery](http://aclweb.org/anthology/S18-1116) |
|MFH | 28.93 | 35.80 | 34.20 | -- |
|300-sparsans (Berend et al., 2018) | 20.75 | 40.60 | 21.43 | [Hypernymy as interaction of sparse attributes ](http://aclweb.org/anthology/S18-1152) |
|vTE (Espinosa-Anke et al., 2016) | 18.84 | 41.07 | 20.71 | [Supervised Distributional Hypernym Discovery via Domain Adaptation](https://aclweb.org/anthology/D16-1041) |
|EXPR (Issa Alaa Aldine et al., 2018) | 13.77 | 40.76 | 12.76 | [A Combined Approach for Hypernym Discovery](http://aclweb.org/anthology/S18-1150) |
|SJTU BCMI (Zhang et al., 2018) | 11.69 | 25.95 | 11.69 | [Neural Hypernym Discovery with Term Embeddings](http://aclweb.org/anthology/S18-1147) |
|ADAPT (Maldonado and Klubička, 2018) | 8.13 | 20.56 | 8.32 | [Skip-Gram Word Embeddings for Unsupervised Hypernym Discovery in Specialised Corpora ](http://aclweb.org/anthology/S18-1151) |
|balAPInc (Shwartz et al., 2017) | 0.91 | 2.10 | 1.08 | [Hypernyms under Siege: Linguistically-motivated Artillery for Hypernymy Detection](http://www.aclweb.org/anthology/E17-1007) |


**Music domain:**

| Model           | MAP | MRR | P@5 |  Paper / Source |
| ------------- | :-----:|:-----:|:-----:| --- |
|CRIM (Bernier-Colborne and Barrière, 2018) | 40.97 | 60.93 | 41.31 | [A Hybrid Approach to Hypernym Discovery](http://aclweb.org/anthology/S18-1116) |
|MFH | 33.32 | 51.48 | 35.76 | -- |
|300-sparsans (Berend et al., 2018) | 29.54 | 46.43 | 28.86 | [Hypernymy as interaction of sparse attributes ](http://aclweb.org/anthology/S18-1152) |
|vTE (Espinosa-Anke et al., 2016) | 12.99 | 39.36 | 12.41 | [Supervised Distributional Hypernym Discovery via Domain Adaptation](https://aclweb.org/anthology/D16-1041) |
|SJTU BCMI (Zhang et al., 2018) | 4.71 | 9.15 | 4.91 | [Neural Hypernym Discovery with Term Embeddings](http://aclweb.org/anthology/S18-1147) |
|ADAPT (Maldonado and Klubička, 2018) | 2.63 | 7.46 | 2.64 | [Skip-Gram Word Embeddings for Unsupervised Hypernym Discovery in Specialised Corpora ](http://aclweb.org/anthology/S18-1151) |
|balAPInc (Shwartz et al., 2017) | 1.95 | 5.01 | 2.15 | [Hypernyms under Siege: Linguistically-motivated Artillery for Hypernymy Detection](http://www.aclweb.org/anthology/E17-1007) |


## Taxonomy Enrichment

Given words that are not included in a taxonomy, the task is to associate each query word with its appropriate hypernyms. For instance, given an input word “milk” we need to provide a list of the most probable hypernyms the word could be attached to, e.g. “dairy product”, “beverage”. A word may have multiple hypernyms.

### Datasets

#### SemEval 2016 Task 14

The SemEval-2016 Task 14 aims to enrich the WordNet taxonomy with new words and word senses. A system's task is to identify the WordNet synset with which the new word sense should be merged (i.e., the term is synonymous with those in the synset) or added as a hyponym (i.e., the new word sense is a specialization of an exisiting word sense).

The following table gives examples of word senses that are not defined in WordNet and their corresponding operations, illustrating the type of data that might be seen in the task.

| OOV word | Definition |	Target synset |	Operation |
| :------------- | :-----: | :-----:|:-----:|
|geoscience#n | any of several sciences that deal with the Earth	| earth_science (any of the sciences that deal with the earth or its parts) |	MERGE |
|mudslide#n | a mixed drink consisting of vodka, Kahlua and Bailey's.	| cocktail (a short mixed drink)	| ATTACH |
| euthanize#v | to submit or animal to euthanasia |	destroy, put down (put (an animal) to death)	| MERGE |

The SemEval-2016 taxonomy enrichment evaluation benchmark ([Jurgens and Pilehvar 2016](https://aclanthology.org/S16-1169/)), which can be freely downloaded [here](http://alt.qcri.org/semeval2016/task14/data/uploads/semeval-2016-task-14.zip).

Novel concepts were limited to nouns and verbs, as only these parts of speech have fully-developed taxonomies in WordNet. For each item, in addition to the target synset and
the operation MERGE/ATTACH, the glosses were also provided along with the source URL from which the new word sense was obtained. The dataset consists of a total of 1000 items, split into training and test datasets containing 400 and 600 items, respectively. The following table lists the number of items for each dataset:

| Partition           | Noun | Verb |
| ------------- | :-----:|:-----:|
|Trial | 93 | 34 | 
|Training |  349 | 51|
|Test |  516 | 84 | 

The results for each model participant are presented below.

| Model | Lemma Match | Wu&P | Recall  | F1 | Paper / Source |
| ------------- | :-----:|:-----:|:-----:|:-----:|  --- |
|MSejrKU (Schlichtkrull and Alonso, 2016) |0.428 |0.523| 0.973| 0.680|[MSejrKu at SemEval-2016 Task 14: Taxonomy Enrichment by Evidence Ranking](https://aclanthology.org/S16-1209/)|
|TALN (Anke et al., 2016) |0.360| 0.476| 1.000| 0.645|[Semantic Taxonomy Enrichment Via Sense-Based Embeddings](https://aclanthology.org/S16-1208/)|
|VCU (McInnes, 2016) |0.161 |0.432 |0.997| 0.602|[Evaluating definitional-based similarity measure for semantic taxonomy enrichment](https://aclanthology.org/S16-1212/)|
|Duluth (Pedersen, 2016) |0.043| 0.347| 1.000| 0.515|[Extending Gloss Overlaps to Enrich Semantic Taxonomies](https://aclanthology.org/S16-1207/)|
|Deftor (Tanev and Rotondi, 2016) |0.066| 0.347| 0.987| 0.513|[Taxonomy Enrichment using Definition Vectors](https://aclanthology.org/S16-1210)|
|UMNDuluth (Rusert and Pedersen, 2016) |0.098 |0.340| 0.998 |0.507|[WordNet’s Missing Lemmas](https://aclanthology.org/S16-1211/)|
|Baseline: First word, first sense (Jurgens and Pilehvar, 2016) |0.415| 0.514| 1.000| 0.679|[SemEval-2016 Task 14: Semantic Taxonomy Enrichment](https://aclanthology.org/S16-1169/)|
|Baseline: Random synset (Jurgens and Pilehvar, 2016) | 0.000 |0.227| 1.000| 0.370|[SemEval-2016 Task 14: Semantic Taxonomy Enrichment](https://aclanthology.org/S16-1169/)|


####  Diachronic WordNet Datasets

The SemEval-2016 Task 14 setting implies pre-defined glosses. However, it is possible that new words that should be added to the taxonomy may have no definition in any other sources: they could be very rare (“apparatchik”, “falanga”), relatively new (“selfie”, “hashtag”) or come from a narrow domain (“vermiculite”).

[Nikishina et al., 2020](https://aclanthology.org/2020.coling-main.276/) created multiple datasets for studying diachronic evolution of wordnets, which can be downloaded from [here](https://doi.org/10.5281/zenodo.4279821). They chose two versions of WordNet and then select words which appear only in a newer version. For each word, they got its hypernyms from the newer WordNet version and consider them as gold standard
hypernyms. The words were added to the dataset if only their hypernyms appear in both snippets. They skipped one or more WordNet versions, otherwise the dataset would be too small. 

| Dataset | Noun | Verb |
| ------------- | :-----:|:-----:|
|WordNet 1.6 - WordNet 3.0 | 17 043 | 755 | 
|WordNet 1.7 - WordNet 3.0 |  6 161 | 362|
|WordNet 2.0 - WordNet 3.0 | 2 620 | 193 | 

The results for each system on the current dataset are presented below.

##### WordNet 1.6 - WordNet 3.0

| Model           | MAP (Nouns) | MAP (Verbs)|  Paper / Source |
| ------------- | :-----:| :-----:| --- |
|DWRank-Meta (Meta-embeddings based on Word and Graph Embeddings) | 0.367 | 0.288 | [Taxonomy enrichment with text and graph vector representations](https://content.iospress.com/articles/semantic-web/sw212955)|
|AAEME triplet loss (Tikhomirov and Loukachevitch, 2021) | 0.345 | 0.289 | [Meta-Embeddings in Taxonomy Enrichment Task](http://www.dialog-21.ru/media/5287/tikhomirovmmplusloukachevitchnv091.pdf)|
|Ranking + Wiki (Nikishina et al., 2020) | 0.337 | 0.270 | [Studying Taxonomy Enrichment on Diachronic WordNet Versions](https://aclanthology.org/2020.coling-main.276/) |
|Ranking + Wiki + node2vec + Poincare (Nikishina et al., 2021) | 0.311 | 0.251 | [Exploring Graph-based Representations for Taxonomy Enrichment](https://aclanthology.org/2021.gwc-1.15/)|


##### WordNet 1.7 - WordNet 3.0

| Model           | MAP (Nouns) | MAP (Verbs)|  Paper / Source |
| ------------- | :-----:| :-----:| --- |
|DWRank-Meta (Meta-embeddings based on Word and Graph Embeddings) | 0.418 | 0.227 | [Taxonomy enrichment with text and graph vector representations](https://content.iospress.com/articles/semantic-web/sw212955)|
|AAEME triplet loss (Tikhomirov and Loukachevitch, 2021) |  0.394 | 0.239 | [Meta-Embeddings in Taxonomy Enrichment Task](http://www.dialog-21.ru/media/5287/tikhomirovmmplusloukachevitchnv091.pdf)|
|Ranking + Wiki (Nikishina et al., 2020) | 0.380 | 0.200 | [Studying Taxonomy Enrichment on Diachronic WordNet Versions](https://aclanthology.org/2020.coling-main.276/) |
|Ranking + Wiki + node2vec + Poincare (Nikishina et al., 2021) | 0.350 |  0.177 | [Exploring Graph-based Representations for Taxonomy Enrichment](https://aclanthology.org/2021.gwc-1.15/)|


##### WordNet 2.0 - WordNet 3.0

| Model           | MAP (Nouns) | MAP (Verbs)|  Paper / Source |
| ------------- | :-----:| :-----:| --- |
|DWRank-Meta (Meta-embeddings based on Word and Graph Embeddings) | 0.480 | 0.280 | [Taxonomy enrichment with text and graph vector representations](https://content.iospress.com/articles/semantic-web/sw212955)|
|AAEME triplet loss (Tikhomirov and Loukachevitch, 2021) | 0.445 | 0.272 | [Meta-Embeddings in Taxonomy Enrichment Task](http://www.dialog-21.ru/media/5287/tikhomirovmmplusloukachevitchnv091.pdf)|
|Ranking + Wiki (Nikishina et al., 2020) | 0.400 | 0.238 | [Studying Taxonomy Enrichment on Diachronic WordNet Versions](https://aclanthology.org/2020.coling-main.276/) |
|Ranking + Wiki + node2vec + Poincare (Nikishina et al., 2021) | 0.300 | 0.248 | [Exploring Graph-based Representations for Taxonomy Enrichment](https://aclanthology.org/2021.gwc-1.15/)|

