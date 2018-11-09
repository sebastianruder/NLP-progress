# Grammatical Error Correction

Grammatical Error Correction (GEC) is the task of correcting different kinds of errors in text such as spelling, grammatical, and word choice errors. 

GEC is usually formulated as a sentence-to-sentence correction task. A GEC system takes a potentially erroneous sentence as input and is expected to transform it into its corrected version. See the example given below: 

| Input (Erroneous)          | Output (Corrected)     |
| -------------------------  | ---------------------- |
|She see Tom is catched by policeman in park at last night. | She saw Tom caught by a policeman in the park last night.|

### CoNLL-2014 Shared Task

The CoNLL-2014 shared task test set (https://www.comp.nus.edu.sg/~nlp/conll14st/conll14st-test-data.tar.gz) is the most widely used dataset to benchmark GEC systems.  The test set contains 1,312 english sentences with error annotations by 2 expert annotators. Models are evaluated with MaxMatch scorer ([Dahlmeier and Ng, 2012](http://www.aclweb.org/anthology/N12-1067)) which is a phrase-level F<sub>β</sub>-score with β=0.5 that weights precision twice as recall.

The shared task setting restricts that systems use only publicly available datasets for training to fairer comparisons. The best published results on the CoNLL-2014 test set are given below. A distinction is made between papers that report results in the restricted CoNLL-2014 shared task setting using publicly-available training datasets (_Restricted_) and those that made use of large non-public datasets (_Unrestricted_).


| Model           | F0.5  |  Paper / Source | Code |
| ------------- | :-----:| --- | :-----: |
|_**Restricted**_     |      
| CNN Seq2Seq + Quality Estimation (Chollampatt & Ng, EMNLP 2018) | 56.52 | [Neural Quality Estimation of Grammatical Error Correction](http://aclweb.org/anthology/D18-1274) | |
| SMT + BiGRU (Grundkiewicz et al., 2018) |  56.25 | [Near Human-Level Performance in Grammatical Error Correction with Hybrid Machine Translation](https://arxiv.org/abs/1804.05945)| NA |
| Transformer (Junczys-Dowmunt et al., 2018) | 55.8 | [Approaching Neural Grammatical Error Correction as a Low-Resource Machine Translation Task](http://aclweb.org/anthology/N18-1055)| NA |
| CNN Seq2Seq (Chollampatt & Ng, 2018)| 54.79 | [ A Multilayer Convolutional Encoder-Decoder Neural Network for Grammatical Error Correction](https://arxiv.org/abs/1801.08831)| [Official](https://github.com/nusnlp/mlconvgec2018) |
|_**Unrestricted**_            |
| CNN Seq2Seq + Fluency Boost (Ge et al., 2018) |  61.34 | [Reaching Human-level Performance in Automatic Grammatical Error Correction: An Empirical Study](https://arxiv.org/abs/1807.01270)| NA |

### CoNLL-2014 10 Annotations

[Bryant and Ng, 2015](https://pdfs.semanticscholar.org/f76f/fd242c3dc88e52d1f427cdd0f5dccd814937.pdf) released 8 additional annotations (in addition to the two official annotations) for the CoNLL-2014 shared task test set (http://www.comp.nus.edu.sg/~nlp/sw/10gec_annotations.zip).

| Model           | F0.5  |  Paper / Source | Code |
| ------------- | :-----:| --- | :-----: |
|_**Restricted**_     |           
| SMT + BiGRU (Grundkiewicz et al., 2018) |  72.04 | [Near Human-Level Performance in Grammatical Error Correction with Hybrid Machine Translation](https://arxiv.org/abs/1804.05945)| NA |
| CNN Seq2Seq (Chollampatt & Ng, 2018)| 70.14 (measured by Ge et al., 2018) | [ A Multilayer Convolutional Encoder-Decoder Neural Network for Grammatical Error Correction](https://arxiv.org/abs/1801.08831)| [Official](https://github.com/nusnlp/mlconvgec2018) |
|_**Unrestricted**_            |
| CNN Seq2Seq + Fluency Boost (Ge et al., 2018) |  76.88 | [Reaching Human-level Performance in Automatic Grammatical Error Correction: An Empirical Study](https://arxiv.org/abs/1807.01270)| NA |


### JFLEG

[JFLEG corpus](https://github.com/keisks/jfleg) by [Napoles et al., 2017](https://arxiv.org/abs/1702.04066) consists of 1,511 english sentences with annotations. Models are evaluated with [GLEU metric](https://arxiv.org/abs/1609.08144).

| Model           | GLEU  |  Paper / Source | Code |
| ------------- | :-----:| --- | :-----: |
|_**Restricted**_     |           
| SMT + BiGRU (Grundkiewicz et al., 2018) |  61.50 | [Near Human-Level Performance in Grammatical Error Correction with Hybrid Machine Translation](https://arxiv.org/abs/1804.05945)| NA |
| Transformer (Junczys-Dowmunt et al., 2018) | 59.9 | [Approaching Neural Grammatical Error Correction as a Low-Resource Machine Translation Task](http://aclweb.org/anthology/N18-1055)| NA |
| CNN Seq2Seq (Chollampatt & Ng, 2018)| 57.47 | [ A Multilayer Convolutional Encoder-Decoder Neural Network for Grammatical Error Correction](https://arxiv.org/abs/1801.08831)| [Official](https://github.com/nusnlp/mlconvgec2018) |
|_**Unrestricted**_           |
| CNN Seq2Seq + Fluency Boost and inference (Ge et al., 2018) |  62.37 | [Reaching Human-level Performance in Automatic Grammatical Error Correction: An Empirical Study](https://arxiv.org/abs/1807.01270)| NA |

