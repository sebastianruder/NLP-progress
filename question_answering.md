# Question answering

Question answering is the task of answering a question.

### ARC

The [AI2 Reasoning Challenge (ARC)](http://ai2-website.s3.amazonaws.com/publications/AI2ReasoningChallenge2018.pdf)
dataset is a question answering, which contains 7,787 genuine grade-school level, multiple-choice science questions.
The dataset is partitioned into a Challenge Set and an Easy Set. The Challenge Set contains only questions
answered incorrectly by both a retrieval-based algorithm and a word co-occurrence algorithm. Models are evaluated
based on accuracy.

A public leaderboard is available on the [ARC website](http://data.allenai.org/arc/).

## Reading comprehension

Most current question answering datasets frame the task as reading comprehension where the question is about a paragraph
or document and the answer often is a span in the document. The Machine Reading group
at UCL also provides an [overview of reading comprehension tasks](https://uclmr.github.io/ai4exams/data.html).

### CliCR

The [CliCR dataset](http://aclweb.org/anthology/N18-1140) is a gap-filling reading comprehension dataset consisting of around 100,000 queries and their associated documents. The dataset was built from clinical case reports, requiring the reader to answer the query with a medical problem/test/treatment entity. The abilities to perform bridging inferences and track objects have been found to be the most frequently required skills for successful answering.

The instructions for accessing the dataset, the processing scripts, the baselines and the adaptations of some neural models can be found [here](https://github.com/clips/clicr).

Example:

| Document  | Question | Answer |
| ------------- | -----:| -----: |
| We report a case of a 72-year-old Caucasian woman with pl-7 positive antisynthetase syndrome. Clinical presentation included interstitial lung disease, myositis, mechanic’s hands and dysphagia. As lung injury was the main concern, treatment consisted of prednisolone and cyclophosphamide. Complete remission with reversal of pulmonary damage was achieved, as reported by CT scan, pulmonary function tests and functional status. [...] | Therefore, in severe cases an aggressive treatment, combining ________ and glucocorticoids as used in systemic vasculitis, is suggested.| cyclophoshamide |

| Model           | F1 |  Paper |
| ------------- | :-----:| --- |
| Gated-Attention Reader (Dhingra et al., 2017) | 33.9 | [CliCR: A Dataset of Clinical Case Reports for Machine Reading Comprehension](http://aclweb.org/anthology/N18-1140) |
| Stanford Attentive Reader (Chen et al., 2016) | 27.2| [CliCR: A Dataset of Clinical Case Reports for Machine Reading Comprehension](http://aclweb.org/anthology/N18-1140) |


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
| GA Reader(Dhingra et al., 2017) | 77.9 | 80.9 | [Gated-Attention Readers for Text Comprehension](http://aclweb.org/anthology/P17-1168) |
| BIDAF(Seo et al., 2017) | 76.9 | 79.6 |[Bidirectional Attention Flow for Machine Comprehension](https://arxiv.org/pdf/1611.01603.pdf)|
| AoA Reader(Cui et al., 2017) | 74.4 | - | [Attention-over-Attention Neural Networks for Reading Comprehension](http://aclweb.org/anthology/P17-1055) |
| Neural net (Chen et al., 2016) | 72.4 | 75.8 | [A Thorough Examination of the CNN/Daily Mail Reading Comprehension Task](https://www.aclweb.org/anthology/P16-1223) |
| Classifier (Chen et al., 2016) | 67.9 | 68.3 | [A Thorough Examination of the CNN/Daily Mail Reading Comprehension Task](https://www.aclweb.org/anthology/P16-1223) |
| Impatient Reader (Hermann et al., 2015) | 63.8 | 68.0 | [Teaching Machines to Read and Comprehend](https://arxiv.org/abs/1506.03340) |


### MS MARCO
[MS MARCO](http://www.msmarco.org/dataset.aspx) aka Human Generated MAchine
Reading COmprehension Dataset, is designed and developed by Microsoft AI & Research. [Link to paper](https://arxiv.org/abs/1611.09268)
- The questions are obtained from real anonymized user queries.
- The answers are human generated. The context passages from which the answers are obtained are extracted from real documents using the latest Bing search engine.
- The data set contains 100,000 queries and a subset of them contain multiple answers, and aim to release 1M queries in the future.  

The leaderboards for multiple tasks are available on the [MS MARCO leaderboard page](http://www.msmarco.org/leaders.aspx).

### MultiRC
MultiRC (Multi-Sentence Reading Comprehension) is a dataset of short paragraphs and multi-sentence questions that can be answered from the content of the paragraph.
We have designed the dataset with three key challenges in mind:
 - The number of correct answer-options for each question is not pre-specified. This removes the over-reliance of current approaches on answer-options and forces them to decide on the correctness of each candidate answer independently of others. In other words, unlike previous work, the task here is not to simply identify the best answer-option, but to evaluate the correctness of each answer-option individually.
 - The correct answer(s) is not required to be a span in the text.
 - The paragraphs in our dataset have diverse provenance by being extracted from 7 different domains such as news, fiction, historical text etc., and hence are expected to be more diverse in their contents as compared to single-domain datasets.

The leaderboards for the dataset is available on the [MultiRC website](http://cogcomp.org/multirc/).

### NewsQA

The [NewsQA dataset](https://arxiv.org/pdf/1611.09830.pdf) is a reading comprehension dataset of over 100,000
human-generated question-answer pairs from over 10,000 news articles from CNN, with answers consisting of spans of text
from the corresponding articles.
Some challenging characteristics of this dataset are:
- Answers are spans of arbitrary length;
- Some questions have no answer in the corresponding article;
- There are no candidate answers from which to choose.
Although very similar to the SQuAD dataset, NewsQA offers a greater challenge to existing models at time of
introduction (eg. the paragraphs are longer than those in SQuAD). Models are evaluated based on F1 and Exact Match.

Example:

| Story  | Question | Answer |
| ------------- | -----:| -----: |
| MOSCOW, Russia (CNN) -- Russian space officials say the crew of the Soyuz space ship is resting after a rough ride back to Earth. A South Korean bioengineer was one of three people on board the Soyuz capsule. The craft carrying South Korea's first astronaut landed in northern Kazakhstan on Saturday, 260 miles (418 kilometers) off its mark, they said. Mission Control spokesman Valery Lyndin said the condition of the crew -- South Korean bioengineer Yi So-yeon, American astronaut Peggy Whitson and Russian flight engineer Yuri Malenchenko -- was satisfactory, though the three had been subjected to severe G-forces during the re-entry. [...] | Where did the Soyuz capsule land? | northern Kazakhstan |

The dataset can be downloaded [here](https://github.com/Maluuba/newsqa).

| Model           | F1 | EM | Paper / Source |
| ------------- | :-----: | :-----: | --- |
| MINIMAL(Dyn) (Min et al., 2018) | 63.2 | 50.1 | [Efficient and Robust Question Answering from Minimal Context over Documents](https://arxiv.org/abs/1805.08092) |
| FastQAExt (Weissenborn et al., 2017) | 56.1 | 43.7 | [Making Neural QA as Simple as Possible but not Simpler](https://arxiv.org/abs/1703.04816) |

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
| Liu et al. (2018) | 78.7 | [Narrative Modeling with Memory Chains and Semantic Supervision](http://aclweb.org/anthology/P18-2045) |
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
