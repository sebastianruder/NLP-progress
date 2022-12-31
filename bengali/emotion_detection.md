# Fine-grained Emotion Detection

Fine-grained Emotion Detection is the task of detecting one or multiple emotion of a given text.

## EmoNoBa

[EmoNoBa: A Dataset for Analyzing Fine-Grained Emotions on Noisy Bangla Texts](https://aclanthology.org/2022.aacl-short.17.pdf) is a dataset which contains 22,698 instances with each labeled with one or atmost all 6 emotions. The dataset is available [here](https://www.kaggle.com/datasets/saifsust/emonoba). The models are evaluated based on Macro Average F1-score.

| Model | F1-score | Paper / Source | Code |
| ------------ | ------------- | ------------ | ------------- |
| W1 + W2 + W3+ W4 + C1 + C2 + C3 | 42.81 | [EmoNoBa: A Dataset for Analyzing Fine-Grained Emotions on Noisy Bangla Texts](https://aclanthology.org/2022.aacl-short.17.pdf) | [Official](https://github.com/KhondokerIslam/EmoNoBa) |
