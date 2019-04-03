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
| MT-DNN (Liu et al., 2019) | 95.6 | [Multi-Task Deep Neural Networks for Natural Language Understanding](https://arxiv.org/abs/1901.11504) |
| Bidirectional Encoder Representations from Transformers (Devlin et al., 2018) | 94.9 | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) |
| Block-sparse LSTM (Gray et al., 2017) | 93.2 | [GPU Kernels for Block-Sparse Weights](https://s3-us-west-2.amazonaws.com/openai-assets/blocksparse/blocksparsepaper.pdf) |
| bmLSTM (Radford et al., 2017) | 91.8 | [Learning to Generate Reviews and Discovering Sentiment](https://arxiv.org/abs/1704.01444) |
| Single layer bilstm distilled from BERT (Tang et al., 2019)| 90.7 |[Distilling Task-Specific Knowledge from BERT into Simple Neural Networks](https://arxiv.org/abs/1903.12136)|
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
3,862 of which contain a single target, and the remainder multiple targets.

Dataset mirror: https://github.com/uclmr/jack/tree/master/data/sentihood

| Model           | Aspect (F1) | Sentiment (acc) |  Paper / Source |  Code |
| ------------- | :-----:| :-----:| --- | --- |
| Sun et al. (2019) | 87.9 | 93.6 | [Utilizing BERT for Aspect-Based Sentiment Analysis via Constructing Auxiliary Sentence](https://arxiv.org/pdf/1903.09588.pdf) | [Official](https://github.com/HSLCY/ABSA-BERT-pair)
| Liu et al. (2018) | 78.5 | 91.0 | [Recurrent Entity Networks with Delayed Memory Update for Targeted Aspect-based Sentiment Analysis](http://aclweb.org/anthology/N18-2045) | [Official](https://github.com/liufly/delayed-memory-update-entnet)
| SenticLSTM (Ma et al., 2018) | 78.2 | 89.3 | [Targeted Aspect-Based Sentiment Analysis via Embedding Commonsense Knowledge into an Attentive LSTM](http://sentic.net/sentic-lstm.pdf) | 
| LSTM-LOC (Saeidi et al., 2016) | 69.3 | 81.9 | [Sentihood: Targeted aspect based sentiment analysis dataset for urban neighbourhoods](http://www.aclweb.org/anthology/C16-1146) |

### SemEval-2014 Task 4

The [SemEval-2014 Task 4](http://alt.qcri.org/semeval2014/task4/) contains two domain-specific datasets for laptops and restaurants, consisting of over 6K sentences with fine-grained aspect-level human annotations.

The task consists of the following subtasks:

- Subtask 1: Aspect term extraction

- Subtask 2: Aspect term polarity

- Subtask 3: Aspect category detection

- Subtask 4: Aspect category polarity

Preprocessed dataset: https://github.com/songyouwei/ABSA-PyTorch/tree/master/datasets/semeval14

Subtask 2 results:

| Model           | Restaurant (acc) | Laptop (acc) |  Paper / Source |  Code |
| ------------- | :-----:| :-----:| --- | --- |
| AOA (Huang, Binxuan, et al., 2018) | 81.20 | 74.50 | [Aspect Level Sentiment Classification with Attention-over-Attention Neural Networks](https://arxiv.org/pdf/1804.06536.pdf) | [Link](https://github.com/songyouwei/ABSA-PyTorch/blob/master/models/aoa.py)
| TNet (Li, Xin, et al., 2018) | 80.79 | 76.01 | [Transformation Networks for Target-Oriented Sentiment Classification](http://aclweb.org/anthology/P18-1087) | [Official](https://github.com/lixin4ever/TNet) / [Link](https://github.com/songyouwei/ABSA-PyTorch/blob/master/models/tnet_lf.py)
| RAM (Chen, Peng, et al., 2017) | 80.23 | 74.49 | [Recurrent Attention Network on Memory for Aspect Sentiment Analysis](http://www.aclweb.org/anthology/D17-1047) | [Link](https://github.com/songyouwei/ABSA-PyTorch/blob/master/models/ram.py)
| MemNet (Tang, Duyu, et al., 2016) | 80.95 | 72.21 | [Aspect Level Sentiment Classification with Deep Memory Network](https://pdfs.semanticscholar.org/b28f/7e2996b6ee2784dd2dbb8212cfa0c79ba9e7.pdf) | [Official](https://drive.google.com/open?id=1Hc886aivHmIzwlawapzbpRdTfPoTyi1U) / [Link](https://github.com/songyouwei/ABSA-PyTorch/blob/master/models/memnet.py)
| IAN (Ma, Dehong, et al., 2017) | 78.60 | 72.10 | [Interactive Attention Networks for Aspect-Level Sentiment Classification](http://www.ijcai.org/proceedings/2017/0568.pdf) | [Link](https://github.com/songyouwei/ABSA-PyTorch/blob/master/models/ian.py)
| ATAE-LSTM (Wang, Yequan, et al. 2016) | 77.20 | 68.70 | [Attention-based lstm for aspect-level sentiment classification](https://aclweb.org/anthology/D16-1058) | [Link](https://github.com/songyouwei/ABSA-PyTorch/blob/master/models/atae_lstm.py)
| TD-LSTM (Tang, Duyu, et al., 2016) | 75.63 | 68.13 | [Effective LSTMs for Target-Dependent Sentiment Classification](https://www.aclweb.org/anthology/C/C16/C16-1311.pdf) | [Official](https://drive.google.com/open?id=17RF8MZs456ov9MDiUYZp0SCGL6LvBQl6) / [Link](https://github.com/songyouwei/ABSA-PyTorch/blob/master/models/td_lstm.py)

## Sentiment classification with user and product information

This is the same task on sentiment classification, where the given text is a review, but we are also additionally given (a) the *user* who wrote the text, and (b) the *product* which the text is written for. There are three widely used datasets, introduced by [Tang et. al (2015)](http://aclweb.org/anthology/P15-1098): IMDB, Yelp 2013, and Yelp 2014. Evaluation is done using both accuracy and RMSE, but for brevity, we only provide the accuracy here. Please look at the papers for the RMSE values.

| Model              | IMDB (acc) | Yelp 2013 (acc) | Yelp 2014 (acc) | Paper / Source | Code |
| ------------------ | :--------: | :-------------: | :-------------: | -------------- | ---- |
| BiLSTM + linear-basis-cust (Kim, Jihyeok, et al., 2019) | - | 67.1 | - | [Categorical Metadata Representation for Customized Text Classification](https://arxiv.org/pdf/1902.05196.pdf) | [Link](https://github.com/zizi1532/BasisCustomize) |
| CMA (Ma, Dehong, et al., 2017) | 54.0 | 66.4 | 67.6 | [Cascading Multiway Attention for Document-level Sentiment Classification](http://aclweb.org/anthology/I17-1064) | - |
| DUPMN (Long, Yunfei, et al., 2018) | 53.9 | 66.2 | 67.6 | [Dual Memory Network Model for Biased Product Review Classification](http://aclweb.org/anthology/W18-6220) | - |
| HCSC (Amplayo, Reinald Kim, et al., 2018) | 54.2 | 65.7 | - | [Cold-Start Aware User and Product Attention for Sentiment Classification](http://aclweb.org/anthology/P18-1236) | [Link](https://github.com/rktamplayo/HCSC) |
| NSC (Chen, Huimin, et al., 2016) | 53.3 | 65.0 | 66.7 | [Neural Sentiment Classification with User and Product Attention](http://aclweb.org/anthology/D16-1171) | [Link](https://github.com/thunlp/NSC) |
| UPDMN (Dou, Zi-Yi, 2017) | 46.5 | 63.9 | 61.3 | [Capturing User and Product Information for Document Level Sentiment Analysis with Deep Memory Network](http://aclweb.org/anthology/D17-1054) | - |
| UPNN (Tang, Duyu, et al., 2016) | 43.5 | 59.6 | 60.8 | [Learning Semantic Representations of Users and Products for Document Level Sentiment Classification](http://aclweb.org/anthology/P15-1098) | [Link](http://ir.hit.edu.cn/~dytang/paper/acl2015/UserTextNN.zip) |

# Subjectivity analysis

A related task to sentiment analysis is the subjectivity analysis with the goal of labeling an opinion as either subjective or objective.

### SUBJ

[Subjectivity dataset](http://www.cs.cornell.edu/people/pabo/movie-review-data/) includes 5,000 subjective and 5,000 objective processed sentences. 

| Model           | Accuracy |  Paper / Source |
| ------------- | :-----:| --- |
| AdaSent (Zhao et al., 2015) | 95.50 | [Self-Adaptive Hierarchical Sentence Model](https://arxiv.org/pdf/1504.05070.pdf) |
| CNN+MCFA (Amplayo et al., 2018) | 94.80 | [Translations as Additional Contexts for Sentence Classification](https://arxiv.org/abs/1806.05516) |
| Byte mLSTM (Radford et al., 2017) | 94.60 | [Learning to Generate Reviews and Discovering Sentiment](https://arxiv.org/pdf/1704.01444.pdf) |
| USE (Cer et al., 2018) | 93.90 | [Universal Sentence Encoder](https://arxiv.org/pdf/1803.11175.pdf) |
| Fast Dropout (Wang and Manning, 2013) | 93.60 | [Fast Dropout Training](http://proceedings.mlr.press/v28/wang13a.pdf) |

[Go back to the README](../README.md)
