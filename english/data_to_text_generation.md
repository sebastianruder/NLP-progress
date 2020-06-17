# Data-to-Text Generation

**Data-to-Text Generation (D2T NLG)** can be described as Natural Language Generation from structured input.
<!-- is a task of NLG where the **textual output** is generated using **structured input** (such as tables or graphs). -->
Unlike other NLG tasks such as, Machine Translation or Question Answering (also referred as **Text-to-Text Generation or T2T NLG**) where requirement is to generate textual output using some unstructured textual input, in D2T NLG the requirement is to generate textual output from the input provided in a structured format such as: tables; or knowledge graphs; or JSONs <sup>[[1]](#myfootnote1)</sup>.

## RotoWire
The [dataset](https://github.com/harvardnlp/boxscore-data/blob/master/rotowire.tar.bz2) consists of articles summarizing NBA basketball games, paired with their corresponding box- and line-score tables. It is professionally written, medium length game summaries targeted at fantasy basketball fans. The writing is colloquial, but structured, and targets an audience primarily interested in game statistics <sup>[[2]](#myfootnote2)</sup>.

The performance is evaluated on two different automated metrics: first, **BLEU score**; and second, a family of **Extractive Evaluations (EE)**. EE contains three different submetrics evaluating three different aspects of the generation:

1. **Content Selection (CS)**: precision (P%) and recall (R%) of unique relations extracted from generated text that are also extracted from golden text. This measures how well the generated document matches the gold document in terms of selecting which records to generate.

2. **Relation Generation (RG)**: precision (P%) and number of unique relations (#) extracted from generated text that also appear in structured input provided. This measures how well the system is able to generate text containing factual (i.e., correct) records.

3. **Content Ordering (CO)**: normalized Damerau-Levenshtein Distance (DLD%) between the sequences of records extracted from golden text and that extracted from generated text. This measures how well the system orders the records it chooses to discuss.

| Model           | BLEU | CS (P% & R%) | RG (P% & #) | CO (DLD%) |  Paper / Source | Code |
| ------------- | :-----: | :-----: | :-----: | :-----:| --- | --- |
| Rebuffel, Clément, et al. (2020)<sup>[[4]](#myfootnote4)</sup> | 17.50 | 39.47 & 51.64 | 89.46 & 21.17 | 18.90 | [A Hierarchical Model for Data-to-Text Generation](https://link.springer.com/chapter/10.1007/978-3-030-45439-5_5) |[Official](https://github.com/KaijuML/data-to-text-hierarchical) |
| Puduppully et al. (2019)<sup>[[3]](#myfootnote3)</sup> | 16.50 | 34.18 & 51.22 | 87.47 & 34.28 | 18.58 | [Data-to-text generation with content selection and planning](https://www.aaai.org/ojs/index.php/AAAI/article/view/4668) |[Official](https://github.com/ratishsp/data2text-plan-py) |
| Wiseman et al. (2017)<sup>[[2]](#myfootnote2)</sup> | 14.49 | 22.17 & 27.16 | 71.82 & 12.82 | 8.68 | [Challenges in Data-to-Document Generation](https://www.aclweb.org/anthology/D17-1239.pdf) |[Official](https://github.com/harvardnlp/data2text) |

## WebNLG
The [WebNLG challenge](https://webnlg-challenge.loria.fr/) consists in mapping data to text. The training data consists of Data/Text pairs where the data is a set of triples extracted from DBpedia and the text is a verbalisation of these triples. For example, given the three DBpedia triples (as shown in [a]), the aim is to generate a text (as shown in [b]):

* **[a]**. (John_E_Blaha birthDate 1942_08_26) (John_E_Blaha birthPlace San_Antonio) (John_E_Blaha occupation Fighter_pilot)

* **[b]**. John E Blaha, born in San Antonio on 1942-08-26, worked as a fighter pilot.

The performance is evaluated on the basis of **BLEU, METEOR and TER scores**. The data from WebNLG Challenge 2017 can be downloaded [here](https://gitlab.com/shimorina/webnlg-dataset).
<!-- The test-set is also divided into two broad groups: **seen (S)**, test samples from the *categories present in training set*; and **unseen (U)**, test samples from *categories not-present in training set*. -->

<!-- | Model           | BLEU (S & U) | METEOR (S & U) | TER (S & U) |  Paper / Source | Code | -->
| Model           | BLEU | METEOR | TER |  Paper / Source | Code |
| ------------- | :-----: | :-----: | :-----: | --- | --- |
| Kale, Mihir. (2020) <sup>[[9]](#myfootnote9)</sup> | 57.1 | 0.44 |  | [Text-to-Text Pre-Training for Data-to-Text Tasks](https://arxiv.org/pdf/2005.10433v2.pdf) |  |
| Moryossef et al. (2019) <sup>[[5]](#myfootnote5)</sup> | 47.4 | 0.391 | 0.631 | [Step-by-Step: Separating Planning from Realization in Neural Data-to-Text Generation](https://www.aclweb.org/anthology/N19-1236.pdf) | [Official](https://github.com/AmitMY/chimera) |
| Baseline | 33.24 | 0.235436 | 0.613080 | [Baseline system provided during the challenge](https://webnlg-challenge.loria.fr/challenge_2017/#webnlg-baseline-system) |[Official](https://gitlab.com/webnlg/webnlg-baseline) |
<!-- | Baseline System | 52.39 & 6.13 | 37.7 & 07.53 | 44.86 & 80.0 | [Baseline](https://webnlg-challenge.loria.fr/challenge_2017/#webnlg-baseline-system) |[Official](https://gitlab.com/webnlg/webnlg-baseline) | -->
<!-- | Distiawan, Bayu, et al. (2018) | 58.6 & 34.1 | 40.6 & 32.0 | 41.7 & 57.9 | [GTR-LSTM: A Triple Encoder for Sentence Generation from RDF Data](https://www.aclweb.org/anthology/P18-1151.pdf) | | -->

**P.S.**: The **test dataset** of WebNLG consists of **total 15 categories**, out of which 10 (**seen**) catgories are used for training while 5 (**unseen**) are not. The results reported here are those obtained on overall test data, i.e., all 15 categories.

## Meaning Representations

The dataset was first provided for the [E2E Challenge](http://www.macs.hw.ac.uk/InteractionLab/E2E/) in 2017. It is a crowd-sourced data set of 50k instances in the restaurant domain.Each instance consist of a dialogue act-based meaning representations (MR) and up to 5 references in natural language (NL). For example:

* **MR**: name[The Eagle], eatType[coffee shop], food[French], priceRange[moderate], customerRating[3/5], area[riverside], kidsFriendly[yes], near[Burger King]

* **NL**: “The three star coffee shop, The Eagle, gives families a mid-priced dining experience featuring a variety of wines and cheeses. Find The Eagle near Burger King.”

The performance is evaluated using **BLEU, NIST, METEOR, ROUGE-L, CIDEr scores**. The data from E2E Challenge 2017 can be downloaded [here](https://github.com/tuetschek/e2e-dataset/releases/download/v1.0.0/e2e-dataset.zip).

| Model           | BLEU | NIST | METEOR | ROUGE-L | CIDEr |  Paper / Source | Code |
| ------------- | :-----: | :-----: |:-----: |:-----: | :-----: | --- | --- |
| Shen, Sheng, et al. (2019) <sup>[[7]](#myfootnote6)</sup> | 68.60 | 8.73 | 45.25 | 70.82 | 2.37 | [Pragmatically Informative Text Generation](https://www.aclweb.org/anthology/N19-1410.pdf) |[Official](https://github.com/sIncerass/prag_generation) |
| Elder, Henry, et al. (2019) <sup>[[8]](#myfootnote8)</sup> | 67.38 | 8.7277 | 45.72 | 71.52 | 2.2995 | [Designing a Symbolic Intermediate Representation for Neural Surface Realization](https://www.aclweb.org/anthology/W19-2308.pdf) | |
| Gehrmann, Sebastian, et al. (2018) <sup>[[6]](#myfootnote7)</sup> | 66.2 | 8.60 | 45.7 | 70.4 | 2.34 | [End-to-End Content and Plan Selection for Data-to-Text Generation](https://www.aclweb.org/anthology/W18-6505.pdf) |[Official](https://github.com/sebastianGehrmann/diverse_ensembling) |
| Baseline | 65.93 | 8.61 | 44.83 | 68.50 | 2.23 | [Baseline system provided during the challenge](http://www.macs.hw.ac.uk/InteractionLab/E2E/#baseline) |[Official](https://github.com/UFAL-DSG/tgen/tree/master/e2e-challenge) |

<!-- ## WikiBio  -->

## References
<a name="myfootnote1">[1]</a> Albert Gatt and Emiel Krahmer. 2018. [Survey of the state of the art in natural language generation: core tasks, applications and evaluation](https://www.jair.org/index.php/jair/article/download/11173/26378/). J. Artif. Int. Res. 61, 1 (January 2018), 65–170.

<a name="myfootnote2">[2]</a> Wiseman, Sam, Stuart M. Shieber, and Alexander M. Rush. "[Challenges in Data-to-Document Generation](https://www.aclweb.org/anthology/D17-1239.pdf)." Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing. 2017.

<a name="myfootnote3">[3]</a> Puduppully, Ratish, Li Dong, and Mirella Lapata. "[Data-to-text generation with content selection and planning](https://www.aaai.org/ojs/index.php/AAAI/article/view/4668)." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 33. 2019.

<a name="myfootnote4">[4]</a> Rebuffel, Clément, et al. "[A Hierarchical Model for Data-to-Text Generation](https://link.springer.com/chapter/10.1007/978-3-030-45439-5_5)." European Conference on Information Retrieval. Springer, Cham, 2020.

<a name="myfootnote5">[5]</a> Moryossef, Amit, Yoav Goldberg, and Ido Dagan. "[Step-by-Step: Separating Planning from Realization in Neural Data-to-Text Generation](https://www.aclweb.org/anthology/N19-1236.pdf)." Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers). 2019.

<a name="myfootnote6">[6]</a> Gehrmann, Sebastian, et al. "[End-to-End Content and Plan Selection for Data-to-Text Generation](https://www.aclweb.org/anthology/W18-6505.pdf)." Proceedings of the 11th International Conference on Natural Language Generation. 2018.

<a name="myfootnote7">[7]</a> Shen, Sheng, et al. "[Pragmatically Informative Text Generation](https://www.aclweb.org/anthology/N19-1410.pdf)." Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers). 2019.

<a name="myfootnote8">[8]</a> Elder, Henry, et al. "[Designing a Symbolic Intermediate Representation for Neural Surface Realization](https://www.aclweb.org/anthology/W19-2308.pdf)." Proceedings of the Workshop on Methods for Optimizing and Evaluating Neural Language Generation. 2019.

<a name="myfootnote9">[9]</a> Kale, Mihir. "[Text-to-Text Pre-Training for Data-to-Text Tasks](https://arxiv.org/pdf/2005.10433v2.pdf)" arXiv preprint arXiv:2005.10433 (2020).

[Go back to the README](../README.md)
