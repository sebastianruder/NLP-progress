# Part-of-speech tagging

Part-of-speech tagging (POS tagging) is the task of tagging a word in a text with its part of speech.
A part of speech is a category of words with similar grammatical properties. Common English
parts of speech are noun, verb, adjective, adverb, pronoun, preposition, conjunction, etc.

Example: 

| Vinken | , | 61 | years | old |
| --- | ---| --- | --- | --- |
| NNP | , | CD | NNS | JJ |

### Penn Treebank

A standard dataset for POS tagging is the Wall Street Journal (WSJ) portion of the Penn Treebank, containing 45 
different POS tags. Sections 0-18 are used for training, sections 19-21 for development, and sections 
22-24 for testing. Models are evaluated based on accuracy.

| Model           | Accuracy  |  Paper / Source |
| ------------- | :-----:| --- |
| Meta BiLSTM (Bohnet et al., 2018) | 97.96 | [Morphosyntactic Tagging with a Meta-BiLSTM Model over Context Sensitive Tokenn Encodings](https://arxiv.org/abs/1805.08237) |
| Char Bi-LSTM (Ling et al., 2015) | 97.78 | [Finding Function in Form: Compositional Character Models for Open Vocabulary Word Representation](https://www.aclweb.org/anthology/D/D15/D15-1176.pdf) |
| Adversarial Bi-LSTM (Yasunaga et al., 2018) | 97.59 | [Robust Multilingual Part-of-Speech Tagging via Adversarial Training](https://arxiv.org/abs/1711.04903) | 
| Yang et al. (2017) | 97.55 | [Transfer Learning for Sequence Tagging with Hierarchical Recurrent Networks](https://arxiv.org/abs/1703.06345) |
| Ma and Hovy (2016) | 97.55 | [End-to-end Sequence Labeling via Bi-directional LSTM-CNNs-CRF](https://arxiv.org/abs/1603.01354) |
| Feed Forward (Vaswani et a. 2016) | 97.4 | [Supertagging with LSTMs](https://aclweb.org/anthology/N/N16/N16-1027.pdf) |
| Bi-LSTM (Ling et al., 2017) | 97.36 | [Finding Function in Form: Compositional Character Models for Open Vocabulary Word Representation](https://www.aclweb.org/anthology/D/D15/D15-1176.pdf) | | 
| Bi-LSTM (Plank et al., 2016) | 97.22 | [Multilingual Part-of-Speech Tagging with Bidirectional Long Short-Term Memory Models and Auxiliary Loss](https://arxiv.org/abs/1604.05529) | 


### Social media

The [Ritter (2011)](https://aclanthology.coli.uni-saarland.de/papers/D11-1141/d11-1141) dataset has become the benchmark for social media part-of-speech tagging. This is comprised of  some 50K tokens of English social media sampled in late 2011, and is tagged using an extended version of the PTB tagset.

| Model | Accuracy | Paper |
| --- | --- | ---|
| GATE  | 88.69 | [Twitter Part-of-Speech Tagging for All: Overcoming Sparse and Noisy Data](https://aclanthology.coli.uni-saarland.de/papers/R13-1026/r13-1026) | 
| CMU | 90.0 ± 0.5 | [Improved Part-of-Speech Tagging for Online Conversational Text with Word Clusters](http://www.cs.cmu.edu/~ark/TweetNLP/owoputi+etal.naacl13.pdf) | 


### UD

[Universal Dependencies (UD)](http://universaldependencies.org/) is a framework for 
cross-linguistic grammatical annotation, which contains more than 100 treebanks in over 60 languages.
Models are typically evaluated based on the average test accuracy across 28 languages.

| Model           | Avg accuracy  |  Paper / Source |
| ------------- | :-----:| --- |
| Adversarial Bi-LSTM (Yasunaga et al., 2018) | 96.73 | [Robust Multilingual Part-of-Speech Tagging via Adversarial Training](https://arxiv.org/abs/1711.04903) | 
| Bi-LSTM (Plank et al., 2016) | 96.40 | [Multilingual Part-of-Speech Tagging with Bidirectional Long Short-Term Memory Models and Auxiliary Loss](https://arxiv.org/abs/1604.05529) | 
| Joint Bi-LSTM (Nguyen et al., 2017) | 95.55 | [A Novel Neural Network Model for Joint POS Tagging and Graph-based Dependency Parsing](https://arxiv.org/abs/1705.05952) |

[Go back to the README](README.md)
