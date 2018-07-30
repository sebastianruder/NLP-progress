# Hypernym Discovery

Given a corpus and a target term (hyponym), the task of hypernym discovery consists of extracting a set of its most appropriate hypernyms from the corpus. For example, for the input word “dog”, some valid hypernyms would be “canine”, “mammal” or “animal”.

### SemEval 2018

The SemEval-2018 hypernym discovery evaluation benchmark ([Camacho-Collados et al. 2018](http://aclweb.org/anthology/S18-1115)), which can be freely downloaded [here](https://competitions.codalab.org/competitions/17119), contains three domains (general, medical and music) and is also available in Italian and Spanish (not in this repository). For each domain a target corpus and vocabulary (i.e. hypernym search space) are provided. The dataset contains both concepts (e.g. dog) and entities (e.g. Manchester United) up to trigrams. The following table lists the number of hyponym-hypernym pairs for each dataset: 

| Partition           | General | Medical | Music |
| ------------- | :-----:|:-----:|:-----:|
|Trial | 200 | 101 | 355 |
|Training |  11779 | 3256 | 5455 |
|Test | 7048 | 4116 | 5233 |

The results for each model and dataset are presented below (MFH stands for “Most Frequent Hypernyms” and is used as a baseline).

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
|CRIM | 40.97 | 60.93 | 41.31 | [A Hybrid Approach to Hypernym Discovery](http://aclweb.org/anthology/S18-1116) |
|MFH | 33.32 | 51.48 | 35.76 | -- |
|300-sparsans (Berend et al., 2018) | 29.54 | 46.43 | 28.86 | [Hypernymy as interaction of sparse attributes ](http://aclweb.org/anthology/S18-1152) |
|vTE (Espinosa-Anke et al., 2016) | 12.99 | 39.36 | 12.41 | [Supervised Distributional Hypernym Discovery via Domain Adaptation](https://aclweb.org/anthology/D16-1041) |
|SJTU BCMI (Zhang et al., 2018) | 4.71 | 9.15 | 4.91 | [Neural Hypernym Discovery with Term Embeddings](http://aclweb.org/anthology/S18-1147) |
|ADAPT (Maldonado and Klubička, 2018) | 2.63 | 7.46 | 2.64 | [Skip-Gram Word Embeddings for Unsupervised Hypernym Discovery in Specialised Corpora ](http://aclweb.org/anthology/S18-1151) |
|balAPInc (Shwartz et al., 2017) | 1.95 | 5.01 | 2.15 | [Hypernyms under Siege: Linguistically-motivated Artillery for Hypernymy Detection](http://www.aclweb.org/anthology/E17-1007) |
