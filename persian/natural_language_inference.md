# Natural language inference

Natural language inference is the task of determining whether a "hypothesis" is 
true (entailment), false (contradiction), or undetermined (neutral) given a "premise".

Example:

| Premise | Label | Hypothesis |
| --- | ---| --- |
| منشور سازمان ملل متحد ۲۶ ژوئن ۱۹۴۵، در شهر سانفرانسیسکو، ایالات متحده امریکا به وسیله ۵۰ دولت از ۵۱ دولت مؤسس سازمان ملل متحد به امضا رسید. | منشور سازمان ملل متحد در سانفرانسیسکو به امضا رسید. | Entailment |
| منشور سازمان ملل متحد ۲۶ ژوئن ۱۹۴۵، در شهر سانفرانسیسکو، ایالات متحده امریکا به وسیله ۵۰ دولت از ۵۱ دولت مؤسس سازمان ملل متحد به امضا رسید. | منشور سازمان ملل متحد در نیویورک تاسیس شد. | Contradiction |
| منشور سازمان ملل متحد ۲۶ ژوئن ۱۹۴۵، در شهر سانفرانسیسکو، ایالات متحده امریکا به وسیله ۵۰ دولت از ۵۱ دولت مؤسس سازمان ملل متحد به امضا رسید. | ایران از جمله دولت‌های عضو مؤسس سازمان ملل متحد است. | Neutral |


### FarsTail

[FarsTail](https://github.com/dml-qom/FarsTail) is the first Natural Language Inference dataset effort on Persian, containing 10,367 pairs of sentences labeled as entailment, contradiction, or neutral.

| Model           | Test Accuracy | Paper |
| ------------- | :-----:| :-----:|
| Translate-Source + fastText| 78.1 | [FarsTail: A Persian Natural Language Inference Dataset](https://arxiv.org/abs/2009.08820) |
| LSTM + BERT (FarsTail) | 75.8 | [FarsTail: A Persian Natural Language Inference Dataset](https://arxiv.org/abs/2009.08820) |
| ESIM + BERT (FarsTail+MultiNLI) | 74.6 | [FarsTail: A Persian Natural Language Inference Dataset](https://arxiv.org/abs/2009.08820) |
