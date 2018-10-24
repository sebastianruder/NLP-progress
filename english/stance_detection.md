# Stance detection

Stance detection is the extraction of a subject's reaction to a claim made by a primary actor. It is a core part of a set of approaches to fake news assessment.

Example:

* Source: "Apples are the most delicious fruit in existence"
* Reply: "Obviously not, because that is a reuben from Katz's"
* Stance: deny

### RumourEval

The [RumourEval 2017](http://www.aclweb.org/anthology/S/S17/S17-2006.pdf) dataset has been used for stance detection in English (subtask A). It features multiple stories and thousands of reply:response pairs, with train, test and evaluation splits each containing a distinct set of over-arching narratives.

This dataset subsumes the large [PHEME collection of rumors and stance](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0150989), which includes German.

| Model           | Accuracy  |  Paper / Source |
| ------------- | ----- | --- |
| Kochkina et al. 2017 | 0.784 | [Turing at SemEval-2017 Task 8: Sequential Approach to Rumour Stance Classification with Branch-LSTM](http://www.aclweb.org/anthology/S/S17/S17-2083.pdf)|
| Bahuleyan and Vechtomova 2017| 0.780 | [UWaterloo at SemEval-2017 Task 8: Detecting Stance towards Rumours with Topic Independent Features](http://www.aclweb.org/anthology/S/S17/S17-2080.pdf) |
|

[Go back to the README](../README.md)
