# Missing Elements

Missing elements are a collection of phenomenon that deals with things that are meant, but not explicitly mentioned in the text.
There are different kinds of missing elements, which have different aspects and behaviour. 
For example, [Ellipsis](https://en.wikipedia.org/wiki/Ellipsis_(linguistics)), Fused-Head, Bridging Anaphora, etc.


### Numeric Fused-Head (NFH)
FHs constructions are noun phrases (NPs) in which the head noun is missing and is said to be “fused” with its dependent modifier.
This missing information is implicit and is important for sentence understanding.

The Numeric [Fused-Head dataset](https://github.com/yanaiela/num_fh/tree/master/data/resolution/processed)
consists of ~10K examples of crowd-sourced classified examples, labeled into 7 different categories, from two types.
In the first type, *Reference*, the missing head is referenced explicitly somewhere else in the discourse, either in the
same sentence or in surrounding sentences.
In the second type, *Implicit*, the missing head does not appear in the text and needs to be inferred by the reader or
hearer based on the context or world knowledge. This category was labeled into the 6 most common categories of the dataset.
Models are evaluated based on accuracy.

Annotated Examples:

#### Reference

| I | bought | 5 | apples | but | got | only | 4 | . |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|   |        |   | HEAD   |     |     |      | NFH-REFERENCE | |

#### Implicit

| Let | 's | meet | at | 5 | tomorrow | ? |
| --- | --- | --- | --- | --- | --- | --- |
|     |    |      |    | NFH-TIME |   |   |


| Model           | Accuracy  |  Paper / Source | Code |
| ------------- | :-----:| --- | :-----: |
| Bi-LSTM + Scoring (Elazar and Goldberg, 2019) | 60.8 | [Where’s My Head? Definition, Dataset and Models for Numeric Fused-Heads Identification and Resolution](https://arxiv.org/abs/1905.10886) | [Official](https://github.com/yanaiela/num_fh) |
| Bi-LSTM + Elmo + Scoring (Elazar and Goldberg, 2019) | 74.0 | [Where’s My Head? Definition, Dataset and Models for Numeric Fused-Heads Identification and Resolution](https://arxiv.org/abs/1905.10886) | [Official](https://github.com/yanaiela/num_fh) |
