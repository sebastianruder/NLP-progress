# Vietnamese NLP tasks

## Dependency parsing

* Experiments employ the [benchmark Vietnamese dependency treebank VnDT](http://vndp.sourceforge.net) of 10K+ sentences, using  1,020 sentences for test, 200 sentences for development and the remaining sentences for training. LAS and UAS scores are computed on all tokens (i.e. including punctuation). 

#### VnDT v1.1:

| | Model           | LAS |  UAS  |  Paper | Code | 
| ----- | ------------- | :-----:| --- | --- | --- |
| **Predicted POS** | PhoNLP (2021) | 79.11 | 85.47 | [PhoNLP: A joint multi-task learning model for Vietnamese part-of-speech tagging, named entity recognition and dependency parsing](https://aclanthology.org/2021.naacl-demos.1.pdf) | [Official](https://github.com/VinAIResearch/PhoNLP) |
| **Predicted POS** | PhoBERT-base (2020) | 78.77 | 85.22 | [PhoBERT: Pre-trained language models for Vietnamese](https://arxiv.org/abs/2003.00744) | [Official](https://github.com/VinAIResearch/PhoBERT) | 
| **Predicted POS** | PhoBERT-large (2020) | 77.85 | 84.32 | [PhoBERT: Pre-trained language models for Vietnamese](https://arxiv.org/abs/2003.00744) |  [Official](https://github.com/VinAIResearch/PhoBERT) | 
| **Predicted POS** | Biaffine (2017) | 74.99 | 81.19 | [Deep Biaffine Attention for Neural Dependency Parsing](https://arxiv.org/abs/1611.01734) |  | 
| **Predicted POS** | jointWPD (2018) | 73.90 | 80.12 | [A neural joint model for Vietnamese word segmentation, POS tagging and dependency parsing](https://arxiv.org/abs/1812.11459)  |  | 
| **Predicted POS** | jPTDP-v2 (2018) |  73.12 | 79.63 | [An improved neural network model for joint POS tagging and dependency parsing](http://aclweb.org/anthology/K18-2008) |  | 
| **Predicted POS** | VnCoreNLP (2018) | 71.38 | 77.35 | [VnCoreNLP: A Vietnamese Natural Language Processing Toolkit](http://aclweb.org/anthology/N18-5012) | [Official](https://github.com/vncorenlp/VnCoreNLP) | 

* Results on the VnDT v1.1 for Biaffine, jPTDP-v2 and VnCoreNLP are reported in the jointWPD paper "[A neural joint model for Vietnamese word segmentation, POS tagging and dependency parsing](https://arxiv.org/abs/1812.11459)."

#### VnDT v1.0:

| | Model           | LAS |  UAS  |  Paper | Code | 
| ----- | ------------- | :-----:| --- | --- | --- |
| **Predicted POS** | VnCoreNLP (2018) | 70.23 | 76.93 | [VnCoreNLP: A Vietnamese Natural Language Processing Toolkit](http://aclweb.org/anthology/N18-5012) | [Official](https://github.com/vncorenlp/VnCoreNLP) | 
| Gold POS | VnCoreNLP (2018) |73.39 |79.02 | [VnCoreNLP: A Vietnamese Natural Language Processing Toolkit](http://aclweb.org/anthology/N18-5012) | [Official](https://github.com/vncorenlp/VnCoreNLP) | 
| Gold POS | BIST BiLSTM graph-based parser (2016) | 73.17|79.39 | [Simple and Accurate Dependency Parsing Using Bidirectional LSTM Feature Representations](https://aclweb.org/anthology/Q16-1023) | [Official](https://github.com/elikip/bist-parser/tree/master/bmstparser/src) | 
| Gold POS | BIST BiLSTM transition-based parser (2016) | 72.53| 79.33 | [Simple and Accurate Dependency Parsing Using Bidirectional LSTM Feature Representations](https://aclweb.org/anthology/Q16-1023) | [Official](https://github.com/elikip/bist-parser/tree/master/barchybrid/src) | 
| Gold POS | MSTparser (2006) | 70.29 | 76.47 | [Online large-margin training of dependency parsers](http://www.aclweb.org/anthology/P05-1012) | | 
| Gold POS | MaltParser (2007) | 69.10 | 74.91 | [MaltParser: A language-independent system for datadriven dependency parsing](https://stp.lingfil.uu.se/~nivre/docs/nle07.pdf) | | 


* Results for the BIST graph/transition-based parsers, MSTparser and MaltParser are reported in "[An empirical study for Vietnamese dependency parsing](http://www.aclweb.org/anthology/U16-1017)."

## Intent detection and Slot filling
### [PhoATIS](https://github.com/VinAIResearch/JointIDSF)
* The first dataset for intent detection and slot filling for Vietnamese, based on the common ATIS benchmark in the flight booking domain. Data is localized (e.g. replacing slot values with Vietnamese-specific entities) to fit the context of flight booking in Vietnam.
* Training set: 4478 sentences
* Development set: 500 sentences
* Test set: 893 sentences

| Model           | Intent Acc. | Slot F1 | Sentence Acc.  |  Paper | Code | Note |
| ------------- | :-----:| --- |--- |--- | --- | --- |
| JointIDSF (2021) | 97.62 | 94.98 | 86.25 | [Intent Detection and Slot Filling for Vietnamese](https://arxiv.org/abs/2104.02021) | [Official](https://github.com/VinAIResearch/JointIDSF) | Text are automatically word-segmented using [RDRSegmenter](https://github.com/vncorenlp/VnCoreNLP)
| JointBERT (2019) with PhoBERT encoder | 97.40 | 94.75 | 85.55 | [Intent Detection and Slot Filling for Vietnamese](https://arxiv.org/abs/2104.02021) | [Official](https://github.com/VinAIResearch/JointIDSF) | Text are automatically word-segmented using [RDRSegmenter](https://github.com/vncorenlp/VnCoreNLP)

## Machine translation

### English-Vietnamese translation
* Dataset is from [The IWSLT 2015 Evaluation Campaign](http://workshop2015.iwslt.org/downloads/proceeding.pdf), also be obtained from [https://github.com/tensorflow/nmt](https://github.com/tensorflow/nmt).

#### English-to-Vietnamese
`tst2015` is used for test

| Model           | BLEU  |  Paper | Code | 
| ------------- | :-----:| --- | --- | 
| Stanford (2015) | 26.4 | [Stanford Neural Machine Translation Systems for Spoken Language Domains](https://nlp.stanford.edu/pubs/luong-manning-iwslt15.pdf) | | 

---
`tst2013` is used for test

| Model           | BLEU  |  Paper | Code | 
| ------------- | :-----:| --- | --- | 
| Nguyen and Salazar (2019) | 32.8 | [Transformers without Tears: Improving the Normalization of Self-Attention](https://arxiv.org/abs/1910.05895) | [Official](https://github.com/tnq177/transformers_without_tears) | 
| Provilkov et al. (2019) | 33.27 (uncased) | [BPE-Dropout: Simple and Effective Subword Regularization](https://arxiv.org/abs/1910.13267) | |
| Xu et al. (2019) | 31.4 | [Understanding and Improving Layer Normalization](https://papers.nips.cc/paper/8689-understanding-and-improving-layer-normalization.pdf) | [Official](https://github.com/lancopku/AdaNorm) |
| CVT (2018) | 29.6 (SST) | [Semi-Supervised Sequence Modeling with Cross-View Training](https://arxiv.org/abs/1809.08370) | |
| ELMo (2018) | 29.3 (SST) | [Deep contextualized word representations](http://aclweb.org/anthology/N18-1202)| | 
| Transformer (2017) | 28.9 | [Attention is all you need](http://papers.nips.cc/paper/7181-attention-is-all-you-need) | [Link](https://github.com/duyvuleo/Transformer-DyNet) |
| Kudo (2018) | 28.5 | [Subword Regularization: Improving Neural Network Translation Models with Multiple Subword Candidates](https://arxiv.org/abs/1804.10959) | | 
| Google (2017) | 26.1 | [Neural machine translation (seq2seq) tutorial](https://github.com/tensorflow/nmt)  | [Official](https://github.com/tensorflow/nmt) | 
| Stanford (2015) |23.3 | [Stanford Neural Machine Translation Systems for Spoken Language Domains](https://nlp.stanford.edu/pubs/luong-manning-iwslt15.pdf) | | 

* The ELMo score is reported in [Semi-Supervised Sequence Modeling with Cross-View Training](https://arxiv.org/abs/1809.08370). The Transformer score is available at  [https://github.com/duyvuleo/Transformer-DyNet](https://github.com/duyvuleo/Transformer-DyNet).

#### Vietnamese-to-English

`tst2013` is used for test

| Model           | BLEU  |  Paper | Code | 
| ------------- | :-----:| --- | --- | 
| Provilkov et al. (2019) | 32.99 (uncased) | [BPE-Dropout: Simple and Effective Subword Regularization](https://arxiv.org/abs/1910.13267) | |
| Kudo (2018) | 26.31 | [Subword Regularization: Improving Neural Network Translation Models with Multiple Subword Candidates](https://arxiv.org/abs/1804.10959) | | 


## Named entity recognition
### [PhoNER_COVID19](https://github.com/VinAIResearch/PhoNER_COVID19)
* A named entity recognition dataset for Vietnamese with 10 newly-defined entity types in the context of the COVID-19 pandemic. Data is extracted from news articles and manually annotated. In total, there are 34 984 entities over 10 027 sentences.
* Training set: 5027 sentences
* Development set: 2000 sentences
* Test set: 3000 sentences

| Model           | F1  |  Paper | Code | Note | 
| ------------- | :-----:| --- | --- | --- | 
| PhoBERT-large (2020) | 94.5 | [PhoBERT: Pre-trained language models for Vietnamese](https://arxiv.org/abs/2003.00744) | [Official](https://github.com/VinAIResearch/PhoBERT) | 
| PhoBERT-base (2020) | 94.2 | [PhoBERT: Pre-trained language models for Vietnamese](https://arxiv.org/abs/2003.00744) | [Official](https://github.com/VinAIResearch/PhoBERT) | 
| XLM-R-large (2019) | 93.8 | [Unsupervised Cross-lingual Representation Learning at Scale](https://aclanthology.org/2020.acl-main.747/) | [Official](https://github.com/facebookresearch/XLM) | 
| XLM-R-base (2019) | 92.5 | [Unsupervised Cross-lingual Representation Learning at Scale](https://aclanthology.org/2020.acl-main.747/) | [Official](https://github.com/facebookresearch/XLM) | 
| BiLSTM-CRF + CNN-char (2016) + Word Segmentation | 91 | [End-to-end Sequence Labeling via Bi-directional LSTM-CNNs-CRF](http://www.aclweb.org/anthology/P16-1101) | [Link](https://github.com/UKPLab/emnlp2017-bilstm-cnn-crf/) | Text are automatically word-segmented using [RDRSegmenter](https://github.com/vncorenlp/VnCoreNLP) |
| BiLSTM-CRF + CNN-char  (2016) | 90.6 | [End-to-end Sequence Labeling via Bi-directional LSTM-CNNs-CRF](http://www.aclweb.org/anthology/P16-1101) | [Link](https://github.com/UKPLab/emnlp2017-bilstm-cnn-crf/) | No word segmentation |

### VLSP
* 16,861 sentences for training and development from the VLSP 2016 NER shared task:
  *  14,861 sentences are used for training.
  *  2k sentences are used for development.
* Test data: 2,831 test sentences from the VLSP 2016 NER  shared task.
* **NOTE** that in the VLSP 2016 NER data, each word representing a full personal name are separated into syllables that constitute the word. The VLSP 2016 NER data also consists of gold POS and chunking tags as [reconfirmed by VLSP 2016 organizers](https://drive.google.com/file/d/1XzrgPw13N4C_B6yrQy_7qIxl8Bqf7Uqi/view?usp=sharing). This scheme results in an unrealistic scenario for a pipeline evaluation: 
  * The standard annotation for Vietnamese word segmentation and POS tagging forms each full name as a word token, thus all   word segmenters have been trained to output a full name as a word and all POS taggers have been trained to assign a POS label to the entire full-name.
  * Gold POS and chunking tags are NOT available in a real-world application.
* For a realistic scenario, contiguous syllables constituting a full name are merged to form a word. POS/chunking tags--if used--have to be automatically predicted! 

| Model           | F1  |  Paper | Code | Note | 
| ------------- | :-----:| --- | --- | --- | 
| PhoBERT-large (2020) | 94.7 | [PhoBERT: Pre-trained language models for Vietnamese](https://arxiv.org/abs/2003.00744) | [Official](https://github.com/VinAIResearch/PhoBERT) | 
| PhoNLP (2021) | 94.41 | [PhoNLP: A joint multi-task learning model for Vietnamese part-of-speech tagging, named entity recognition and dependency parsing](https://aclanthology.org/2021.naacl-demos.1.pdf) | [Official](https://github.com/VinAIResearch/PhoNLP) |
| vELECTRA (2020) | 94.07 | [Improving Sequence Tagging for Vietnamese Text Using Transformer-based Neural Models](https://arxiv.org/abs/2006.15994) | [Official](https://github.com/fpt-corp/viBERT) |
| PhoBERT-base (2020) | 93.6 | [PhoBERT: Pre-trained language models for Vietnamese](https://arxiv.org/abs/2003.00744) |  [Official](https://github.com/VinAIResearch/PhoBERT) | 
| VnCoreNLP (2018) [1] | 91.30 | [VnCoreNLP: A Vietnamese Natural Language Processing Toolkit](http://aclweb.org/anthology/N18-5012) | [Official](https://github.com/vncorenlp/VnCoreNLP) | Used ETNLP embeddings |
| BiLSTM-CRF + CNN-char  (2016) [1] | 91.09 | [End-to-end Sequence Labeling via Bi-directional LSTM-CNNs-CRF](http://www.aclweb.org/anthology/P16-1101) | [Official](https://github.com/XuezheMax/LasagneNLP) / [Link](https://github.com/UKPLab/emnlp2017-bilstm-cnn-crf/)  | Used ETNLP embeddings | 
| VNER (2019) | 89.58 | [Attentive Neural Network for Named Entity Recognition in Vietnamese](https://arxiv.org/abs/1810.13097) | | 
| VnCoreNLP (2018) | 88.55 | [VnCoreNLP: A Vietnamese Natural Language Processing Toolkit](http://aclweb.org/anthology/N18-5012) | [Official](https://github.com/vncorenlp/VnCoreNLP) | Pre-trained embeddings learned from Baomoi corpus |
| BiLSTM-CRF + CNN-char  (2016) [2] | 88.28 | [End-to-end Sequence Labeling via Bi-directional LSTM-CNNs-CRF](http://www.aclweb.org/anthology/P16-1101) | [Official](https://github.com/XuezheMax/LasagneNLP) / [Link](https://github.com/UKPLab/emnlp2017-bilstm-cnn-crf/) | Pre-trained embeddings learned from Baomoi corpus |
| BiLSTM-CRF + LSTM-char (2016) [2] | 87.71 | [Neural Architectures for Named Entity Recognition](http://www.aclweb.org/anthology/N16-1030) | [Link](https://github.com/UKPLab/emnlp2017-bilstm-cnn-crf/) | Pre-trained embeddings learned from Baomoi corpus |
| BiLSTM-CRF (2015) [2] | 86.48 | [Bidirectional LSTM-CRF Models for Sequence Tagging](https://arxiv.org/abs/1508.01991) | [Link](https://github.com/UKPLab/emnlp2017-bilstm-cnn-crf/) | Pre-trained embeddings learned from Baomoi corpus |

* [1] denotes that scores are reported in  "[ETNLP: a visual-aided systematic approach to select pre-trained embeddings for a downstream task](https://arxiv.org/abs/1903.04433)"
* [2] denotes that BiLSTM-CRF-based scores are reported in  "[VnCoreNLP: A Vietnamese Natural Language Processing Toolkit](http://aclweb.org/anthology/N18-5012)"


## Part-of-speech tagging 

* 27,870 sentences for training and development from the VLSP 2013 POS tagging shared task:
  *  27k sentences are used for training.
  *  870 sentences are used for development.
* Test data: 2120 test sentences from the VLSP 2013 POS tagging shared task.

| Model           | Accuracy  |  Paper | Code | 
| ------------- | :-----:| --- | --- | 
| PhoBERT-large (2020) | 96.8 | [PhoBERT: Pre-trained language models for Vietnamese](https://arxiv.org/abs/2003.00744) | [Official](https://github.com/VinAIResearch/PhoBERT) |
| vELECTRA (2020) | 96.77 | [Improving Sequence Tagging for Vietnamese Text Using Transformer-based Neural Models](https://arxiv.org/abs/2006.15994) | [Official](https://github.com/fpt-corp/viBERT) |
| PhoNLP (2021) | 96.76 | [PhoNLP: A joint multi-task learning model for Vietnamese part-of-speech tagging, named entity recognition and dependency parsing](https://aclanthology.org/2021.naacl-demos.1.pdf) | [Official](https://github.com/VinAIResearch/PhoNLP) |
| PhoBERT-base (2020) | 96.7 | [PhoBERT: Pre-trained language models for Vietnamese](https://arxiv.org/abs/2003.00744) |  [Official](https://github.com/VinAIResearch/PhoBERT) | 
| jointWPD (2018) | 95.97 | [A neural joint model for Vietnamese word segmentation, POS tagging and dependency parsing](https://arxiv.org/abs/1812.11459) | | 
| VnCoreNLP-VnMarMoT (2017) | 95.88 | [From Word Segmentation to POS Tagging for Vietnamese](http://aclweb.org/anthology/U17-1013) | [Official](https://github.com/datquocnguyen/vnmarmot) | 
| jPTDP-v2 (2018) | 95.70 | [An improved neural network model for joint POS tagging and dependency parsing](http://aclweb.org/anthology/K18-2008) | | 
| BiLSTM-CRF + CNN-char  (2016) | 95.40 | [End-to-end Sequence Labeling via Bi-directional LSTM-CNNs-CRF](http://www.aclweb.org/anthology/P16-1101) | [Official](https://github.com/XuezheMax/LasagneNLP) /  [Link](https://github.com/UKPLab/emnlp2017-bilstm-cnn-crf/) | 
| BiLSTM-CRF + LSTM-char (2016) | 95.31 | [Neural Architectures for Named Entity Recognition](http://www.aclweb.org/anthology/N16-1030) | [Link](https://github.com/UKPLab/emnlp2017-bilstm-cnn-crf/) | 
| BiLSTM-CRF (2015) | 95.06 | [Bidirectional LSTM-CRF Models for Sequence Tagging](https://arxiv.org/abs/1508.01991) | [Link](https://github.com/UKPLab/emnlp2017-bilstm-cnn-crf/) | 
| RDRPOSTagger (2014) | 95.11 |  [RDRPOSTagger: A Ripple Down Rules-based Part-Of-Speech Tagger](http://www.aclweb.org/anthology/E14-2005) | [Official](https://github.com/datquocnguyen/rdrpostagger) | 

* Result for jPTDP-v2 is reported in "[A neural joint model for Vietnamese word segmentation, POS tagging and dependency parsing](https://arxiv.org/abs/1812.11459)." 
* Results for BiLSTM-CRF-based models and RDRPOSTagger are reported in  "[From Word Segmentation to POS Tagging for Vietnamese](http://aclweb.org/anthology/U17-1013)."

## Word segmentation 

* Training & development data: 75k manually word-segmented training sentences from the [VLSP](http://vlsp.org.vn/) 2013 word segmentation shared task.
* Test data: 2120 test sentences from the VLSP 2013 POS tagging shared task.

| Model           | F1  |  Paper | Code | 
| ------------- | :-----:| --- | --- | 
| UITws-v1 (2019) | 98.06 | [Vietnamese Word Segmentation with SVM: Ambiguity Reduction and Suffix Capture](https://arxiv.org/abs/2006.07804) | [Official](https://github.com/ngannlt/UITws-v1) |
| VnCoreNLP-RDRsegmenter (2018) | 97.90 | [A Fast and Accurate Vietnamese Word Segmenter](http://www.lrec-conf.org/proceedings/lrec2018/pdf/55.pdf) | [Official](https://github.com/datquocnguyen/RDRsegmenter) | 
| UETsegmenter (2016) | 97.87 | [A hybrid approach to Vietnamese word segmentation](http://doi.org/10.1109/RIVF.2016.7800279) | [Official](https://github.com/phongnt570/UETsegmenter) |
| jointWPD (2018) | 97.81 | [A neural joint model for Vietnamese word segmentation, POS tagging and dependency parsing](https://arxiv.org/abs/1812.11459) | | 
| vnTokenizer (2008) | 97.33 | [A Hybrid Approach to Word Segmentation of Vietnamese Texts](https://link.springer.com/chapter/10.1007/978-3-540-88282-4_23) |  |
| JVnSegmenter (2006) | 97.06 | [Vietnamese Word Segmentation with CRFs and SVMs: An Investigation](http://www.aclweb.org/anthology/Y06-1028) |  |
| DongDu (2012) | 96.90 |  [Ứng dụng phương pháp Pointwise vào bài toán tách từ cho tiếng Việt](https://tiengvietmenyeu.wordpress.com/2013/02/16/ung%C2%B7dung-phuong%C2%B7phap-pointwise-vao-bai%C2%B7toan-tach-tu-cho-tieng%C2%B7viet/) |  |

* Results for VnTokenizer, JVnSegmenter and DongDu are reported in "[A hybrid approach to Vietnamese word segmentation](http://doi.org/10.1109/RIVF.2016.7800279)."
