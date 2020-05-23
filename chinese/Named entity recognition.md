# Chinese Named Entity Recognition

Named entity recognition (NER) is the task of tagging entities in text with their corresponding type. Approaches typically use BIO notation, which differentiates the beginning (B) and the inside (I) of entities. O is used for non-entity tokens.
Example:

| 张 | 三 | 是 | 他 |
| --- | ---| --- | --- |
| B-PER | I-PER | O | O |

## Evaluation

### Metric

F1-score

### Dataset
#### Ontonotes 4.0
| Model         | F1 | Paper / Source | Code |
| ------------- | :-----: |  --- | --- |
| FLAT | 76.45 |[FLAT: Chinese NER Using Flat-Lattice Transformer](https://arxiv.org/abs/2004.11795)|[Github](https://github.com/LeeSureman/Flat-Lattice-Transformer)|
| FLAT+BERT | 81.82 |[FLAT: Chinese NER Using Flat-Lattice Transformer](https://arxiv.org/abs/2004.11795)|[Github](https://github.com/LeeSureman/Flat-Lattice-Transformer)|

#### MSRA
| Model         | F1 | Paper / Source | Code |
| ------------- | :-----: |  --- | --- |
| FLAT | 94.12 |[FLAT: Chinese NER Using Flat-Lattice Transformer](https://arxiv.org/abs/2004.11795)|[Github](https://github.com/LeeSureman/Flat-Lattice-Transformer)|
| FLAT+BERT | 96.09 |[FLAT: Chinese NER Using Flat-Lattice Transformer](https://arxiv.org/abs/2004.11795)|[Github](https://github.com/LeeSureman/Flat-Lattice-Transformer)|

#### Resume
| Model         | F1 | Paper / Source | Code |
| ------------- | :-----: |  --- | --- |
| FLAT | 95.45 |[FLAT: Chinese NER Using Flat-Lattice Transformer](https://arxiv.org/abs/2004.11795)|[Github](https://github.com/LeeSureman/Flat-Lattice-Transformer)|
| FLAT+BERT | 95.86 |[FLAT: Chinese NER Using Flat-Lattice Transformer](https://arxiv.org/abs/2004.11795)|[Github](https://github.com/LeeSureman/Flat-Lattice-Transformer)|

#### Weibo
| Model         | F1 | Paper / Source | Code |
| ------------- | :-----: |  --- | --- |
| FLAT | 60.32 |[FLAT: Chinese NER Using Flat-Lattice Transformer](https://arxiv.org/abs/2004.11795)|[Github](https://github.com/LeeSureman/Flat-Lattice-Transformer)|
| FLAT+BERT | 68.55 |[FLAT: Chinese NER Using Flat-Lattice Transformer](https://arxiv.org/abs/2004.11795)|[Github](https://github.com/LeeSureman/Flat-Lattice-Transformer)|
