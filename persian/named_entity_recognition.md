# Named entity recognition

Named entity recognition (NER) is the task of tagging entities in text with their corresponding type.
Approaches typically use BIO notation, which differentiates the beginning (B) and the inside (I) of entities.
O is used for non-entity tokens.

Example:

| Mark | Watney | visited | Mars |
| --- | ---| --- | --- |
| B-PER | I-PER | O | B-LOC |

### ArmanPersoNERCorpus

The [ArmanPersoNERCorpus](https://www.aclweb.org/anthology/C16-1319/) dataset contains 7,682 sentences with 250,015 tokens tagged in IOB format in six different classes, Organization, Person, Location, Facility, Event, and Product.

Download Links: [ARMAN](https://github.com/HaniehP/PersianNER/blob/master/ArmanPersoNERCorpus.zip) 

| Model           | F1  |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| ParsBERT (Farahani et al., 2020) | 99.84  | [ParsBERT: Transformer-based Model for Persian Language Understanding](https://arxiv.org/abs/2005.12515) | [Official](https://github.com/hooshvare/parsbert) |
| LSTM-CRF (Hafezi, Rezaeian, 2018) | 86.55 | [Neural Architecture for Persian Named Entity Recognition](https://ieeexplore.ieee.org/abstract/document/8700549) | - |
| mBERT (Taher et al., 2020) | 84.03  | [Beheshti-NER: Persian Named Entity Recognition Using BERT](https://arxiv.org/abs/2003.08875) | [Official](https://github.com/sEhsanTaher/Beheshti-NER) |
| Deep-CRF (Bokaei, Mahmoudi, 2018) | 81.50 | [Improved Deep Persian Named Entity Recognition](https://ieeexplore.ieee.org/abstract/document/8661067) | - |
| Deep-Local (Bokaei, Mahmoudi, 2018) | 79.19 | [Improved Deep Persian Named Entity Recognition](https://ieeexplore.ieee.org/abstract/document/8661067) | - |
| BiLSTM-CRF (Poostchi et al., 2018) | 77.45 | [BiLSTM-CRF for Persian Named-Entity Recognition](https://www.aclweb.org/anthology/L18-1701/) | - |
| SVM-HMM (Poostchi et al., 2016) | 72.59 | [PersoNER: Persian Named-Entity Recognition](https://www.aclweb.org/anthology/C16-1319/) | - |

### PEYMA

The [PEYMA](https://arxiv.org/abs/1801.09936) dataset includes 7,145 sentences with 302,530 tokens from which 41,148 tokens are tagged in IOB format in with seven different classes, Organization, Percent, Money, Location, Date, Time, and Person.

Download Links: [PEYMA](http://en.itrc.ac.ir/sites/default/files/pictures/NER.rar) 

| Model           | F1  |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| ParsBERT (Farahani et al., 2020) | 93.40  | [ParsBERT: Transformer-based Model for Persian Language Understanding](https://arxiv.org/abs/2005.12515) | [Official](https://github.com/hooshvare/parsbert) |
| mBERT (Taher et al., 2020) | 90.59  | [Beheshti-NER: Persian Named Entity Recognition Using BERT](https://arxiv.org/abs/2003.08875) | [Official](https://github.com/sEhsanTaher/Beheshti-NER) |
| Rule-Based-CRF (Shahshahani et al., 2018) | 84.00 | [PEYMA: A Tagged Corpus for Persian Named Entities](https://arxiv.org/abs/1801.09936) | - |
