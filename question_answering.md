# Question answering

Question answering is the task of answering a question.

### ARC

The [AI2 Reasoning Challenge (ARC)](http://ai2-website.s3.amazonaws.com/publications/AI2ReasoningChallenge2018.pdf) 
dataset is a question answering, which contains 7,787 genuine grade-school level, multiple-choice science questions.
The dataset is partitioned into a Challenge Set and an Easy Set. The Challenge Set contains only questions 
answered incorrectly by both a retrieval-based algorithm and a word co-occurrence algorithm. Models are evaluated
based on accuracy.

A public leaderboard is available on the [ARC website](http://data.allenai.org/arc/).

## Reading comprehension

Most current question answering datasets frame the task as reading comprehension where the question is about a paragraph
or document and the answer often is a span in the document. The Machine Reading group
at UCL also provides an [overview of reading comprehension tasks](https://uclmr.github.io/ai4exams/data.html).

### CNN / Daily Mail

The [CNN / Daily Mail dataset](https://arxiv.org/abs/1506.03340) is a Cloze-style reading comprehension dataset
created from CNN and Daily Mail news articles using heuristics. [Close-style](https://en.wikipedia.org/wiki/Cloze_test)
means that a missing word has to be inferred. In this case, "questions" were created by replacing entities
from bullet points summarizing one or several aspects of the article. Coreferent entities have been replaced with an
entity marker @entityn where n is a distinct index.
The model is tasked to infer the missing entity
in the bullet point based on the content of the corresponding article and models are evaluated based on
their accuracy on the test set.

|         | CNN | Daily Mail |
| ------------- | -----:| -----: |
| # Train | 380,298 | 879,450 |
| # Dev | 3,924 | 64,835 |
| # Test | 3,198 | 53,182 |

Example:

| Passage  | Question | Answer |
| ------------- | -----:| -----: |
| ﻿( @entity4 ) if you feel a ripple in the force today , it may be the news that the official @entity6 is getting its first gay character . according to the sci-fi website @entity9 , the upcoming novel " @entity11 " will feature a capable but flawed @entity13 official named @entity14 who " also happens to be a lesbian . " the character is the first gay figure in the official @entity6 -- the movies , television shows , comics and books approved by @entity6 franchise owner @entity22 -- according to @entity24 , editor of " @entity6 " books at @entity28 imprint @entity26 . | characters in " @placeholder " movies have gradually become more diverse | @entity6 |

| Model           | CNN  | Daily Mail  |  Paper / Source |
| ------------- | :-----:| :-----:|--- |
| Neural net (Chen et al., 2016) | 72.4 | 75.8 | [A Thorough Examination of the CNN/Daily Mail Reading Comprehension Task](https://www.aclweb.org/anthology/P16-1223) |
| Classifier (Chen et al., 2016) | 67.9 | 68.3 | [A Thorough Examination of the CNN/Daily Mail Reading Comprehension Task](https://www.aclweb.org/anthology/P16-1223) |
| Impatient Reader (Hermann et al., 2015) | 63.8 | 68.0 | [Teaching Machines to Read and Comprehend](https://arxiv.org/abs/1506.03340) |

### QAngaroo

[QAngaroo](http://qangaroo.cs.ucl.ac.uk/index.html) is a set of two reading comprehension datasets,
which require multiple steps of inference that combine facts from multiple documents. The first dataset, WikiHop
is open-domain and focuses on Wikipedia articles. The second dataset, MedHop is based on paper abstracts from
PubMed.

The leaderboards for both datasets are available on the [QAngaroo website](http://qangaroo.cs.ucl.ac.uk/leaderboard.html).

### RACE

The [RACE dataset](https://arxiv.org/abs/1704.04683) is a reading comprehension dataset 
collected from English examinations in China, which are designed for middle school and high school students. 
The dataset contains more than 28,000 passages and nearly 100,000 questions and can be 
downloaded [here](http://www.cs.cmu.edu/~glai1/data/race/). Models are evaluated based on accuracy
on middle school examinations (RACE-m), high school examinations (RACE-h), and on the total dataset (RACE).

| Model           | RACE-m | RACE-h | RACE | Paper / Source |
| ------------- | :-----:| :-----:| :-----:| --- |
| Finetuned Transformer LM (Radford et al., 2018) | 62.9 | 57.4 | 59.0 | [Improving Language Understanding by Generative Pre-Training](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf) |
| BiAttention MRU (Tay et al., 2018) | 60.2 | 50.3 | 53.3 | [Multi-range Reasoning for Machine Comprehension](https://arxiv.org/abs/1803.09074) |

### SQuAD

The [Stanford Question Answering Dataset (SQuAD)](https://arxiv.org/abs/1606.05250)
is a reading comprehension dataset, consisting of questions posed by crowdworkers 
on a set of Wikipedia articles. The answer to every question is a segment of text (a span)
from the corresponding reading passage. Recently, [SQuAD 2.0](https://arxiv.org/abs/1806.03822)
has been released, which includes unanswerable questions.

The public leaderboard is available on the [SQuAD website](https://rajpurkar.github.io/SQuAD-explorer/).

### Story Cloze Test

The [Story Cloze Test](http://aclweb.org/anthology/W17-0906.pdf) is a dataset for
story understanding that provides systems with four-sentence stories and two possible
endings. The systems must then choose the correct ending to the story.

| Model           | Accuracy  |  Paper / Source |
| ------------- | :-----:| --- |
| Finetuned Transformer LM (Radford et al., 2018) | 86.5 | [Improving Language Understanding by Generative Pre-Training](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf) |
| Hidden Coherence Model (Chaturvedi et al., 2017) | 77.6 | [Story Comprehension for Predicting What Happens Next](http://aclweb.org/anthology/D17-1168) |
| val-LS-skip (Srinivasan et al., 2018) | 76.5 | [A Simple and Effective Approach to the Story Cloze Test](http://aclweb.org/anthology/N18-2015) |

### Winograd Schema Challenge

The [Winograd Schema Challenge](https://www.aaai.org/ocs/index.php/KR/KR12/paper/view/4492)
is a dataset for common sense reasoning. It employs Winograd Schema questions that 
require the resolution of anaphora: the system must identify the antecedent of an ambiguous pronoun in a statement. Models
are evaluated based on accuracy.

Example:

The trophy doesn’t fit in the suitcase because _it_ is too big. What is too big?
Answer 0: the trophy. Answer 1: the suitcase

| Model           | Score  |  Paper / Source |
| ------------- | :-----:| --- |
| Word-LM-partial (Trinh and Le, 2018) | 62.6 | [A Simple Method for Commonsense Reasoning](https://arxiv.org/abs/1806.02847) |
| Char-LM-partial (Trinh and Le, 2018) | 57.9 | [A Simple Method for Commonsense Reasoning](https://arxiv.org/abs/1806.02847) |
| USSM + Supervised DeepNet + KB (Liu et al., 2017) | 52.8 | [Combing Context and Commonsense Knowledge Through Neural Networks for Solving Winograd Schema Problems](https://aaai.org/ocs/index.php/SSS/SSS17/paper/view/15392) |

[Go back to the README](README.md)
