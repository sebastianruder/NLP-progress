# Hindi

## Chunking

| Model           | Dev accuracy  | Test F1 | Paper / Source | Code | 
| ------------- | :-----:| :-----:| --- | --- | 
| Dalal et al. (2006) | 87.40 | 82.40 | [Hindi Part-of-Speech Tagging and Chunking: A Maximum Entropy Approach](https://www.researchgate.net/publication/241211496_Hindi_Part-of-Speech_Tagging_and_Chunking_A_Maximum_Entropy_Approach) | | 

## Part-of-speech tagging

| Model           | Dev accuracy  | Test F1 | Paper / Source | Code | 
| ------------- | :-----:| :-----:| --- | --- | 
| Jha et al. (2018) | 99.30 | 99.06 | [Multi-Task Deep Morphological Analyzer: Context-Aware Joint Morphological Tagging and Lemma Prediction](https://arxiv.org/ftp/arxiv/papers/1811/1811.08619.pdf) | [mt-dma](https://github.com/Saurav0074/mt-dma)
| Dalal et al. (2006) | 89.35 | 82.22 | [Hindi Part-of-Speech Tagging and Chunking: A Maximum Entropy Approach](https://www.researchgate.net/publication/241211496_Hindi_Part-of-Speech_Tagging_and_Chunking_A_Maximum_Entropy_Approach) | | 

## Machine Translation

The IIT Bombay English-Hindi Parallel Corpus used by Kunchukuttan et al. (2018) can be accessed [here](http://www.cfilt.iitb.ac.in/iitb_parallel/). A live leaderboard involving more directions involving Hindi can be accessed at the evaluation website for the [Workshop on Asian Translation](http://lotus.kuee.kyoto-u.ac.jp/WAT/).

### Hindi -> English 

* [WAT:HINDENhi-en](http://lotus.kuee.kyoto-u.ac.jp/WAT/evaluation/list.php?t=14&o=4)

| Model           | BLEU | Paper / Source | Code | 
| ------------- | :-----:| --- | --- | 
| Philip et al. (2020) | 24.85 | Revisiting Low Resource Status of Indian Languages in MT | [ilmulti](https://github.com/jerinphilip/ilmulti) | 
| Siripragada et al. (2020) | 22.91 | [A Multilingual Parallel Corpora Collection Effort for Indian Languages](https://www.aclweb.org/anthology/2020.lrec-1.462/) | [ilmulti](https://github.com/jerinphilip/ilmulti) | 
| Goyal et al. (2019) | 19.06 | [LTRC-MT Simple & Effective Hindi-English Neural Machine Translation Systems at WAT 2019](https://www.aclweb.org/anthology/D19-5216.pdf) 

### English -> Hindi 

* [WAT:HINDENen-hi](http://lotus.kuee.kyoto-u.ac.jp/WAT/evaluation/list.php?t=13&o=7)


| Model           | BLEU | Paper / Source | Code | 
| ------------- | :-----:| --- | --- | 
| Philip et al. (2018)  | 21.57 | [CVIT-MT Systems for WAT-2018](https://www.aclweb.org/anthology/Y18-3010/) || 
| Philip et al. (2020) | 21.20 | Revisiting Low Resource Status of Indian Languages in MT | [ilmulti](https://github.com/jerinphilip/ilmulti) | 
| Saini et al. (2018) | 18.215| [Neural Machine Translation for English to Hindi](https://www.researchgate.net/publication/327717152_Neural_Machine_Translation_for_English_to_Hindi) | | 

## G2P Conversion

### Schwa Deletion

Due to diachronic processes the inherent vowel of Hindi (the *schwa*, automatically applied to consonants that have no other vowel diacritic or vowel-killer diacritic attached) is sometimes dropped in pronunciation despite being present in the orthography. This process is known as schwa deletion. There are no known linguistic rules that can consistently and accurately predict what happens to the inherent vowel in speech. Thus, this is an open problem in the field.

Each paper below has used different datasets. The dataset for Arora et al. (2020) is the largest of all, extracted from the Oxford Hindi-English Dictionary, and future work should ideally compare against that dataset.

| Model | Schwa-level accuracy | Word-level accuracy | Paper / Source | Code |
| ----- | :------------------: | :-----------------: | -------------- | ---- |
| Arora et al. (2020) | 98.00 | 97.78 | [Supervised Grapheme-to-Phoneme Conversion of Orthographic Schwas in Hindi and Punjabi](https://www.aclweb.org/anthology/2020.acl-main.696.pdf) | [schwa-deletion](https://github.com/aryamanarora/schwa-deletion) |
| Tyson and Nagar (2009) | | 95.00 | [Prosodic rules for schwa-deletion in hindi text-to-speech synthesis](http://www.academia.edu/download/38321628/tyson_nagar_2009.pdf) | |
| Narasimhan et al. (2004) | | 88.97 | [Schwa-Deletion in Hindi Text-to-Speech Synthesis](https://pure.mpg.de/rest/items/item_59025/component/file_59026/content) | | 
| Choudhury et al. (2004) | | 99.89 | [A Diachronic Approach for Schwa Deletion in Indo Aryan Languages](https://www.aclweb.org/anthology/W04-0103.pdf) | |
