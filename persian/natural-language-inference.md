# Natural Language Inference

Natural Language Inference (NLI) is the task of determining the inference relationship between a premise and a hypothesis. It is a three-class problem assigning each input pair to one of the classes {entailment, contradiction, neutral}. 

### Table of contents

- [FarsTail](#farstail)
  
## FarsTail

[FarsTail](https://arxiv.org/abs/2009.08820) is a Persian NLI dataset including an indexed version for non-Persian research.  
The dataset is available [here](https://github.com/dml-qom/FarsTail).

#### Example

| Premise  | Hypothesis | Relationship |
| ------------- | -----:| -----: |
| مجمع عمومی سازمان ملل متحد رسماً آنتونیو گوترش را بعنوان دبیرکل بعدي سازمان ملل متحد و جانشین بان کی مون انتخاب کرد. |دبیر کل سازمان ملل متحد قبل از آنتونیو گوترش، بان کی مون بود. |Entailment |

#### Results
| Model           | Test Accuracy | Paper |
| ------------- | :-----:| :-----:|
| Translate-Source + fastText| 78.1 | [FarsTail: A Persian Natural Language Inference Dataset](https://arxiv.org/abs/2009.08820) |
| LSTM + BERT (FarsTail) | 75.8 | [FarsTail: A Persian Natural Language Inference Dataset](https://arxiv.org/abs/2009.08820) |
| ESIM + BERT (FarsTail+MultiNLI) | 74.6 | [FarsTail: A Persian Natural Language Inference Dataset](https://arxiv.org/abs/2009.08820) |
