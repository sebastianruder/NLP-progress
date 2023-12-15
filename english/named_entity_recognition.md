# Named entity recognition

Named entity recognition (NER) is the task of tagging entities in text with their corresponding type.
Approaches typically use BIO notation, which differentiates the beginning (B) and the inside (I) of entities.
O is used for non-entity tokens.

Example:

| Mark  | Watney | visited | Mars  |
| ----- | ------ | ------- | ----- |
| B-PER | I-PER  | O       | B-LOC |

### CoNLL 2003 (English)

The [CoNLL 2003 NER task](http://www.aclweb.org/anthology/W03-0419.pdf) consists of newswire text from the Reuters RCV1 
corpus tagged with four different entity types (PER, LOC, ORG, MISC). Models are evaluated based on span-based F1 on the test set. ♦ used both the train and development splits for training.

| Model           | F1  |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| ACE + document-context (Wang et al., 2021) | 94.6 | [Automated Concatenation of Embeddings for Structured Prediction](https://arxiv.org/pdf/2010.05006.pdf) | [Official](https://github.com/Alibaba-NLP/ACE)|
| LUKE (Yamada et al., 2020) | 94.3 | [LUKE: Deep Contextualized Entity Representations with Entity-aware Self-attention](https://www.aclweb.org/anthology/2020.emnlp-main.523/) | [Official](https://github.com/studio-ousia/luke) |
| CL-KL (Wang et al., 2021) | 93.85 | [Improving Named Entity Recognition by External Context Retrieving and Cooperative Learning](https://arxiv.org/abs/2105.03654) | [Official](https://github.com/Alibaba-NLP/CLNER)|
| InferNER (Moemmur et al., 2021) | 93.76| [InferNER: an attentive model leveraging the sentence-level information for Named Entity Recognition in Microblogs](https://journals.flvc.org/FLAIRS/article/view/128538) | |
| ACE (Wang et al., 2021) | 93.6 | [Automated Concatenation of Embeddings for Structured Prediction](https://arxiv.org/pdf/2010.05006.pdf) | [Official](https://github.com/Alibaba-NLP/ACE)|
| CNN Large + fine-tune (Baevski et al., 2019) | 93.5 | [Cloze-driven Pretraining of Self-attention Networks](https://arxiv.org/pdf/1903.07785.pdf) | |
| RNN-CRF+Flair | 93.47 | [Improved Differentiable Architecture Search for Language Modeling and Named Entity Recognition](https://www.aclweb.org/anthology/D19-1367/) | |
| CrossWeigh + Flair (Wang et al., 2019)♦ | 93.43 | [CrossWeigh: Training Named Entity Tagger from Imperfect Annotations](https://www.aclweb.org/anthology/D19-1519/) | [Official](https://github.com/ZihanWangKi/CrossWeigh) |
| LSTM-CRF+ELMo+BERT+Flair | 93.38 | [Neural Architectures for Nested NER through Linearization](https://www.aclweb.org/anthology/P19-1527/) | [Official](https://github.com/ufal/acl2019_nested_ner) |
| Flair embeddings (Akbik et al., 2018)♦ | 93.09 | [Contextual String Embeddings for Sequence Labeling](https://drive.google.com/file/d/17yVpFA7MmXaQFTe-HDpZuqw9fJlmzg56/view) | [Flair framework](https://github.com/zalandoresearch/flair)
| BERT Large (Devlin et al., 2018) | 92.8 | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) | |
| CVT + Multi-Task (Clark et al., 2018) | 92.61 | [Semi-Supervised Sequence Modeling with Cross-View Training](https://arxiv.org/abs/1809.08370) | [Official](https://github.com/tensorflow/models/tree/master/research/cvt_text) |
| BERT Base (Devlin et al., 2018) | 92.4 | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) | |
| BiLSTM-CRF+ELMo (Peters et al., 2018) | 92.22 | [Deep contextualized word representations](https://arxiv.org/abs/1802.05365) | [AllenNLP Project](https://allennlp.org/elmo) [AllenNLP GitHub](https://github.com/allenai/allennlp) |
| Peters et al. (2017) ♦| 91.93 | [Semi-supervised sequence tagging with bidirectional language models](https://arxiv.org/abs/1705.00108) | |
| CRF + AutoEncoder (Wu et al., 2018) | 91.87 | [Evaluating the Utility of Hand-crafted Features in Sequence Labelling](http://aclweb.org/anthology/D18-1310) | [Official](https://github.com/minghao-wu/CRF-AE) | 
| Bi-LSTM-CRF + Lexical Features (Ghaddar and Langlais 2018) | 91.73 | [Robust Lexical Features for Improved Neural Network Named-Entity Recognition](https://arxiv.org/pdf/1806.03489.pdf) | [Official](https://github.com/ghaddarAbs/NER-with-LS) |
| BiLSTM-CRF + IntNet (Xin et al., 2018) | 91.64 | [Learning Better Internal Structure of Words for Sequence Labeling](https://www.aclweb.org/anthology/D18-1279) | |
| Chiu and Nichols (2016) ♦| 91.62 | [Named entity recognition with bidirectional LSTM-CNNs](https://arxiv.org/abs/1511.08308) | |
| HSCRF (Ye and Ling, 2018)| 91.38 | [Hybrid semi-Markov CRF for Neural Sequence Labeling](http://aclweb.org/anthology/P18-2038) | [HSCRF](https://github.com/ZhixiuYe/HSCRF-pytorch) |
| IXA pipes (Agerri and Rigau 2016) | 91.36 | [Robust multilingual Named Entity Recognition with shallow semi-supervised features](https://doi.org/10.1016/j.artint.2016.05.003)| [Official](https://github.com/ixa-ehu/ixa-pipe-nerc)|
| NCRF++ (Yang and Zhang, 2018)| 91.35 | [NCRF++: An Open-source Neural Sequence Labeling Toolkit](http://www.aclweb.org/anthology/P18-4013) | [NCRF++](https://github.com/jiesutd/NCRFpp) |
| LM-LSTM-CRF (Liu et al., 2018)| 91.24 | [Empowering Character-aware Sequence Labeling with Task-Aware Neural Language Model](https://arxiv.org/pdf/1709.04109.pdf) | [LM-LSTM-CRF](https://github.com/LiyuanLucasLiu/LM-LSTM-CRF) |
| Yang et al. (2017) ♦| 91.26 | [Transfer Learning for Sequence Tagging with Hierarchical Recurrent Networks](https://arxiv.org/abs/1703.06345) | |
| Ma and Hovy (2016) | 91.21 | [End-to-end Sequence Labeling via Bi-directional LSTM-CNNs-CRF](https://arxiv.org/abs/1603.01354) | |
| LSTM-CRF (Lample et al., 2016) | 90.94 | [Neural Architectures for Named Entity Recognition](https://arxiv.org/abs/1603.01360) | |

### CoNLL++ 

This is a cleaner version of the CoNLL 2003 NER task, where about 5% of instances in the test set are corrected due to mislabelling. The training set is left untouched.  Models are evaluated based on span-based F1 on the test set. ♦ used both the train and development splits for training. 

Links: [CoNLL++](https://github.com/ZihanWangKi/CrossWeigh) (including direct download links for data)

| Model                                   |  F1   | Paper / Source                           | Code                                     |
| --------------------------------------- | :---: | ---------------------------------------- | ---------------------------------------- |
| CL-KL (Wang et al., 2021) | 94.81 | [Improving Named Entity Recognition by External Context Retrieving and Cooperative Learning](https://arxiv.org/abs/2105.03654) | [Official](https://github.com/Alibaba-NLP/CLNER)|
| CrossWeigh + Flair (Wang et al., 2019)♦ | 94.28 | [CrossWeigh: Training Named Entity Tagger from Imperfect Annotations](https://www.aclweb.org/anthology/D19-1519/) | [Official](https://github.com/ZihanWangKi/CrossWeigh) |
| Flair embeddings (Akbik et al., 2018)♦ | 93.89 | [Contextual String Embeddings for Sequence Labeling](https://drive.google.com/file/d/17yVpFA7MmXaQFTe-HDpZuqw9fJlmzg56/view) | [Flair framework](https://github.com/zalandoresearch/flair)
| BiLSTM-CRF+ELMo (Peters et al., 2018) | 93.42 | [Deep contextualized word representations](https://arxiv.org/abs/1802.05365) | [AllenNLP Project](https://allennlp.org/elmo) [AllenNLP GitHub](https://github.com/allenai/allennlp) |
| Ma and Hovy (2016) | 91.87 | [End-to-end Sequence Labeling via Bi-directional LSTM-CNNs-CRF](https://arxiv.org/abs/1603.01354) | |
| LSTM-CRF (Lample et al., 2016) | 91.47 | [Neural Architectures for Named Entity Recognition](https://arxiv.org/abs/1603.01360) | |


### Long-tail emerging entities

The [WNUT 2017 Emerging Entities task](http://aclweb.org/anthology/W17-4418) operates over a wide range of English 
text and focuses on generalisation beyond memorisation in high-variance environments. Scores are given both over
entity chunk instances, and unique entity surface forms, to normalise the biasing impact of entities that occur frequently.

| Feature   | Train  | Dev    | Test   |
| --------- | ------ | ------ | ------ |
| Posts     | 3,395  | 1,009  | 1,287  |
| Tokens    | 62,729 | 15,733 | 23,394 |
| NE tokens | 3,160  | 1,250  | 1,589  |

The data is annotated for six classes - person, location, group, creative work, product and corporation.

Links: [WNUT 2017 Emerging Entity task page](https://noisy-text.github.io/2017/emerging-rare-entities.html) (including direct download links for data and scoring script)

| Model         | F1  | F1 (surface form) |  Paper / Source |
| ---           | --- | ---               | --- |
| InferNER (Moemmur et al., 2021)          | 50.52| ---               | [InferNER: an attentive model leveraging the sentence-level information for Named Entity Recognition in Microblogs](https://journals.flvc.org/FLAIRS/article/view/128538) |
| CrossWeigh + Flair (Wang et al., 2019) | 50.03 | [CrossWeigh: Training Named Entity Tagger from Imperfect Annotations](https://www.aclweb.org/anthology/D19-1519/) | [Official](https://github.com/ZihanWangKi/CrossWeigh) |
| Flair embeddings (Akbik et al., 2018)  | 49.59 |                                          | [Pooled Contextualized Embeddings for Named Entity Recognition](http://alanakbik.github.io/papers/naacl2019_embeddings.pdf) / [Flair framework](https://github.com/zalandoresearch/flair) |
| Aguilar et al. (2018)                  | 45.55 |                                          | [Modeling Noisiness to Recognize Named Entities using Multitask Neural Networks on Social Media](http://aclweb.org/anthology/N18-1127.pdf) |
| SpinningBytes                          | 40.78 | 39.33                                    | [Transfer Learning and Sentence Level Features for Named Entity Recognition on Tweets](http://aclweb.org/anthology/W17-4422.pdf) |

### Ontonotes v5 (English)

The [Ontonotes corpus v5](https://catalog.ldc.upenn.edu/docs/LDC2013T19/OntoNotes-Release-5.0.pdf) is a richly annotated corpus with several layers of annotation, including named entities, coreference, part of speech, word sense, propositions, and syntactic parse trees. These annotations are over a large number of tokens, a broad cross-section of domains, and 3 languages (English, Arabic, and Chinese). The NER dataset (of interest here) includes 18 tags, consisting of 11 _types_ (PERSON, ORGANIZATION, etc) and 7 _values_ (DATE, PERCENT, etc), and contains 2 million tokens. The common datasplit used in NER is defined in [Pradhan et al 2013](https://www.semanticscholar.org/paper/Towards-Robust-Linguistic-Analysis-using-OntoNotes-Pradhan-Moschitti/a94e4fe6f475e047be5dcc9077f445e496240852) and can be found [here](http://cemantix.org/data/ontonotes.html).

| Model                                    |  F1   | Paper / Source                           | Code                                     |
| ---------------------------------------- | :---: | ---------------------------------------- | ---------------------------------------- |
| BERT+KVMN (Nie et al., 2020)    | 90.32 | [Improving Named Entity Recognition with Attentive Ensemble of Syntactic Information](https://aclanthology.org/2020.findings-emnlp.378/) | [Official](https://github.com/cuhksz-nlp/AESINER) |
| Flair embeddings (Akbik et al., 2018)    | 89.71 | [Contextual String Embeddings for Sequence Labeling](http://aclweb.org/anthology/C18-1139) | [Official](https://github.com/zalandoresearch/flair) |
| CVT + Multi-Task (Clark et al., 2018)    | 88.81 | [Semi-Supervised Sequence Modeling with Cross-View Training](https://arxiv.org/abs/1809.08370) | [Official](https://github.com/tensorflow/models/tree/master/research/cvt_text) |
| Bi-LSTM-CRF + Lexical Features (Ghaddar and Langlais 2018) | 87.95 | [Robust Lexical Features for Improved Neural Network Named-Entity Recognition](https://arxiv.org/pdf/1806.03489.pdf) | [Official](https://github.com/ghaddarAbs/NER-with-LS) |
| BiLSTM-CRF (Strubell et al, 2017)        | 86.99 | [Fast and Accurate Entity Recognition with Iterated Dilated Convolutions](https://arxiv.org/pdf/1702.02098.pdf) | [Official](https://github.com/iesl/dilated-cnn-ner) |
| Iterated Dilated CNN (Strubell et al, 2017) | 86.84 | [Fast and Accurate Entity Recognition with Iterated Dilated Convolutions](https://arxiv.org/pdf/1702.02098.pdf) | [Official](https://github.com/iesl/dilated-cnn-ner) |
| Chiu and Nichols (2016)                  | 86.28 | [Named entity recognition with bidirectional LSTM-CNNs](https://arxiv.org/abs/1511.08308) |                                          |
| Joint Model (Durrett and Klein 2014)     | 84.04 | [A Joint Model for Entity Analysis: Coreference, Typing, and Linking](https://pdfs.semanticscholar.org/2eaf/f2205c56378e715d8d12c521d045c0756a76.pdf) |                                          |
| Averaged Perceptron (Ratinov and Roth 2009) | 83.45 | [Design Challenges and Misconceptions in Named Entity Recognition](https://www.semanticscholar.org/paper/Design-Challenges-and-Misconceptions-in-Named-Ratinov-Roth/27496a2ee337db705e7c611dea1fd8e6f41437c2) (These scores reported in ([Durrett and Klein 2014](https://pdfs.semanticscholar.org/2eaf/f2205c56378e715d8d12c521d045c0756a76.pdf))) | [Official](https://github.com/CogComp/cogcomp-nlp/tree/master/ner) |



### Few-NERD

[Few-NERD](https://arxiv.org/abs/2105.07464) is a large-scale, fine-grained manually annotated named entity recognition dataset, which contains 8 coarse-grained types, 66 fine-grained types, 188,200 sentences, 491,711 entities and 4,601,223 tokens. Three benchmark tasks are built:

- Few-NERD (SUP) is a standard NER task;
- Few-NERD (INTRA) is a few-shot NER task across different coarse-grained types;
- Few-NERD (INTER) is a few-shot NER task within coarse-grained types.

Website: [Few-NERD page](https://ningding97.github.io/fewnerd/);

Download & code: https://github.com/thunlp/Few-NERD



#### Results on Few-NERD (SUP)

| Model                           |  F1   | Paper / Source                           | Code                                     |
| ------------------------------- | :---: | ---------------------------------------- | ---------------------------------------- |
| BERT-Tagger (Ding et al., 2021) | 68.88 | [Few-NERD: A Few-shot Named Entity Recognition Dataset](https://www.stingning.cn/assets/pdf/ACL2021-fewnerd.pdf) | [Official](https://github.com/thunlp/Few-NERD) |



### MultiCoNER (SemEval 2022 Task 11)
MultiCoNER, a large multilingual dataset for Named Entity Recognition that covers 3 domains (Wiki sentences, questions, and search queries) across 11 languages, as well as multilingual and code-mixing subsets. This dataset is designed to represent contemporary challenges in NER, including low-context scenarios (short and uncased text), syntactically complex entities like movie titles, and long-tail entity distributions. The 26M token dataset is compiled from public resources using techniques such as heuristic-based sentence sampling, template extraction and slotting, and machine translation. MultiCoNER poses challenges even for large pre-trained language models, and we believe that it can help further research in building robust NER systems. MultiCoNER is publicly available at https://registry.opendata.aws/multiconer/ and we hope that this resource will help advance research in various aspects of NER.
It was part of <a href"https://multiconer.github.io/multiconer_1/">SemEval 2022 Task 11</a>

### MultiCoNER v2 (SemEval 2023 Task 2)
We present MULTICONER V2, a dataset for fine-grained Named Entity Recognition covering 33 entity classes across 12 languages, in both monolingual and multilingual settings. This dataset aims to tackle the following practical challenges in NER: (i) effective handling of fine-grained classes that include complex entities like movie titles, and (ii) performance degradation due to noise generated from typing mistakes or OCR errors. The dataset is compiled from open resources like Wikipedia and Wikidata, and is publicly available. Evaluation based on the XLM-RoBERTa baseline highlights the unique challenges posed by MULTICONER V2: (i) the fine-grained taxonomy is challenging, where the scores are low with macro-F1=0.63 (across all languages), and (ii) the corruption strategy significantly impairs performance, with entity corruption resulting in 9% lower performance relative to non-entity corruptions across all languages. This highlights the greater impact of entity noise in contrast to context noise.
It was part of <a href"https://multiconer.github.io/">SemEval 2023 Task 2</a>



#### 




[Go back to the README](../README.md)
