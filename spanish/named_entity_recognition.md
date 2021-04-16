# Named entity recognition

Named entity recognition (NER) is the task of tagging entities in text with their corresponding type.
Approaches typically use BIO notation, which differentiates the beginning (B) and the inside (I) of entities.
O is used for non-entity tokens.

Example:

| Mark | Watney | visited | Mars |
| --- | ---| --- | --- |
| B-PER | I-PER | O | B-LOC |

(NER definition taken from english/named_entity_recognition.md)

### CANTEMIST 2020

The [CANTEMIST-NER 2020](https://temu.bsc.es/cantemist/) task consists of Spanish oncology clinical reports corpus tagged with one entity type (MORFOLOGIA_NEOPLASIA). 
Models are evaluated based on span-based F1 on the test set: see [evaluation scripts](https://github.com/TeMU-BSC/cantemist-evaluation-library).

The CANTEMIST shared task contains as well an entity linking subtrack (CANTEMIST-NORM) and a document indexing subtrack (CANTEMIST-CODING).

Data link: [Zenodo](https://doi.org/10.5281/zenodo.3773228)

| Model           | F1  |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| MRC mBERT-MLP (Xiong et al., 2020) | 87.0 | [A Joint Model for Medical Named Entity Recognition and Normalization](http://ceur-ws.org/Vol-2664/cantemist_paper18.pdf) | [Official](https://github.com/xy-always/2020Iberlef) |
| BETO-SciBERT (Garcia-Pablos et al., 2020) | 86.9 | [Vicomtech at CANTEMIST 2020](http://ceur-ws.org/Vol-2664/cantemist_paper17.pdf) | |
| BiLSTM-CRF+GloVe+SME+CWE (López-Úbeda et al., 2020) | 85.5 | [Extracting Neoplasms Morphology Mentions in Spanish Clinical Cases through Word Embeddings](http://ceur-ws.org/Vol-2664/cantemist_paper1.pdf) | |
| Biaffine Classifier (Lange et al., 2020) | 85.3 | [NLNDE at CANTEMIST: Neural Sequence Labeling and Parsing Approaches for Clinical Concept Extraction](http://ceur-ws.org/Vol-2664/cantemist_paper2.pdf) | |
| BETO (Han et al., 2020) | 85.0 | [Pre-trained Language Model for CANTEMIST Named Entity Recognition](http://ceur-ws.org/Vol-2664/cantemist_paper3.pdf) | |
| BiLSTM-CRF+FasText+Char (Carreto Fidalgo et al., 2020) | 84.5 | [Recognai’s Working Notes for CANTEMIST-NER Track](http://ceur-ws.org/Vol-2664/cantemist_paper4.pdf) | [Official](https://github.com/recognai/cantemist-ner) |
| BiLSTM-BiLSTM-CRF+FasText+PoS+Char (Santamaria Carrasco et al., 2020) | 83.4 | [Using Embeddings and Bi-LSTM+CRF Model to Detect Tumor Morphology Entities in Spanish Clinical Cases](http://ceur-ws.org/Vol-2664/cantemist_paper6.pdf) | [Official](https://github.com/ssantamaria94/CANTEMIST-Participation) |

[Go back to the README](../README.md)
