# Semantic textual similarity

Semantic textual similarity deals with determining how similar two pieces of texts are.
This can take the form of assigning a score from 1 to 5. Related tasks are paraphrase or duplicate identification.

### SentEval

[SentEval](https://arxiv.org/abs/1803.05449) is an evaluation toolkit for evaluating sentence
representations. It includes 17 downstream tasks, including common semantic textual similarity
tasks. The semantic textual similarity (STS) benchmark tasks from 2012-2016 (STS12, STS13, STS14, STS15, STS16, STSB) measure the relatedness
of two sentences based on the cosine similarity of the two representations. The evaluation criterion is Pearson correlation.

The SICK relatedness (SICK-R) task trains a linear model to output a score from 1 to 5 indicating the relatedness of two sentences. For
the same dataset (SICK-E) can be treated as a binary classification problem using the entailment labels.
The evaluation metric for SICK-R is Pearson correlation and classification accuracy for SICK-E.

The Microsoft Research Paraphrase Corpus (MRPC) corpus is a paraphrase identification dataset, where systems
aim to identify if two sentences are paraphrases of each other. The evaluation metric is classification accuracy and F1.

The data can be downloaded from [here](https://github.com/facebookresearch/SentEval).

| Model           | MRPC | SICK-R | SICK-E | STS | Paper / Source | Code |
| ------------- | :-----:| :-----:| :-----:| :-----:| --- | --- |
| GenSen (Subramanian et al., 2018) | 78.6/84.4 | 0.888 | 87.8 | 78.9/78.6 | [Learning General Purpose Distributed Sentence Representations via Large Scale Multi-task Learning](https://arxiv.org/abs/1804.00079) | [Official](https://github.com/Maluuba/gensen) |
| InferSent (Conneau et al., 2017) | 76.2/83.1 | 0.884 | 86.3 | 75.8/75.5 | [Supervised Learning of Universal Sentence Representations from Natural Language Inference Data](https://arxiv.org/abs/1705.02364) | [Official](https://github.com/facebookresearch/InferSent) |
| TF-KLD (Ji and Eisenstein, 2013) | 80.4/85.9 | - | - | - | [Discriminative Improvements to Distributional Sentence Similarity](http://www.aclweb.org/anthology/D/D13/D13-1090.pdf) |  |

## Paraphrase identification

### Quora Question Pairs

The [Quora Question Pairs dataset](https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs)
consists of over 400,000 pairs of questions on Quora. Systems must identify whether one question is a
duplicate of the other. Models are evaluated based on accuracy.

| Model           | Accuracy  |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| DIIN (Gong et al., 2018) | 89.06 | [Natural Language Inference Over Interaction Space](https://arxiv.org/pdf/1709.04348.pdf) | [Official](https://github.com/YichenGong/Densely-Interactive-Inference-Network) |
| pt-DecAtt (Char) (Tomar et al., 2017) | 88.40 | [Neural Paraphrase Identification of Questions with Noisy Pretraining](https://arxiv.org/abs/1704.04565) | |
| BiMPM (Wang et al., 2017) | 88.17 | [Bilateral Multi-Perspective Matching for Natural Language Sentences](https://arxiv.org/abs/1702.03814) | [Official](https://github.com/zhiguowang/BiMPM) |
| GenSen (Subramanian et al., 2018) | 87.01 | [Learning General Purpose Distributed Sentence Representations via Large Scale Multi-task Learning](https://arxiv.org/abs/1804.00079) | [Official](https://github.com/Maluuba/gensen) |

[Go back to the README](../README.md)
