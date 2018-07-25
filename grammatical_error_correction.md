# Grammatical Error Correction

Grammatical Error Correction (GEC) is the task of correcting grammatical mistakes in a sentence.


| Error           | Corrected     |
| -------------   | ------------- |
|She see Tom is catched by policeman in park at last night. | She saw Tom caught by a policeman in the park last night.|

### CoNLL-2014

CoNLL-14 benchmark is done on the [test split](https://www.comp.nus.edu.sg/~nlp/conll14st/conll14st-test-data.tar.gz) of [NUS Corpus of Learner English/NUCLE](https://www.comp.nus.edu.sg/~nlp/corpora.html) dataset.
CoNLL-2014 test set contains 1,312 english sentences with grammatical error correction annotations by 2 annotators. Models are evaluated with [F-score](https://en.wikipedia.org/wiki/F1_score) with β=0.5 which weighs precision twice as recall.


| Model           | F0.5  |  Paper / Source | Code |
| ------------- | :-----:| --- | :-----: |
| CNN Seq2Seq + Fluency Boost (Ge et al., 2018) |  61.34 | [Reaching Human-level Performance in Automatic Grammatical Error Correction: An Empirical Study](https://arxiv.org/abs/1807.01270)| NA |
| SMT + BiGRU (Grundkiewicz et al., 2018) |  56.25 | [Near Human-Level Performance in Grammatical Error Correction with Hybrid Machine Translation](https://arxiv.org/abs/1804.05945)| NA |
| Transformer (Junczys-Dowmunt et al., 2018) | 55.8 | [Approaching Neural Grammatical Error Correction as a Low-Resource Machine Translation Task](http://aclweb.org/anthology/N18-1055)| NA |
| CNN Seq2Seq (Chollampatt & Ng, 2018)| 54.79 | [ A Multilayer Convolutional Encoder-Decoder Neural Network for Grammatical Error Correction](https://arxiv.org/abs/1801.08831)| [Official](https://github.com/nusnlp/mlconvgec2018) |



### CoNLL-2014 10 Annotators

[Bryant and Ng 2015](https://pdfs.semanticscholar.org/f76f/fd242c3dc88e52d1f427cdd0f5dccd814937.pdf) used 10 annotators to do grammatical error correction on CoNll-14's [1312 sentences](http://www.comp.nus.edu.sg/~nlp/sw/10gec_annotations.zip).

| Model           | F0.5  |  Paper / Source | Code |
| ------------- | :-----:| --- | :-----: |
| CNN Seq2Seq + Fluency Boost (Ge et al., 2018) |  76.88 | [Reaching Human-level Performance in Automatic Grammatical Error Correction: An Empirical Study](https://arxiv.org/abs/1807.01270)| NA |
| SMT + BiGRU (Grundkiewicz et al., 2018) |  72.04 | [Near Human-Level Performance in Grammatical Error Correction with Hybrid Machine Translation](https://arxiv.org/abs/1804.05945)| NA |
| CNN Seq2Seq (Chollampatt & Ng, 2018)| 70.14 (measured by Ge et al., 2018) | [ A Multilayer Convolutional Encoder-Decoder Neural Network for Grammatical Error Correction](https://arxiv.org/abs/1801.08831)| [Official](https://github.com/nusnlp/mlconvgec2018) |



### JFLEG

[JFLEG corpus](https://github.com/keisks/jfleg) by [Napoles et al., 2017](https://arxiv.org/abs/1702.04066) consists of 1,511 english sentences with annotations. Models are evaluated with [GLEU metric](https://arxiv.org/abs/1609.08144).

| Model           | GLEU  |  Paper / Source | Code |
| ------------- | :-----:| --- | :-----: |
| CNN Seq2Seq + Fluency Boost and inference (Ge et al., 2018) |  62.37 | [Reaching Human-level Performance in Automatic Grammatical Error Correction: An Empirical Study](https://arxiv.org/abs/1807.01270)| NA |
| SMT + BiGRU (Grundkiewicz et al., 2018) |  61.50 | [Near Human-Level Performance in Grammatical Error Correction with Hybrid Machine Translation](https://arxiv.org/abs/1804.05945)| NA |
| Transformer (Junczys-Dowmunt et al., 2018) | 59.9 | [Approaching Neural Grammatical Error Correction as a Low-Resource Machine Translation Task](http://aclweb.org/anthology/N18-1055)| NA |
| CNN Seq2Seq (Chollampatt & Ng, 2018)| 57.47 | [ A Multilayer Convolutional Encoder-Decoder Neural Network for Grammatical Error Correction](https://arxiv.org/abs/1801.08831)| [Official](https://github.com/nusnlp/mlconvgec2018) |
