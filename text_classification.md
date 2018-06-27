# Text classification

Text classification is the task of assigning a sentence or document an appropriate category.
The categories depend on the chosen dataset and can range from topics.

### AG News

The [AG News corpus](https://papers.nips.cc/paper/5782-character-level-convolutional-networks-for-text-classification.pdf)
consists of news articles from the [AG's corpus of news articles on the web](http://www.di.unipi.it/~gulli/AG_corpus_of_news_articles.html)
pertaining to the 4 largest classes. The dataset contains 30,000 training examples for each class
1,900 examples for each class for testing. Models are evaluated based on error rate (lower is better).

| Model           | Error  |  Paper / Source | Code |
| ------------- | :-----:| --- | :-----: |
| ULMFiT (Howard and Ruder, 2018) | 5.01 | [Universal Language Model Fine-tuning for Text Classification](https://arxiv.org/abs/1801.06146) | [Official](https://github.com/fastai/fastai/tree/master/courses/dl2/imdb_scripts) |
| CNN (Johnson and Zhang, 2016) * | 6.57 | [Supervised and Semi-Supervised Text Categorization using LSTM for Region Embeddings](https://arxiv.org/abs/1602.02373) |
| DPCNN (Johnson and Zhang, 2017) | 6.87 | [Deep Pyramid Convolutional Neural Networks for Text Categorization](http://aclweb.org/anthology/P17-1052) |
| VDCN (Alexis et al., 2016) | 8.67 | [Very Deep Convolutional Networks for Text Classification](https://arxiv.org/abs/1606.01781) |
| Char-level CNN (Zhang et al., 2015) | 9.51 | [Character-level Convolutional Networks for Text Classification](https://papers.nips.cc/paper/5782-character-level-convolutional-networks-for-text-classification.pdf) |

\* Results reported in Johnson and Zhang, 2017

### DBpedia

The [DBpedia ontology](https://papers.nips.cc/paper/5782-character-level-convolutional-networks-for-text-classification.pdf) 
dataset contains 40,000 training samples and 5,000 testing samples for each of 14 nonoverlapping classes from DBpedia.
Models are evaluated based on error rate (lower is better).

| Model           | Error  |  Paper / Source | Code |
| ------------- | :-----:| --- | :-----: |
| ULMFiT (Howard and Ruder, 2018) | 0.80 | [Universal Language Model Fine-tuning for Text Classification](https://arxiv.org/abs/1801.06146)  | [Official](https://github.com/fastai/fastai/tree/master/courses/dl2/imdb_scripts) |
| CNN (Johnson and Zhang, 2016) | 0.84 | [Supervised and Semi-Supervised Text Categorization using LSTM for Region Embeddings](https://arxiv.org/abs/1602.02373) |
| DPCNN (Johnson and Zhang, 2017) | 0.88 | [Deep Pyramid Convolutional Neural Networks for Text Categorization](http://aclweb.org/anthology/P17-1052) |
| VDCN (Alexis et al., 2016) | 1.29 | [Very Deep Convolutional Networks for Text Classification](https://arxiv.org/abs/1606.01781) |
| Char-level CNN (Zhang et al., 2015) | 1.55 | [Character-level Convolutional Networks for Text Classification](https://papers.nips.cc/paper/5782-character-level-convolutional-networks-for-text-classification.pdf) |

### TREC

The [TREC dataset](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.11.2766&rep=rep1&type=pdf) is dataset for
question classification consisting of open-domain, fact-based questions divided into broad semantic categories. 
It has both a six-class (TREC-6) and a fifty-class (TREC-50) version. Both have 4,300 training examples, 
but TREC-50 has finer-grained labels. Models are evaluated based on accuracy.

TREC-6:

| Model           | Error  |  Paper / Source | Code |
| ------------- | :-----:| --- | :-----: |
| ULMFiT (Howard and Ruder, 2018) | 3.6 | [Universal Language Model Fine-tuning for Text Classification](https://arxiv.org/abs/1801.06146) | [Official](https://github.com/fastai/fastai/tree/master/courses/dl2/imdb_scripts) |
| LSTM-CNN (Zhou et al., 2016) | 3.9 | [Text Classification Improved by Integrating Bidirectional LSTM with Two-dimensional Max Pooling](http://www.aclweb.org/anthology/C16-1329) |
| TBCNN (Mou et al., 2015) | 4 | [Discriminative Neural Sentence Modeling by Tree-Based Convolution](http://aclweb.org/anthology/D15-1279) |
| CoVe (McCann et al., 2017) | 4.2 | [Learned in Translation: Contextualized Word Vectors](https://arxiv.org/abs/1708.00107) |

TREC-50:

| Model           | Error  |  Paper / Source | Code |
| ------------- | :-----:| --- | :-----: |
| Rules (Madabushi and Lee, 2016) | 2.8 |[High Accuracy Rule-based Question Classification using Question Syntax and Semantics](http://www.aclweb.org/anthology/C16-1116)| |
| SVM (Van-Tu and Anh-Cuong, 2016) | 8.4 | [Improving Question Classification by Feature Extraction and Selection](https://www.researchgate.net/publication/303553351_Improving_Question_Classification_by_Feature_Extraction_and_Selection) | |

[Go back to the README](README.md)
