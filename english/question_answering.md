# Question answering

Question answering is the task of answering a question.

### Table of contents

- [ARC](#arc)
- [ShARC](#sharc)
- [Reading comprehension](#reading-comprehension)
  - [CliCR](#clicr)
  - [CNN / Daily Mail](#cnn--daily-mail)
  - [CoQA](#coqa)
  - [HotpotQA](#hotpotqa)
  - [MS MARCO](#ms-marco)
  - [MultiRC](#multirc)
  - [NewsQA](#newsqa)
  - [QAngaroo](#qangaroo)
  - [QuAC](#quac)
  - [RACE](#race)
  - [SQuAD](#squad)
  - [Story Cloze Test](#story-cloze-test)
  - [Recipe QA](#recipeqa)
  - [NarrativeQA](#narrativeqa)
  - [DuoRC](#duorc)
  - [DROP](#drop)
- [Open-domain Question Answering](#open-domain-question-answering)
  - [DuReader](#dureader)
  - [Quasar](#quasar)
  - [SearchQA](#searchqa)

### ARC

The [AI2 Reasoning Challenge (ARC)](http://ai2-website.s3.amazonaws.com/publications/AI2ReasoningChallenge2018.pdf)
dataset is a question answering, which contains 7,787 genuine grade-school level, multiple-choice science questions.
The dataset is partitioned into a Challenge Set and an Easy Set. The Challenge Set contains only questions
answered incorrectly by both a retrieval-based algorithm and a word co-occurrence algorithm. Models are evaluated
based on accuracy.

A public leaderboard is available on the [ARC website](http://data.allenai.org/arc/).

### ShARC

[ShARC](https://arxiv.org/abs/1809.01494) is a challenging QA dataset that requires  logical reasoning, elements of entailment/NLI and natural language generation.

Most work in machine reading focuses on question answering problems where the answer is directly expressed in the text to read. However, many real-world question answering problems require the reading of text not because it contains the literal answer, but because it contains a recipe to derive an answer together with the reader's background knowledge. We formalise this task and introduce the challenging ShARC dataset with 32k task instances. 

The goal is to answer questions by possibly asking follow-up questions first. We assume that the question does not provide enough information to be answered directly. However, a model can use the supporting rule text to infer what needs to be asked in order to determine the final answer. Concretely, The model must decide whether to answer with "Yes", "No", "Irrelevant", or to generate a follow-up question given rule text, a user scenario and a conversation history. Performance is measured with Micro and Macro Accuracy for "Yes"/"No"/"Irrelevant"/"More" classifications, and the quality of follow-up questions are measured with BLEU.

The public data, further task details and public leaderboard are available on the [ShARC Website](https://sharc-data.github.io/).

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

### CoQA

[CoQA](https://arxiv.org/abs/1808.07042) is a large-scale dataset for building Conversational Question Answering systems. 
CoQA contains 127,000+ questions with answers collected from 8000+ conversations.
Each conversation is collected by pairing two crowdworkers to chat about a passage in the form of questions and answers.

The data and public leaderboard are available [here](https://stanfordnlp.github.io/coqa/).

### HotpotQA

HotpotQA is a dataset with 113k Wikipedia-based question-answer pairs. Questions require 
finding and reasoning over multiple supporting documents and are not constrained to any pre-existing knowledge bases.
Sentence-level supporting facts are available.

The data and public leaderboard are available from the [HotpotQA website](https://hotpotqa.github.io/).

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
| DecaProp (Tay et al., 2018) | 66.3 | 53.1 | [Densely Connected Attention Propagation for Reading Comprehension](https://arxiv.org/abs/1811.04210) |
| AMANDA (Kundu et al., 2018) | 63.7 | 48.4| [A Question-Focused Multi-Factor Attention Network for Question Answering](https://arxiv.org/abs/1801.08290) |
| MINIMAL(Dyn) (Min et al., 2018) | 63.2 | 50.1 | [Efficient and Robust Question Answering from Minimal Context over Documents](https://arxiv.org/abs/1805.08092) |
| FastQAExt (Weissenborn et al., 2017) | 56.1 | 43.7 | [Making Neural QA as Simple as Possible but not Simpler](https://arxiv.org/abs/1703.04816) |

### QAngaroo

[QAngaroo](http://qangaroo.cs.ucl.ac.uk/index.html) is a set of two reading comprehension datasets,
which require multiple steps of inference that combine facts from multiple documents. The first dataset, WikiHop
is open-domain and focuses on Wikipedia articles. The second dataset, MedHop is based on paper abstracts from
PubMed.

The leaderboards for both datasets are available on the [QAngaroo website](http://qangaroo.cs.ucl.ac.uk/leaderboard.html).

### QuAC

Question Answering in Context (QuAC) is a dataset for modeling, understanding, and participating in information seeking dialog.
Data instances consist of an interactive dialog between two crowd workers:
(1) a student who poses a sequence of freeform questions to learn as much as possible about a hidden Wikipedia text,
and (2) a teacher who answers the questions by providing short excerpts (spans) from the text.

The leaderboard and data are available on the [QuAC website](http://quac.ai/).

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

| Model           | Accuracy  |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| GPT+General Reading Strategies (Sun et al., 2018) | 88.3 | [Improving Machine Reading Comprehension by General Reading Strategies](https://arxiv.org/pdf/1810.13441v1.pdf) |
| Finetuned Transformer LM (Radford et al., 2018) | 86.5 | [Improving Language Understanding by Generative Pre-Training](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf) | | [Official](https://github.com/openai/finetune-transformer-lm)
| Liu et al. (2018) | 78.7 | [Narrative Modeling with Memory Chains and Semantic Supervision](http://aclweb.org/anthology/P18-2045) | [Official](https://github.com/liufly/narrative-modeling)
| Hidden Coherence Model (Chaturvedi et al., 2017) | 77.6 | [Story Comprehension for Predicting What Happens Next](http://aclweb.org/anthology/D17-1168) |
| val-LS-skip (Srinivasan et al., 2018) | 76.5 | [A Simple and Effective Approach to the Story Cloze Test](http://aclweb.org/anthology/N18-2015) |

### RecipeQA

[RecipeQA](https://arxiv.org/abs/1809.00812) is a dataset for multimodal comprehension of cooking recipes. It consists of over 36K question-answer pairs automatically generated from approximately 20K unique recipes with step-by-step instructions and images. Each question in RecipeQA involves multiple modalities such as titles, descriptions or images, and working towards an answer requires (i) joint understanding of images and text, (ii) capturing the temporal flow of events, and (iii) making sense of procedural knowledge.

The public leaderboard is available on the [RecipeQA website](https://hucvl.github.io/recipeqa/).



### NarrativeQA
[NarrativeQA](https://arxiv.org/abs/1712.07040) is a dataset built to encourage deeper comprehension of language. This dataset involves reasoning over reading entire books or movie scripts. This dataset contains approximately 45K question answer pairs in free form text. There are two modes of this dataset (1) reading comprehension over summaries and (2) reading comprehension over entire books/scripts. 

| Model                        | BLEU-1     | BLEU-4   | METEOR | Rouge-L | Paper / Source | Code |
| -------------                | :-----:   | :-----:|:-----:| :-----:|---            | ---  |
|DecaProp (Tay et al., 2018)	   |44.35    |27.61	 | 21.80 | 44.69   |[Densely Connected Attention Propagation for Reading Comprehension](https://arxiv.org/abs/1811.04210)       |  [official](https://github.com/vanzytay/NIPS2018_DECAPROP)    |
|BiAttention + DCU-LSTM (Tay et al., 2018)	   |36.55    |19.79	 | 17.87 | 41.44  |[Multi-Granular Sequence Encoding via Dilated Compositional Units for Reading Comprehension](http://aclweb.org/anthology/D18-1238)       |      |
|BiDAF (Seo et al., 2017)	   |33.45    |15.69	 | 15.68 | 36.74  |[Bidirectional Attention Flow for Machine Comprehension](https://arxiv.org/abs/1611.01603)       |      |

*Note that the above is for the Summary setting. There are no official published results for reading over entire books/stories except for the original paper. 

### DuoRC

[DuoRC](https://duorc.github.io) contains 186,089 unique question-answer pairs created from a collection of 7680 pairs of movie plots where each pair in the collection reflects two versions of the same movie. 

DuoRC pushes the NLP community to address challenges on incorporating knowledge and reasoning in neural architectures for reading comprehension. It poses several interesting challenges such as:
  - DuoRC using parallel plots is especially designed to contain a large number of questions with low lexical overlap between questions and their corresponding passages
  - It requires models to go beyond the content of the given passage itself and incorporate world-knowledge, background knowledge, and common-sense knowledge to arrive at the answer
  - It revolves around narrative passages from movie plots describing complex events and therefore naturally require complex reasoning (e.g. temporal reasoning, entailment, long-distance anaphoras, etc.) across multiple sentences to infer the answer to questions
  - Several of the questions in DuoRC, while seeming relevant, cannot actually be answered from the given passage. This requires the model to detect the unanswerability of questions. This aspect is important for machines to achieve in industrial settings in particular.
  
### DROP

[DROP](https://allennlp.org/drop) is a crowdsourced, adversarially-created, 96k-question benchmark, in which a system must resolve references in a question, perhaps to multiple input positions, and perform discrete operations over them (such as addition, counting, or sorting). These operations require a much more comprehensive understanding of the content of paragraphs than what was necessary for prior datasets.

## Open-domain Question Answering

### DuReader
[DuReader](https://ai.baidu.com/broad/subordinate?dataset=dureader) is a large-scale, open-domain Chinese machine reading comprehension (MRC) dataset, designed to address real-world MRC. [Link to paper](https://arxiv.org/pdf/1711.05073.pdf) 

DuReader has three advantages over other MRC datasets: 
- (1) data sources: questions and documents are based on Baidu Search and Baidu Zhidao; answers are manually generated. 
- (2) question types: it provides rich annotations for more question types, especially yes-no and opinion questions, that leaves more opportunity for the research community. 
- (3) scale: it contains 300K questions, 660K answers and 1.5M documents; it is the largest Chinese MRC dataset so far. 

To help the community make these improvements, both the [dataset](https://ai.baidu.com/broad/download?dataset=dureader) of DuReader and [baseline systems](https://github.com/baidu/DuReader) have been posted online. 

The [leaderboard](https://ai.baidu.com/broad/leaderboard?dataset=dureader) is avaiable on DuReader page.

### Quasar
[Quasar](https://arxiv.org/abs/1707.03904) is a dataset for open-domain question answering. It includes two parts: (1) The Quasar-S dataset consists of 37,000 cloze-style queries constructed from definitions of software entity tags on the popular website Stack Overflow. (2) The Quasar-T dataset consists of 43,000 open-domain trivia questions and their answers obtained from various internet sources. 

| Model                        | EM (Quasar-T)     | F1 (Quasar-T)    |Paper / Source | Code |
| -------------                | :-----:| :-----:|---            | ---  |
|Denoising QA (Lin et al. 2018)|42.2	  |49.3    |[Denoising Distantly Supervised Open-Domain Question Answering](http://aclweb.org/anthology/P18-1161)|[official](https://github.com/thunlp/OpenQA)|
|DecaProp (Tay et al., 2018)	     |38.6	  |46.9	   |[Densely Connected Attention Propagation for Reading Comprehension](https://arxiv.org/abs/1811.04210)|[official](https://github.com/vanzytay/NIPS2018_DECAPROP)|
|R^3 (Wang et al., 2018)	     |35.3	  |41.7	   |[R^3: Reinforced Ranker-Reader for Open-Domain Question Answering](https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16712/16165)|[official](https://github.com/shuohangwang/mprc)|
|BiDAF (Seo et al., 2017)	     |25.9	  |28.5	   |[Bidirectional Attention Flow for Machine Comprehensio](https://arxiv.org/abs/1611.01603)               | [official](https://github.com/allenai/bi-att-flow)|
|GA (Dhingra et al., 2017)	   |26.4    |26.4	   |[Gated-Attention Readers for Text Comprehension](https://arxiv.org/pdf/1606.01549)       |      |



### SearchQA
[SearchQA](https://arxiv.org/abs/1704.05179) was constructed to reflect a full pipeline of general question-answering. SearchQA consists of more than 140k question-answer pairs with each pair having 49.6 snippets on average. Each question-answer-context tuple of the SearchQA comes with additional meta-data such as the snippet's URL.

| Model                        | Unigram Acc     | N-gram F1   | EM     |  F1   |Paper / Source | Code |
| -------------                | :-----:| :-----:| :-----:| :-----:|---            | ---  |
|DecaProp (Tay et al., 2018)	   |62.2    |70.8	   |56.8 |63.6    |[Densely Connected Attention Propagation for Reading Comprehension](https://arxiv.org/abs/1811.04210)       | [official](https://github.com/vanzytay/NIPS2018_DECAPROP)     |
|Denoising QA (Lin et al. 2018)| - |-    | 58.8| 64.5|[Denoising Distantly Supervised Open-Domain Question Answering](http://aclweb.org/anthology/P18-1161)|[official](https://github.com/thunlp/OpenQA)|
|R^3 (Wang et al., 2018)	     |-	  |-	 | 49.0| 55.3  |[R^3: Reinforced Ranker-Reader for Open-Domain Question Answering](https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16712/16165)|[official](https://github.com/shuohangwang/mprc)|
|Bi-Attention + DCU-LSTM (Tay et al., 2018)	   |49.4    |59.5	   |- |-    |[Multi-Granular Sequence Encoding via Dilated Compositional Units for Reading Comprehension](http://aclweb.org/anthology/D18-1238)       |      |
|AMANDA (Kundu et al., 2018)	     |46.8	  |56.6	   |- |-    |[A Question-Focused Multi-Factor Attention Network for Question Answering](https://arxiv.org/abs/1801.08290)               | [official](https://github.com/nusnlp/amanda)|
|Focused Hierarchical RNN	(Ke et al., 2018)     |46.8	  |53.4	   |- |-    |[Focused Hierarchical RNNs for Conditional Sequence Processing](http://proceedings.mlr.press/v80/ke18a/ke18a.pdf)||
|ASR (Kadlec et al, 2016) |41.3	  |22.8    |- |-    |[Text Understanding with the Attention Sum Reader Network](https://arxiv.org/abs/1603.01547)|


[Go back to the README](../README.md)
