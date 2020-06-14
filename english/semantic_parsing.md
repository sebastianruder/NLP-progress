# Semantic parsing

### Table of contents

- [AMR parsing](#amr-parsing)
  - [LDC2014T12](#ldc2014t12)
  - [LDC2015E86](#ldc2015e86)
  - [LDC2016E25](#ldc2016e25)
- [UCCA parsing](#ucca-parsing)
  - [SemEval 2019 Task 1](semeval-2019-task-1)
  - [CoNLL 2019](conll-2019)
- [SQL parsing](#sql-parsing)
  - [ATIS](#atis)
  - [Advising](#advising)
  - [GeoQuery](#geoquery)
  - [Scholar](#scholar)
  - [Spider](#spider)
  - [WikiSQL](#wikisql)
  - [Smaller datasets](#smaller-datasets)

Semantic parsing is the task of translating natural language into a formal meaning
representation on which a machine can act. Representations may be an executable language
such as SQL or more abstract representations such as [Abstract Meaning Representation (AMR)](https://en.wikipedia.org/wiki/Abstract_Meaning_Representation)
and [Universal Conceptual Cognitive Annotation (UCCA)](http://www.cs.huji.ac.il/~oabend/ucca.html).

## AMR parsing

Each AMR is a single rooted, directed graph. AMRs include PropBank semantic roles, within-sentence coreference, named entities and types, modality, negation, questions, quantities, and so on. [See](https://amr.isi.edu/index.html).
In the following tables, systems marked with &hearts; are pipeline systems that require POS as input,
&spades; is for those require NER,
&diams; is for those require syntax parsing,
and &clubs; is for those require SRL.

### LDC2014T12: 
13,051 sentences

Models are evaluated on the newswire section and the full dataset based on [smatch](https://amr.isi.edu/smatch-13.pdf).

| Model           | F1 Newswire  | F1 Full |  Paper / Source |
| ------------- | :-----:| :-----:| --- |
| AMR Parsing via Graph-Sequence Iterative Inference (Cai and Lam , 2020)&hearts;&spades; | -- | 75.4 | [AMR Parsing via Graph-Sequence Iterative Inference](https://arxiv.org/pdf/2004.05572.pdf) |
| Broad-Coverage Semantic Parsing as Transduction (Zhang et al., 2019)&hearts; | -- | 71.3 | [Broad-Coverage Semantic Parsing as Transduction](https://www.aclweb.org/anthology/D19-1392.pdf) |
| Two-stage Sequence-to-Graph Transducer (Zhang et al., 2019)&hearts; | -- | 70.2 | [AMR Parsing as Sequence-to-Graph Transduction](https://www.aclweb.org/anthology/P19-1009.pdf) |
| Transition-based+improved aligner+ensemble (Liu et al. 2018)&hearts; | 73.3 | 68.4 | [An AMR Aligner Tuned by Transition-based Parser](http://aclweb.org/anthology/D18-1264) |
| Improved CAMR (Wang and Xue, 2017)&spades;&diams; | --| 68.1| [Getting the Most out of AMR Parsing](http://aclweb.org/anthology/D17-1129) |
| Incremental joint model (Zhou et al., 2016)&hearts;&spades; | 71 | 66 | [AMR Parsing with an Incremental Joint Model](https://aclweb.org/anthology/D16-1065) |
| Transition-based transducer (Wang et al., 2015)&hearts;&diams;&clubs; | 70 | 66 | [Boosting Transition-based AMR Parsing with Refined Actions and Auxiliary Analyzers](http://www.aclweb.org/anthology/P15-2141) |
| Imitation learning  (Goodman et al., 2016)&hearts;&spades; | 70 |  -- | [Noise reduction and targeted exploration in imitation learning for Abstract Meaning Representation parsing](http://www.aclweb.org/anthology/P16-1001) |
| MT-Based (Pust et al., 2015)&spades; | -- | 66 | [Parsing English into Abstract Meaning Representation Using Syntax-Based Machine Translation ](http://www.aclweb.org/anthology/D15-1136)
| Transition-based parser-Stack-LSTM (Ballesteros and Al-Onaizan, 2017)&hearts;&diams; | 69 | 64  | [AMR Parsing using Stack-LSTMs](http://www.aclweb.org/anthology/D17-1130) |
| Transition-based parser-Stack-LSTM (Ballesteros and Al-Onaizan, 2017) | 68 | 63  | [AMR Parsing using Stack-LSTMs](http://www.aclweb.org/anthology/D17-1130) |

### LDC2015E86: 
19,572 sentences

Models are evaluated based on [smatch](https://amr.isi.edu/smatch-13.pdf).

| Model           | Smatch  |  Paper / Source |
| ------------- | :-----:| --- |
| Joint model (Lyu and Titov, 2018)&hearts;&spades; | 73.7 | [AMR Parsing as Graph Prediction with Latent Alignment](https://arxiv.org/abs/1805.05286) |
| Mul-BiLSTM (Foland and Martin, 2017)&spades; | 70.7 | [Abstract Meaning Representation Parsing using LSTM Recurrent Neural Networks](http://aclweb.org/anthology/P17-1043) |
| JAMR (Flanigan et al., 2016)&hearts;&diams;&clubs; | 67.0 | [CMU at SemEval-2016 Task 8: Graph-based AMR Parsing with Infinite Ramp Loss](http://www.aclweb.org/anthology/S16-1186) |
| CAMR (Wang et al., 2016)&hearts;&diams;&clubs; | 66.5 | [CAMR at SemEval-2016 Task 8: An Extended Transition-based AMR Parser](http://www.aclweb.org/anthology/S16-1181) |
| AMREager (Damonte et al., 2017)&hearts;&spades;&diams; | 64.0 | [An Incremental Parser for Abstract Meaning Representation](http://www.aclweb.org/anthology/E17-1051) |
| SEQ2SEQ + 20M (Konstas et al., 2017)&spades; | 62.1 | [Neural AMR: Sequence-to-Sequence Models for Parsing and Generation](https://arxiv.org/abs/1704.08381) |

### LDC2016E25
39,260 sentences

Models are evaluated based on [smatch](https://amr.isi.edu/smatch-13.pdf).

| Model           | Smatch  |  Paper / Source |
| ------------- | :-----:| --- |
| AMR Parsing via Graph-Sequence Iterative Inference (Cai and Lam, 2020)&hearts;&spades; | 80.2 | [AMR Parsing via Graph-Sequence Iterative Inference](https://arxiv.org/pdf/2004.05572.pdf) |
| Broad-Coverage Semantic Parsing as Transduction (Zhang et al., 2019)&hearts; | 77.0 | [Broad-Coverage Semantic Parsing as Transduction](https://www.aclweb.org/anthology/D19-1392.pdf) |
| Two-stage Sequence-to-Graph Transducer (Zhang et al., 2019)&hearts; | 76.3 | [AMR Parsing as Sequence-to-Graph Transduction](https://www.aclweb.org/anthology/P19-1009.pdf) |
| Rewarding Smatch: Transition-Based AMR Parsing with Reinforcement Learning (Naseem et al., 2019)&hearts;&spades;&diams; | 75.5 | [Rewarding Smatch: Transition-Based AMR Parsing with Reinforcement Learning](https://arxiv.org/pdf/1905.13370) |
| Joint model (Lyu and Titov, 2018)&hearts;&spades; | 74.4 | [AMR Parsing as Graph Prediction with Latent Alignment](https://arxiv.org/abs/1805.05286) |
| Rewarding Smatch: Transition-Based AMR Parsing with Reinforcement Learning (Naseem et al., 2019); | 73.4 | [Rewarding Smatch: Transition-Based AMR Parsing with Reinforcement Learning](https://arxiv.org/pdf/1905.13370) |
| Core Semantic First: A Top-down Approach for AMR Parsing (Cai and Lam, 2019)&hearts;&spades; | 73.2 | [Core Semantic First: A Top-down Approach for AMR Parsing](https://www.aclweb.org/anthology/D19-1393.pdf) |
| ChSeq + 100K (van Noord and Bos, 2017)&hearts; | 71.0 | [Neural Semantic Parsing by Character-based Translation: Experiments with Abstract Meaning Representations](https://arxiv.org/abs/1705.09980) |
| Neural-Pointer (Buys and Blunsom, 2017)&hearts;&spades; | 61.9 | [Oxford at SemEval-2017 Task 9: Neural AMR Parsing with Pointer-Augmented Attention](http://aclweb.org/anthology/S17-2157) |

## UCCA parsing

UCCA ([Abend and Rappoport, 2013](https://www.aclweb.org/anthology/P13-1023.pdf))
is a semantic representation whose main design principles
are ease of annotation, cross-linguistic applicability, and a modular architecture. UCCA represents
the semantics of linguistic utterances as directed acyclic graphs (DAGs), where terminal (childless)
nodes correspond to the text tokens, and non-terminal nodes to semantic units that participate in
some super-ordinate relation. Edges are labeled,
indicating the role of a child in the relation the parent represents.
UCCA's foundational layer mostly covers predicate-argument structure,
semantic heads and inter-Scene relations.
UCCA distinguishes primary edges, corresponding to explicit relations, from remote edges
that allow for a unit to participate in several super-ordinate relations.
Primary edges form a tree in each layer, whereas remote edges enable reentrancy, forming a DAG.

Evaluation is done by labeled F1 on the graph edges, matched by child terminal yield.

### [SemEval 2019 Task 1](https://www.aclweb.org/anthology/S19-2001.pdf)

Open and closed tracks on English, French and German [UCCA corpora](https://github.com/UniversalConceptualCognitiveAnnotation) from Wikipedia and *Twenty Thousand Leagues Under the Sea*.
Results for the English open track data are given here, with 5,141 training sentences.

| Model | English-Wiki (open) F1 | English-20K (open) F1 | Paper / Source | Code |
| ------| :--------------------: | :-------------------: | -------------- | ---- |
| Constituent Tree Parsing + BERT (Jiang et al., 2019) | 80.5 | 76.7 | [HLT@SUDA at SemEval-2019 Task 1: UCCA Graph Parsing as Constituent Tree Parsing](https://www.aclweb.org/anthology/S19-2002/) | https://github.com/SUDA-LA/ucca-parser |
| Neural Transducer (Zhang et al., 2019) | 76.6 | -- | [Broad-Coverage Semantic Parsing as Transduction](https://www.aclweb.org/anthology/D19-1392.pdf) | https://github.com/sheng-z/stog |
| Transition-based + MTL (Hershcovich et al., 2018) | 73.5 | 68.4 | [Multitask Parsing Across Semantic Representations](https://www.aclweb.org/anthology/P18-1035.pdf) | https://github.com/danielhers/tupa |
| Transition-based (Hershcovich et al., 2017) | 72.8 | 67.2 | [A Transition-Based Directed Acyclic Graph Parser for UCCA](https://www.aclweb.org/anthology/P17-1104.pdf) | https://github.com/danielhers/tupa |

### [CoNLL 2019](https://www.aclweb.org/anthology/K19-2001.pdf)

The CoNLL 2019 shared task included parsing to AMR, UCCA, DM, PSD, and EDS.
The [UCCA training data](http://svn.nlpl.eu/mrp/2019/public/ucca.tgz) is freely available.

UCCA evaluation is done both by UCCA F1 (as in SemEval 2019) and by the MRP metric, which is similar to smatch.
The training data contains 6,572 sentences from web reviews and Wikipedia.
There are two evaluation sets: one with 1,131, from the same domains (Full), and one with 87 sentences, from *The Little Prince* (LPP). Note that due to an error, 535 of the 1,131 Full Evaluation sentences were included in the training data, and therefore the full evaluation scores are an overestimate. The LPP scores are unaffected by this.

| Model | Full UCCA F1 | Full MRP F1 | LPP UCCA F1 | LPP MRP F1 | Paper / Source | Code |
| ------| :----------: | :---------: | :---------: | :--------: | -------------- | ---- |
| Transition-based + BERT + Efficient Training + Effective Encoding (Che et al., 2019) | 66.7 | 81.7 | 64.4 | 82.6 | [HIT-SCIR at MRP 2019: A Unified Pipeline for Meaning Representation Parsing via Efficient Training and Effective Encoding](https://www.aclweb.org/anthology/K19-2007.pdf) | https://github.com/DreamerDeo/HIT-SCIR-CoNLL2019 |
| Transition-based + BERT (Hershcovich and Arviv, 2019) | 57.4 | 77.7 |  65.9 | 82.2 | [TUPA at MRP 2019: A Multi-Task Baseline System](https://www.aclweb.org/anthology/K19-2002.pdf) | https://github.com/danielhers/tupa/tree/mrp |
| Transition-based + BERT + MTL (Hershcovich and Arviv, 2019) | 35.6 | 64.1 |  50.3 | 73.1 | [TUPA at MRP 2019: A Multi-Task Baseline System](https://www.aclweb.org/anthology/K19-2002.pdf) | https://github.com/danielhers/tupa/tree/mrp |

## SQL parsing

### ATIS

5,280 user questions for a flight-booking task:

- Collected and manually annotated with SQL [Dahl et al., (1994)](http://dl.acm.org/citation.cfm?id=1075823)
- Modified by [Iyer et al., (2017)](http://www.aclweb.org/anthology/P17-1089) to reduce nesting
- Bugfixes and changes to a canonical style by [Finegan-Dollak et al., (2018)](http://arxiv.org/abs/1806.09029)


Example:

| Question | SQL query |
| ------------- |  --- |
| what flights from any city land at MKE | `SELECT DISTINCT FLIGHTalias0.FLIGHT_ID FROM AIRPORT AS AIRPORTalias0 , AIRPORT_SERVICE AS AIRPORT_SERVICEalias0 , CITY AS CITYalias0 , FLIGHT AS FLIGHTalias0 WHERE AIRPORTalias0.AIRPORT_CODE = "MKE" AND CITYalias0.CITY_CODE = AIRPORT_SERVICEalias0.CITY_CODE AND FLIGHTalias0.FROM_AIRPORT = AIRPORT_SERVICEalias0.AIRPORT_CODE AND FLIGHTalias0.TO_AIRPORT = AIRPORTalias0.AIRPORT_CODE ;` |

| Model           | Question Split | Query Split |  Paper / Source | Code |
| --------------- | ----- |  :-----:| --------------- | ---- |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | 51 | 32 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |
| Iyer et al., (2017) | 45 | 17 | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) | [System](https://github.com/sriniiyer/nl2sql) |
| Template Baseline (Finegan-Dollak et al., 2018) | 45 | 0 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |

### Advising

4,570 user questions about university course advising, with manually annotated SQL [Finegan-Dollak et al., (2018)](http://arxiv.org/abs/1806.09029).

Example:

| Question | SQL query |
| ------------- |  --- |
| Can undergrads take 550 ? | `SELECT DISTINCT COURSEalias0.ADVISORY_REQUIREMENT , COURSEalias0.ENFORCED_REQUIREMENT , COURSEalias0.NAME FROM COURSE AS COURSEalias0 WHERE COURSEalias0.DEPARTMENT = \"department0\" AND COURSEalias0.NUMBER = 550 ;` |

| Model           | Question Split | Query Split |  Paper / Source | Code |
| --------------- | ----- |  :-----:| --------------- | ---- |
| Template Baseline (Finegan-Dollak et al., 2018) | 80 | 0 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | 70 | 0  | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |
| Iyer et al., (2017) | 41 | 1 | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) | [System](https://github.com/sriniiyer/nl2sql) |

### GeoQuery

877 user questions about US geography:

- Collected and manually annotated with Prolog [Zelle and Mooney (1996)](http://dl.acm.org/citation.cfm?id=1864519.1864543)
- Most questions were converted to SQL by [Popescu et al., (2003)](http://doi.acm.org/10.1145/604045.604070)
- Remaining question converted to SQL by [Giordani and Moschitti (2012)](https://doi.org/10.1007/978-3-642-45260-4_5), and independently by [Iyer et al., (2017)](http://www.aclweb.org/anthology/P17-1089)
- Bugfixes and changes to a canonical style by [Finegan-Dollak et al., (2018)](http://arxiv.org/abs/1806.09029)

Example:

| Question | SQL query |
| ------------- |  --- |
| what is the biggest city in arizona | `SELECT CITYalias0.CITY_NAME FROM CITY AS CITYalias0 WHERE CITYalias0.POPULATION = ( SELECT MAX( CITYalias1.POPULATION ) FROM CITY AS CITYalias1 WHERE CITYalias1.STATE_NAME = "arizona" ) AND CITYalias0.STATE_NAME = "arizona"` |

| Model           | Question Split | Query Split |  Paper / Source | Code |
| --------------- | ----- |  :-----:| --------------- | ---- |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | 71 | 20 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |
| Iyer et al., (2017) | 66 | 40 | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) | [System](https://github.com/sriniiyer/nl2sql) |
| Template Baseline (Finegan-Dollak et al., 2018) | 66 | 0  | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |

### Scholar

817 user questions about academic publications, with automatically generated SQL that was checked by asking the user if the output was correct.

- Collected by [Iyer et al., (2017)](http://www.aclweb.org/anthology/P17-1089)
- Bugfixes and changes to a canonical style by [Finegan-Dollak et al., (2018)](http://arxiv.org/abs/1806.09029)

Example:

| Question | SQL query |
| ------------- |  --- |
| What papers has sharon goldwater written ? | `SELECT DISTINCT WRITESalias0.PAPERID FROM AUTHOR AS AUTHORalias0 , WRITES AS WRITESalias0 WHERE AUTHORalias0.AUTHORNAME = "sharon goldwater" AND WRITESalias0.AUTHORID = AUTHORalias0.AUTHORID ;` |

| Model           | Question Split | Query Split |  Paper / Source | Code |
| --------------- | ----- |  :-----:| --------------- | ---- |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | 59 | 5 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |
| Template Baseline (Finegan-Dollak et al., 2018) | 52 | 0   | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |
| Iyer et al., (2017) | 44 | 3 | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) | [System](https://github.com/sriniiyer/nl2sql) |

### Spider

Spider is a large-scale complex and cross-domain semantic parsing and text-to-SQL 
dataset. It consists of 10,181 questions and 5,693 unique complex SQL queries on 
200 databases with multiple tables covering 138 different domains. In Spider 1.0, 
different complex SQL queries and databases appear in train and test sets. 

The Spider dataset can be accessed and leaderboard can be accessed [here](https://yale-lily.github.io/spider).

### WikiSQL

The [WikiSQL dataset](https://arxiv.org/abs/1709.00103) consists of 87,673 
examples of questions, SQL queries, and database tables built from 26,521 tables.
Train/dev/test splits are provided so that each table is only in one split.
Models are evaluated based on accuracy on execute result matches.

Example:

| Question | SQL query |
| ------------- |  --- |
| How many engine types did Val Musetti use? | `SELECT COUNT Engine WHERE Driver = Val Musetti` |

The WikiSQL dataset and leaderboard can be accessed [here](https://github.com/salesforce/WikiSQL).

### Smaller Datasets

Restaurants - 378 questions about restaurants, their cuisine and locations, collected by [Tang and Mooney (2000)](http://www.aclweb.org/anthology/W/W00/W00-1317.pdf), converted to SQL by [Popescu et al., (2003)]((http://doi.acm.org/10.1145/604045.604070) and [Giordani and Moschitti (2012)](https://doi.org/10.1007/978-3-642-45260-4_5), improved and converted to canonical style by [Finegan-Dollak et al., (2018)](http://arxiv.org/abs/1806.09029)

Example:

| Question | SQL query |
| ------------- |  --- |
| where is a restaurant in alameda ? | `SELECT LOCATIONalias0.HOUSE_NUMBER , RESTAURANTalias0.NAME FROM LOCATION AS LOCATIONalias0 , RESTAURANT AS RESTAURANTalias0 WHERE LOCATIONalias0.CITY_NAME = "alameda" AND RESTAURANTalias0.ID = LOCATIONalias0.RESTAURANT_ID ;` |

| Model           | Question Split | Query Split |  Paper / Source | Code |
| --------------- | ----- |  :-----:| --------------- | ---- |
| Iyer et al., (2017) | 100 | 8 | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) | [System](https://github.com/sriniiyer/nl2sql) |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | 100 | 4 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |
| Template Baseline (Finegan-Dollak et al., 2018) | 95 | 0  | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |

Academic - 196 questions about publications generated by enumerating all of the different queries possible with the Microsoft Academic Search interface, then writing questions for each query [Li and Jagadish (2014)](http://dx.doi.org/10.14778/2735461.2735468). Improved and converted to a cononical style by [Finegan-Dollak et al., (2018)](http://arxiv.org/abs/1806.09029).

Example:

| Question | SQL query |
| ------------- |  --- |
| return me the homepage of PVLDB | `SELECT JOURNALalias0.HOMEPAGE FROM JOURNAL AS JOURNALalias0 WHERE JOURNALalias0.NAME = "PVLDB" ;` |

| Model           | Question Split | Query Split |  Paper / Source | Code |
| --------------- | ----- |  :-----:| --------------- | ---- |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | 81 | 74 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |
| Iyer et al., (2017) | 76 | 70 | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) | [System](https://github.com/sriniiyer/nl2sql) |
| Template Baseline (Finegan-Dollak et al., 2018) | 0 | 0 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |

Yelp - 128 user questions about the Yelp website [Yaghmazadeh et al., 2017](http://doi.org/10.1145/3133887). Improved and converted to a cononical style by [Finegan-Dollak et al., (2018)](http://arxiv.org/abs/1806.09029).

Example:

| Question | SQL query |
| ------------- |  --- |
| List all businesses with rating 3.5 | `SELECT BUSINESSalias0.NAME FROM BUSINESS AS BUSINESSalias0 WHERE BUSINESSalias0.RATING = 3.5 ;` |

| Model           | Question Split | Query Split |  Paper / Source | Code |
| --------------- | ----- |  :-----:| --------------- | ---- |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | 12 | 4 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |
| Iyer et al., (2017) | 6 | 6 | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) | [System](https://github.com/sriniiyer/nl2sql) |
| Template Baseline (Finegan-Dollak et al., 2018) | 1 | 0 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |

IMDB - 131 user questions about the Internet Movie Database [Yaghmazadeh et al., 2017](http://doi.org/10.1145/3133887). Improved and converted to a cononical style by [Finegan-Dollak et al., (2018)](http://arxiv.org/abs/1806.09029).

Example:

| Question | SQL query |
| ------------- |  --- |
| What year was the movie " The Imitation Game " produced | `SELECT MOVIEalias0.RELEASE_YEAR FROM MOVIE AS MOVIEalias0 WHERE MOVIEalias0.TITLE = "The Imitation Game" ;` |

| Model           | Question Split | Query Split |  Paper / Source | Code |
| --------------- | ----- |  :-----:| --------------- | ---- |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | 26 | 9 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |
| Iyer et al., (2017) | 10 | 4 | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) | [System](https://github.com/sriniiyer/nl2sql) |
| Template Baseline (Finegan-Dollak et al., 2018) | 0 | 0 | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) | [Data and System](https://github.com/jkkummerfeld/text2sql-data) |

[Go back to the README](../README.md)
