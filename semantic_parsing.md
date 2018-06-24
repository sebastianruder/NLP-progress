# Semantic parsing

Semantic parsing is the task of translating natural language into a formal meaning
representation on which a machine can act. Representations may be an executable language
such as SQL or more abstract representations such as [Abstract Meaning Representation (AMR)](https://en.wikipedia.org/wiki/Abstract_Meaning_Representation).

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
