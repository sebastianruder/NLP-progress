# Question answering

Question answering is the task of answering a question.

### Table of contents

- [Reading comprehension](#reading-comprehension)
  - [SberQuAD](#sberquad)
  
  
## Reading comprehension
  
### SberQuAD

The [Sberbank Question Answering dataset (SberQuAD)](https://arxiv.org/abs/1912.09723) is a reading comprehension dataset
in the style of SQuAD, which was created as part of a competition in 2017 by Sberbank. The data consists of around 50k
questions on Wikipeda. 

Because the original SberQuAD development set is not available, the original training set of SberQuAD was partitioned
into a (new) training (45,328) and testing (5,036) sets by the DeepPavlov team.

| Model           | F1 | EM |  Paper |
| ------------- | :-----:| :-----:| --- |
| BERT (Efimov et al., 2019) | 84.8 | 66.6 | [SberQuAD - Russian Reading Comprehension Dataset: Description and Analysis](https://arxiv.org/abs/1912.09723) |
| DocQA (Efimov et al., 2019) | 79.5 | 59.6 | [SberQuAD - Russian Reading Comprehension Dataset: Description and Analysis](https://arxiv.org/abs/1912.09723) |
