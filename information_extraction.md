# Information Extraction

## Open Knowledge Graph Canonicalization
#### Problem

Open Information Extraction approaches leads to creation of large Knowledge bases (KB) from the web. The problem with such methods is that their entities and relations are not canonicalized, which leads to storage of redundant and ambiguous facts. For example, an Open KB storing *\<Barack Obama, was born in, Honolulu\>* and *\<Obama, took birth in, Honolulu\>* doesn't know that *Barack Obama* and *Obama* mean the same entity. Similarly, *took birth in* and *was born in* also refer to the same relation. Problem of Open KB canonicalization involves identifying groups of equivalent entities and relations in the KB.

#### Datasets 

| Datasets                                 | # Gold Entities | #NPs  | #Relations | #Triples |
| ---------------------------------------- | :-------------: | ----- | ---------- | -------- |
| [Base](https://suchanek.name/work/publications/cikm2014.pdf) |       150       | 290   | 3K         | 9K       |
| [Ambiguous](https://suchanek.name/work/publications/cikm2014.pdf) |       446       | 717   | 11K        | 37K      |
| [ReVerb45K](https://github.com/malllabiisc/cesi) |      7.5K       | 15.5K | 22K        | 45K      |

#### Noun Phrase Canonicalization:

|                                          |               | Base Dataset |        |               | Ambiguous dataset |        |               | ReVerb45k  |        |
| :--------------------------------------- | :-----------: | :----------: | :----: | :-----------: | :---------------: | ------ | :-----------: | :--------: | :----: |
|                                          | **Precision** |  **Recall**  | **F1** | **Precision** |    **Recall**     | **F1** | **Precision** | **Recall** | **F1** |
| Morphological Normalization              |     58.3      |     88.3     |  83.5  |     49.1      |       57.2        | 70.9   |      1.4      |    77.7    |  75.1  |
| [Galárraga-StrSim](https://suchanek.name/work/publications/cikm2014.pdf) |     88.2      |     96.5     |  97.7  |     66.6      |       85.3        | 82.2   |     69.9      |    51.7    |  0.5   |
| [Galárraga-IDF](https://suchanek.name/work/publications/cikm2014.pdf) |     94.8      |     97.9     |  98.3  |     67.9      |       82.9        | 79.3   |     71.6      |    50.8    |  0.5   |
| [Galárraga-Attr](https://suchanek.name/work/publications/cikm2014.pdf) |     76.1      |     51.4     |  18.1  |     82.9      |       27.7        | 8.4    |     75.1      |    20.1    |  0.2   |
| [CESI](https://github.com/malllabiisc/cesi) |     98.2      |     99.8     |  99.9  |     66.2      |       92.4        | 91.9   |     62.7      |    84.4    |  81.9  |

