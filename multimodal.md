## Multimodal Sentiment Analysis

### MOSI
The MOSI dataset ([Zadeh et al., 2016](https://arxiv.org/pdf/1606.06259.pdf)) is a dataset rich in sentimental expressions where 93 people review topics in English. The videos are segmented with each segments sentiment label scored between +3 (strong positive) to -3 (strong negative)  by  5  annotators.

| Model           | Accuracy  |  Paper / Source |
| ------------- | :-----:| --- |
| bc-LSTM (Poria et al., 2017) | 80.3%  | [Context-Dependent Sentiment Analysis in User-Generated Videos](http://sentic.net/context-dependent-sentiment-analysis-in-user-generated-videos.pdf) |
| MARN (Zadeh et al., 2018) | 77.1%  | [Multi-attention Recurrent Network for Human Communication Comprehension](https://arxiv.org/pdf/1802.00923.pdf) |

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
| Memn2n | 75.08 | [Conversational Memory Network for Emotion Recognition in Dyadic Dialogue Videos](http://aclweb.org/anthology/N18-1193)

[Go back to the README](README.md)
