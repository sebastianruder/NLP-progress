# Semantic parsing

Semantic parsing is the task of translating natural language into a formal meaning
representation on which a machine can act. Representations may be an executable language
such as SQL or more abstract representations such as [Abstract Meaning Representation (AMR)](https://en.wikipedia.org/wiki/Abstract_Meaning_Representation).

## AMR parsing

Each AMR is a single rooted, directed graph. AMRs include PropBank semantic roles, within-sentence coreference, named entities and types, modality, negation, questions, quantities, and so on. [See](https://amr.isi.edu/index.html).

### LDC2014T12: 
13,051 sentences

Models are evaluated on the newswire section and the full dataset based on [smatch](https://amr.isi.edu/smatch-13.pdf).
Systems marked with \* are pipeline systems that require other systems (i.e. a dependency parse or a SRL parse) as input.

| Model           | F1 Newswire  | F1 Full |  Paper / Source |
| ------------- | :-----:| :-----:| --- |
| Incremental joint model (Zhou et al., 2016)* | 0.71 | 0.66 | [AMR Parsing with an Incremental Joint Model](https://aclweb.org/anthology/D16-1065) |
| Transition-based transducer (Wang et al., 2015)* | 0.70 | 0.66 | [Boosting Transition-based AMR Parsing with Refined Actions and Auxiliary Analyzers](http://www.aclweb.org/anthology/P15-2141) |
| Imitation learning  (Goodman et al., 2016)* | 0.70 |  -- | [Noise reduction and targeted exploration in imitation learning for Abstract Meaning Representation parsing](http://www.aclweb.org/anthology/P16-1001) |
MT-Based (Pust et al., 2015)* | -- | 0.66 | [Parsing English into Abstract Meaning Representation Using Syntax-Based Machine Translation ](http://www.aclweb.org/anthology/D15-1136)
| Transition-based parser-Stack-LSTM (Ballesteros and Al-Onaizan, 2017)* | 0.69 | 0.64  | [AMR Parsing using Stack-LSTMs](http://www.aclweb.org/anthology/D17-1130) |
| Transition-based parser-Stack-LSTM (Ballesteros and Al-Onaizan, 2017) | 0.68 | 0.63  | [AMR Parsing using Stack-LSTMs](http://www.aclweb.org/anthology/D17-1130) |

### LDC2015E86: 
19,572 sentences

Models are evaluated based on [smatch](https://amr.isi.edu/smatch-13.pdf).

| Model           | Smatch  |  Paper / Source |
| ------------- | :-----:| --- |
Joint model (Lyu and Titov, 2018) | 73.7 | [AMR Parsing as Graph Prediction with Latent Alignment](https://arxiv.org/abs/1805.05286) |
Mul-BiLSTM (Foland and Martin, 2017) | 70.7 | [Abstract Meaning Representation Parsing using LSTM Recurrent Neural Networks](http://aclweb.org/anthology/P17-1043) |
JAMR (Flanigan et al., 2016) | 67.0 | [CMU at SemEval-2016 Task 8: Graph-based AMR Parsing with Infinite Ramp Loss](http://www.aclweb.org/anthology/S16-1186) |
CAMR (Wang et al., 2016) | 66.5 | [CAMR at SemEval-2016 Task 8: An Extended Transition-based AMR Parser](http://www.aclweb.org/anthology/S16-1181) |
AMREager (Damonte et al., 2017) | 64.0 | [An Incremental Parser for Abstract Meaning Representation](http://www.aclweb.org/anthology/E17-1051) |
SEQ2SEQ + 20M (Konstas et al., 2017) | 62.1 | [Neural AMR: Sequence-to-Sequence Models for Parsing and Generation](https://arxiv.org/abs/1704.08381) |

### LDC2016E25
39,260 sentences

Results are computed over 8 runs. Models are evaluated based on [smatch](https://amr.isi.edu/smatch-13.pdf).

| Model           | Smatch  |  Paper / Source |
| ------------- | :-----:| --- |
Joint model (Lyu and Titov, 2018) | 74.4 | [AMR Parsing as Graph Prediction with Latent Alignment](https://arxiv.org/abs/1805.05286) |
ChSeq + 100K (van Noord and Bos, 2017) | 71.0 | [Neural Semantic Parsing by Character-based Translation: Experiments with Abstract Meaning Representations](https://arxiv.org/abs/1705.09980) |
Neural-Pointer (Buys and Blunsom, 2017) | 61.9 | [Oxford at SemEval-2017 Task 9: Neural AMR Parsing with Pointer-Augmented Attention](http://aclweb.org/anthology/S17-2157) |

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

| Model           | Split | Acc ex |  Paper / Source |
| --------------- | ----- |  :-----:| --------------- |
| Iyer et al., (2017) | question | 45  | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | question | 51   | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |
| Template Baseline (Finegan-Dollak et al., 2018) | question | 45   | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |
| Iyer et al., (2017) | query | 17  | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | query | 32  | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |

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

| Model           | Split | Acc ex |  Paper / Source |
| --------------- | ----- |  :-----:| --------------- |
| Iyer et al., (2017) | question | 66  | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | question | 71   | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |
| Template Baseline (Finegan-Dollak et al., 2018) | question | 66   | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |
| Iyer et al., (2017) | query | 40  | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | query | 20  | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |

### Scholar

817 user questions about academic publications, with automatically generated SQL that was checked by asking the user if the output was correct.

- Collected by [Iyer et al., (2017)](http://www.aclweb.org/anthology/P17-1089)
- Bugfixes and changes to a canonical style by [Finegan-Dollak et al., (2018)](http://arxiv.org/abs/1806.09029)

Example:

| Question | SQL query | 
| ------------- |  --- |
| What papers has sharon goldwater written ? | `SELECT DISTINCT WRITESalias0.PAPERID FROM AUTHOR AS AUTHORalias0 , WRITES AS WRITESalias0 WHERE AUTHORalias0.AUTHORNAME = "sharon goldwater" AND WRITESalias0.AUTHORID = AUTHORalias0.AUTHORID ;` |

| Model           | Split | Acc ex |  Paper / Source |
| --------------- | ----- |  :-----:| --------------- |
| Iyer et al., (2017) | question | 44  | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | question | 59   | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |
| Template Baseline (Finegan-Dollak et al., 2018) | question | 52   | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |
| Iyer et al., (2017) | query | 3  | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | query | 5  | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |

### Advising

4,570 user questions about university course advising, with manually annotated SQL [Finegan-Dollak et al., (2018)](http://arxiv.org/abs/1806.09029).

Example:

| Question | SQL query | 
| ------------- |  --- |
| Can undergrads take 550 ? | SELECT DISTINCT COURSEalias0.ADVISORY_REQUIREMENT , COURSEalias0.ENFORCED_REQUIREMENT , COURSEalias0.NAME FROM COURSE AS COURSEalias0 WHERE COURSEalias0.DEPARTMENT = \"department0\" AND COURSEalias0.NUMBER = 550 ; |

| Model           | Split | Acc ex |  Paper / Source |
| --------------- | ----- |  :-----:| --------------- |
| Iyer et al., (2017) | question | 41  | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | question | 70   | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |
| Template Baseline (Finegan-Dollak et al., 2018) | question | 80   | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |
| Iyer et al., (2017) | query | 1  | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | query | 0  | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |

### Smaller Datasets

Restaurants - 378 questions about restaurants, their cuisine and locations, collected by [Tang and Mooney (2000)](http://www.aclweb.org/anthology/W/W00/W00-1317.pdf), converted to SQL by [Popescu et al., (2003)]((http://doi.acm.org/10.1145/604045.604070) and [Giordani and Moschitti (2012)](https://doi.org/10.1007/978-3-642-45260-4_5), improved and converted to canonical style by [Finegan-Dollak et al., (2018)](http://arxiv.org/abs/1806.09029)

Example:

| Question | SQL query | 
| ------------- |  --- |
| where is a restaurant in alameda ? | `SELECT LOCATIONalias0.HOUSE_NUMBER , RESTAURANTalias0.NAME FROM LOCATION AS LOCATIONalias0 , RESTAURANT AS RESTAURANTalias0 WHERE LOCATIONalias0.CITY_NAME = "alameda" AND RESTAURANTalias0.ID = LOCATIONalias0.RESTAURANT_ID ;` |

| Model           | Split | Acc ex |  Paper / Source |
| --------------- | ----- |  :-----:| --------------- |
| Iyer et al., (2017) | question | 100  | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | question | 100   | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |
| Template Baseline (Finegan-Dollak et al., 2018) | question | 95   | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |
| Iyer et al., (2017) | query | 8  | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | query | 4  | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |

Academic - 196 questions about publications generated by enumerating all of the different queries possible with the Microsoft Academic Search interface, then writing questions for each query [Li and Jagadish (2014)](http://dx.doi.org/10.14778/2735461.2735468). Improved and converted to a cononical style by [Finegan-Dollak et al., (2018)](http://arxiv.org/abs/1806.09029).

Example:

| Question | SQL query | 
| ------------- |  --- |
| return me the homepage of PVLDB | SELECT JOURNALalias0.HOMEPAGE FROM JOURNAL AS JOURNALalias0 WHERE JOURNALalias0.NAME = "PVLDB" ; |

| Model           | Split | Acc ex |  Paper / Source |
| --------------- | ----- |  :-----:| --------------- |
| Iyer et al., (2017) | question | 76  | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) |
| Iyer et al., (2017) | query | 70  | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | question | 81   | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | query | 74  | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |
| Template Baseline (Finegan-Dollak et al., 2018) | question | 0   | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |

Yelp - 128 user questions about the Yelp website [Yaghmazadeh et al., 2017](http://doi.org/10.1145/3133887). Improved and converted to a cononical style by [Finegan-Dollak et al., (2018)](http://arxiv.org/abs/1806.09029).

Example:

| Question | SQL query | 
| ------------- |  --- |
| List all businesses with rating 3.5 | `SELECT BUSINESSalias0.NAME FROM BUSINESS AS BUSINESSalias0 WHERE BUSINESSalias0.RATING = 3.5 ;` |

| Model           | Split | Acc ex |  Paper / Source |
| --------------- | ----- |  :-----:| --------------- |
| Iyer et al., (2017) | question | 6  | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | question | 12   | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |
| Template Baseline (Finegan-Dollak et al., 2018) | question | 1  | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |
| Iyer et al., (2017) | query | 6  | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | query | 4  | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |

IMDB - 131 user questions about the Internet Movie Database [Yaghmazadeh et al., 2017](http://doi.org/10.1145/3133887). Improved and converted to a cononical style by [Finegan-Dollak et al., (2018)](http://arxiv.org/abs/1806.09029).

Example:

| Question | SQL query | 
| ------------- |  --- |
| What year was the movie " The Imitation Game " produced | `SELECT MOVIEalias0.RELEASE_YEAR FROM MOVIE AS MOVIEalias0 WHERE MOVIEalias0.TITLE = "The Imitation Game" ;` |

| Model           | Split | Acc ex |  Paper / Source |
| --------------- | ----- |  :-----:| --------------- |
| Iyer et al., (2017) | question | 10  | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | question | 26   | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |
| Template Baseline (Finegan-Dollak et al., 2018) | question | 0  | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |
| Iyer et al., (2017) | query | 4  | [Learning a neural semantic parser from user feedback](http://www.aclweb.org/anthology/P17-1089) |
| Seq2Seq with copying (Finegan-Dollak et al., 2018) | query | 9  | [Improving Text-to-SQL Evaluation Methodology](http://arxiv.org/abs/1806.09029) |

### WikiSQL

The [WikiSQL dataset](https://arxiv.org/abs/1709.00103) consists of 87,673 
examples of questions, SQL queries, and database tables built from 26,521 tables.
Train/dev/test splits are provided so that each table is only in one split.
Models are evaluated based on accuracy on execute result matches.

Example:

| Question | SQL query | 
| ------------- |  --- |
| How many engine types did Val Musetti use? | `SELECT COUNT Engine WHERE Driver = Val Musetti` | 

| Model           | Acc ex |  Paper / Source |
| -------------| :-----:| --- |
| TypeSQL+TC (Yu et al., 2018) | 82.6 | [TypeSQL: Knowledge-based Type-Aware Neural Text-to-SQL Generation](https://arxiv.org/abs/1804.09769) |
| SQLNet (Xu et al., 2017) | 68.0 | [Sqlnet: Generating structured queries from natural language without reinforcement learning](https://arxiv.org/abs/1711.04436) |
| Seq2SQL (Zhong et al., 2017) | 59.4 | [Seq2sql: Generating structured queries from natural language using reinforcement learning](https://arxiv.org/abs/1709.00103) |

[Go back to the README](README.md)
