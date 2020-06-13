# Data-to-Text Generation

**Data-to-Text Generation (D2T NLG)** can be described as Natural Language Generation from structured input.
<!-- is a task of NLG where the **textual output** is generated using **structured input** (such as tables or graphs). -->
Unlike Machine Translation or Question Answering tasks (also referred as **Text-to-Text Generation, or T2T NLG**) where requirement is to generate textual output using some unstructured textual input only, here the input will be provided in a structured format such as tables or knowledge graphs <sup>[[1]](#myfootnote1)</sup>.

## RotoWire
The [dataset](https://github.com/harvardnlp/boxscore-data/blob/master/rotowire.tar.bz2) consists of articles summarizing NBA basketball games, paired with their corresponding box- and line-score tables. It is professionally written, medium length game summaries targeted at fantasy basketball fans. The writing is colloquial, but structured, and targets an audience primarily interested in game statistics <sup>[[2]](#myfootnote2)</sup>.

The performance is evaluated on two different automated metrics: first, **BLEU** score; and second, a family of **Extractive Evaluation (EE)**. EE contains three different metrics evaluating three different aspects of the generation:

1. **Content Selection (CS)**: precision (P%) and recall (R%) of unique relations extracted from generated text that are also extracted from golden text. This measures how well the generated document matches the gold document in terms of selecting which records to generate.

2. **Relation Generation (RG)**: precision (P%) and number of unique relations (#) extracted from generated text that also appear in structured input provided. This measures how well the system is able to generate text containing factual (i.e., correct) records.

3. **Content Ordering (CO)**: normalized Damerau-Levenshtein Distance (DLD%) between the sequences of records extracted from golden text and that extracted from generated text. This measures how well the system orders the records it chooses to discuss.

| Model           | BLEU | CS (P% & R%) | RG (P% & #) | CO (DLD%) |  Paper / Source | Code |
| ------------- | :-----: | :-----: | :-----: | :-----:| --- | --- |
| Wiseman et al. (2017)<sup>[[2]](#myfootnote2)</sup> | 14.49 | 22.17 & 27.16 | 71.82 & 12.82 | 8.68 | [Challenges in Data-to-Document Generation](https://www.aclweb.org/anthology/D17-1239.pdf) |[Official](https://github.com/harvardnlp/data2text) |
| Puduppully et al. (2019)<sup>[[3]](#myfootnote3)</sup> | 16.50 | 34.18 & 51.22 | 87.47 & 34.28 | 18.58 | [Data-to-text generation with content selection and planning](https://arxiv.org/pdf/1809.00582.pdf) |[Official](https://github.com/ratishsp/data2text-plan-py) |
| Rebuffel, Clément, et al. (2020)<sup>[[4]](#myfootnote4)</sup> | 17.50 | 39.47 & 51.64 | 89.46 & 21.17 | 18.90 | [A Hierarchical Model for Data-to-Text Generation](https://link.springer.com/chapter/10.1007/978-3-030-45439-5_5) |[Official](https://github.com/KaijuML/data-to-text-hierarchical) |

## WebNLG
The [WebNLG challenge](https://webnlg-challenge.loria.fr/) consists in mapping data to text. The training data consists of Data/Text pairs where the data is a set of triples extracted from DBpedia and the text is a verbalisation of these triples. For example, given the three DBpedia triples (as shown in [a]), the aim is to generate a text (as shown in [b]):

[a]. (John_E_Blaha birthDate 1942_08_26) (John_E_Blaha birthPlace San_Antonio) (John_E_Blaha occupation Fighter_pilot)
[b]. John E Blaha, born in San Antonio on 1942-08-26, worked as a fighter pilot.

The performance is evaluated based on BLEU, METEOR and TER scores. 
<!-- The test-set is also divided into two broad groups: **seen (S)**, test samples from the *categories present in training set*; and **unseen (U)**, test samples from *categories not-present in training set*. -->

<!-- | Model           | BLEU (S & U) | METEOR (S & U) | TER (S & U) |  Paper / Source | Code | -->
| Model           | BLEU | METEOR | TER |  Paper / Source | Code |
| ------------- | :-----: | :-----: | :-----: | --- | --- |
| Baseline System | 33.24 | 0.235436 | 0.613080 | [Baseline](https://webnlg-challenge.loria.fr/challenge_2017/#webnlg-baseline-system) |[Official](https://gitlab.com/webnlg/webnlg-baseline) |
| Moryossef et al. (2019) <sup>[[5]](#myfootnote5)</sup> | 47.4 | 0.391 | 0.631 | [Step-by-Step: Separating Planning from Realization in Neural Data-to-Text Generation](https://www.aclweb.org/anthology/N19-1236.pdf) | [Official](https://github.com/AmitMY/chimera) |
<!-- | Baseline System | 52.39 & 6.13 | 37.7 & 07.53 | 44.86 & 80.0 | [Baseline](https://webnlg-challenge.loria.fr/challenge_2017/#webnlg-baseline-system) |[Official](https://gitlab.com/webnlg/webnlg-baseline) | -->
<!-- | Distiawan, Bayu, et al. (2018) | 58.6 & 34.1 | 40.6 & 32.0 | 41.7 & 57.9 | [GTR-LSTM: A Triple Encoder for Sentence Generation from RDF Data](https://www.aclweb.org/anthology/P18-1151.pdf) | | -->


## E2E Challenge

## WikiBio 

## References
<a name="myfootnote1">[1]</a> Albert Gatt and Emiel Krahmer. 2018. Survey of the state of the art in natural language generation: core tasks, applications and evaluation. J. Artif. Int. Res. 61, 1 (January 2018), 65–170.

<a name="myfootnote2">[2]</a> Wiseman, Sam, Stuart M. Shieber, and Alexander M. Rush. "Challenges in Data-to-Document Generation." Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing. 2017.

<a name="myfootnote3">[3]</a> Puduppully, Ratish, Li Dong, and Mirella Lapata. "Data-to-text generation with content selection and planning." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 33. 2019.

<a name="myfootnote4">[4]</a> Rebuffel, Clément, et al. "A Hierarchical Model for Data-to-Text Generation." European Conference on Information Retrieval. Springer, Cham, 2020.

<a name="myfootnote5">[5]</a> Moryossef, Amit, Yoav Goldberg, and Ido Dagan. "Step-by-Step: Separating Planning from Realization in Neural Data-to-Text Generation." Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers). 2019.