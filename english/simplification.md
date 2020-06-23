# Simplification

Simplification consists of modifying the content and structure of a text in order to make it easier to read and understand, while preserving its main idea and approximating its original meaning. A simplified version of a text could benefit low literacy readers, English learners, children, and people with aphasia, dyslexia or autism. Also, simplifying a text automatically could improve performance on other NLP tasks, such as parsing, summarisation, information extraction, semantic role labeling, and machine translation.

## Sentence Simplification

Research on automatic simplification has been traditionally limited to executing transformations at the sentence-level. What should we expect from a sentence simplificatin model? Let's take a look at how humans simplify (from [here](http://videolectures.net/esslli2011_lapata_simplification/)):

| Original Sentence   | Simplified   Sentence |
| ---------------------------------- | ---------------------------------- |
| Owls are the order Strigiformes, comprising 200 bird of prey species. | An owl is a bird. There are about 200 kinds of owls. |
| Owls hunt mostly small mammals, insects, and other birds though some species specialize in hunting fish. | Owls’ prey may be birds, large insects (such as crickets), small reptiles (such as lizards) or small mammals (such as mice, rats, and rabbits). |

Notice the simplification transformations performed: 

- Unusual concepts are explained: insects *(such as crickets)*, small reptiles *(such as lizards)* or small mammals *(such as mice, rats, and rabbits)*. 

- Uncommon words are replaced with a more familiar term or phrase: "comprising" &rarr; "There are about".

- Syntactic structures are changed by a simpler pattern. For example, the first sentence is split into two.

- Some *unimportant* information is removed: the clause "though some species specialize in hunting fish" in the second sentence does not appear in its simplified version. 

When the set of transformations is limited to replacing a word or phrase by a simpler synonym, we are dealing with *Lexical Simplification* (an overview of that area can be found [here](https://www.jair.org/index.php/jair/article/view/11091/26278)). In this section, we consider research that attempts to develop models that learn as many text transformations as possible.

### Evaluation

The ideal method for determining the quality of a simplification is through human evaluation. Traditionally, a simplified output is judged in terms of *grammaticality* (or fluency), *meaning preservation* (or adequacy) and *simplicity*, using Likert scales (1-3 or 1-5) . **Warning:** Are these criteria (at the sentence level) the most appropriate for assessing a simplified sentence? It has been suggested [(Siddharthan, 2014)](https://www.jbe-platform.com/content/journals/10.1075/itl.165.2.06sid) that a task-oriented evaluation (e.g. through reading comprehension tests [(Angrosh et al., 2014)](http://aclweb.org/anthology/C14-1188)) could be more informative of the usefulness of the generated simplification. However, this is not general practice.

For tuning and comparing models, the most commonly-used automatic metrics are:

- **BLEU** [(Papineni et al., 2012)](https://aclweb.org/anthology/P02-1040), borrowed from Machine Translation. This metric is not one without [problems](https://towardsdatascience.com/evaluating-text-output-in-nlp-bleu-at-your-own-risk-e8609665a213) for different text generation tasks. However, simplification studies ([Stajner et al., 2014](http://aclweb.org/anthology/W14-1201); [Wubben et al., 2012](http://aclweb.org/anthology/P12-1107); [Xu et al., 2016](http://aclweb.org/anthology/Q16-1029)) have shown that it correlates with human judgments of grammaticality and meaning preservation. BLEU is not well suited, though, for assessing simplicity from a lexical [(Xu et al., 2016)](http://aclweb.org/anthology/Q16-1029) nor a structural [(Sulem et al., 2018b)](http://aclweb.org/anthology/D18-1081) point of view.
- **SARI** [(Xu et al., 2016)](http://aclweb.org/anthology/Q16-1029) is a *lexical simplicity* metric that measures "how good" are the words added, deleted and kept by a simplification model. The metric compares the model's output to *multiple simplification references* and the original sentence. SARI has shown high correlation with human judgements of simplicity gain [(Xu et al., 2016)](http://aclweb.org/anthology/Q16-1029). Currently, this is the main metric used for evaluating sentence simplification models.

The previous two metrics will be used to rank the models in the following sections. Despite popular practice, we refrain from using **Flesch Reading Ease** or **Flesch-Kincaid Grade Level**. Because of the way these metrics are [computed](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests), short sentences could get good scores, even if they are ungrammatical or non-meaning preserving [(Wubben et al., 2012)](http://aclweb.org/anthology/P12-1107), resulting in a missleading ranking. 

Since a simplification could involve text transformations beyond paraphrasing (which SARI intends to assess).  For these cases, it could be more suitable to use **SAMSA** [(Sulem et al., 2018a)](http://aclweb.org/anthology/N18-1063), a metric designed to measure *structural simplicity* (i.e. sentence splitting). However, it has not been used in papers besides the one where it was introduced (yet).

**EASSE:** [Alva-Manchego et al. (2019)](https://www.aclweb.org/anthology/D19-3009) released a [tool](https://github.com/feralvam/easse) that provides easy access to all of the above metrics (and several others) through the command line and as a python package. EASSE also contains commonly-used test sets for the task. Its aim is to help standarise automatic evaluation for sentence simplification.

**IMPORTANT NOTE:** In the tables of the following sections, a score with a \* means that it was not reported by the original authors but by future research that re-implemented and/or re-trained and re-tested the model. In these cases, the original reported score (if there is one) is shown in parentheses. 

### Main - Simple English Wikipedia

[Simple English Wikipedia](https://simple.wikipedia.org) is an online encyclopedia aimed at English learners. Its articles are expected to contain fewer words and simpler grammar structures than those in their [Main English Wikipedia](https://en.wikipedia.org) counterpart. Much of the popularity of using Wikipedia for research in Simplification comes from publicly available sentence alignments between “equivalent” articles in Main and Simple English Wikipedia. 

#### PWKP / WikiSmall

[Zu et al. (2010)](http://aclweb.org/anthology/C10-1152) compiled a parallel corpus with more than 108K sentence pairs from 65,133 Wikipedia articles, allowing **1-to-1 and 1-to-N alignments**. The latter type of alignments represents instances of sentence splitting. The original full corpus can be found [here](https://www.informatik.tu-darmstadt.de/ukp/research_6/data/sentence_simplification/simple_complex_sentence_pairs/index.en.jsp). The test set is composed of 100 instances, with **one simplification reference per original sentence**. [Zhang and Lapata (2017)](http://aclweb.org/anthology/D17-1062) released a more standardised split of this dataset called [*WikiSmall*](https://github.com/XingxingZhang/dress), with 89,042 instances for training, 205 for development and the same original 100 instances for testing. 

We present the models tested in this dataset **ranked by BLEU score** (or SARI if BLEU is not available). SARI cannot be reliably computed in this dataset since it does not contain multiple simplification references per original sentence. In addition, there are instances of more advanced simplification transformations (e.g. splitting) which SARI does not assess by definition.

| Model           | BLEU | SARI | Paper / Source | Code |
| --------------- | :-----: | :-----: | -------------- | ---- |
| EditNTS (Dong et al., 2019) |  | 32.35 | [EditNTS: An Neural Programmer-Interpreter Model for Sentence Simplification through Explicit Editing](https://www.aclweb.org/anthology/P19-1331) | [Official](https://github.com/yuedongP/EditNTS) |
| SeqLabel (Alva-Manchego et al., 2017) |  | 30.50\* | [Learning How to Simplify From Explicit Labeling of Complex-Simplified Text Pairs](https://www.aclweb.org/anthology/I17-1030) | |
| Hybrid (Narayan and Gardent, 2014) | 53.94\* (53.6) | 30.46\* | [Hybrid Simplification using Deep Semantics and Machine Translation](http://aclweb.org/anthology/P/P14/P14-1041.pdf) | [Official](https://github.com/shashiongithub/Sentence-Simplification-ACL14) |
| NSELSTM-B (Vu et al., 2018) | 53.42 | 17.47 | [Sentence Simplification with Memory-Augmented Neural Networks](http://aclweb.org/anthology/N18-2013) |  |
| PBMT-R (Wubben et al., 2012) | 46.31\* (43.0) | 15.97\* | [Sentence Simplification by Monolingual Machine Translation](http://aclweb.org/anthology/P12-1107) |  |
| RevILP (Woodsend and Lapata, 2011) | 42.0 | | [Learning to Simplify Sentences with Quasi-Synchronous Grammar and Integer Programming](http://aclweb.org/anthology/D11-1038) |  |
| UNSUP (Narayan and Gardent, 2016) | 38.47 | | [Unsupervised Sentence Simplification Using Deep Semantics](http://aclweb.org/anthology/W16-6620) |  |
| TSM (Zhu et al., 2010) | 38.0 | | [A Monolingual Tree-based Translation Model for Sentence Simplification](http://aclweb.org/anthology/C10-1152) |  |
| DRESS-LS (Zhang and Lapata, 2017) | 36.32 | 27.24 | [Sentence Simplification with Deep Reinforcement Learning](http://aclweb.org/anthology/D17-1062) | [Official](https://github.com/XingxingZhang/dress) |
| DRESS (Zhang and Lapata, 2017) | 34.53 | 27.48 | [Sentence Simplification with Deep Reinforcement Learning](http://aclweb.org/anthology/D17-1062) | [Official](https://github.com/XingxingZhang/dress) |
| NSELSTM-S (Vu et al., 2018) | 29.72 | 29.75 | [Sentence Simplification with Memory-Augmented Neural Networks](http://aclweb.org/anthology/N18-2013) |  |
| Pointer + Multi-task Entailment and Paraphrase Generation (Guo et al., 2018) | 27.23 | 29.58 | [Dynamic Multi-Level Multi-Task Learning for Sentence Simplification](http://aclweb.org/anthology/C18-1039) | [Official](https://github.com/HanGuo97/MultitaskSimplification) |

#### Coster and Kauchack (2011)

[Coster and Kauchack (2011)](http://aclweb.org/anthology/P11-2117) automatically aligned 137K sentence pairs from 10K Wikipedia articles, considering **1-to-1 and 1-to-N alignments**, with **one simplification reference per original sentence**. The corpus was split into 124K instances for training, 12K for development, and 1.3K for testing. The dataset is available [here](http://www.cs.pomona.edu/~dkauchak/simplification/). As before, models tested in this dataset are **ranked by BLEU score** and not SARI.

| Model           | BLEU | SARI | Paper / Source | Code |
| --------------- | :-----: | :-----: | -------------- | ---- |
| Moses-Del (Coster and Kauchak, 2011b) | 60.46 |      | [Learning to Simplify Sentences Using Wikipedia](http://aclweb.org/anthology/W11-1601) |  |
| Moses (Coster and Kauchak, 2011a) | 59.87 | |[Simple English Wikipedia: A New Text Simplification Task](http://aclweb.org/anthology/P11-2117)  |  |
| SimpleTT (Feblowitz and Kauchak, 2013) | 56.4 | | [Sentence Simplification as Tree Transduction](aclweb.org/anthology/W13-2901) |  |
| PBMT-R (Wubben et al., 2012) | 54.3\* |      | [Sentence Simplification by Monolingual Machine Translation](http://aclweb.org/anthology/P12-1107) |  |

#### Turk Corpus

Together with defining SARI, [Xu et al. (2016)](http://aclweb.org/anthology/Q16-1029) released a dataset properly collected to calculate this simplicity metric: **1-to-1 alignments** focused on paraphrasing transformations (extracted from PWKP), and **multiple (8) simplification references per original sentence** (collected through Amazon Mechanical Turk). The  [dataset](https://github.com/cocoxu/simplification/) contains 2,350 sentences split into 2,000 instances for tuning and 350 for testing. For training, most models use [*WikiLarge*](https://github.com/XingxingZhang/dress), which was compiled by [Zhang and Lapata (2017)](http://aclweb.org/anthology/D17-1062) using alignments from other Wikipedia-based datasets ([Zhu et al., 2010](http://aclweb.org/anthology/C10-1152); [Woodsend and Lapata, 2011](http://aclweb.org/anthology/D11-1038); [Kauchak, 2013](http://aclweb.org/anthology/P13-1151)), and contains 296K instances of not only 1-to-1 alignments. 

We present the models tested in this dataset **ranked by SARI score**.

| Model           | BLEU | SARI | Paper / Source | Code |
| --------------- | :-----: | :-----: | -------------- | ---- |
| ACCESS (Martin et al., 2019) | 72.53 | 41.87  | [Controllable Sentence Simplification](https://arxiv.org/abs/1910.02677) | [Official](https://github.com/facebookresearch/access) |
| DMASS + DCSS (Zhao et al., 2018) |  | 40.45 | [Integrating Transformer and Paraphrase Rules for Sentence Simplification](http://aclweb.org/anthology/D18-1355) | [Official](https://github.com/Sanqiang/text_simplification) |
| SBSMT + PPDB + SARI (Xu et al, 2016) | 73.08\* (72.36) | 39.96\* (37.91) | [Optimizing Statistical Machine Translation for Text Simplification](http://aclweb.org/anthology/Q16-1029) | [Official](https://github.com/cocoxu/simplification/) |
| PBMT-R (Wubben et al., 2012) | 81.11\* | 38.56\* | [Sentence Simplification by Monolingual Machine Translation](http://aclweb.org/anthology/P12-1107) |  |
| EditNTS (Dong et al., 2019) | 86.69 | 38.22 | [EditNTS: An Neural Programmer-Interpreter Model for Sentence Simplification through Explicit Editing](https://www.aclweb.org/anthology/P19-1331) | [Official](https://github.com/yuedongP/EditNTS) |
| Edit-Unsup-TS (Kumar et al., 2020) | 73.62 | 37.85 | [Iterative Edit-Based Unsupervised Sentence Simplification](https://www.aclweb.org/anthology/2020.acl-main.707.pdf) | [Official](https://github.com/ddhruvkr/Edit-Unsup-TS) |
| Pointer + Multi-task Entailment and Paraphrase Generation (Guo et al., 2018) | 81.49 | 37.45 | [Dynamic Multi-Level Multi-Task Learning for Sentence Simplification](http://aclweb.org/anthology/C18-1039) | [Official](https://github.com/HanGuo97/MultitaskSimplification) |
| NTS + SARI (Nisioi et al., 2017) | 80.69 | 37.25 | [Exploring Neural Text Simplification Models](http://aclweb.org/anthology/P17-2014) | [Official](https://github.com/senisioi/NeuralTextSimplification) |
| DRESS-LS (Zhang and Lapata, 2017) | 80.12 | 37.27 | [Sentence Simplification with Deep Reinforcement Learning](http://aclweb.org/anthology/D17-1062) | [Official](https://github.com/XingxingZhang/dress) |
| UnsupNTS (Surya et al., 2019) | 74.02 | 37.20| [Unsupervised Neural Text Simplification](https://www.aclweb.org/anthology/P19-1198) | [Official](https://github.com/subramanyamdvss/UnsupNTS) |
| DRESS (Zhang and Lapata, 2017) | 77.18 | 37.08 | [Sentence Simplification with Deep Reinforcement Learning](http://aclweb.org/anthology/D17-1062) | [Official](https://github.com/XingxingZhang/dress) |
| SeqLabel (Alva-Manchego et al., 2017) |  | 37.08\* | [Learning How to Simplify From Explicit Labeling of Complex-Simplified Text Pairs](https://www.aclweb.org/anthology/I17-1030) | |
| NSELSTM-S (Vu et al., 2018) | 80.43 | 36.88 | [Sentence Simplification with Memory-Augmented Neural Networks](http://aclweb.org/anthology/N18-2013) |  |
| SEMoses (Sulem et al., 2018)                                 |      74.49       |     36.70      | [Simple and Effective Text Simplification Using Semantic and Neural Methods](http://aclweb.org/anthology/P18-1016) | [Official](https://github.com/eliorsulem/simplification-acl2018) |
| NSELSTM-B (Vu et al., 2018) | 92.02 | 33.43 | [Sentence Simplification with Memory-Augmented Neural Networks](http://aclweb.org/anthology/N18-2013) | |
| Hybrid (Narayan and Gardent, 2014) | 48.97\* | 31.40\* | [Hybrid Simplification using Deep Semantics and Machine Translation](http://aclweb.org/anthology/P/P14/P14-1041.pdf) | [Official](https://github.com/shashiongithub/Sentence-Simplification-ACL14) |

#### Other Datasets

[Hwang et al. (2015)](http://aclweb.org/anthology/N15-1022) released a [dataset](http://ssli.ee.washington.edu/tial/projects/simplification/) of 392K instances, while [Kajiwara and Komachi (2016)](http://aclweb.org/anthology/C16-1109) collected the [sscorpus](https://github.com/tmu-nlp/sscorpus) of 493K instances, also from Main - Simple English Wikipedia article pairs. Both datasets contain only **1-to-1 alignments** with **one simplification reference per original sentence**. Despite their bigger sizes and the more sophisticated sentence alignment algorithms used to collect them, these datasets are not commonly used in simplification research.

### Newsela

[Xu et al. (2015)](http://aclweb.org/anthology/Q15-1021) introduced the Newsela corpus, which contains 1,130 news articles with four simplification versions each. The original article is considered version 0, and each simplification version goes from 1 to 4 (the highest being the simplest). These simplifications were produced manually by professional editors, considering children of different grade levels as target audience. Through manual evaluation on a subset of the data, [Xu et al. (2015)](http://aclweb.org/anthology/Q15-1021) showed that there is a better presence and distribution of simplification transformations in Newsela than in PWKP. 

The dataset can be requested [here](https://newsela.com/data/). However, researchers are not allowed to publicly shared splits of the data. This is not ideal for proper reproducibility and comparison among models.

#### Splits by Zhang and Lapata (2017)

[Xu et al. (2015)](http://aclweb.org/anthology/Q15-1021) generated sentence alignments between all versions of each article in the Newsela corpus. [Zhang and Lapata (2017)](http://aclweb.org/anthology/D17-1062) imply that they used those alignments but removed some sentence pairs that are "too similar". In the end, they used a dataset composed of 94,208 instances for training, 1,129 instances for development, and 1,076 instances for testing. Their test set, in particular, contains only **1-to-1 alignments** with **one simplification reference per original sentence**.

Using their splits, [Zhang and Lapata (2017)](http://aclweb.org/anthology/D17-1062) trained and tested several models, which we include in our ranking. Other research that claims to have used the same dataset splits is also considered. Despite not being the ideal scenario, the models tested in this dataset are commonly **ranked by SARI score**.

| Model           | BLEU | SARI | Paper / Source | Code |
| --------------- | :-----: | :-----: | -------------- | ---- |
| Pointer + Multi-task Entailment and Paraphrase Generation (Guo et al., 2018) | 11.14 | 33.22 | [Dynamic Multi-Level Multi-Task Learning for Sentence Simplification](http://aclweb.org/anthology/C18-1039) | [Official](https://github.com/HanGuo97/MultitaskSimplification) |
|S2S-Cluster-FA (Kriz et al., 2019) | 19.55 | 30.73 | [Complexity-Weighted Loss and Diverse Reranking for Sentence Simplification](https://www.aclweb.org/anthology/N19-1317) | [Official](https://github.com/rekriz11/sockeye-recipes) |
| Edit-Unsup-TS (Kumar et al., 2020) | 17.36 | 30.44 | [Iterative Edit-Based Unsupervised Sentence Simplification](https://www.aclweb.org/anthology/2020.acl-main.707.pdf) | [Official](https://github.com/ddhruvkr/Edit-Unsup-TS) |
| EditNTS (Dong et al., 2019) | 19.85 | 30.27 | [EditNTS: An Neural Programmer-Interpreter Model for Sentence Simplification through Explicit Editing](https://www.aclweb.org/anthology/P19-1331) | [Official](https://github.com/yuedongP/EditNTS) |
| NSELSTM-S (Vu et al., 2018) | 22.62 | 29.58 | [Sentence Simplification with Memory-Augmented Neural Networks](http://aclweb.org/anthology/N18-2013) | |
| SeqLabel (Alva-Manchego et al., 2017) |  | 29.53\* | [Learning How to Simplify From Explicit Labeling of Complex-Simplified Text Pairs](https://www.aclweb.org/anthology/I17-1030) | |
| Hybrid (Narayan and Gardent, 2014) | 14.46\* | 28.61\* | [Hybrid Simplification using Deep Semantics and Machine Translation](http://aclweb.org/anthology/P/P14/P14-1041.pdf) | [Official](https://github.com/shashiongithub/Sentence-Simplification-ACL14) |
| NSELSTM-B (Vu et al., 2018) | 26.31 | 27.42 | [Sentence Simplification with Memory-Augmented Neural Networks](http://aclweb.org/anthology/N18-2013) | |
| DRESS (Zhang and Lapata, 2017) | 23.21 | 27.37 | [Sentence Simplification with Deep Reinforcement Learning](http://aclweb.org/anthology/D17-1062) | [Official](https://github.com/XingxingZhang/dress) |
| DMASS + DCSS (Zhao et al., 2018) |  | 27.28 | [Integrating Transformer and Paraphrase Rules for Sentence Simplification](http://aclweb.org/anthology/D18-1355) | [Official](https://github.com/Sanqiang/text_simplification) |
| DRESS-LS (Zhang and Lapata, 2017) | 24.30 | 26.63 | [Sentence Simplification with Deep Reinforcement Learning](http://aclweb.org/anthology/D17-1062) | [Official](https://github.com/XingxingZhang/dress) |
| PBMT-R (Wubben et al., 2012) | 18.19\* | 15.77\* | [Sentence Simplification by Monolingual Machine Translation](http://aclweb.org/anthology/P12-1107) |  |

As mentioned before, a big disadvantage of the Newsela corpus is that a unique train/dev/test split of the data is not (cannot be made?) publicly available. In addition, due to its characteristics, it is not clear what should be the best way to generate sentence alignments and split the data:

-  [Zhang and Lapata (2017)](http://aclweb.org/anthology/D17-1062) removed sentences from version pairs 0–1, 1–2, and 2–3 because they are "too similar to each other". This could prevent the model from learning when a sentence should not be simplified. In addition, their test set only considers 1-to-1 sentence alignments, even though it is possible to generate 1-to-N and N-to-1 sentence pairs as shown by other researchers ([Scarton et al., 2018](http://aclweb.org/anthology/L18-1553); [Stajner et al., 2018](http://aclweb.org/anthology/L18-1615)).
- [Alva-Manchego et al. (2017)](http://aclweb.org/anthology/I17-1030), [Scarton et al. (2018)](http://aclweb.org/anthology/L18-1553), and [Stajner and Nisioi (2018)](http://www.aclweb.org/anthology/L18-1479) generate sentence alignments (using different algorithms) only between adjacent article versions (i.e. 0-1, 1-2, 2-3, and 3-4). Meanwhile, [Scarton and Specia (2018)](http://aclweb.org/anthology/P18-2113) generate alignments between all versions (i.e., 0-{1,2,3,4}, 1-{2,3,4}, 2-{3,4}, and 3-4). The assumption behind using only adjacent versions is that, to write an article's simplification, an editor takes the immediately previous simplified version as basis (i.e. 0&rarr;1, 1&rarr;2, etc.). However, since the simplification manual followed by the Newsela editors is not public, it is not possible to corroborate that hypothesis.



[Go back to the README](../README.md)
