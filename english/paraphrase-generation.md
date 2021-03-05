# Paraphrase Generation
[Paraphrase generation](https://arxiv.org/abs/1908.07831) is the task to generate an output sentence which is sementically identical to the input sentence but contains variations in lexicon or syntext. See the example given below:

| Input (Erroneous)          | Output (Corrected)     |
| -------------------------  | ---------------------- |
|The need for investors to earn a commercial return may put upward pressure on prices| The need for profit is likely to push up prices|

### PRANMT-50M
[PARANMT-50M dataset](https://arxiv.org/pdf/1711.05732v2.pdf) is a dataset for training paraphrastic sentence embeddings. It consists of more than 50 million English-English sentential paraphrase pairs.

| Model           | BLEU  |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| Trigram (baseline)| 47.4| [Wieting and Gimpel, 2018](https://arxiv.org/pdf/1711.05732v2.pdf)| Unvailable|
| Unsupervised BART w/ Dynamic Blocking | 20.9 | [Niu et al., 2020](https://arxiv.org/pdf/2010.12885v1.pdf)| Unavailable|

### QQP-Pos
The [QQP-POS dataset](https://www.kaggle.com/c/quora-question-pairs/overview) is a datast for paraphrase generation with 400K source-target pairs. Each pair is labelled as negative if two questions are not duplicates and positive otherwise.

| Model           | BLEU  |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| Unsupervised BART w/ Dynamic Blocking | 26.76 | [Niu et al., 2020](https://arxiv.org/pdf/2010.12885v1.pdf)| Unavailable|
| ParafraGPT-UC| 35.9| [Bui et al., 2020](https://arxiv.org/pdf/2011.14344v1.pdf)| [Code](https://github.com/BH-So/unsupervised-paraphrase-generation)|
