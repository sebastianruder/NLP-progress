# Question answering

Question answering is the task of answering a question.

### Table of contents

- [Reading comprehension](#reading-comprehension)
  - [FQuAD](#fquad)
  
## Reading comprehension
  
### FQuAD

The [French Question Answering dataset (FQuAD)](https://arxiv.org/abs/2002.06071) is a 
reading comprehension dataset in the style of SQuAD. It consists of 25k questions on 
Wikipedia articles. The dataset is available [here](https://fquad.illuin.tech/).

Example:

| Document  | Question | Answer |
| ------------- | -----:| -----: |
| Des observations de 2015 par la sonde Dawn ont confirmé qu'elle possède une forme sphérique, à la différence des corps plus petits qui ont une forme irrégulière. [...] |A quand remonte les observations faites par la sonde Dawn ? | 2015 |

| Model           | F1 | EM |  Paper |
| ------------- | :-----:| :-----:| --- |
| Human performance | 92.1 | 78.4 | [FQuAD: French Question Answering Dataset](https://arxiv.org/abs/2002.06071) |
| CamemBERTQA (d'Hoffschmidt et al., 2020)* | 88.0 | 77.9 | [FQuAD: French Question Answering Dataset](https://arxiv.org/abs/2002.06071) |
| CamemBERTQA (d'Hoffschmidt et al., 2020)† | 84.1 | 70.9 | [FQuAD: French Question Answering Dataset](https://arxiv.org/abs/2002.06071) |

*: trained on the FQuAD training set 

†: trained on the SQuAD training set and zero-shot transferred to the FQuAD test set.