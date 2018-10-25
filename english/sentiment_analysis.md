# Sentiment analysis

Sentiment analysis is the task of classifying the polarity of a given text.

### IMDb

The [IMDb dataset](https://ai.stanford.edu/~ang/papers/acl11-WordVectorsSentimentAnalysis.pdf) is a binary
sentiment analysis dataset consisting of 50,000 reviews from the Internet Movie Database (IMDb) labeled as positive or
negative. The dataset contains an even number of positive and negative reviews. Only highly polarizing reviews are considered. 
A negative review has a score ≤ 4 out of 10, and a positive review has a score ≥ 7 out of 10. No more than 30 reviews are 
included per movie. Models are evaluated based on accuracy.

| Model           | Accuracy  |  Paper / Source |
| ------------- | :-----:| --- |
| ULMFiT (Howard and Ruder, 2018) | 95.4 | [Universal Language Model Fine-tuning for Text Classification](https://arxiv.org/abs/1801.06146) |
| Block-sparse LSTM (Gray et al., 2017) | 94.99 | [GPU Kernels for Block-Sparse Weights](https://s3-us-west-2.amazonaws.com/openai-assets/blocksparse/blocksparsepaper.pdf) |
| oh-LSTM (Johnson and Zhang, 2016) | 94.1 | [Supervised and Semi-Supervised Text Categorization using LSTM for Region Embeddings](https://arxiv.org/abs/1602.02373) |
| Virtual adversarial training (Miyato et al., 2016) | 94.1 | [Adversarial Training Methods for Semi-Supervised Text Classification](https://arxiv.org/abs/1605.07725) |
| BCN+Char+CoVe (McCann et al., 2017) | 91.8 | [Learned in Translation: Contextualized Word Vectors](https://arxiv.org/abs/1708.00107) |

### SST

The [Stanford Sentiment Treebank](https://nlp.stanford.edu/sentiment/index.html) 
contains of 215,154 phrases with fine-grained sentiment labels in the parse trees
of 11,855 sentences in movie reviews. Models are evaluated either on fine-grained
(five-way) or binary classification based on accuracy.

Fine-grained classification (SST-5, 94,2k examples):

| Model           | Accuracy |  Paper / Source |
| ------------- | :-----:| --- |
| BCN+ELMo (Peters et al., 2018) | 54.7 | [Deep contextualized word representations](https://arxiv.org/abs/1802.05365) |
| BCN+Char+CoVe (McCann et al., 2017) | 53.7 | [Learned in Translation: Contextualized Word Vectors](https://arxiv.org/abs/1708.00107) |

Binary classification (SST-2, 56.4k examples):

| Model           | Accuracy  |  Paper / Source |
| ------------- | :-----:| --- |
| Block-sparse LSTM (Gray et al., 2017) | 93.2 | [GPU Kernels for Block-Sparse Weights](https://s3-us-west-2.amazonaws.com/openai-assets/blocksparse/blocksparsepaper.pdf) |
| bmLSTM (Radford et al., 2017) | 91.8 | [Learning to Generate Reviews and Discovering Sentiment](https://arxiv.org/abs/1704.01444) |
| BCN+Char+CoVe (McCann et al., 2017) | 90.3 | [Learned in Translation: Contextualized Word Vectors](https://arxiv.org/abs/1708.00107)
| Neural Semantic Encoder (Munkhdalai and Yu, 2017) | 89.7 | [Neural Semantic Encoders](http://www.aclweb.org/anthology/E17-1038) | 
| BLSTM-2DCNN (Zhou et al., 2017) | 89.5 | [Text Classification Improved by Integrating Bidirectional LSTM with Two-dimensional Max Pooling](http://www.aclweb.org/anthology/C16-1329) |

### Yelp

The [Yelp Review dataset](https://papers.nips.cc/paper/5782-character-level-convolutional-networks-for-text-classification.pdf)
consists of more than 500,000 Yelp reviews. There is both a binary and a fine-grained (five-class)
version of the dataset. Models are evaluated based on error (1 - accuracy; lower is better).

Fine-grained classification: 

| Model           | Error  |  Paper / Source |
| ------------- | :-----:| --- |
| ULMFiT (Howard and Ruder, 2018) | 29.98 | [Universal Language Model Fine-tuning for Text Classification](https://arxiv.org/abs/1801.06146) |
| DPCNN (Johnson and Zhang, 2017) | 30.58 | [Deep Pyramid Convolutional Neural Networks for Text Categorization](http://aclweb.org/anthology/P17-1052) |
| CNN (Johnson and Zhang, 2016) | 32.39 | [Supervised and Semi-Supervised Text Categorization using LSTM for Region Embeddings](https://arxiv.org/abs/1602.02373) |
| Char-level CNN (Zhang et al., 2015) | 37.95 | [Character-level Convolutional Networks for Text Classification](https://papers.nips.cc/paper/5782-character-level-convolutional-networks-for-text-classification.pdf) |

Binary classification:

| Model           | Error |  Paper / Source |
| ------------- | :-----:| --- |
| ULMFiT (Howard and Ruder, 2018) | 2.16 | [Universal Language Model Fine-tuning for Text Classification](https://arxiv.org/abs/1801.06146) |
| DPCNN (Johnson and Zhang, 2017) | 2.64 | [Deep Pyramid Convolutional Neural Networks for Text Categorization](http://aclweb.org/anthology/P17-1052) |
| CNN (Johnson and Zhang, 2016) | 2.90 | [Supervised and Semi-Supervised Text Categorization using LSTM for Region Embeddings](https://arxiv.org/abs/1602.02373) |
| Char-level CNN (Zhang et al., 2015) | 4.88 | [Character-level Convolutional Networks for Text Classification](https://papers.nips.cc/paper/5782-character-level-convolutional-networks-for-text-classification.pdf) |


### SemEval
SemEval (International Workshop on Semantic Evaluation) has a specific task for Sentiment analysis.
Latest year overview of such task (Task 4) can be reached at: http://www.aclweb.org/anthology/S17-2088

SemEval-2017 Task 4 consists of five subtasks, each offered for both Arabic and English:

1. Subtask A: Given a tweet, decide whether it expresses POSITIVE, NEGATIVE or NEUTRAL
sentiment.

2. Subtask B: Given a tweet and a topic, classify the sentiment conveyed towards that
topic on a two-point scale: POSITIVE vs. NEGATIVE.

3. Subtask C: Given a tweet and a topic, classify the sentiment conveyed in the
tweet towards that topic on a five-point scale: STRONGLYPOSITIVE, WEAKLYPOSITIVE,
NEUTRAL, WEAKLYNEGATIVE, and STRONGLYNEGATIVE.

4. Subtask D: Given a set of tweets about a topic, estimate the distribution of tweets
across the POSITIVE and NEGATIVE classes. 

5. Subtask E: Given a set of tweets about a topic, estimate the distribution of tweets
across the five classes: STRONGLYPOSITIVE, WEAKLYPOSITIVE, NEUTRAL, WEAKLYNEGATIVE, and STRONGLYNEGATIVE.

Subtask A  results:

| Model           | F1-score |  Paper / Source |
| ------------- | :-----:| --- |
| LSTMs+CNNs ensemble with multiple conv. ops (Cliche. 2017) | 0.685 | [BB twtr at SemEval-2017 Task 4: Twitter Sentiment Analysis with CNNs and LSTMs](http://www.aclweb.org/anthology/S17-2094) |
| Deep Bi-LSTM+attention (Baziotis et al., 2017) | 0.677 | [DataStories at SemEval-2017 Task 4: Deep LSTM with Attention for Message-level and Topic-based Sentiment Analysis](http://aclweb.org/anthology/S17-2126) |


## Aspect-based sentiment analysis

### Sentihood

[Sentihood](http://www.aclweb.org/anthology/C16-1146) is a dataset for targeted aspect-based sentiment analysis (TABSA), which aims
to identify fine-grained polarity towards a specific aspect. The dataset consists of 5,215 sentences,
3,862 of which contain a single target, and the remainder multiple targets. F1 is used as evaluation metric
for aspect detection and accuracy as evaluation metric for sentiment analysis.

| Model           | Aspect  | Sentiment |  Paper / Source |  Code |
| ------------- | :-----:| :-----:| --- | --- |
| Liu et al. (2018) | 78.5 | 91.0 | [Recurrent Entity Networks with Delayed Memory Update for Targeted Aspect-based Sentiment Analysis](http://aclweb.org/anthology/N18-2045) | [Official](https://github.com/liufly/delayed-memory-update-entnet)
| SenticLSTM (Ma et al., 2018) | 78.2 | 89.3 | [Targeted Aspect-Based Sentiment Analysis via Embedding Commonsense Knowledge into an Attentive LSTM](http://sentic.net/sentic-lstm.pdf) | 
| LSTM-LOC (Saeidi et al., 2016) | 69.3 | 81.9 | [Sentihood: Targeted aspect based sentiment analysis dataset for urban neighbourhoods](http://www.aclweb.org/anthology/C16-1146) |

# Subjectivity analysis

A related task to sentiment analysis is the subjectivity analysis with the goal of labeling an opinion as either subjective or objective.

### SUBJ

[Subjectivity dataset](http://www.cs.cornell.edu/people/pabo/movie-review-data/) includes 5,000 subjective and 5,000 objective processed sentences. 

| Model           | Accuracy |  Paper / Source |
| ------------- | :-----:| --- |
| USE (Cer et al., 2018) | 93.90 | [Universal Sentence Encoder](https://arxiv.org/pdf/1803.11175.pdf) |
| Fast Dropout (Wang and Manning, 2013) | 93.60 | [Fast Dropout Training](http://proceedings.mlr.press/v28/wang13a.pdf) |

[Go back to the README](../README.md)
