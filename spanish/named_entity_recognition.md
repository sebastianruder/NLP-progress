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


### ProfNER 2021

The [ProfNER-NER 2021](https://temu.bsc.es/smm4h-spanish/) task consists of Spanish COVID-19 related Twitter corpus tagged with four entity types (PROFESION,SITUACION_LABORAL,ACTIVIDAD,FIGURATIVA). 
Models are evaluated based on span AND label-based F1 on the test set: see [Task 7 of Codalab SMM4H competition](https://competitions.codalab.org/competitions/28766).

The ProfNER shared task contains as well a tweet classification subtrack (ProfNER-Track A).

Data link: [Zenodo](https://doi.org/10.5281/zenodo.4309356)

| Model           | F1  |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| BETO-Linear-CRF (David Carreto Fidalgo et al., 2021) | 83.9 | [Recognai](https://www.aclweb.org/anthology/2021.smm4h-1.11.pdf) | [Official](https://github.com/recognai/profner) |
| 3xBiLSTM-CRF+BPE+FastText+BETOemb (Usama Yaseen et al., 2021) | 82.4 | [MIC-NLP](https://www.aclweb.org/anthology/2021.smm4h-1.14.pdf) | |
| BiLSTM-LSTM-CRF+Char+STE+SME+BETO+Syllabes+POS (Sergio Santamaría Carrasco et al., 2021) | 82.3 | [Troy](https://www.aclweb.org/anthology/2021.smm4h-1.12.pdf) | [Official](https://github.com/ssantamaria94/ProfNER-SMM4H) |
| BiGRU-BiLSTM-TokenClassification-CRF+STE+Char (David Carreto Fidalgo et al., 2021) | 76.4 | [Recognai](https://www.aclweb.org/anthology/2021.smm4h-1.11.pdf) | [Official](https://github.com/recognai/profner) | [Official](https://github.com/recognai/profner) |
| BiLSTM-CRF+Char+STE+SME+WikiFastText (Vasile Pais, et al., 2021) | 75.7 | [RACAI](https://www.aclweb.org/anthology/2021.smm4h-1.27.pdf) | |
| 30xBETO-BiLSTM (Tong Zhou et al., 2021) | 73.3 | [CASIA_Unisound](https://www.aclweb.org/anthology/2021.smm4h-1.13.pdf) | [Official](https://github.com/recognai/cantemist-ner) |
| Dictionaries-CRF (Alberto Mesa Murgado et al., 2021) | 72.8 | [SINAI](https://www.aclweb.org/anthology/2021.smm4h-1.31.pdf) | [Official](https://github.com/ssantamaria94/CANTEMIST-Participation) |
| BiLSTM-CRF+FLAIR+FastText (Pedro Ruas et al., 2021) | 72.7 | [Lasige-BioTM](https://www.aclweb.org/anthology/2021.smm4h-1.21.pdf) | [Official](https://github.com/lasigeBioTM/LASIGE-participation-in-ProfNER) |


[Go back to the README](../README.md)
