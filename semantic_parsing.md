# Semantic parsing

Semantic parsing is the task of translating natural language into a formal meaning
representation on which a machine can act. Representations may be an executable language
such as SQL or more abstract representations such as [Abstract Meaning Representation (AMR)](https://en.wikipedia.org/wiki/Abstract_Meaning_Representation).

## AMR parsing

### LDC2014T12

Models are evaluated on the newswire section and the full dataset based on F1.
Brackets indicates the preprocessed features a model uses.
Systems marked with \* are pipeline systems that require a dependency parse as input.

| Model           | F1 Newswire  | F1 Full |  Paper / Source |
| ------------- | :-----:| :-----:| --- |
| Incremental joint model (POS, DEP, NER, SRL) (Zhou et al., 2016)* | 0.71 | 0.66 | [AMR Parsing with an Incremental Joint Model](https://aclweb.org/anthology/D16-1065) |
| Augmented parser (POS, DEP, NER, SRL) (Wang et al., 2015)* | 0.70 | 0.66 | [Boosting Transition-based AMR Parsing with Refined Actions and Auxiliary Analyzers](http://www.aclweb.org/anthology/P15-2141) |
| Stack-LSTM (POS, DEP) (Ballesteros and Al-Onaizan, 2017) | 0.69 | 0.64  | [AMR Parsing using Stack-LSTMs](http://www.aclweb.org/anthology/D17-1130) |

### LDC2015E86

Models are evaluated based on smatch.

| Model           | Smatch  |  Paper / Source |
| ------------- | :-----:| --- |
Joint model (Lyu and Titov, 2018) | 73.7 | [AMR Parsing as Graph Prediction with Latent Alignment](https://arxiv.org/abs/1805.05286) |
Mul-BiLSTM (Foland and Martin, 2017) | 70.7 | [Abstract Meaning Representation Parsing using LSTM Recurrent Neural Networks](http://aclweb.org/anthology/P17-1043) |
JAMR (Flanigan et al., 2016) | 67.0 | [CMU at SemEval-2016 Task 8: Graph-based AMR Parsing with Infinite Ramp Loss](http://www.aclweb.org/anthology/S16-1186) |
CAMR (Wang et al., 2016) | 66.5 | [CAMR at SemEval-2016 Task 8: An Extended Transition-based AMR Parser](http://www.aclweb.org/anthology/S16-1181) |
AMREager (Damonte et al., 2017) | 64.0 | [An Incremental Parser for Abstract Meaning Representation](http://www.aclweb.org/anthology/E17-1051) |
SEQ2SEQ + 20M (Konstas et al., 2017) | 62.1 | [Neural AMR: Sequence-to-Sequence Models for Parsing and Generation](https://arxiv.org/abs/1704.08381) |

### LDC2016E25

Results are computed over 8 runs. Models are evaluated based on smatch.

| Model           | Smatch  |  Paper / Source |
| ------------- | :-----:| --- |
Joint model (Lyu and Titov, 2018) | 74.4 | [AMR Parsing as Graph Prediction with Latent Alignment](https://arxiv.org/abs/1805.05286) |
ChSeq + 100K (van Noord and Bos, 2017) | 71.0 | [Neural Semantic Parsing by Character-based Translation: Experiments with Abstract Meaning Representations](https://arxiv.org/abs/1705.09980) |
Neural-Pointer (Buys and Blunsom, 2017) | 61.9 | [Oxford at SemEval-2017 Task 9: Neural AMR Parsing with Pointer-Augmented Attention](http://aclweb.org/anthology/S17-2157) |

## SQL parsing

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
