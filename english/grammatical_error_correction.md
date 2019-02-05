# Grammatical Error Correction

Grammatical Error Correction (GEC) is the task of correcting different kinds of errors in text such as spelling, punctuation, grammatical, and word choice errors. 

GEC is typically formulated as a sentence correction task. A GEC system takes a potentially erroneous sentence as input and is expected to transform it to its corrected version. See the example given below: 

| Input (Erroneous)          | Output (Corrected)     |
| -------------------------  | ---------------------- |
|She see Tom is catched by policeman in park at last night. | She saw Tom caught by a policeman in the park last night.|

### CoNLL-2014 Shared Task

The [CoNLL-2014 shared task test set](https://www.comp.nus.edu.sg/~nlp/conll14st/conll14st-test-data.tar.gz) is the most widely used dataset to benchmark GEC systems. The test set contains 1,312 English sentences with error annotations by 2 expert annotators. Models are evaluated with MaxMatch scorer ([Dahlmeier and Ng, 2012](http://www.aclweb.org/anthology/N12-1067)) which computes a span-based F<sub>β</sub>-score (β set to 0.5 to weight precision twice as recall).

The shared task setting restricts that systems use only publicly available datasets for training to ensure a fair comparison between systems. The highest published scores on the the CoNLL-2014 test set are given below. A distinction is made between papers that report results in the restricted CoNLL-2014 shared task setting of training using publicly-available training datasets only (_**Restricted**_) and those that made use of large, non-public datasets (_**Unrestricted**_).

**Restricted**:

| Model           | F0.5  |  Paper / Source | Code |
| ------------- | :-----:| --- | :-----: |
| CNN Seq2Seq + Quality Estimation (Chollampatt and Ng, EMNLP 2018) | 56.52 | [Neural Quality Estimation of Grammatical Error Correction](http://aclweb.org/anthology/D18-1274) | [Official](https://github.com/nusnlp/neuqe/) |
| SMT + BiGRU (Grundkiewicz and Junczys-Dowmunt, 2018) |  56.25 | [Near Human-Level Performance in Grammatical Error Correction with Hybrid Machine Translation](http://aclweb.org/anthology/N18-2046)| NA |
| Transformer (Junczys-Dowmunt et al., 2018) | 55.8 | [Approaching Neural Grammatical Error Correction as a Low-Resource Machine Translation Task](http://aclweb.org/anthology/N18-1055)| [Official](https://github.com/grammatical/neural-naacl2018) |
| CNN Seq2Seq (Chollampatt and Ng, 2018)| 54.79 | [A Multilayer Convolutional Encoder-Decoder Neural Network for Grammatical Error Correction](https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewFile/17308/16137)| [Official](https://github.com/nusnlp/mlconvgec2018) |

**Unrestricted**:

| Model           | F0.5  |  Paper / Source | Code |
| ------------- | :-----:| --- | :-----: |
| CNN Seq2Seq + Fluency Boost (Ge et al., 2018) |  61.34 | [Reaching Human-level Performance in Automatic Grammatical Error Correction: An Empirical Study](https://arxiv.org/pdf/1807.01270.pdf)| NA |

_**Restricted**_: uses only publicly available datasets. _**Unrestricted**_: uses non-public datasets.


### CoNLL-2014 10 Annotations

[Bryant and Ng, 2015](http://aclweb.org/anthology/P15-1068) released 8 additional annotations (in addition to the two official annotations) for the CoNLL-2014 shared task test set ([link](http://www.comp.nus.edu.sg/~nlp/sw/10gec_annotations.zip)).

**Restricted**:

| Model           | F0.5  |  Paper / Source | Code |
| ------------- | :-----:| --- | :-----: |
| SMT + BiGRU (Grundkiewicz and Junczys-Dowmunt, 2018) |  72.04 | [Near Human-Level Performance in Grammatical Error Correction with Hybrid Machine Translation](http://aclweb.org/anthology/N18-2046)| NA |
| CNN Seq2Seq (Chollampatt and Ng, 2018)| 70.14 (measured by Ge et al., 2018) | [ A Multilayer Convolutional Encoder-Decoder Neural Network for Grammatical Error Correction](https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewFile/17308/16137)| [Official](https://github.com/nusnlp/mlconvgec2018) |

**Unrestricted**:

| Model           | F0.5  |  Paper / Source | Code |
| ------------- | :-----:| --- | :-----: |
| CNN Seq2Seq + Fluency Boost (Ge et al., 2018) |  76.88 | [Reaching Human-level Performance in Automatic Grammatical Error Correction: An Empirical Study](https://arxiv.org/pdf/1807.01270.pdf)| NA |

_**Restricted**_: uses only publicly available datasets. _**Unrestricted**_: uses non-public datasets.


### JFLEG

[JFLEG test set](https://github.com/keisks/jfleg) released by [Napoles et al., 2017](http://aclweb.org/anthology/E17-2037) consists of 747 English sentences with 4 references for each sentence. Models are evaluated with [GLEU](https://github.com/cnap/gec-ranking/) metric ([Napoles et al., 2016](https://arxiv.org/pdf/1605.02592.pdf)).


**Restricted**:  

| Model           | GLEU  |  Paper / Source | Code |
| ------------- | :-----:| --- | :-----: |
| SMT + BiGRU (Grundkiewicz and Junczys-Dowmunt, 2018) |  61.50 | [Near Human-Level Performance in Grammatical Error Correction with Hybrid Machine Translation](http://aclweb.org/anthology/N18-2046)| NA |
| Transformer (Junczys-Dowmunt et al., 2018) | 59.9 | [Approaching Neural Grammatical Error Correction as a Low-Resource Machine Translation Task](http://aclweb.org/anthology/N18-1055)| NA |
| CNN Seq2Seq (Chollampatt and Ng, 2018)| 57.47 | [ A Multilayer Convolutional Encoder-Decoder Neural Network for Grammatical Error Correction](https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewFile/17308/16137)| [Official](https://github.com/nusnlp/mlconvgec2018) |


**Unrestricted**:

| Model           | GLEU  |  Paper / Source | Code |
| ------------- | :-----:| --- | :-----: |
| CNN Seq2Seq + Fluency Boost and inference (Ge et al., 2018) |  62.37 | [Reaching Human-level Performance in Automatic Grammatical Error Correction: An Empirical Study](https://arxiv.org/pdf/1807.01270.pdf)| NA |

_**Restricted**_: uses only publicly available datasets. _**Unrestricted**_: uses non-public datasets.


