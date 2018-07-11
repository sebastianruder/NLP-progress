# Named entity recognition

Named entity recognition (NER) is the task of tagging entities in text with their corresponding type.
Approaches typically use BIO notation, which differentiates the beginning (B) and the inside (I) of entities.
O is used for non-entity tokens.

Example:

| Mark | Watney | visited | Mars |
| --- | ---| --- | --- |
| B-PER | I-PER | O | B-LOC |

### CoNLL 2003

The [CoNLL 2003 NER task](http://www.aclweb.org/anthology/W03-0419.pdf) consists of newswire text from the Reuters RCV1 
corpus tagged with four different entity types (PER, LOC, ORG, MISC). Models are evaluated based on span-based F1.

| Model           | F1  |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| Flair embeddings (Akbik et al., 2018) | 93.09 | [Contextual String Embeddings for Sequence Labeling](https://drive.google.com/file/d/17yVpFA7MmXaQFTe-HDpZuqw9fJlmzg56/view) | [Flair framework](https://github.com/zalandoresearch/flair)
| BiLSTM-CRF+ELMo (Peters et al., 2018) | 92.22 | [Deep contextualized word representations](https://arxiv.org/abs/1802.05365) | |
| Peters et al. (2017) | 91.93 | [Semi-supervised sequence tagging with bidirectional language models](https://arxiv.org/abs/1705.00108) | |
| Yang et al. (2017) | 91.26 | [Transfer Learning for Sequence Tagging with Hierarchical Recurrent Networks](https://arxiv.org/abs/1703.06345) | |
| Ma and Hovy (2016) | 91.21 | [End-to-end Sequence Labeling via Bi-directional LSTM-CNNs-CRF](https://arxiv.org/abs/1603.01354) | |
| LSTM-CRF (Lample et al., 2016) | 90.94 | [Neural Architectures for Named Entity Recognition](https://arxiv.org/abs/1603.01360) | |

### Long-tail emerging entities

The [WNUT 2017 Emerging Entities task](http://aclweb.org/anthology/W17-4418) operates over a wide range of English 
text and focuses on generalisation beyond memorisation in high-variance environments. Scores are given both over
entity chunk instances, and unique entity surface forms, to normalise the biasing impact of entities that occur frequently.

#### Dataset

| Feature | Train | Dev | Test |
| --- | --- | --- | --- |
| Posts | 3,395 | 1,009 | 1,287 |
| Tokens | 62,729 | 15,733 | 23,394 |
| NE tokens | 3,160 | 1,250 | 1,589 |

The data is annotated for six classes - person, location, group, creative work, product and corporation.

Links: [WNUT 2017 Emerging Entity task page](https://noisy-text.github.io/2017/emerging-rare-entities.html) (including direct download links for data and scoring script)

#### State-of-the-art

| Model         | F1  | F1 (surface form) |  Paper / Source |
| ---           | --- | ---               | --- |
| SpinningBytes | 40.78 | 39.33 | [Transfer Learning and Sentence Level Features for Named Entity Recognition on Tweets](http://aclweb.org/anthology/W17-4422.pdf) | 
| Aguilar et al. (2018) | 45.55 | | [Modeling Noisiness to Recognize Named Entities using Multitask Neural Networks on Social Media](http://aclweb.org/anthology/N18-1127.pdf) |


[Go back to the README](README.md)
