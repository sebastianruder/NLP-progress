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

- [CCG supertagging](ccg_supertagging.md)
- [Chunking](chunking.md)
- [Constituency parsing](constituency_parsing.md)
- [Coreference resolution](coreference_resolution.md)
- [Dependency parsing](dependency_parsing.md)
- [Dialog](dialog.md)
- [Domain adaptation](domain_adaptation.md)
- [Language modelling](language_modeling.md)
- [Machine translation](machine_translation.md)
- [Multi-task learning](multi-task_learning.md)
- [Multimodal](multimodal.md)
- [Named entity recognition](named_entity_recognition.md)
- [Natural language inference](natural_language_inference.md)
- [Part-of-speech tagging](part-of-speech_tagging.md)
- [Question answering](question_answering.md)
- [Semantic textual similarity](semantic_textual_similarity.md)
- [Sentiment analysis](sentiment_analysis.md)
- [Semantic parsing](semantic_parsing.md)
- [Semantic role labeling](semantic_role_labeling.md)
- [Summarization](summarization.md)
- [Text classification](text_classification.md)
