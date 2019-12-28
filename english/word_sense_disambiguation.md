# Word Sense Disambiguation

The task of Word Sense Disambiguation (WSD) consists of associating words in context with their most suitable entry in a pre-defined sense inventory. The de-facto sense inventory for English in WSD is [WordNet](https://wordnet.princeton.edu).
For example, given the word “mouse” and the following sentence:

“A mouse consists of an object held in one's hand, with one or more buttons.” 

we would assign “mouse”  with its electronic device sense ([the 4th sense in the WordNet sense inventory](http://wordnetweb.princeton.edu/perl/webwn?c=8&sub=Change&o2=&o0=1&o8=1&o1=1&o7=&o5=&o9=&o6=&o3=&o4=&i=-1&h=000000&s=mouse)).


### Fine-grained WSD:

The [Evaluation framework](http://lcl.uniroma1.it/wsdeval/) of [Raganato et al. 2017](http://aclweb.org/anthology/E/E17/E17-1010.pdf) [1] includes two training sets (SemCor-Miller et al., 1993- and OMSTI-Taghipour and Ng, 2015-) and five test sets from the Senseval/SemEval series (Edmonds and Cotton, 2001; Snyder and Palmer, 2004; Pradhan et al., 2007; Navigli et al., 2013; Moro and Navigli, 2015), standardized to the same format and sense inventory (i.e. WordNet 3.0).

Typically, there are two kinds of approach for WSD: supervised (which make use of sense-annotated training data) and knowledge-based (which make use of the properties of lexical resources).

Supervised: The most widely used training corpus used is SemCor, with 226,036 sense annotations from 352 documents manually annotated. All supervised systems in the evaluation table are trained on SemCor. Some supervised methods, particularly neural architectures, usually employ the SemEval 2007 dataset as development set (marked by *). The most usual baseline is the Most Frequent Sense (MFS) heuristic, which selects for each target word the most frequent sense in the training data.

Knowledge-based:  Knowledge-based systems usually exploit WordNet or [BabelNet](https://babelnet.org/) as semantic network. The first sense given by the underlying sense inventory (i.e. WordNet 3.0) is included as a baseline.

The main evaluation measure is F1-score.


### Supervised:

| Model           | Senseval 2  |Senseval 3  |SemEval 2007 |SemEval 2013 |SemEval 2015 | Paper / Source |
| ------------- | :-----:|:-----:|:-----:|:-----:|:-----:| --- |
|MFS baseline | 65.6 | 66.0 | 54.5 | 63.8 | 67.1 |  [[1]](http://aclweb.org/anthology/E/E17/E17-1010.pdf) |
|Bi-LSTM<sub>att+LEX</sub> |  72.0 | 69.4 |63.7* | 66.4 | 72.4 | [[2]](http://aclweb.org/anthology/D17-1120) |
|Bi-LSTM<sub>att+LEX+POS</sub> |   72.0 | 69.1|64.8* | 66.9 | 71.5 | [[2]](http://aclweb.org/anthology/D17-1120) |
|context2vec | 71.8 | 69.1 |61.3  | 65.6 | 71.9 | [[3]](http://www.aclweb.org/anthology/K16-1006) | 
|ELMo | 71.6 | 69.6 | 62.2 | 66.2 | 71.3 | [[4]](http://aclweb.org/anthology/N18-1202) |
|GAS (Linear) | 72.0  | 70.0 | --* | 66.7 | 71.6 | [[5]](http://aclweb.org/anthology/P18-1230) |
|GAS (Concatenation) | 72.1 | 70.2 | --* | 67 | 71.8 |  [[5]](http://aclweb.org/anthology/P18-1230)  |
|GAS<sub>ext</sub> (Linear) | 72.4 | 70.1 | --* | 67.1 | 72.1 |[[5]](http://aclweb.org/anthology/P18-1230)  |
|GAS<sub>ext</sub> (Concatenation) | 72.2 | 70.5 | --* | 67.2 | 72.6 | [[5]](http://aclweb.org/anthology/P18-1230)  |
|supWSD | 71.3 | 68.8 | 60.2 | 65.8 | 70.0 | [[6]](https://aclanthology.info/pdf/P/P10/P10-4014.pdf) [[11]](http://aclweb.org/anthology/D17-2018) |
|supWSD<sub>emb</sub> | 72.7 | 70.6 | 63.1 | 66.8 | 71.8 | [[7]](http://www.aclweb.org/anthology/P16-1085) [[11]](http://aclweb.org/anthology/D17-2018) |
|BERT (nearest neighbor) | 73.8 | 71.6 | 64.0 | 69.2 | 74.4 | [[13]](https://arxiv.org/pdf/1910.00194.pdf) [[code]](https://github.com/nusnlp/contextemb-wsd) |
|BERT (linear projection) | 76.4 | 74.0 | 69.3 | 71.1 | 76.2 | [[13]](https://arxiv.org/pdf/1910.00194.pdf) [[code]](https://github.com/nusnlp/contextemb-wsd) |
|GlossBERT | 77.7 | 75.2 | 72.5 | 76.1 | 80.4 | [[14]](https://arxiv.org/pdf/1908.07245.pdf) |
|SemCor+WNGC, hypernyms | 79.7 | 77.8 | 73.4 | 78.7 | 82.6 | [[15]](https://arxiv.org/abs/1905.05677) |


### Knowledge-based:

| Model           | All | Senseval 2 |Senseval 3 |SemEval 2007 |SemEval 2013 |SemEval 2015 |  Paper / Source |
| ------------- | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | --- |
|WN 1st sense baseline | 65.2 | 66.8 | 66.2 | 55.2 | 63.0 | 67.8 | [[1]](http://aclweb.org/anthology/E/E17/E17-1010.pdf) |
|Babelfy | 65.5 | 67.0 | 63.5 | 51.6 | 66.4 | **70.3** | [[8]](http://aclweb.org/anthology/Q14-1019) |
|UKB<sub>ppr_w2w-nf</sub> | 57.5 | 64.2 | 54.8 | 40.0 | 64.5 | 64.5 | [[9]](https://www.mitpressjournals.org/doi/full/10.1162/COLI_a_00164) [[12]](http://aclweb.org/anthology/W18-2505) |
|UKB<sub>ppr_w2w</sub> | **67.3** | 68.8 | 66.1 | 53.0 | **68.8** | **70.3** | [[9]](https://www.mitpressjournals.org/doi/full/10.1162/COLI_a_00164) [[12]](http://aclweb.org/anthology/W18-2505) |
|WSD-TM | 66.9 | **69.0** | **66.9** | **55.6** | 65.3 | 69.6 | [[10]](https://arxiv.org/pdf/1801.01900.pdf) |

Note: 'All' is the concatenation of all datasets, as described in [10] and [12]. The scores of [6,7] and [9] are not taken from the original papers but from the results of the implementations of [11] and [12], respectively.

[1] [Word Sense Disambiguation: A Unified Evaluation Framework and Empirical Comparison](http://aclweb.org/anthology/E/E17/E17-1010.pdf)

[2] [Neural Sequence Learning Models for Word Sense Disambiguation](http://aclweb.org/anthology/D17-1120)

[3] [context2vec: Learning generic context embedding with bidirectional lstm](http://www.aclweb.org/anthology/K16-1006)

[4] [Deep contextualized word representations](http://aclweb.org/anthology/N18-1202)

[5] [Incorporating Glosses into Neural Word Sense Disambiguation](http://aclweb.org/anthology/P18-1230)

[6] [It makes sense: A wide-coverage word sense disambiguation system for free text](https://aclanthology.info/pdf/P/P10/P10-4014.pdf)

[7] [Embeddings for Word Sense Disambiguation: An Evaluation Study](http://www.aclweb.org/anthology/P16-1085)

[8] [Entity Linking meets Word Sense Disambiguation: A Unified Approach](http://aclweb.org/anthology/Q14-1019)

[9] [Random walks for knowledge-based word sense disambiguation](https://www.mitpressjournals.org/doi/full/10.1162/COLI_a_00164)

[10] [Knowledge-based Word Sense Disambiguation using Topic Models](https://arxiv.org/pdf/1801.01900.pdf)

[11] [SupWSD: A Flexible Toolkit for Supervised Word Sense Disambiguation](http://aclweb.org/anthology/D17-2018)

[12] [The risk of sub-optimal use of Open Source NLP Software: UKB is inadvertently state-of-the-art in knowledge-based WSD](http://aclweb.org/anthology/W18-2505)

[13] [Improved Word Sense Disambiguation Using Pre-Trained Contextualized Word Representations](https://arxiv.org/pdf/1910.00194.pdf)

[14] [GlossBERT: BERT for Word Sense Disambiguation with Gloss Knowledge](https://arxiv.org/pdf/1908.07245.pdf)

[15] [Sense Vocabulary Compression through the Semantic Knowledge of WordNet for Neural Word Sense Disambiguation](https://arxiv.org/abs/1905.05677)

## Word Sense Induction

Word sense induction (WSI) is widely known as the "unsupervised version" of WSD. The problem states as: Given a target word (e.g., "cold") and a collection of sentences (e.g., "I caught a cold", "The weather is cold") that use the word, cluster the sentences according to their different senses/meanings. We do not need to know the sense/meaning of each cluster, but sentences inside a cluster should have used the target words with the same sense.

There are two widely used datasets: SemEval 2010 and 2013, and both of them use different kinds of metrices: V-Measure (V-M) and paired F-Score (F-S) for SemEval 2010, and fuzzy B-Cubed (F-BC) and fuzzy normalized mutual information (F-NMI). For ease of system comparisons, the metrics are usually aggregated using a geometric mean (AVG).

### SemEval 2010

| Model         | F-S    | V-M   | AVG   | Paper/source | Code |
| ------------- | :-----:|:-----:|:-----:| ------------ | ---- |
| BERT+DP (Amrami and Goldberg, 2019) | 71.3 | 40.4 | 53.6 | [Towards better substitution-based word sense induction](https://arxiv.org/pdf/1905.12598.pdf) | [Code](https://github.com/asafamr/bertwsi) |
| AutoSense (Amplayo et al., 2019) | 61.7 | 9.8 | 24.59 | [AutoSense Model for Word Sense Induction](https://wvvw.aaai.org/ojs/index.php/AAAI/article/view/4580/4458) | [Code](https://github.com/rktamplayo/AutoSense) |
| SE-WSI-fix (Song et al., 2016) | 55.1 | 9.8 | 23.24 | [Sense Embedding Learning for Word Sense Induction](https://aclweb.org/anthology/S16-2009/) |  |
| BNP-HC (Chang et al., 2014) | 23.1 | 21.4 | 22.23 | [Inducing Word Sense with Automatically Learned Hidden Concepts](https://www.aclweb.org/anthology/C14-1035/) |  |
| LDA (Goyal and Hovy, 2014) | 60.7 | 4.4 | 16.34 | [Unsupervised Word Sense Induction using Distributional Statistics](https://www.aclweb.org/anthology/C14-1123/) |  |

### SemEval 2013

| Model         | F-BC    | F_NMI   | AVG   | Paper/source | Code |
| ------------- | :-----:|:-----:|:-----:| ------------ | ---- |
| BERT+DP (Amrami and Goldberg, 2019) | 64.0 | 21.4 | 37.0 | [Towards better substitution-based word sense induction](https://arxiv.org/pdf/1905.12598.pdf) | [Code](https://github.com/asafamr/bertwsi) |
| LSDP (Amrami and Goldberg, 2018) | 57.5 | 11.3 | 25.4 | [Word Sense Induction with Neural biLM and Symmetric Patterns](https://www.aclweb.org/anthology/D18-1523/) | [Code](https://github.com/asafamr/SymPatternWSI) |
| AutoSense (Amplayo et al., 2019) | 61.7 | 7.96 | 22.16 | [AutoSense Model for Word Sense Induction](https://wvvw.aaai.org/ojs/index.php/AAAI/article/view/4580/4458) | [Code](https://github.com/rktamplayo/AutoSense) |
| MCC-S (Komninos and Manandhar, 2016) | 55.6 | 7.62 | 20.58 | [Structured Generative Models of Continuous Features for Word Sense Induction](https://www.aclweb.org/anthology/C16-1337/) |  |
| STM+w2v (Wang et al., 2016) | 55.4 | 7.14 | 19.89 | [A Sense-Topic Model for Word Sense Induction with Unsupervised Data Enrichment](https://www.aclweb.org/anthology/Q15-1005/) |  |
| AI-KU (Baskaya et al., 2013) | 39.0 | 6.5 | 15.92 | [AI-KU: Using Substitute Vectors and Co-Occurrence Modeling For Word Sense Induction and Disambiguation](https://www.aclweb.org/anthology/S13-2050/) |  |
