# Tracking Progress in Natural Language Processing

This document aims to track the progress in Natural Language Processing (NLP) and give an overview
of the state-of-the-art across the most common NLP tasks and their corresponding datasets.

It aims to cover both traditional and core NLP tasks such as dependency parsing and part-of-speech tagging
as well as more recent ones such as reading comprehension and natural language inference. The main objective
is to provide the reader with a quick overview of benchmark datasets and the state-of-the-art for their
task of interest, which serves as a stepping stone for further research. To this end, if there is a 
place where results for a task are already published and regularly maintained, such as a public leaderboard,
the reader will be pointed there.

### Contributing

If you would like to add a new result, you can do so with a pull request. 
In order to minimize noise and to make maintenance somewhat manageable, results reported
in published papers will be preferred (indicate the venue of publication in your PR);
an exception may be made for influential preprints. The result should include the name
of the method, the citation, the score, and a link to the paper.

To add a new dataset or task, follow the below steps. Any new datasets
should have been used for evaluation in at least one published paper besides 
the one that introduced the dataset.

1. Fork the repository.
2. Add your dataset/task to the respective section of this document.
3. Add your dataset/task to the table of contents.
4. Briefly describe the dataset/task and include relevant references. 
5. Describe the evaluation setting and evaluation metric.
6. Show how an annotated example of the dataset/task looks like.
7. Add a download link if available.
8. Copy the below table and fill in at least two results (including the state-of-the-art)
  for your dataset/task.
9. Submit your change as a pull request.
  
| Model           | Score  |  Paper / Source |
| ------------- | :-----:| --- |
|  |  |  |

### Things to do

- Add pointers on how to retrieve data.
- Provide more details regarding the evaluation setup of each task.
- Add an example to every task/dataset.
- Add statistics to every dataset.
- Provide a description and details for every task / dataset.
- We could potentially use [readthedocs](https://github.com/rtfd/readthedocs.org) to provide a clearer structure.
- All current datasets in this list are for the English language (except for [UD](#ud)). In a separate section, we could add
datasets for other languages.

### Table of contents

- [CCG supertagging](#ccg-supertagging)
  - [CCGBank](#ccgbank)
- [Chunking](#chunking)
  - [Penn Treebank](#penn-treebank&mdash;chunking)
- [Constituency parsing](#constituency-parsing)
  - [Penn Treebank](#penn-treebank&mdash;constituency-parsing)
- [Coreference resolution](#coreference-resolution)
  - [CoNLL 2012](#conll-2012)
- [Dependency parsing](#dependency-parsing)
  - [Penn Treebank](#penn-treebank&mdash;dependency-parsing)
- [Dialog](#dialog)
  - [Second dialog state tracking challenge](#second-dialog-state-tracking-challenge)
- [Domain adaptation](#domain-adaptation)
  - [Multi-Domain Sentiment Dataset](#multi-domain-sentiment-dataset)
- [Language modelling](#language-modeling)
  - [Penn Treebank](#penn-treebank&mdash;language-modeling)
  - [WikiText-2](#wikitext-2)
- [Machine translation](#machine-translation)
  - [WMT 2014 EN-DE](#wmt-2014-en-de)
  - [WMT 2014 EN-FR](#wmt-2014-en-fr)
- [Multi-task learning](#multi-task-learning)
  - [GLUE](#glue)
- [Named entity recognition](#named-entity-recognition)
  - [CoNLL 2003](#conll-2003)
- [Natural language inference](#natural-language-inference)
  - [SNLI](#snli)
  - [MultiNLI](#multinli)
  - [SciTail](#scitail)
- [Part-of-speech tagging](#part-of-speech-tagging)
  - [UD](#ud)
  - [WSJ](#penn-treebank&mdash;pos-tagging)
- [Reading comprehension](#reading-comprehension-/-question-answering)
  - [ARC](#arc)
  - [CNN / Daily Mail](#cnn-/-daily-mail&mdash;reading-comprehension)
  - [QAngaroo](#qangaroo)
  - [RACE](#race)
  - [SQuAD](#squad)
  - [Story Cloze Test](#story-cloze-test)
  - [Winograd Schema Challenge](#winograd-schema-challenge)
- [Semantic textual similarity](#semantic-textual-similarity)
  - [SentEval](#senteval)
  - [Quora Question Pairs](#quora-question-pairs)
- [Sentiment analysis](#sentiment-analysis)
  - [IMDb](#imdb)
  - [Sentihood](#sentihood)
  - [SST](#sst)
  - [Yelp](#yelp)
- [Semantic parsing](#semantic-parsing)
  - [WikiSQL](#wikisql)
- [Semantic role labeling](#semantic-role-labeling)
  - [OntoNotes](#ontonotes&mdash;semantic-role-labeling)
- [Summarization](#summarization)
  - [CNN / Daily Mail](#cnn-/-daily-mail&mdash;summarization)
- [Text classification](#text-classification)
  - [AG News](#ag-news)
  - [DBpedia](#dbpedia)
  - [TREC](#trec)

## CCG supertagging

Combinatory Categorical Grammar (CCG; [Steedman, 2000](http://www.citeulike.org/group/14833/article/8971002)) is a
highly lexicalized formalism. The standard parsing model of [Clark and Curran (2007)](https://www.mitpressjournals.org/doi/abs/10.1162/coli.2007.33.4.493)
uses over 400 lexical categories (or _supertags_), compared to about 50 part-of-speech tags for typical parsers.

Example:

| Vinken | , | 61 | years | old |
| --- | ---| --- | --- | --- |
| N| , | N/N | N | (S[adj]\ NP)\ NP |

### CCGBank

The CCGBank is a corpus of CCG derivations and dependency structures extracted from the Penn Treebank by 
[Hockenmaier and Steedman (2007)](http://www.aclweb.org/anthology/J07-3004). Sections 2-21 are used for training, 
section 00 for development, and section 23 as in-domain test set.
Performance is only calculated on the 425 most frequent labels. Models are evaluated based on accuracy.

| Model           | Accuracy |  Paper / Source |
| ------------- | :-----:| --- |
| Low supervision (Søgaard and Goldberg, 2016) | 93.26 | [Deep multi-task learning with low level tasks supervised at lower layers](http://anthology.aclweb.org/P16-2038) |
| Xu et al. (2015) | 93.00 | [CCG Supertagging with a Recurrent Neural Network](http://www.aclweb.org/anthology/P15-2041) |

## Chunking

Chunking is a shallow form of parsing that identifies continuous spans of tokens that form syntactic units such as noun phrases or verb phrases.

Example:

| Vinken | , | 61 | years | old |
| --- | ---| --- | --- | --- |
| B-NLP| I-NP | I-NP | I-NP | I-NP |

### Penn Treebank&mdash;chunking

The [Penn Treebank](https://catalog.ldc.upenn.edu/LDC99T42) is typically used for evaluating chunking.
Sections 15-18 are used for training, section 19 for development, and and section 20
for testing. Models are evaluated based on F1.

| Model           | F1 score  |  Paper / Source |
| ------------- | :-----:| --- |
| Low supervision (Søgaard and Goldberg, 2016) | 95.57 | [Deep multi-task learning with low level tasks supervised at lower layers](http://anthology.aclweb.org/P16-2038) |
| Suzuki and Isozaki (2008) | 95.15 | [Semi-Supervised Sequential Labeling and Segmentation using Giga-word Scale Unlabeled Data](https://aclanthology.info/pdf/P/P08/P08-1076.pdf) | 

## Constituency parsing

Consituency parsing aims to extract a constituency-based parse tree from a sentence that 
represents its syntactic structure according to a [phrase structure grammar](https://en.wikipedia.org/wiki/Phrase_structure_grammar).

Example:

                 Sentence (S)
                     |
       +-------------+------------+
       |                          |
     Noun (N)                Verb Phrase (VP)
       |                          |
     John                 +-------+--------+
                          |                |
                        Verb (V)         Noun (N)
                          |                |
                        sees              Bill

[Recent approaches](https://papers.nips.cc/paper/5635-grammar-as-a-foreign-language.pdf)
convert the parse tree into a sequence following a depth-first traversal in order to
be able to apply sequence-to-sequence models to it. The linearized version of the
above parse tree looks as follows: (S (N) (VP V N)).
 
### Penn Treebank&mdash;constituency parsing

The Wall Street Journal section of the [Penn Treebank](https://catalog.ldc.upenn.edu/LDC99T42) is used for 
evaluating constituency parsers. Section 22 is used for development and Section 23 is used for evaluation.
Models are evaluated based on F1. Most of the below models incorporate external data or features.
For a comparison of single models trained only on WSJ, refer to [Kitaev and Klein (2018)](https://arxiv.org/abs/1805.01052).

| Model           | F1 score  |  Paper / Source |
| ------------- | :-----:| --- |
| Self-attentive encoder + ELMo (Kitaev and Klein, 2018) | 95.13 | [Constituency Parsing with a Self-Attentive Encoder](https://arxiv.org/abs/1805.01052) |
| Model combination (Fried et al., 2017) | 94.66 | [Improving Neural Parsing by Disentangling Model Combination and Reranking Effects](https://arxiv.org/abs/1707.03058) |
| In-order (Liu and Zhang, 2017) | 94.2 | [In-Order Transition-based Constituent Parsing](http://aclweb.org/anthology/Q17-1029) |
| Semi-supervised LSTM-LM (Choe and Charniak, 2016) | 93.8 | [Parsing as Language Modeling](http://www.aclweb.org/anthology/D16-1257) | 
| Stack-only RNNG (Kuncoro et al., 2017) | 93.6 | [What Do Recurrent Neural Network Grammars Learn About Syntax?](https://arxiv.org/abs/1611.05774) |
| RNN Grammar (Dyer et al., 2016) | ﻿93.3 | [Recurrent Neural Network Grammars](https://www.aclweb.org/anthology/N16-1024) |
| Transformer (Vaswani et al., 2017) | 92.7 | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) |
| Semi-supervised LSTM (Vinyals et al., 2015) | 92.1  | [Grammar as a Foreign Language](https://papers.nips.cc/paper/5635-grammar-as-a-foreign-language.pdf) |
| Self-trained parser (McClosky et al., 2006) | 92.1 | [Effective Self-Training for Parsing](https://pdfs.semanticscholar.org/6f0f/64f0dab74295e5eb139c160ed79ff262558a.pdf) |

## Coreference resolution

Coreference resolution is the task of clustering mentions in text that refer to the same underlying real world entities.

Example:

```
               +-----------+
               |           |
I voted for Obama because he was most aligned with my values", she said.
 |                                                 |            |
 +-------------------------------------------------+------------+
```

"I", "my", and "she" belong to the same cluster and "Obama" and "he" belong to the same cluster.

### CoNLL 2012

Experiments are conducted on the data of the [CoNLL-2012 shared task](http://www.aclweb.org/anthology/W12-4501), which
uses OntoNotes coreference annotations. Papers
report the precision, recall, and F1 of the MUC, B3, and CEAFφ4 metrics using the official
CoNLL-2012 evaluation scripts. The main evaluation metric is the average F1 of the three metrics.

| Model           | Avg F1 |  Paper / Source |
| ------------- | :-----:| --- |
| (Lee et al., 2017)+ELMo (Peters et al., 2018)+coarse-to-fine & second-order inference (Lee et al., 2018) | 73.0 | [Higher-order Coreference Resolution with Coarse-to-fine Inference](http://aclweb.org/anthology/N18-2108) |
| (Lee et al., 2017)+ELMo (Peters et al., 2018) | 70.4 | [Deep contextualized word representatIions](https://arxiv.org/abs/1802.05365) |
| Lee et al. (2017) | 67.2 | [End-to-end Neural Coreference Resolution](https://arxiv.org/abs/1707.07045) |

## Dependency parsing

Dependency parsing is the task of extracting a dependency parse of a sentence that represents its grammatical
structure and defines the relationships between "head" words and words, which modify those heads.

Example:

```
     root
      |
      | +-------dobj---------+
      | |                    |
nsubj | |   +------det-----+ | +-----nmod------+
+--+  | |   |              | | |               |
|  |  | |   |      +-nmod-+| | |      +-case-+ |
+  |  + |   +      +      || + |      +      | |
I  prefer  the  morning   flight  through  Denver
```

Relations among the words are illustrated above the sentence with directed, labeled
arcs from heads to dependents (+ indicates the dependent).

### Penn Treebank&mdash;dependency parsing

Models are evaluated on the [Stanford Dependency](https://nlp.stanford.edu/software/dependencies_manual.pdf)
conversion of the Penn Treebank with predicted POS-tags. Punctuation symbols
are excluded from the evaluation. Evaluation metrics are unlabeled attachment score (UAS) and
labeled attachment score (LAS).

| Model           | UAS | LAS | Paper / Source |
| ------------- | :-----:| :-----:| --- |
| Stack-only RNNG (Kuncoro et al., 2017) | 95.8 | 94.6 | [What Do Recurrent Neural Network Grammars Learn About Syntax?](https://arxiv.org/abs/1611.05774) |
| Semi-supervised LSTM-LM (Choe and Charniak, 2016) | 95.9 | 94.1 | [Parsing as Language Modeling](http://www.aclweb.org/anthology/D16-1257) | 
| Deep Biaffine (Dozat and Manning, 2017) | 95.66 | 94.03 | [Deep Biaffine Attention for Neural Dependency Parsing](https://arxiv.org/abs/1611.01734) | 
| Andor et al. (2016) | 94.61 | 92.79 | [Globally Normalized Transition-Based Neural Networks](https://www.aclweb.org/anthology/P16-1231) |
| Distilled neural FOG (Kuncoro et al., 2016) | 94.26 | 92.06 | [Distilling an Ensemble of Greedy Dependency Parsers into One MST Parser](https://arxiv.org/abs/1609.07561) | 
| Weiss et al. (2015) | 94.0 | 92.0 | [Structured Training for Neural Network Transition-Based Parsing](http://anthology.aclweb.org/P/P15/P15-1032.pdf) |
| Arc-hybrid (Ballesteros et al., 2016) | 93.56 | 91.42 | [Training with Exploration Improves a Greedy Stack-LSTM Parser](https://arxiv.org/abs/1603.03793) |
| BIST parser (Kiperwasser and Goldberg, 2016) | 93.2 | 91.2 | [Simple and Accurate Dependency Parsing Using Bidirectional LSTM Feature Representations](https://aclweb.org/anthology/Q16-1023) |

## Dialog

Dialogue is notoriously hard to evaluate. Past approaches have used human evaluation.

### Second dialog state tracking challenge

For goal-oriented dialogue, the dataset of the [second dialog state tracking challenge](http://www.aclweb.org/anthology/W14-4337)
(DSTC2) is a common evaluation dataset. Dialogue state tacking consists of determining
at each turn of a dialog the full representation of what the user wants at that point 
in the dialog, which contains a goal constraint, a set of requested slots, and
the user's dialog act. The DSTC2 focuses on the restaurant search domain. Models are
evaluated based on accuracy on both individual and joint slot tracking.

| Model           | Area  |  Food  |  Price  |  Joint  |  Paper / Source |
| ------------- | :-----:| :-----:| :-----:| :-----:| --- |
| Liu et al. (2018) | 90 | 84 | 92 | 72 | [Dialogue Learning with Human Teaching and Feedback in End-to-End Trainable Task-Oriented Dialogue Systems](https://arxiv.org/abs/1804.06512) |
| Neural belief tracker (Mrkšić et al., 2017) | 90 | 84 | 94 | 72 | [Neural Belief Tracker: Data-Driven Dialogue State Tracking](https://arxiv.org/abs/1606.03777) |
| RNN (Henderson et al., 2014) |﻿92 | 86 | 86 | 69 | [Robust dialog state tracking using delexicalised recurrent neural networks and unsupervised gate](http://svr-ftp.eng.cam.ac.uk/~sjy/papers/htyo14.pdf) | 

## Domain adaptation

### Multi-Domain Sentiment Dataset

The [Multi-Domain Sentiment Dataset](https://www.cs.jhu.edu/~mdredze/datasets/sentiment/) is a common
evaluation dataset for domain adaptation for sentiment analysis. It contains product reviews from
Amazon.com from different product categories, which are treated as distinct domains.
Reviews contain star ratings (1 to 5 stars) that are generally converted into binary labels. Models are
typically evaluated on a target domain that is different from the source domain they were trained on, while only
having access to unlabeled examples of the target domain (unsupervised domain adaptation). The evaluation
metric is accuracy and scores are averaged across each domain.

| Model           | DVD | Books | Electronics | Kitchen | Average |  Paper / Source |
| ------------- | :-----:| :-----:| :-----:| :-----:| :-----:| --- |
| Multi-task tri-training (Ruder and Plank, 2018) | 78.14 | 74.86 | 81.45 | 82.14 | 79.15 | [Strong Baselines for Neural Semi-supervised Learning under Domain Shift](https://arxiv.org/abs/1804.09530) |
| Asymmetric tri-training (Saito et al., 2017) | 76.17 | 72.97 | 80.47 | 83.97 | 78.39 | [Asymmetric Tri-training for Unsupervised Domain Adaptation](https://arxiv.org/abs/1702.08400) |
| VFAE (Louizos et al., 2015) | 76.57 | 73.40 | 80.53 | 82.93 | 78.36 | [The Variational Fair Autoencoder](https://arxiv.org/abs/1511.00830) |
| DANN (Ganin et al., 2016) | 75.40 | 71.43 | 77.67 | 80.53 | 76.26 | [Domain-Adversarial Training of Neural Networks](https://arxiv.org/abs/1505.07818) |

## Language modeling

Language modeling is the task of predicting the next word in a document. * indicates models using dynamic evaluation.

### Penn Treebank&mdash;language modeling

A common evaluation dataset for language modeling ist the Penn Treebank,
as pre-processed by [Mikolov et al. (2010)](http://www.fit.vutbr.cz/research/groups/speech/publi/2010/mikolov_interspeech2010_IS100722.pdf).
The dataset consists of 929k training words, 73k validation words, and
82k test words. As part of the pre-processing, words were lower-cased, numbers
were replaced with N, newlines were replaced with <eos>,
and all other punctuation was removed. The vocabulary is
the most frequent 10k words with the rest of the tokens replaced by an <unk> token.
Models are evaluated based on perplexity, which is the average
per-word log-probability (lower is better).

| Model           | Validation perplexity | Test perplexity |  Paper / Source |
| ------------- | :-----:| :-----:| --- |
| AWD-LSTM-MoS + dynamic eval (Yang et al., 2018)* | 48.33 | 47.69 | [Breaking the Softmax Bottleneck: A High-Rank RNN Language Model](https://arxiv.org/abs/1711.03953) |
| AWD-LSTM + dynamic eval (Krause et al., 2017)* | 51.6 | 51.1 | [Dynamic Evaluation of Neural Sequence Models](https://arxiv.org/abs/1709.07432) |
| AWD-LSTM + continuous cache pointer (Merity et al., 2017)* | 53.9 | 52.8 | [Regularizing and Optimizing LSTM Language Models](https://arxiv.org/abs/1708.02182) | 
| AWD-LSTM-MoS (Yang et al., 2018) | 56.54 | 54.44 | [Breaking the Softmax Bottleneck: A High-Rank RNN Language Model](https://arxiv.org/abs/1711.03953) |
| AWD-LSTM (Merity et al., 2017) | 60.0 | 57.3 | [Regularizing and Optimizing LSTM Language Models](https://arxiv.org/abs/1708.02182) | 

### WikiText-2

[WikiText-2](https://arxiv.org/abs/1609.07843) has been proposed as a more realistic
benchmark for language modeling than the pre-processed Penn Treebank. WikiText-2
consists of around 2 million words extracted from Wikipedia articles.

| Model           | Validation perplexity | Test perplexity |  Paper / Source |
| ------------- | :-----:| :-----:| --- |
| AWD-LSTM-MoS + dynamic eval (Yang et al., 2018)* | 42.41 | 40.68 | [Breaking the Softmax Bottleneck: A High-Rank RNN Language Model](https://arxiv.org/abs/1711.03953) |
| AWD-LSTM + dynamic eval (Krause et al., 2017)* | 46.4 | 44.3 | [Dynamic Evaluation of Neural Sequence Models](https://arxiv.org/abs/1709.07432) |
| AWD-LSTM + continuous cache pointer (Merity et al., 2017)* | 53.8 | 52.0 | [Regularizing and Optimizing LSTM Language Models](https://arxiv.org/abs/1708.02182) | 
| AWD-LSTM-MoS (Yang et al., 2018) | 63.88 | 61.45 | [Breaking the Softmax Bottleneck: A High-Rank RNN Language Model](https://arxiv.org/abs/1711.03953) |
| AWD-LSTM (Merity et al., 2017) | 68.6 | 65.8 | [Regularizing and Optimizing LSTM Language Models](https://arxiv.org/abs/1708.02182) | 

## Machine translation

Machine translation is the task of translating a sentence in a source language to a different target language. 

Results with a * indicate that the mean test score over the the best window based on average dev-set BLEU score over 
21 consecutive evaluations is reported as in [Chen et al. (2018)](https://arxiv.org/abs/1804.09849).

### WMT 2014 EN-DE

Models are evaluated on the English-German dataset of the Ninth Workshop on Statistical Machine Translation (WMT 2014) based
on BLEU.

| Model           | BLEU  |  Paper / Source |
| ------------- | :-----:| --- |
| RNMT+ (Chen et al., 2018) | 28.5* | [The Best of Both Worlds: Combining Recent Advances in Neural Machine Translation](https://arxiv.org/abs/1804.09849) |
| Transformer Big (Vaswani et al., 2017) | 28.4 | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) |
| Transformer Base (Vaswani et al., 2017) | 27.3 | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) |
| MoE (Shazeer et al., 2017) | 26.03 | [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538) |
| ConvS2S (Gehring et al., 2017) | 25.16 | [Convolutional Sequence to Sequence Learning](https://arxiv.org/abs/1705.03122) | 

### WMT 2014 EN-FR

Similarly, models are evaluated on the English-French dataset of the Ninth Workshop on Statistical Machine Translation (WMT 2014) based
on BLEU.

| Model           | BLEU  |  Paper / Source |
| ------------- | :-----:| --- |
| RNMT+ (Chen et al., 2018) | 41.0* | [The Best of Both Worlds: Combining Recent Advances in Neural Machine Translation](https://arxiv.org/abs/1804.09849) |
| Transformer Big (Vaswani et al., 2017) | 41.0 | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) |
| MoE (Shazeer et al., 2017) | 40.56 | [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538) |
| ConvS2S (Gehring et al., 2017) | 40.46 | [Convolutional Sequence to Sequence Learning](https://arxiv.org/abs/1705.03122) | 
| Transformer Base (Vaswani et al., 2017) | 38.1 | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) |

## Multi-task learning

Multi-task learning aims to learn multiple different tasks simultaneously while maximizing
performance on one or all of the tasks. 

### GLUE

The [General Language Understanding Evaluation benchmark](https://arxiv.org/abs/1804.07461) (GLUE)
is a tool for evaluating and analyzing the performance of models across a diverse
range of existing natural language understanding tasks. Models are evaluated based on their
average accuracy across all tasks.

The state-of-the-art results can be seen on the public [GLUE leaderboard](https://gluebenchmark.com/leaderboard).

## Named entity recognition

Named entity recognition (NER) is the task of tagging entities in text with their corresponding type.
Approaches typically use BIO notation, which differentiates the beginning (B) and the inside (I) of entities.
O is used for non-entity tokens.

Example:

| Mark | Watney | visited | Mars |
| --- | ---| --- | --- |
| B-PER | I-PER | O | B-LOC |

### CoNLL 2003

The [CoNLL 2003 NER task](http://www.aclweb.org/anthology/W03-0419.pdf) consists of newswire text from the Reuters RCV1 
corpus tagged with four different entity types (PER, LOC, ORG, MISC). Models are evaluated based on span-based F1.

| Model           | F1  |  Paper / Source |
| ------------- | :-----:| --- |
| BiLSTM-CRF+ELMo (Peters et al., 2018) | 92.22 | [Deep contextualized word representations](https://arxiv.org/abs/1802.05365) |
| Peters et al. (2017) | 91.93 | [Semi-supervised sequence tagging with bidirectional language models](https://arxiv.org/abs/1705.00108) |
| Yang et al. (2017) | 91.26 | [Transfer Learning for Sequence Tagging with Hierarchical Recurrent Networks](https://arxiv.org/abs/1703.06345) |
| Ma and Hovy (2016) | 91.21 | [End-to-end Sequence Labeling via Bi-directional LSTM-CNNs-CRF](https://arxiv.org/abs/1603.01354) |
| LSTM-CRF (Lample et al., 2016) | 90.94 | [Neural Architectures for Named Entity Recognition](https://arxiv.org/abs/1603.01360) |

## Natural language inference

Natural language inference is the task of determining whether a "hypothesis" is 
true (entailment), false (contradiction), or undetermined (neutral) given a "premise".

Example:

| Premise | Label | Hypothesis |
| --- | ---| --- |
| A man inspects the uniform of a figure in some East Asian country. | contradiction | The man is sleeping. |
| An older and younger man smiling. | neutral  | Two men are smiling and laughing at the cats playing on the floor. |
| A soccer game with multiple males playing. | entailment | Some men are playing a sport. |

### SNLI

The [Stanford Natural Language Inference (SNLI) Corpus](https://arxiv.org/abs/1508.05326)
contains around 550k hypothesis/premise pairs. Models are evaluated based on accuracy.

State-of-the-art results can be seen on the [SNLI website](https://nlp.stanford.edu/projects/snli/).

### MultiNLI

The [Multi-Genre Natural Language Inference (MultiNLI) corpus](https://arxiv.org/abs/1704.05426)
contains around 433k hypothesis/premise pairs. It is similar to the SNLI corpus, but
covers a range of genres of spoken and written text and supports cross-genre evaluation. The data
can be downloaded from the [MultiNLI](https://www.nyu.edu/projects/bowman/multinli/) website.

Public leaderboards for [in-genre (matched)](https://www.kaggle.com/c/multinli-matched-open-evaluation/leaderboard) 
and [cross-genre (mismatched)](https://www.kaggle.com/c/multinli-mismatched-open-evaluation/leaderboard)
evaluation are available, but entries do not correspond to published models.

| Model           | Matched  | Mismatched | Paper / Source |
| ------------- | :-----:| :-----:| --- |
| Finetuned Transformer LM (Radford et al., 2018) | 82.1 | 81.4 | [Improving Language Understanding by Generative Pre-Training](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf) |
| Multi-task BiLSTM + Attn (Wang et al., 2018) | 72.2 | 72.1 | [GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding](https://arxiv.org/abs/1804.07461) |
| GenSen (Subramanian et al., 2018) | 71.4 | 71.3 | [Learning General Purpose Distributed Sentence Representations via Large Scale Multi-task Learning](https://arxiv.org/abs/1804.00079) | |

### SciTail

The [SciTail](http://ai2-website.s3.amazonaws.com/publications/scitail-aaai-2018_cameraready.pdf)
entailment dataset consists of 27k. In contrast to the SNLI and MultiNLI, it was not crowd-sourced
but created from sentences that already exist "in the wild". Hypotheses were created from
science questions and the corresponding answer candidates, while relevant web sentences from a large
corpus were used as premises. Models are evaluated based on accuracy.

| Model           | Accuracy  |  Paper / Source |
| ------------- | :-----:| --- |
| Finetuned Transformer LM (Radford et al., 2018) | 88.3 | [Improving Language Understanding by Generative Pre-Training](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf) |
| CAFE (Tay et al., 2018) | 83.3 | [A Compare-Propagate Architecture with Alignment Factorization for Natural Language Inference](https://arxiv.org/abs/1801.00102) |

## Part-of-speech tagging

Part-of-speech tagging (POS tagging) is the task of tagging a word in a text with its part of speech.
A part of speech is a category of words with similar grammatical properties. Common English
parts of speech are noun, verb, adjective, adverb, pronoun, preposition, conjunction, etc.

Example: 

| Vinken | , | 61 | years | old |
| --- | ---| --- | --- | --- |
| NNP | , | CD | NNS | JJ |

### UD

[Universal Dependencies (UD)](http://universaldependencies.org/) is a framework for 
cross-linguistic grammatical annotation, which contains more than 100 treebanks in over 60 languages.
Models are typically evaluated based on the average test accuracy across 28 languages.

| Model           | Avg accuracy  |  Paper / Source |
| ------------- | :-----:| --- |
| Adversarial Bi-LSTM (Yasunaga et al., 2018) | 96.73 | [Robust Multilingual Part-of-Speech Tagging via Adversarial Training](https://arxiv.org/abs/1711.04903) | 
| Bi-LSTM (Plank et al., 2016) | 96.40 | [Multilingual Part-of-Speech Tagging with Bidirectional Long Short-Term Memory Models and Auxiliary Loss](https://arxiv.org/abs/1604.05529) | 
| Joint Bi-LSTM (Nguyen et al., 2017) | 95.55 | [A Novel Neural Network Model for Joint POS Tagging and Graph-based Dependency Parsing](https://arxiv.org/abs/1705.05952) |

### Penn Treebank&mdash;POS tagging

A standard dataset for POS tagging is the Wall Street Journal (WSJ) portion of the Penn Treebank, containing 45 
different POS tags. Sections 0-18 are used for training, sections 19-21 for development, and sections 
22-24 for testing. Models are evaluated based on accuracy.

| Model           | Accuracy  |  Paper / Source |
| ------------- | :-----:| --- |
| Char Bi-LSTM (Ling et al., 2015) | 97.78 | [Finding Function in Form: Compositional Character Models for Open Vocabulary Word Representation](https://www.aclweb.org/anthology/D/D15/D15-1176.pdf) |
| Adversarial Bi-LSTM (Yasunaga et al., 2018) | 97.59 | [Robust Multilingual Part-of-Speech Tagging via Adversarial Training](https://arxiv.org/abs/1711.04903) | 
| Yang et al. (2017) | 97.55 | [Transfer Learning for Sequence Tagging with Hierarchical Recurrent Networks](https://arxiv.org/abs/1703.06345) |
| Ma and Hovy (2016) | 97.55 | [End-to-end Sequence Labeling via Bi-directional LSTM-CNNs-CRF](https://arxiv.org/abs/1603.01354) |
| Bi-LSTM (Ling et al., 2017) | 97.36 | [Finding Function in Form: Compositional Character Models for Open Vocabulary Word Representation](https://www.aclweb.org/anthology/D/D15/D15-1176.pdf) | | 
| Bi-LSTM (Plank et al., 2016) | 97.22 | [Multilingual Part-of-Speech Tagging with Bidirectional Long Short-Term Memory Models and Auxiliary Loss](https://arxiv.org/abs/1604.05529) | 

## Reading comprehension / Question answering

Question answering is the task of answering a question. Most current datasets
frame this task as reading comprehension where the question is about a paragraph
or document and the answer often is a span in the document. The Machine Reading group
at UCL also provides an [overview of reading comprehension tasks](https://uclmr.github.io/ai4exams/data.html).

### ARC

The [AI2 Reasoning Challenge (ARC)](http://ai2-website.s3.amazonaws.com/publications/AI2ReasoningChallenge2018.pdf) 
dataset is a question answering, which contains 7,787 genuine grade-school level, multiple-choice science questions.
The dataset is partitioned into a Challenge Set and an Easy Set. The Challenge Set contains only questions 
answered incorrectly by both a retrieval-based algorithm and a word co-occurrence algorithm. Models are evaluated
based on accuracy.

A public leaderboard is available on the [ARC website](http://data.allenai.org/arc/).

### CNN / Daily Mail&mdash;reading comprehension

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

## Semantic textual similarity

Semantic textual similarity deals with determining how similar two pieces of texts are.
This can take the form of assigning a score from 1 to 5. Related tasks are paraphrase or duplicate identification.

### SentEval

[SentEval](https://arxiv.org/abs/1803.05449) is an evaluation toolkit for evaluating sentence
representations. It includes 17 downstream tasks, including common semantic textual similarity
tasks. The semantic textual similarity (STS) benchmark tasks from 2012-2016 (STS12, STS13, STS14, STS15, STS16, STSB) measure the relatedness
of two sentences based on the cosine similarity of the two representations. The evaluation criterion is Pearson correlation.

The SICK relatedness (SICK-R) task trains a linear model to output a score from 1 to 5 indicating the relatedness of two sentences. For
the same dataset (SICK-E) can be treated as a binary classification problem using the entailment labels. 
The evaluation metric for SICK-R is Pearson correlation and classification accuracy for SICK-E.

The Microsoft Research Paraphrase Corpus (MRPC) corpus is a paraphrase identification dataset, where systems 
aim to identify if two sentences are paraphrases of each other. The evaluation metric is classification accuracy and F1.

The data can be downloaded from [here](https://github.com/facebookresearch/SentEval).

| Model           | MRPC | SICK-R | SICK-E | STS | Paper / Source |
| ------------- | :-----:| :-----:| :-----:| :-----:| --- |
| GenSen (Subramanian et al., 2018) | 78.6/84.4 | 0.888 | 87.8 | 78.9/78.6 | [Learning General Purpose Distributed Sentence Representations via Large Scale Multi-task Learning](https://arxiv.org/abs/1804.00079) | |
| InferSent (Conneau et al., 2017) | 76.2/83.1 | 0.884 | 86.3 | 75.8/75.5 | [Supervised Learning of Universal Sentence Representations from Natural Language Inference Data](https://arxiv.org/abs/1705.02364) |

### Quora Question Pairs

The [Quora Question Pairs dataset](https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs)
consists of over 400,000 pairs of questions on Quora. Systems must identify whether one question is a
duplicate of the other. Models are evaluated based on accuracy.

| Model           | Accuracy  |  Paper / Source |
| ------------- | :-----:| --- |
| pt-DecAtt (Char) (Tomar et al., 2017) | 88.40 | [Neural Paraphrase Identification of Questions with Noisy Pretraining](https://arxiv.org/abs/1704.04565) |
| BiMPM (Wang et al., 2017) | 88.17 | [Bilateral Multi-Perspective Matching for Natural Language Sentences](https://arxiv.org/abs/1702.03814) |
| GenSen (Subramanian et al., 2018) | 87.01 | [Learning General Purpose Distributed Sentence Representations via Large Scale Multi-task Learning](https://arxiv.org/abs/1804.00079) | |

## Sentiment analysis

Sentiment analysis is the task of classifying the polarity of a given text.

### IMDb

The [IMDb dataset](https://ai.stanford.edu/~ang/papers/acl11-WordVectorsSentimentAnalysis.pdf) is a binary
sentiment analysis dataset consisting of 50,000 reviews from the Internet Movie Database (IMDb) labeled as positive or
negative. Models are evaluated based on accuracy.

| Model           | Score  |  Paper / Source |
| ------------- | :-----:| --- |
| ULMFiT (Howard and Ruder, 2018) | 95.4 | [Universal Language Model Fine-tuning for Text Classification](https://arxiv.org/abs/1801.06146) |
| oh-LSTM (Johnson and Zhang, 2016) | 94.1 | [Supervised and Semi-Supervised Text Categorization using LSTM for Region Embeddings](https://arxiv.org/abs/1602.02373) |
| Virtual adversarial training (Miyato et al., 2016) | 94.1 | [Adversarial Training Methods for Semi-Supervised Text Classification](https://arxiv.org/abs/1605.07725) |
| BCN+Char+CoVe (McCann et al., 2017) | 91.8 | [Learned in Translation: Contextualized Word Vectors](https://arxiv.org/abs/1708.00107) |

### Sentihood

[Sentihood](http://www.aclweb.org/anthology/C16-1146) is a dataset for targeted aspect-based sentiment analysis (TABSA), which aims
to identify fine-grained polarity towards a specific aspect. The dataset consists of 5,215 sentences,
3,862 of which contain a single target, and the remainder multiple targets. F1 is used as evaluation metric
for aspect detection and accuracy as evaluation metric for sentiment analysis.

| Model           | Aspect  | Sentiment |  Paper / Source |
| ------------- | :-----:| :-----:| --- |
| Liu et al. (2018) | 78.5 | 91.0 | [Recurrent Entity Networks with Delayed Memory Update for Targeted Aspect-based Sentiment Analysis](http://aclweb.org/anthology/N18-2045) |
| SenticLSTM (Ma et al., 2018) | 78.2 | 89.3 | [Targeted Aspect-Based Sentiment Analysis via Embedding Commonsense Knowledge into an Attentive LSTM](http://sentic.net/sentic-lstm.pdf) | 
| LSTM-LOC (Saeidi et al., 2016) | 69.3 | 81.9 | [Sentihood: Targeted aspect based sentiment analysis dataset for urban neighbourhoods](http://www.aclweb.org/anthology/C16-1146) |

### SST

The [Stanford Sentiment Treebank](https://nlp.stanford.edu/sentiment/index.html) 
contains of 215,154 phrases with fine-grained sentiment labels in the parse trees
of 11,855 sentences in movie reviews. Models are evaluated either on fine-grained
(five-way) or binary classification based on accuracy.

Fine-grained classification:

| Model           | Accuracy |  Paper / Source |
| ------------- | :-----:| --- |
| BCN+ELMo (Peters et al., 2018) | 54.7 | [Deep contextualized word representations](https://arxiv.org/abs/1802.05365) |
| BCN+Char+CoVe (McCann et al., 2017) | 53.7 | [Learned in Translation: Contextualized Word Vectors](https://arxiv.org/abs/1708.00107) |

Binary classification:

| Model           | Accuracy  |  Paper / Source |
| ------------- | :-----:| --- |
| bmLSTM (Radford et al., 2017) | 91.8 | [Learning to Generate Reviews and Discovering Sentiment](https://arxiv.org/abs/1704.01444) |
| BCN+Char+CoVe (McCann et al., 2017) | 90.3 | [Learned in Translation: Contextualized Word Vectors](https://arxiv.org/abs/1708.00107)
| Neural Semantic Encoder (Munkhdalai and Yu, 2017) | 89.7 | [Neural Semantic Encoders](http://www.aclweb.org/anthology/E17-1038) | 
| BLSTM-2DCNN (Zhou et al., 2017) | 89.5 | [Text Classification Improved by Integrating Bidirectional LSTM with Two-dimensional Max Pooling](http://www.aclweb.org/anthology/C16-1329) |

### Yelp

The [Yelp Review dataset](https://papers.nips.cc/paper/5782-character-level-convolutional-networks-for-text-classification.pdf)
consists of more than 500,000 Yelp reviews. There is both a binary and a fine-grained (five-class)
version of the dataset. Models are evaluated based on error (1 - accuracy; lower is better).

Fine-grained classification: 

| Model           | Error  |  Paper / Source |
| ------------- | :-----:| --- |
| ULMFiT (Howard and Ruder, 2018) | 29.98 | [Universal Language Model Fine-tuning for Text Classification](https://arxiv.org/abs/1801.06146) |
| DPCNN (Johnson and Zhang, 2017) | 30.58 | [Deep Pyramid Convolutional Neural Networks for Text Categorization](http://aclweb.org/anthology/P17-1052) |
| CNN (Johnson and Zhang, 2016) | 32.39 | [Supervised and Semi-Supervised Text Categorization using LSTM for Region Embeddings](https://arxiv.org/abs/1602.02373) |
| Char-level CNN (Zhang et al., 2015) | 37.95 | [Character-level Convolutional Networks for Text Classification](https://papers.nips.cc/paper/5782-character-level-convolutional-networks-for-text-classification.pdf) |

Binary classification:

| Model           | Error |  Paper / Source |
| ------------- | :-----:| --- |
| ULMFiT (Howard and Ruder, 2018) | 2.16 | [Universal Language Model Fine-tuning for Text Classification](https://arxiv.org/abs/1801.06146) |
| DPCNN (Johnson and Zhang, 2017) | 2.64 | [Deep Pyramid Convolutional Neural Networks for Text Categorization](http://aclweb.org/anthology/P17-1052) |
| CNN (Johnson and Zhang, 2016) | 2.90 | [Supervised and Semi-Supervised Text Categorization using LSTM for Region Embeddings](https://arxiv.org/abs/1602.02373) |
| Char-level CNN (Zhang et al., 2015) | 4.88 | [Character-level Convolutional Networks for Text Classification](https://papers.nips.cc/paper/5782-character-level-convolutional-networks-for-text-classification.pdf) |

## Semantic parsing

Semantic parsing is the task of translating natural language into a formal meaning
representation on which a machine can act. Representations may be an executable language
such as SQL or more abstract representations such as [Abstract Meaning Representation (AMR)](https://en.wikipedia.org/wiki/Abstract_Meaning_Representation).

### WikiSQL

The [WikiSQL dataset](https://arxiv.org/abs/1709.00103) consists of 87,673 
examples of questions, SQL queries, and database tables built from 26,521 tables.
Train/dev/test splits are provided so that each table is only in one split.
Models are evaluated based on accuracy on execute result matches.

Example:

| Question | SQL query | 
| ------------- |  --- |
| How many engine types did Val Musetti use? | `SELECT COUNT Engine WHERE Driver = Val Musetti` | 

| Model           | Acc ex |  Paper / Source |
| -------------| :-----:| --- |
| TypeSQL+TC (Yu et al., 2018) | 82.6 | [TypeSQL: Knowledge-based Type-Aware Neural Text-to-SQL Generation](https://arxiv.org/abs/1804.09769) |
| SQLNet (Xu et al., 2017) | 68.0 | [Sqlnet: Generating structured queries from natural language without reinforcement learning](https://arxiv.org/abs/1711.04436) |
| Seq2SQL (Zhong et al., 2017) | 59.4 | [Seq2sql: Generating structured queries from natural language using reinforcement learning](https://arxiv.org/abs/1709.00103) |

## Semantic role labeling

Semantic role labeling aims to model the predicate-argument structure of a sentence
and is often described as answering "Who did what to whom". BIO notation is typically
used for semantic role labeling.

Example:

| Housing | starts | are | expected | to | quicken | a | bit | from | August’s | pace | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| B-ARG1 | I-ARG1 | O |  O  |  O  |   V  | B-ARG2 | I-ARG2 | B-ARG3 | I-ARG3 | I-ARG3 |    

### OntoNotes&mdash;semantic role labeling

Models are typically evaluated on the [OntoNotes benchmark](http://www.aclweb.org/anthology/W13-3516) based on F1.

| Model           | F1  |  Paper / Source |
| ------------- | :-----:| --- |
| (He et al., 2017)+ELMo (Peters et al., 2018) | 84.6 | [Deep contextualized word representations](https://arxiv.org/abs/1802.05365) |
| He et al. (2017) | 81.7 | [Deep Semantic Role Labeling: What Works and What’s Next](http://aclweb.org/anthology/P17-1044) |

## Summarization

Summarization is the task of producing a shorter version of a document that preserves most of the
original document's meaning.

### CNN / Daily Mail&mdash;summarization

The [CNN / Daily Mail dataset](https://arxiv.org/abs/1506.03340) as processed by 
[Nallapati et al. (2016)](http://www.aclweb.org/anthology/K16-1028) has been used
for evaluating summarization. The dataset contains online news articles (781 tokens 
on average) paired with multi-sentence summaries (3.75 sentences or 56 tokens on average).
The processed version contains 287,226 training pairs, 13,368 validation pairs and 11,490 test pairs.
Models are evaluated based on ROUGE-1, ROUGE-2, and ROUGE-L. * indicates that models
were trained and evaluated on the anonymized version of the dataset.

| Model           | ROUGE-1  | ROUGE-2  | ROUGE-L  |  Paper / Source |
| ------------- | :-----:| :-----:| :-----:| --- |
| Pointer-generator + coverage (See et al., 2017) | 39.53| 17.28 | 36.38 | [Get To The Point: Summarization with Pointer-Generator Networks](https://arxiv.org/abs/1704.04368) |
| Extractive model (Nallapati et al., 2017)* | ﻿39.6 | 16.2 | 35.3 | [SummaRuNNer: A Recurrent Neural Network based Sequence Model for Extractive Summarization of Documents](https://arxiv.org/abs/1611.04230) |
| Abstractive model (Nallapti et al., 2016)* | 35.46 | 13.30 | 32.65 | [Abstractive Text Summarization using Sequence-to-sequence RNNs and Beyond](http://www.aclweb.org/anthology/K16-1028) |

## Text classification

Text classification is the task of assigning a sentence or document an appropriate category.
The categories depend on the chosen dataset and can range from topics.

### AG News

The [AG News corpus](https://papers.nips.cc/paper/5782-character-level-convolutional-networks-for-text-classification.pdf)
consists of news articles from the [AG's corpus of news articles on the web](http://www.di.unipi.it/~gulli/AG_corpus_of_news_articles.html)
pertaining to the 4 largest classes. The dataset contains 30,000 training examples for each class
1,900 examples for each class for testing. Models are evaluated based on error rate (lower is better).

| Model           | Error  |  Paper / Source |
| ------------- | :-----:| --- |
| ULMFiT (Howard and Ruder, 2018) | 5.01 | [Universal Language Model Fine-tuning for Text Classification](https://arxiv.org/abs/1801.06146) |
| CNN (Johnson and Zhang, 2016) | 6.57 | [Supervised and Semi-Supervised Text Categorization using LSTM for Region Embeddings](https://arxiv.org/abs/1602.02373) |
| DPCNN (Johnson and Zhang, 2017) | 6.87 | [Deep Pyramid Convolutional Neural Networks for Text Categorization](http://aclweb.org/anthology/P17-1052) |
| VDCN (Alexis et al., 2016) | 8.67 | [Very Deep Convolutional Networks for Text Classification](https://arxiv.org/abs/1606.01781) |
| Char-level CNN (Zhang et al., 2015) | 9.51 | [Character-level Convolutional Networks for Text Classification](https://papers.nips.cc/paper/5782-character-level-convolutional-networks-for-text-classification.pdf) |

### DBpedia

The [DBpedia ontology](https://papers.nips.cc/paper/5782-character-level-convolutional-networks-for-text-classification.pdf) 
dataset contains 40,000 training samples and 5,000 testing samples for each of 14 nonoverlapping classes from DBpedia.
Models are evaluated based on error rate (lower is better).

| Model           | Error  |  Paper / Source |
| ------------- | :-----:| --- |
| ULMFiT (Howard and Ruder, 2018) | 0.80 | [Universal Language Model Fine-tuning for Text Classification](https://arxiv.org/abs/1801.06146) |
| CNN (Johnson and Zhang, 2016) | 0.84 | [Supervised and Semi-Supervised Text Categorization using LSTM for Region Embeddings](https://arxiv.org/abs/1602.02373) |
| DPCNN (Johnson and Zhang, 2017) | 0.88 | [Deep Pyramid Convolutional Neural Networks for Text Categorization](http://aclweb.org/anthology/P17-1052) |
| VDCN (Alexis et al., 2016) | 1.29 | [Very Deep Convolutional Networks for Text Classification](https://arxiv.org/abs/1606.01781) |
| Char-level CNN (Zhang et al., 2015) | 1.55 | [Character-level Convolutional Networks for Text Classification](https://papers.nips.cc/paper/5782-character-level-convolutional-networks-for-text-classification.pdf) |

### TREC

The [TREC dataset](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.11.2766&rep=rep1&type=pdf) is dataset for
question classification consisting of open-domain, fact-based questions divided into broad semantic categories. 
It has both a six-class (TREC-6) and a fifty-class (TREC-50) version. Both have 4,300 training examples, 
but TREC-50 has finer-grained labels. Models are evaluated based on accuracy.

TREC-6:

| Model           | Error  |  Paper / Source |
| ------------- | :-----:| --- |
| ULMFiT (Howard and Ruder, 2018) | 96.4 | [Universal Language Model Fine-tuning for Text Classification](https://arxiv.org/abs/1801.06146) |
| LSTM-CNN (Zhou et al., 2016) | 96.1 | [Text Classification Improved by Integrating Bidirectional LSTM with Two-dimensional Max Pooling](http://www.aclweb.org/anthology/C16-1329) |
| TBCNN (Mou et al., 2015) | 96.0 | [Discriminative Neural Sentence Modeling by Tree-Based Convolution](http://aclweb.org/anthology/D15-1279) |
| CoVe (McCann et al., 2017) | 95.8 | [Learned in Translation: Contextualized Word Vectors](https://arxiv.org/abs/1708.00107) |

TREC-50:

| Model           | Error  |  Paper / Source |
| ------------- | :-----:| --- |
| Rules (Madabushi and Lee, 2016) | 97.2 |[High Accuracy Rule-based Question Classification using Question Syntax and Semantics](http://www.aclweb.org/anthology/C16-1116)|
| SVM (Van-Tu and Anh-Cuong, 2016) | 91.6 | [Improving Question Classification by Feature Extraction and Selection](https://www.researchgate.net/publication/303553351_Improving_Question_Classification_by_Feature_Extraction_and_Selection) |
