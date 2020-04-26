# Multimodal

## Multimodal Emotion Recognition 

### IEMOCAP

The  IEMOCAP ([Busso  et  al., 2008](https://link.springer.com/article/10.1007/s10579-008-9076-6)) contains the acts of 10 speakers in a two-way conversation segmented into utterances. The medium of the conversations in all the videos is English. The database contains the following categorical labels: anger, happiness, sadness, neutral, excitement, frustration, fear, surprise,  and other.

**Monologue:**

| Model           | Accuracy  |  Paper / Source |
| ------------- | :-----:| --- |
| CHFusion (Poria et al., 2017) | 76.5%  | [Multimodal Sentiment Analysis using Hierarchical Fusion with Context Modeling](https://arxiv.org/pdf/1806.06228.pdf) |
| bc-LSTM (Poria et al., 2017) | 74.10%  | [Context-Dependent Sentiment Analysis in User-Generated Videos](http://sentic.net/context-dependent-sentiment-analysis-in-user-generated-videos.pdf) |

**Conversational:**
Conversational setting enables the models to capture emotions expressed by the speakers in a conversation. Inter speaker dependencies are considered in this setting.

| Model           |  Weighted Accuracy (WAA)  |  Paper / Source |
| ------------- | :-----:| --- |
| CMN (Hazarika et al., 2018) |  77.62%  | [Conversational Memory Network for Emotion Recognition in Dyadic Dialogue Videos](http://aclweb.org/anthology/N18-1193) |
| Memn2n | 75.08 | [Conversational Memory Network for Emotion Recognition in Dyadic Dialogue Videos](http://aclweb.org/anthology/N18-1193)|

## Multimodal Metaphor Recognition

[Mohammad et. al, 2016](http://www.aclweb.org/anthology/S16-2003) created a dataset of verb-noun pairs from WordNet that had multiple senses. They annoted these pairs for metaphoricity (metaphor or not a metaphor). Dataset is in English.

| Model                                                        |                            F1 Score                             | Paper / Source                                               | Code        |
| ------------------------------------------------------------ | :----------------------------------------------------------: | ------------------------------------------------------------ | ----------- |
| 5-layer convolutional network (Krizhevsky et al., 2012), Word2Vec | 0.75 | [Shutova et. al, 2016](http://www.aclweb.org/anthology/N16-1020) | Unavailable |

[Tsvetkov  et. al, 2014](http://www.aclweb.org/anthology/P14-1024) created a dataset of adjective-noun pairs that they then annotated for metaphoricity. Dataset is in English.

| Model                                                        |                            F1 Score                             | Paper / Source                                               | Code        |
| ------------------------------------------------------------ | :----------------------------------------------------------: | ------------------------------------------------------------ | ----------- |
| 5-layer convolutional network (Krizhevsky et al., 2012), Word2Vec | 0.79 | [Shutova et. al, 2016](http://www.aclweb.org/anthology/N16-1020) | Unavailable |

## Multimodal Sentiment Analysis

### MOSI
The MOSI dataset ([Zadeh et al., 2016](https://arxiv.org/pdf/1606.06259.pdf)) is a dataset rich in sentimental expressions where 93 people review topics in English. The videos are segmented with each segments sentiment label scored between +3 (strong positive) to -3 (strong negative)  by  5  annotators.

| Model           | Accuracy  |  Paper / Source |
| ------------- | :-----:| --- |
| bc-LSTM (Poria et al., 2017) | 80.3%  | [Context-Dependent Sentiment Analysis in User-Generated Videos](http://sentic.net/context-dependent-sentiment-analysis-in-user-generated-videos.pdf) |
| MARN (Zadeh et al., 2018) | 77.1%  | [Multi-attention Recurrent Network for Human Communication Comprehension](https://arxiv.org/pdf/1802.00923.pdf) |

## Visual Question Answering

### VQAv2 

Given an image and a natural language question about the image, the task is to provide an accurate natural language answer

- [Website](https://visualqa.org)
- [Challenge](https://visualqa.org/challenge.html)

| Model           | Accuracy  |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| UNITER (Chen et al., 2019) | 73.4 | [UNITER: LEARNING UNIVERSAL IMAGE-TEXT REPRESENTATIONS](https://arxiv.org/pdf/1909.11740.pdf) | [Link](https://github.com/ChenRocks/UNITER) |
| LXMERT (Tan et al., 2019) | 72.54 | [LXMERT: Learning Cross-Modality Encoder Representations from Transformers](https://arxiv.org/abs/1908.07490) | [Link](https://github.com/airsplay/lxmert) |

### GQA - Visual Reasoning in the Real World 

GQA focuses on real-world compositional reasoning. 

- [Website](https://cs.stanford.edu/people/dorarad/gqa/)
- [Challenge](https://cs.stanford.edu/people/dorarad/gqa/challenge.html)

| Model           | Accuracy  |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| KaKao Brain | 73.24 | [GQA Challenge](https://drive.google.com/file/d/1CtFk0ldbN5w2qhwvfKrNzAFEj-I9Tjgy/view) | Unavailable |
| LXMERT (Tan et al., 2019) | 60.3 | [LXMERT: Learning Cross-Modality Encoder Representations from Transformers](https://arxiv.org/abs/1908.07490) | [Link](https://github.com/airsplay/lxmert) |

### TextVQA

TextVQA requires models to read and reason about text in an image to answer questions based on them.

- [Website](https://textvqa.org/)
- [Challenge](https://textvqa.org/challenge)

| Model           | Accuracy  |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| M4C (Hu et al., 2020) | 40.46 | [Iterative Answer Prediction with Pointer-Augmented Multimodal Transformers for TextVQA](https://arxiv.org/pdf/1911.06258.pdf) | [Link](https://github.com/facebookresearch/pythia/tree/project/m4c/projects/M4C_Captioner) |


### VizWiz dataset

This task focuses on answering visual questions that originate from a real use case where blind people were submitting images with recorded spoken questions in order to learn about their physical surroundings.
- [Website](https://vizwiz.org/tasks-and-datasets/vqa/)
- [Challenge](https://vizwiz.org/tasks-and-datasets/vqa/)

| Model           | Accuracy  |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| Pythia | 54.22 | [FB's Pythia repository](https://github.com/facebookresearch/pythia/blob/master/docs/source/tutorials/pretrained_models.md) | [Link](https://github.com/facebookresearch/pythia/blob/master/docs/source/tutorials/pretrained_models.md) |
| BUTD Vizwiz (Gurari et al., 2018) | 46.9 | [VizWiz Grand Challenge: Answering Visual Questions from Blind People](https://arxiv.org/abs/1802.08218) | Unavailable |

## Other multimodal resources

- [awesome-multimodal-ml](https://github.com/pliang279/awesome-multimodal-ml)
- [awesome-vision-and-language-papers](https://github.com/sangminwoo/awesome-vision-and-language-papers)

[Go back to the README](../README.md)
