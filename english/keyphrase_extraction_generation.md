# Keyphrase Extraction and Generation

Keyphrase extraction is the NLP task of identifying **key** phrases in the document, and has a wide range of applications applications such as information retrieval, question answering, text summarization etc. There are two aspects to keyphrases - some of them are directly occuring in the document, and are termed **present** keyphrases in the literature. Some of the keyphrases don't occur in the document, but can still function as appropriate summaries/tags for a given document, and they are termed **absent** keyphrases. Traditionally, NLP research addressed extracting the **present** keyphrases, while the post-deep learning approaches are also considering **absent** keyphrases. Thus, while Keyphrase Extraction (KPE) can be termed a "sequence labeling" problem, Keyphrase Generation (KPG) is treated as a "sequence to sequence" generation problem. Another dominant approach is to treat both of them together as a generation problem in an integrated approach.  

Two recent surveys summarizing all research on this topic:
1. "A Survey on Recent Advances in Keyphrase Extraction from Pre-trained Language Models". [Song et.al., 2023](https://aclanthology.org/2023.findings-eacl.161/). EACL 2023. 
2. "From statistical methods to deep learning, automatic keyphrase prediction: A survey". [Xie et.al., 2023](https://www.sciencedirect.com/science/article/pii/S030645732300119X). Information Processing and Management 60(4). 

### Standard Datasets and Evaluation Measures

There are several open datasets for this task, and they generally consists of text instances, followed by a list of assigned keyphrases per text. Keyphrases are either manually annotated or extracted automatically from pre-tagged web content in the training data. Keyphrases can be either *present* or *absent* in the text itself. 

#### **Commonly used Datasets**

#### KP20K
This dataset was first described in [Meng et.al., 2017](https://aclanthology.org/P17-1054/) and contains the titles, abstracts, and keyphrases of 20,000 scientific articles in computer science extracted automaticallly, and it can be accessed from [Huggingface hub](https://huggingface.co/datasets/midas/kp20k).

#### Inspec
The dataset consists of 2000 English scientific abstracts from the [Inspec](https://en.wikipedia.org/wiki/Inspec) database, with keyphrases annotated by professional indexers. The dataset is described in [Hulth, 2003](https://aclanthology.org/W03-1028/) and can be accessed from [Huggingface hub](https://huggingface.co/datasets/midas/inspec). 

#### Krapivin
Krapivin consists of 2000 English scientific articles (full text) from computer science domain, with keyphrases annotated by the authors, and verified by the reviewers. The dataset is described in [Krapivin et.al., 2010](https://link.springer.com/chapter/10.1007/978-3-642-13654-2_12) and can be accessed from [Huggingface hub](https://huggingface.co/datasets/midas/krapivin). 

#### NUS
NUS consists of about 200 English scientific publications (full text), with keyphrases annotated by the authors, as well as an independent set of annotators. The dataset is described in [Nguyen and Kan, 2007](https://link.springer.com/chapter/10.1007/978-3-540-77094-7_41) and can be accessed from [Huggingface hub](https://huggingface.co/datasets/midas/nus). 

#### SemEval
SemEval dataset was originally used in the [SemEval 2017 Task 10: ScienceIE - Extracting Keyphrases and Relations from Scientific Publications](https://aclanthology.org/S17-2091/), and consists of 500 English open-access scientific publications from ScienceDirect. Keyphrases are annotated by a set of student volunteers followed by a second annotation by an expert annotator. It can be accessed from [Huggingface hub](https://huggingface.co/datasets/midas/semeval2017). 

#### Other Datasets

#### DUC
This dataset [Wan and Xiao, 2008](https://dl.acm.org/doi/10.5555/1620163.1620205) consists of around 300 English news articles with their keyphrases, and is hosted on [Huggingface hub](https://huggingface.co/datasets/midas/duc2001).

#### KPTimes
KPTimes [Gallina et.al., 2019](https://aclanthology.org/W19-8617/) is a large dataset of 279,923 news articles from NYTimes and 10,000 articles from JPTimes, with curated keyphrase annotations by editors, and is hosted on [Huggingface hub](https://huggingface.co/datasets/midas/kptimes)

#### OpenKP
OpenKP [Xiong et.al., 2019](https://aclanthology.org/D19-1521/) consists of approximately 150K web documents with manually annotated keyphrases, and is hosted on [Huggingface hub](https://huggingface.co/datasets/midas/openkp). 

**Evaluation Measures**

Macro Precision/Recall/F1 score are calculated for top-k matches while comparing the ground-truth keyphrases and the model output. While F1\@k where k= 5 or 10 are commonly reported, variants such as F1@/O/M are also reported. F1\@O uses the number of gold keyphrases as k, and F1\@M uses the number of predicted keyphrases as k. For "absent" keyphrases, some papers also report R\@10/50. The following tables will rank the models in terms of F1\@5, for the five most commonly reported datasets, KP20K, Inspec, Krapivin, NUS, SemEval [Most recent research reports experiments using KP20K as training data, and testing on KP20k, NUS, Semeval, Inspec and Krapivin]. 

Here are a few notes on results:
 - Asterisk indicates the paper reported **Micro** scores, instead of Macro.  
 - Exclamation indicates the paper does not mention whether they report a macro or a micro measure.  
 - All results are from the original results reported in the paper that describes the model.    
 - Some papers report on a scale of 0-1 and some on 0-100 (sometimes, the same paper uses different scales in different tables!). All results below are changed to 0-1 to maintain uniformity. 

#### KP20K 

| Model           | Present-F1\@5 | Absent-F1\@5 | Paper / Source | Code |
| --------------- | :-----: |  :-----: | -------------- | ---- |
|ChatGPT (Martinez et.al., 2023)|0.232 (!) |0.044 (!) |[ChatGPT vs State-of-the-Art Models: A Benchmarking Study in Keyphrase Generation Task](https://arxiv.org/abs/2304.14177) | - |
| P-AKG (Wu et.al., 2022) |  0.351(!) | 0.032(!)  | [Fast and Constrained Absent Keyphrase Generation by Prompt-Based Learning](https://ojs.aaai.org/index.php/AAAI/article/view/21402) | -  |
|WR-SetTrans (Xie et.al., 2022) |0.370 | 0.050 |[WR-One2Set: Towards Well-Calibrated Keyphrase Generation](https://aclanthology.org/2022.emnlp-main.491/)|
| Beam+KPD-A (Chowdhury et.al., 2022) | 0.363 | 0.067 | [KPDROP: Improving Absent Keyphrase Generation](https://aclanthology.org/2022.findings-emnlp.357) |  
|SetTrans (Ye et.al., 2021) | 0.358| 0.036| [One2Set: Generating Diverse Keyphrases as a Set](https://aclanthology.org/2021.acl-long.354/)|
| UniKeyphrase (Wu et.al., 2021)| 0.408 (!) | 0.047 (!)| [UniKeyphrase: A Unified Extraction and Generation Framework for Keyphrase Prediction](https://aclanthology.org/2021.findings-acl.73/) | 
|ExHiRD-h (Chen et.al., 2020) |0.311 |0.016 |[Exclusive Hierarchical Decoding for Deep Keyphrase Generation](https://aclanthology.org/2020.acl-main.103) |
|CorrRNN (Chen et.al., 2018) |- |- | [Keyphrase Generation with Correlation Constraints](https://aclanthology.org/D18-1439)|
|CopyRNN (Meng et.al., 2017) |0.333 | -| [Deep Keyphrase Generation](https://aclanthology.org/P17-1054) |  


#### SemEval
| Model           | Present-F1\@5 | Absent-F1\@5 | Paper / Source | Code |
| --------------- | :-----: |  :-----: | -------------- | ---- |
|ChatGPT (Martinez et.al., 2023)|-|- |[ChatGPT vs State-of-the-Art Models: A Benchmarking Study in Keyphrase Generation Task](https://arxiv.org/abs/2304.14177) | - |
| P-AKG (Wu et.al., 2022) |  0.329 (!)| 0.028 (!) | [Fast and Constrained Absent Keyphrase Generation by Prompt-Based Learning](https://ojs.aaai.org/index.php/AAAI/article/view/21402) | -  |
|WR-SetTrans (Xie et.al., 2022) |0.360 | 0.043 |[WR-One2Set: Towards Well-Calibrated Keyphrase Generation](https://aclanthology.org/2022.emnlp-main.491/)|
| Beam+KPD-A (Chowdhury et.al., 2022) | 0.343 | 0.053 | [KPDROP: Improving Absent Keyphrase Generation](https://aclanthology.org/2022.findings-emnlp.357) |
|SetTrans (Ye et.al., 2021) | 0.331| 0.026| [One2Set: Generating Diverse Keyphrases as a Set](https://aclanthology.org/2021.acl-long.354/)|
| UniKeyphrase (Wu et.al., 2021)| 0.416 (!) | 0.030 (!)| [UniKeyphrase: A Unified Extraction and Generation Framework for Keyphrase Prediction](https://aclanthology.org/2021.findings-acl.73/) |
|ExHiRD-h (Chen et.al., 2020) |0.284 | 0.017|[Exclusive Hierarchical Decoding for Deep Keyphrase Generation](https://aclanthology.org/2020.acl-main.103) |
|CorrRNN (Chen et.al., 2018) |0.320 | - | [Keyphrase Generation with Correlation Constraints](https://aclanthology.org/D18-1439)|
|CopyRNN (Meng et.al., 2017) |0.293 | - | [Deep Keyphrase Generation](https://aclanthology.org/P17-1054) |

#### Inspec

| Model           | Present-F1\@5 | Absent-F1\@5 | Paper / Source | Code |
| --------------- | :-----: |  :-----: | -------------- | ---- |
|ChatGPT (Martinez et.al., 2023)|0.352 (!)|0.049 (!)|[ChatGPT vs State-of-the-Art Models: A Benchmarking Study in Keyphrase Generation Task](https://arxiv.org/abs/2304.14177) | - |
| P-AKG (Wu et.al., 2022) |  0.26 (!) | 0.017(!) | [Fast and Constrained Absent Keyphrase Generation by Prompt-Based Learning](https://ojs.aaai.org/index.php/AAAI/article/view/21402) | -  |
|WR-SetTrans (Xie et.al., 2022) | 0.330 | 0.025 |[WR-One2Set: Towards Well-Calibrated Keyphrase Generation](https://aclanthology.org/2022.emnlp-main.491/)|
| Beam+KPD-A (Chowdhury et.al., 2022) | 0.322 | 0.036 | [KPDROP: Improving Absent Keyphrase Generation](https://aclanthology.org/2022.findings-emnlp.357) |  
|SetTrans (Ye et.al., 2021) | 0.285| 0.021| [One2Set: Generating Diverse Keyphrases as a Set](https://aclanthology.org/2021.acl-long.354/)|  
| UniKeyphrase (Wu et.al., 2021)| 0.29 (!) | 0.029 (!)| [UniKeyphrase: A Unified Extraction and Generation Framework for Keyphrase Prediction](https://aclanthology.org/2021.findings-acl.73/) | 
|ExHiRD-h (Chen et.al., 2020) |0.253 |0.011 |[Exclusive Hierarchical Decoding for Deep Keyphrase Generation](https://aclanthology.org/2020.acl-main.103) |
|CorrRNN (Chen et.al., 2018) | - |- | [Keyphrase Generation with Correlation Constraints](https://aclanthology.org/D18-1439)|
|CopyRNN (Meng et.al., 2017) |0.278 | - | [Deep Keyphrase Generation](https://aclanthology.org/P17-1054) |

#### Krapivin
| Model           | Present-F1\@5 | Absent-F1\@5 | Paper / Source | Code |
| --------------- | :-----: |  :-----: | -------------- | ---- |
| P-AKG (Wu et.al., 2022) | - |- | [Fast and Constrained Absent Keyphrase Generation by Prompt-Based Learning](https://ojs.aaai.org/index.php/AAAI/article/view/21402) | -  |
|ChatGPT (Martinez et.al., 2023)|-|-|[ChatGPT vs State-of-the-Art Models: A Benchmarking Study in Keyphrase Generation Task](https://arxiv.org/abs/2304.14177) | - |
|WR-SetTrans (Xie et.al., 2022) | 0.360|0.057 |[WR-One2Set: Towards Well-Calibrated Keyphrase Generation](https://aclanthology.org/2022.emnlp-main.491/)|
| Beam+KPD-A (Chowdhury et.al., 2022) | 0.323 | 0.078 | [KPDROP: Improving Absent Keyphrase Generation](https://aclanthology.org/2022.findings-emnlp.357) | 
|SetTrans (Ye et.al., 2021) | 0.326| 0.047| [One2Set: Generating Diverse Keyphrases as a Set](https://aclanthology.org/2021.acl-long.354/)|
| UniKeyphrase (Wu et.al., 2021)| - | - | [UniKeyphrase: A Unified Extraction and Generation Framework for Keyphrase Prediction](https://aclanthology.org/2021.findings-acl.73/) | 
|ExHiRD-h (Chen et.al., 2020) | 0.286 | 0.022 |[Exclusive Hierarchical Decoding for Deep Keyphrase Generation](https://aclanthology.org/2020.acl-main.103) |
|CorrRNN (Chen et.al., 2018) | 0.318|- | [Keyphrase Generation with Correlation Constraints](https://aclanthology.org/D18-1439)|
|CopyRNN (Meng et.al., 2017) |0.311 | - | [Deep Keyphrase Generation](https://aclanthology.org/P17-1054) |

#### NUS 
| Model           | Present-F1\@5 | Absent-F1\@5 | Paper / Source | Code |
| --------------- | :-----: |  :-----: | -------------- | ---- |
|ChatGPT (Martinez et.al., 2023)|-|-|[ChatGPT vs State-of-the-Art Models: A Benchmarking Study in Keyphrase Generation Task](https://arxiv.org/abs/2304.14177) | - |
| P-AKG (Wu et.al., 2022) |  0.412 (!)| 0.036(!) | [Fast and Constrained Absent Keyphrase Generation by Prompt-Based Learning](https://ojs.aaai.org/index.php/AAAI/article/view/21402) | -  |
|WR-SetTrans (Xie et.al., 2022) |0.428 |0.057 |[WR-One2Set: Towards Well-Calibrated Keyphrase Generation](https://aclanthology.org/2022.emnlp-main.491/)|
| Beam+KPD-A (Chowdhury et.al., 2022) | 0.418 | 0.079 | [KPDROP: Improving Absent Keyphrase Generation](https://aclanthology.org/2022.findings-emnlp.357) |
|SetTrans (Ye et.al., 2021) | 0.406| 0.042| [One2Set: Generating Diverse Keyphrases as a Set](https://aclanthology.org/2021.acl-long.354/)|
| UniKeyphrase (Wu et.al., 2021)| 0.434 (!) | 0.037 (!) | [UniKeyphrase: A Unified Extraction and Generation Framework for Keyphrase Prediction](https://aclanthology.org/2021.findings-acl.73/) | 
|ExHiRD-h (Chen et.al., 2020) | - | - |[Exclusive Hierarchical Decoding for Deep Keyphrase Generation](https://aclanthology.org/2020.acl-main.103) |
|CorrRNN (Chen et.al., 2018) |0.358 |- | [Keyphrase Generation with Correlation Constraints](https://aclanthology.org/D18-1439)| 
|CopyRNN (Meng et.al., 2017) |0.334 | - | [Deep Keyphrase Generation](https://aclanthology.org/P17-1054) |

[Go back to the README](../README.md)
