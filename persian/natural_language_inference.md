# Natural Language Inference

Natural Language Inference (NLI) is the task of determining the inference relationship between a premise and a hypothesis. It is a three-class problem assigning each input pair to one of the classes {entailment, contradiction, neutral}. 

## Table of contents

- [FarsTail](#farstail)
  
### FarsTail

[FarsTail](https://arxiv.org/abs/2009.08820) is a Persian NLI dataset including an indexed version for non-Persian research.  
The dataset is available [here](https://github.com/dml-qom/FarsTail).

#### Example

| Premise | Label | Hypothesis |
| --- | ---| --- |
| منشور سازمان ملل متحد ۲۶ ژوئن ۱۹۴۵، در شهر سانفرانسیسکو، ایالات متحده امریکا به وسیله ۵۰ دولت از ۵۱ دولت مؤسس سازمان ملل متحد به امضا رسید. | منشور سازمان ملل متحد در سانفرانسیسکو به امضا رسید. | Entailment |
| منشور سازمان ملل متحد ۲۶ ژوئن ۱۹۴۵، در شهر سانفرانسیسکو، ایالات متحده امریکا به وسیله ۵۰ دولت از ۵۱ دولت مؤسس سازمان ملل متحد به امضا رسید. | منشور سازمان ملل متحد در نیویورک تاسیس شد. | Contradiction |
| منشور سازمان ملل متحد ۲۶ ژوئن ۱۹۴۵، در شهر سانفرانسیسکو، ایالات متحده امریکا به وسیله ۵۰ دولت از ۵۱ دولت مؤسس سازمان ملل متحد به امضا رسید. | ایران از جمله دولت‌های عضو مؤسس سازمان ملل متحد است. | Neutral |

#### Results

| Model           | Accuracy | Paper / Source |
| ------------- | :-----:| :-----:|
| Translate-Source + fastText| 78.1 | [FarsTail: A Persian Natural Language Inference Dataset](https://arxiv.org/abs/2009.08820) |
| LSTM + BERT (FarsTail) | 75.8 | [FarsTail: A Persian Natural Language Inference Dataset](https://arxiv.org/abs/2009.08820) |
| ESIM + BERT (FarsTail+MultiNLI) | 74.6 | [FarsTail: A Persian Natural Language Inference Dataset](https://arxiv.org/abs/2009.08820) |
