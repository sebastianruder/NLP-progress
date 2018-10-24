# Information Extraction

## Open Knowledge Graph Canonicalization

Open Information Extraction approaches leads to creation of large Knowledge bases (KB) from the web. The problem with such methods is that their entities and relations are not canonicalized, which leads to storage of redundant and ambiguous facts. For example, an Open KB storing *\<Barack Obama, was born in, Honolulu\>* and *\<Obama, took birth in, Honolulu\>* doesn't know that *Barack Obama* and *Obama* mean the same entity. Similarly, *took birth in* and *was born in* also refer to the same relation. Problem of Open KB canonicalization involves identifying groups of equivalent entities and relations in the KB.

### Datasets 

| Datasets                                 | # Gold Entities | #NPs  | #Relations | #Triples |
| ---------------------------------------- | :-------------: | ----- | ---------- | -------- |
| [Base](https://suchanek.name/work/publications/cikm2014.pdf) |       150       | 290   | 3K         | 9K       |
| [Ambiguous](https://suchanek.name/work/publications/cikm2014.pdf) |       446       | 717   | 11K        | 37K      |
| [ReVerb45K](https://github.com/malllabiisc/cesi) |      7.5K       | 15.5K | 22K        | 45K      |

### Noun Phrase Canonicalization

| **Model**                     |               | Base Dataset |        |               | Ambiguous dataset |        |               | ReVerb45k  |        | **Paper**/Source                         |
| :---------------------------- | :-----------: | :----------: | :----: | :-----------: | :---------------: | ------ | :-----------: | :--------: | :----: | ---------------------------------------- |
|                               | **Precision** |  **Recall**  | **F1** | **Precision** |    **Recall**     | **F1** | **Precision** | **Recall** | **F1** |                                          |
| CESI (Vashishth et al., 2018) |     98.2      |     99.8     |  99.9  |     66.2      |       92.4        | 91.9   |     62.7      |    84.4    |  81.9  | [CESI: Canonicalizing Open Knowledge Bases using Embeddings and Side Information](https://github.com/malllabiisc/cesi) |
| Galárraga et al., 2014 ( IDF) |     94.8      |     97.9     |  98.3  |     67.9      |       82.9        | 79.3   |     71.6      |    50.8    |  0.5   | [Canonicalizing Open Knowledge Bases](https://suchanek.name/work/publications/cikm2014.pdf) |

[Go back to the README](../README.md)
