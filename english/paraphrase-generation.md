# Paraphrase Generation
[Paraphrase generation](https://arxiv.org/abs/1908.07831) is the task of generating an output sentence that preserves the meaning of the input sentence but contains variations in word choice and grammar. See the example given below:

| Input                      | Output                 |
| -------------------------  | ---------------------- |
|The need for investors to earn a commercial return may put upward pressure on prices| The need for profit is likely to push up prices|

### PRANMT-50M
[PARANMT-50M dataset](https://arxiv.org/pdf/1711.05732v2.pdf) is a dataset for training paraphrastic sentence embeddings. It consists of more than 50 million English-English sentential paraphrase pairs.

| Model           | BLEU  |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| Trigram (baseline)| 47.4| [Wieting and Gimpel, 2018](https://arxiv.org/pdf/1711.05732v2.pdf)| Unavailable|
| Unsupervised BART w/ Dynamic Blocking | 20.9 | [Niu et al., 2020](https://arxiv.org/pdf/2010.12885v1.pdf)| Unavailable|

### QQP-Pos
The [QQP-POS dataset](https://www.kaggle.com/c/quora-question-pairs/overview) is a paraphrase generation dataset with 400K source-target pairs. Each pair is labelled as negative if two questions are not duplicates and positive otherwise.

| Model           | BLEU  |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| Unsupervised BART w/ Dynamic Blocking | 26.76 | [Niu et al., 2020](https://arxiv.org/pdf/2010.12885v1.pdf)| Unavailable|
| ParafraGPT-UC| 35.9| [Bui et al., 2020](https://arxiv.org/pdf/2011.14344v1.pdf)| [Code](https://github.com/BH-So/unsupervised-paraphrase-generation)|

### Quora
The Quora dataset (https://www.kaggle.com/c/quora-question-pairs) contains 140K paraphrased sentence pairs and 260K non-paraphrased sentence pairs

#### Unsupervised

| Model           | BLEU  |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| CGMH | 15.73 | [Miao et al., 2018](https://arxiv.org/pdf/1811.10996.pdf)|  |
| UPSA| 18.18| [Liu et al., 2019](https://arxiv.org/pdf/1909.03588.pdf)|  |
| G2LC| 23.27| [Sha et al., 2020](https://aclanthology.org/2020.emnlp-main.701.pdf)|  |
