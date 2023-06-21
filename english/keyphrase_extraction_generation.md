# Keyphrase Extraction and Generation

Keyphrase extraction is the NLP task of identifying **key** phrases in the document, and has a wide range of applications applications such as information retrieval, question answering, text summarization etc. There are two aspects to keyphrases - some of them are directly occuring in the document, and are termed **present** keyphrases in the literature. Some of the keyphrases don't occur in the document, but can still function as appropriate summaries/tags for a given document, and they are termed **absent** keyphrases. Traditionally, NLP research addressed extracting the **present** keyphrases, while the post-deep learning approaches are also considering **absent** keyphrases. Whle the former is typically treated as "extraction", the latter is addressed as a **generation** problem, and hence, the separation between Keyphrase Extraction (KPE) and Keyphrase Generation (KPG). 

### Datasets


### Evaluation

Precision/Recall/F1 score are calculated for top-k matches while comparing the ground-truth keyphrases and the model output. While F1\@5/10 are commonly reported, variants such as F1@K/O/M are also reported. For "absent" keyphrases, some papers also report R\@10/50. The following tables will rank the models in terms of F1\@5. 

#### Kp20k

##### Present Keyphrases

| Model           | F1\@5 | Paper / Source | Code |
| --------------- | :-----: | :-----: | -------------- | ---- |
| TST (Omelianchuk et al., 2021) |  44.67 | [Text Simplification by Tagging](https://aclanthology.org/2021.bea-1.2.pdf) |   |

##### Absent Keyphrases

#### SemEval

#### Inspec

#### Krapivin

#### NUS 


#### Other Datasets

DUC
KPTimes
StackEx 
etc

[Go back to the README](../README.md)
