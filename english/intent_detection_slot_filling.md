# Intent Detection and Slot Filling
Intent Detection and Slot Filling is the task of interpreting user commands/queries by extracting the intent and the relevant slots.

Example (from ATIS):
```
Query: What flights are available from pittsburgh to baltimore on thursday morning
Intent: flight info
Slots: 
    - from_city: pittsburgh
    - to_city: baltimore
    - depart_date: thursday
    - depart_time: morning
```

## ATIS
ATIS (Air Travel Information System) (Hemphill et al.) is a dataset by Microsoft CNTK. Available from the [github page](https://github.com/microsoft/CNTK/tree/master/Examples/LanguageUnderstanding/ATIS). The slots are labeled in the BIO ([Inside Outside Beginning](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging))) format (similar to NER). This dataset contains only air travel related commands. Most of the ATIS results are based on the work [here](https://github.com/zhenwenzhang/Slot_Filling).

| Model | Slot F1 Score | Intent Accuracy | Paper / Source | Code |
| ------ | ------ | ------ | ------ | ------ |
| Bi-model with decoder | 96.89 | 98.99  | [A Bi-model based RNN Semantic Frame Parsing Model for Intent Detection and Slot Filling](https://arxiv.org/abs/1812.10235) |
| SlotRefine + BERT | 96.16 | 97.74  | [SlotRefine: A Fast Non-Autoregressive Model for Joint Intent Detection and Slot Filling](https://aclanthology.org/2020.emnlp-main.152.pdf) | [Official](https://github.com/moore3930/SlotRefine)|
| SlotRefine | 96.22 | 97.11  | [SlotRefine: A Fast Non-Autoregressive Model for Joint Intent Detection and Slot Filling](https://aclanthology.org/2020.emnlp-main.152.pdf) | [Official](https://github.com/moore3930/SlotRefine)|
| Stack-Propagation + BERT | 96.10 | 97.50 | [A Stack-Propagation Framework with Token-level Intent Detection for Spoken Language Understanding](https://arxiv.org/abs/1909.02188)|[Official](https://github.com/LeePleased/StackPropagation-SLU)|
| Stack-Propagation | 95.90 | 96.90 | [A Stack-Propagation Framework with Token-level Intent Detection for Spoken Language Understanding](https://arxiv.org/abs/1909.02188)|[Official](https://github.com/LeePleased/StackPropagation-SLU)|
| Attention Encoder-Decoder NN | 95.87 | 98.43 | [Attention-Based Recurrent Neural Network Models for Joint Intent Detection and Slot Filling](https://arxiv.org/abs/1609.01454)|
| SF-ID (BLSTM) network | 95.80 | 97.76 | [A Novel Bi-directional Interrelated Model for Joint Intent Detection and Slot Filling](https://arxiv.org/abs/1907.00390) | [Official](https://github.com/ZephyrChenzf/SF-ID-Network-For-NLU) |
| Context Encoder | 95.80 | NA | [Improving Slot Filling by Utilizing Contextual Information](https://arxiv.org/pdf/1911.01680.pdf) |
| Capsule-NLU | 95.20 | 95.00 | [Joint Slot Filling and Intent Detection via Capsule Neural Networks](https://arxiv.org/abs/1812.09471) | [Official](https://github.com/czhang99/Capsule-NLU) |
| Joint GRU model(W) | 95.49 | 98.10  |[A Joint Model of Intent Determination and Slot Filling for Spoken Language Understanding](https://www.ijcai.org/Proceedings/16/Papers/425.pdf)|
| Slot-Gated BLSTM with Attension | 95.20 | 94.10 | [Slot-Gated Modeling for Joint Slot Filling and Intent Prediction](https://www.csie.ntu.edu.tw/~yvchen/doc/NAACL18_SlotGated.pdf)| [Official](https://github.com/MiuLab/SlotGated-SLU) |
| Joint model with recurrent slot label context  | 94.64 |  98.40 | [Joint Online Spoken Language Understanding and Language Modeling with Recurrent Neural Networks](https://arxiv.org/pdf/1609.01462.pdf) | [Official](https://github.com/HadoopIt/joint-slu-lm) |
| Recursive NN  | 93.96 | 95.40 | [JOINT SEMANTIC UTTERANCE CLASSIFICATION AND SLOT FILLING WITH RECURSIVE NEURAL NETWORKS](https://www.microsoft.com/en-us/research/wp-content/uploads/2014/12/RecNNSLU.pdf) | |
| Encoder-labeler Deep LSTM | 95.66 | NA  | [Leveraging Sentence-level Information with Encoder LSTM for Natural Language Understanding](https://arxiv.org/abs/1601.01530) |
| RNN with Label Sampling  | 94.89 | NA | [Recurrent Neural Network Structured Output Prediction for Spoken Language Understanding](http://speech.sv.cmu.edu/publications/liu-nipsslu-2015.pdf) | |
| Hybrid RNN | 95.06 | NA | [Using recurrent neural networks for slot filling in spoken language understanding.](http://www.iro.umontreal.ca/~lisa/pointeurs/taslp_RNNSLU_final_doubleColumn.pdf) | |
| RNN-EM | 95.25 |  NA  | [Recurrent neural networks with external memory for language understanding](https://arxiv.org/abs/1506.00195) |
| CNN-CRF | 94.35 | NA  | [Convolutional neural network based triangular crf for joint intent detection and slot filling](https://www.microsoft.com/en-us/research/wp-content/uploads/2013/12/IEEE-ASRU-2013.pdf) | |


## SNIPS
SNIPS is a dataset by Snips.ai for Intent Detection and Slot Filling benchmarking. Available from the [github page](https://github.com/snipsco/nlu-benchmark). This dataset contains several day to day user command categories (e.g. play a song, book a restaurant).

| Model | Slot F1 Score | Intent Accuracy | Paper / Source | Code |
| ------ | ------ | ------ | ------ | ------ |
| SlotRefine + BERT | 97.05 | 99.04  | [SlotRefine: A Fast Non-Autoregressive Model for Joint Intent Detection and Slot Filling](https://aclanthology.org/2020.emnlp-main.152.pdf) | [Official](https://github.com/moore3930/SlotRefine)|
| SlotRefine | 93.72 | 97.44  | [SlotRefine: A Fast Non-Autoregressive Model for Joint Intent Detection and Slot Filling](https://aclanthology.org/2020.emnlp-main.152.pdf) | [Official](https://github.com/moore3930/SlotRefine)|
| Stack-Propagation + BERT | 97.00 | 99.00 | [A Stack-Propagation Framework with Token-level Intent Detection for Spoken Language Understanding](https://arxiv.org/abs/1909.02188)|[Official](https://github.com/LeePleased/StackPropagation-SLU)|
| Stack-Propagation | 94.20 | 98.00 | [A Stack-Propagation Framework with Token-level Intent Detection for Spoken Language Understanding](https://arxiv.org/abs/1909.02188)|[Official](https://github.com/LeePleased/StackPropagation-SLU)|
| Context Encoder | 93.60 | NA | [Improving Slot Filling by Utilizing Contextual Information](https://arxiv.org/pdf/1911.01680.pdf) |
| SF-ID (BLSTM) network | 92.23 | 97.43 | [A Novel Bi-directional Interrelated Model for Joint Intent Detection and Slot Filling](https://arxiv.org/abs/1907.00390) | [Official](https://github.com/ZephyrChenzf/SF-ID-Network-For-NLU) |
| Capsule-NLU | 91.80 | 97.70 | [Joint Slot Filling and Intent Detection via Capsule Neural Networks](https://arxiv.org/abs/1812.09471) | [Official](https://github.com/czhang99/Capsule-NLU) |
| Slot-Gated BLSTM with Attension | 88.80 | 97.00 | [Slot-Gated Modeling for Joint Slot Filling and Intent Prediction](https://www.csie.ntu.edu.tw/~yvchen/doc/NAACL18_SlotGated.pdf)| [Official](https://github.com/MiuLab/SlotGated-SLU) |
