# Temporal Processing

## Document Dating (Time-stamping)
#### Problem
Document Dating is the problem of automatically predicting the date of a document based on its content. Date of a document, also referred to as the Document Creation Time (DCT), is at the core of many important tasks, such as, information retrieval, temporal reasoning, text summarization, event detection, and analysis of historical text, among others. 

For example, in the following document, the correct creation year is 1999. This can be inferred by the presence of terms *1995* and *Four years after*.

*Swiss adopted that form of taxation in 1995. The concession was approved by the govt last September. Four years after, the IOC….*

#### Datasets 

|                 Datasets                 | # Docs | Start Year | End Year |
| :--------------------------------------: | :----: | :--------: | :------: |
| [APW](https://drive.google.com/file/d/1tll04ZBooB3Mohm6It-v8MBcjMCC3Y1w/view) |  675k  |    1995    |   2010   |
| [NYT](https://drive.google.com/file/d/1wqQRFeA1ESAOJqrwUNakfa77n_S9cmBi/view?usp=sharing) |  647k  |    1987    |   1996   |

#### Comparison on year level granularity:

|                                          | APW Dataset | NYT Dataset |
| ---------------------------------------- | :---------: | :---------: |
| [BurstySimDater](https://pdfs.semanticscholar.org/87af/a0cb4f829ce861da0c721ca666d48a62c404.pdf) |    45.9     |    38.5     |
| [MaxEnt-Time+NER](https://pdfs.semanticscholar.org/87af/a0cb4f829ce861da0c721ca666d48a62c404.pdf) |    52.5     |    42.3     |
| [NeuralDater](https://github.com/malllabiisc/NeuralDater) |    64.1     |    58.9     |
