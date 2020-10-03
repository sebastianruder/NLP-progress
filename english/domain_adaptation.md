# Domain adaptation

## Sentiment analysis

### Multi-Domain Sentiment Dataset

The [Multi-Domain Sentiment Dataset](https://www.cs.jhu.edu/~mdredze/datasets/sentiment/) is a common
evaluation dataset for domain adaptation for sentiment analysis. It contains product reviews from
Amazon.com from different product categories, which are treated as distinct domains.
Reviews contain star ratings (1 to 5 stars) that are generally converted into binary labels. Models are
typically evaluated on a target domain that is different from the source domain they were trained on, while only
having access to unlabeled examples of the target domain (unsupervised domain adaptation). The evaluation
metric is accuracy and scores are averaged across each domain.

| Model           | DVD | Books | Electronics | Kitchen | Average |  Paper / Source |
| ------------- | :-----:| :-----:| :-----:| :-----:| :-----:| --- |
| Multi-task tri-training (Ruder and Plank, 2018) | 78.14 | 74.86 | 81.45 | 82.14 | 79.15 | [Strong Baselines for Neural Semi-supervised Learning under Domain Shift](https://arxiv.org/abs/1804.09530) |
| Asymmetric tri-training (Saito et al., 2017) | 76.17 | 72.97 | 80.47 | 83.97 | 78.39 | [Asymmetric Tri-training for Unsupervised Domain Adaptation](https://arxiv.org/abs/1702.08400) |
| VFAE (Louizos et al., 2015) | 76.57 | 73.40 | 80.53 | 82.93 | 78.36 | [The Variational Fair Autoencoder](https://arxiv.org/abs/1511.00830) |
| DANN (Ganin et al., 2016) | 75.40 | 71.43 | 77.67 | 80.53 | 76.26 | [Domain-Adversarial Training of Neural Networks](https://arxiv.org/abs/1505.07818) |

## Financial Technology and Natural Language Processing (FinNLP) 

The [FinNLP Progress](https://github.com/YangLinyi/FinNLP-Progress) is a repository to track the progress in Natural Language Processing (NLP) related to the domain of Finance, including the datasets, papers, and current state-of-the-art results for the most popular tasks. Examples include Financial Event Prediction, Financial Index Forecasting, Financial Risk Analysis, Financial Text Mining, Fraud Detection, etc.

[Go back to the README](../README.md)
