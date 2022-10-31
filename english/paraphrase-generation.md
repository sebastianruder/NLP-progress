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

### MULTIPIT, MULTIPITCROWD and MULTIPITEXPERT

Past efforts on creating paraphrase corpora only consider one paraphrase criteria without taking into account the fact that the desired “strictness” of semantic equivalence in paraphrases varies from task to task (Bhagat and Hovy, 2013; Liu and Soh, 2022). For example, for the purpose of tracking unfolding events, “A tsunami hit Haiti.” and “303 people died because of the tsunami in Haiti” are sufficiently close to be considered as paraphrases; whereas for paraphrase generation, the extra information “303 people dead” in the latter sentence may lead models to learn to hallucinate and generate more unfaithful content. In this paper, the authors present an effective data collection and annotation method to address these issues.

MULTIPIT is a topic Paraphrase in Twitter corpus that consists of a total of 130k sentence pairs with crowdsoursing (MULTIPITCROWD ) and expert (MULTIPITEXPERT ) annotations. MULTIPITCROWD is a large crowdsourced set of 125K sentence pairs that is useful for tracking information onTwitter.
| Model           | F1  |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| DeBERTaV3large | 92.00 |[Improving Large-scale Paraphrase Acquisition and Generation](https://arxiv.org/pdf/2210.03235v2.pdf)| Unavailable|


MULTIPITEXPERT is an expert annotated set of 5.5K sentence pairs using a stricter definition that is more suitable for acquiring paraphrases for
generation purpose. 
| Model           | F1  |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| DeBERTaV3large | 83.20 |[Improving Large-scale Paraphrase Acquisition and Generation](https://arxiv.org/pdf/2210.03235v2.pdf)| Unavailable|
