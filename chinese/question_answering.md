# Question answering

Question answering is the task of answering a question.

### Table of contents

- [Reading comprehension](#reading-comprehension)
  - [CMRC2018](#cmrc-2018)
  - [DRCD](#drcd)
  - [DuReader](#dureader)
  
## Reading comprehension

### CMRC 2018

The [Chinese Machine Reading Comprehension (CMRC 2018)](https://www.aclweb.org/anthology/D19-1600/) is a SQuAD-like
reading comprehension dataset that consists of 20,000 questions annotated on Wikipedia paragraphs by human experts. The
dataset can be downloaded [here](https://github.com/ymcui/cmrc2018). Below we show the F1 and EM scores both on the
test set and the challenge set. 

| Model           | Test F1 | Test EM | Challenge F1 | Challenge EM | Paper |
| ------------- | :-----:| :-----:| --- |
| Human performance | 97.9 | 92.4 | 95.2 | 90.4 | [A Span-Extraction Dataset for Chinese Machine Reading Comprehension](https://www.aclweb.org/anthology/D19-1600/) |
| Dual BERT (w / SQuAD; Cui et al., 2019) | 90.2 | 73.6 | 55.2 | 27.8 | [Cross-Lingual Machine Reading Comprehension](https://www.aclweb.org/anthology/D19-1169/) |
| Dual BERT (Cui et al., 2019) | 88.1 | 70.4 | 47.9 | 23.8 | [Cross-Lingual Machine Reading Comprehension](https://www.aclweb.org/anthology/D19-1169/) |

### DRCD

The [Delta Reading Comprehension Dataset (DRCD)](https://arxiv.org/abs/1806.00920) is a SQuAD-like reading 
comprehension dataset that contains 30,000+ questions on 10,014 paragraphs from 2,108 Wikipedia articles. The dataset
can be downloaded [here](https://github.com/DRCKnowledgeTeam/DRCD).

| Model           | F1 | EM |  Paper |
| ------------- | :-----:| :-----:| --- |
| Human performance | 93.3 | 80.4 | [DRCD: a Chinese Machine Reading Comprehension Dataset](https://arxiv.org/abs/1806.00920) |
| Dual BERT (w / SQuAD; Cui et al., 2019) | 91.6 | 85.4 | [Cross-Lingual Machine Reading Comprehension](https://www.aclweb.org/anthology/D19-1169/) |
| Dual BERT (Cui et al., 2019) | 90.3 | 83.7 | [Cross-Lingual Machine Reading Comprehension](https://www.aclweb.org/anthology/D19-1169/) |
  
### DuReader

[DuReader](https://www.aclweb.org/anthology/W18-2605/) is a large-scale reading comprehension dataset that is based on
the logs of Baidu Search and contains 200k questions, 420k answers, and 1M documents. For more information, refer to
[its website](https://ai.baidu.com/broad/introduction?dataset=dureader) to see the introduction. You can download the
dataset [here](https://ai.baidu.com/broad/download?dataset=dureader). The best models can be view on the 
[public leaderboard](https://ai.baidu.com/broad/leaderboard?dataset=dureader).
