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
| Transformer + Pre-train with Pseudo Data (Kiyono et al., EMNLP 2019) | 65.0 | [An Empirical Study of Incorporating Pseudo Data into Grammatical Error Correction](https://arxiv.org/abs/1909.00502) | NA |
| Copy-Augmented Transformer + Pre-train (Zhao and Wang, NAACL 2019) | 61.15 | [Improving Grammatical Error Correction via Pre-Training a Copy-Augmented Architecture with Unlabeled Data](https://arxiv.org/pdf/1903.00138.pdf) | [Official](https://github.com/zhawe01/fairseq-gec) |
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
| CNN Seq2Seq + Fluency Boost and inference (Ge et al., 2018) |  62.42 | [Reaching Human-level Performance in Automatic Grammatical Error Correction: An Empirical Study](https://arxiv.org/pdf/1807.01270.pdf)| NA |

_**Restricted**_: uses only publicly available datasets. _**Unrestricted**_: uses non-public datasets.


### BEA Shared Task - 2019
[BEA shared task - 2019 dataset](https://www.cl.cam.ac.uk/research/nl/bea2019st/) released for the BEA Shared Task on Grammatical Error Correction provides a newer and bigger dataset for evaluating GEC models in 3 tracks, based on the datasets used for training:
- [Restricted track](https://competitions.codalab.org/competitions/20228)
- [Unrestricted track](https://competitions.codalab.org/competitions/20229)
- [Low-resource track](https://competitions.codalab.org/competitions/20230)   


Training and dev sets are released publicly and a GEC model's performance is evaluated by F-0.5 score. The model outputs on the test-set have to be uploaded to Codalab(publicly available) where category-wise error metrics are displayed. The test set consists of 4477 sentences(larger and diverse than the CoNLL-14 dataset) and the outputs are scored via [ERRANT](https://github.com/chrisjbryant/errant) toolkit. The released data are collected from 2 sources: 
  - Write & Improve, an online web platform that assists non-native English students with their writing.
  - LOCNESS, a corpus consisting of essays written by native English students.   



The description of tracks from the BEA [site](https://www.cl.cam.ac.uk/research/nl/bea2019st/#tracks) is given below:   


_**Restricted Track:**_
In the restricted track, participants may only use the following learner datasets:
  - FCE (Yannakoudakis et al., 2011)
  - Lang-8 Corpus of Learner English (Mizumoto et al., 2011; Tajiri et al., 2012)
  - NUCLE (Dahlmeier et al., 2013)
  - W&I+LOCNESS (Bryant et al., 2019; Granger, 1998)   
Note that we restrict participants to the preprocessed Lang-8 Corpus of Learner English rather than the raw, multilingual Lang-8 Learner Corpus because participants would otherwise need to filter the raw corpus themselves. We also do not allow the use of the CoNLL 2013/2014 shared task test sets in this track.   


_**Unrestricted Track:**_
In the unrestricted track, participants may use anything and everything to build their systems. This includes proprietary datasets and software.   


_**Low Resource Track (formerly Unsupervised Track):**_
In the low resource track, participants may only use the following learner dataset: W&I+LOCNESS development set.   

Since current state-of-the-art systems rely on as much annotated learner data as possible to reach the best performance, the goal of the low resource track is to encourage research into systems that do not rely on large amounts of learner data. This track should be of particular interest to researchers working on GEC for languages where large learner corpora do not exist.   


### Results on WI-LOCNESS test set:
**Restricted track**:

| Model           | F0.5  |  Paper / Source | Code |
| ------------- | :-----:| --- | :-----: |
| BEA Combination | 73.18 | [Learning to Combine Grammatical Error Corrections ](https://www.aclweb.org/anthology/W19-4414/) | NA |
| Transformer + Pre-train with Pseudo Data (Kiyono et al., EMNLP 2019) | 70.2 | [An Empirical Study of Incorporating Pseudo Data into Grammatical Error Correction](https://arxiv.org/abs/1909.00502) | NA |
| Transformer | 69.47  | [Neural Grammatical Error Correction Systems with UnsupervisedPre-training on Synthetic Data](https://www.aclweb.org/anthology/W19-4427)| [Official: Code to be updated soon](https://github.com/grammatical/pretraining-bea2019) |
| Transformer | 69.00  | [A Neural Grammatical Error Correction System Built OnBetter Pre-training and Sequential Transfer Learning](https://www.aclweb.org/anthology/W19-4423)| [Official](https://github.com/kakaobrain/helo_word/) |
| Ensemble of models | 66.78  | [The LAIX Systems in the BEA-2019 GEC Shared Task](https://www.aclweb.org/anthology/W19-4416)| NA |

**Low-resource track**:

| Model           | F0.5  |  Paper / Source | Code |
| ------------- | :-----:| --- | :-----: |
| Transformer | 64.24  | [Neural Grammatical Error Correction Systems with UnsupervisedPre-training on Synthetic Data](https://www.aclweb.org/anthology/W19-4427)| [Official: Code to be updated soon](https://github.com/grammatical/pretraining-bea2019) |
| Transformer | 58.80  | [A Neural Grammatical Error Correction System Built OnBetter Pre-training and Sequential Transfer Learning](https://www.aclweb.org/anthology/W19-4423)| [Official](https://github.com/kakaobrain/helo_word/) |
| Ensemble of models | 51.81  | [The LAIX Systems in the BEA-2019 GEC Shared Task](https://www.aclweb.org/anthology/W19-4416)| NA |

 
 **Reference**:
 - Helen Yannakoudakis, Ekaterina Kochmar, Claudia Leacock, Nitin Madnani, Ildikó Pilán, Torsten Zesch, in [Proceedings of the Fourteenth Workshop on Innovative Use of NLP for Building Educational Applications](https://www.aclweb.org/anthology/W19-44)
 - Christopher Bryant, Mariano Felice, and Ted Briscoe. 2017. Automatic annotation and evaluation of Error Types for Grammatical Error Correction. In Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). Vancouver, Canada.
