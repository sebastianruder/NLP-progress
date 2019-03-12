# Chinese Word Segmentation

## Task
Chinese word segmentation is the task of
splitting Chinese text (a sequence of Chinese characters)
into words.

Example:
```
'上海浦东开发与建设同步' → ['上海', '浦东', '开发', ‘与', ’建设', '同步']
```

## Systems
&spades; marks the system that uses character unigram as input.
&clubs; marks the systme that uses character bigram as input.

- Huang et al. (2019): BERT + model compression + multi-criterial learing &spades;
- Yang et al. (2018): Lattice LSTM-CRF + BPE subword embeddings &spades;&clubs; 
- Ma et al. (2018): BiLSTM-CRF + hyper-params search&spades;&clubs;
- Yang et al. (2017): Transition-based + Beam-search + Rich pretrain&spades;&clubs; 
- Zhou et al. (2017): Greedy Search + word context&spades;
- Chen et al. (2017): BiLSTM-CRF + adv. loss&spades;&clubs;
- Cai et al. (2017): Greedy Search+Span representation&spades;
- Kurita et al. (2017): Transition-based + Joint model&spades;
- Liu et al. (2016): neural semi-CRF&spades;
- Cai and Zhao (2016): Greedy Search&spades;
- Chen et al. (2015a): Gated Recursive NN&spades;&clubs;
- Chen et al. (2015b): BiLSTM-CRF&spades;&clubs;

## Evaluation

### Metrics

F1-score

### Dataset
#### Chinese Treebank 6

| Model         | F1 | Paper / Source | Code |
| ------------- | :-----: |  --- | --- |
| Huang et al. (2019) | 97.6 |[Toward Fast and Accurate Neural Chinese Word Segmentation with Multi-Criteria Learning](https://arxiv.org/pdf/1903.04190.pdf)||
| Ma et al. (2018) | 96.7 | [State-of-the-art Chinese Word Segmentation with Bi-LSTMs](https://aclweb.org/anthology/D18-1529)| |
| Yang et al. (2018) | 96.3 | [Subword Encoding in Lattice LSTM for Chinese Word Segmentation](https://arxiv.org/pdf/1810.12594.pdf) | [Github](https://github.com/jiesutd/SubwordEncoding-CWS)|
| Yang et al. (2017) | 96.2 | [Neural Word Segmentation with Rich Pretraining](http://aclweb.org/anthology/P17-1078) | [Github](https://github.com/jiesutd/RichWordSegmentor)|
| Zhou et al. (2017) | 96.2 | [Word-Context Character Embeddings for Chinese Word Segmentation](https://www.aclweb.org/anthology/D17-1079)| |
| Chen et al. (2017) | 96.2 | [Adversarial Multi-Criteria Learning for Chinese Word Segmentation](http://aclweb.org/anthology/P17-1110) | [Github](https://github.com/FudanNLP/adversarial-multi-criteria-learning-for-CWS) |
| Liu et al. (2016) | 95.5 | [Exploring Segment Representations for Neural Segmentation Models](https://www.ijcai.org/Proceedings/16/Papers/409.pdf)| [Github](https://github.com/Oneplus/segrep-for-nn-semicrf) |
| Chen et al. (2015b) | 96.0 | [Long Short-Term Memory Neural Networks for Chinese Word Segmentation](http://www.aclweb.org/anthology/D15-1141) | [Github](https://github.com/FudanNLP/CWS_LSTM) |

#### Chinese Treebank 7

| Model         | F1 | Paper / Source | Code |
| ------------- | :-----: |  --- | --- |
| Ma et al. (2018) | 96.6 | [State-of-the-art Chinese Word Segmentation with Bi-LSTMs](https://aclweb.org/anthology/D18-1529)| |
| Kurita et al. (2017) | 96.2 | [Neural Joint Model for Transition-based Chinese Syntactic Analysis](http://www.aclweb.org/anthology/P17-1111) | |
#### AS

| Model         | F1 | Paper / Source | Code |
| ------------- | :-----: |  --- | --- |
| Huang et al. (2019) | 96.6 | [Toward Fast and Accurate Neural Chinese Word Segmentation with Multi-Criteria Learning](https://arxiv.org/pdf/1903.04190.pdf)| |
| Ma et al. (2018) | 96.2 | [State-of-the-art Chinese Word Segmentation with Bi-LSTMs](https://aclweb.org/anthology/D18-1529)| |
| Yang et al. (2017) | 95.7 | [Neural Word Segmentation with Rich Pretraining](http://aclweb.org/anthology/P17-1078) |[Github](https://github.com/jiesutd/RichWordSegmentor) |
| Cai et al. (2017) | 95.3 | [Fast and Accurate Neural Word Segmentation for Chinese](http://aclweb.org/anthology/P17-2096) | [Github](https://github.com/jcyk/greedyCWS) |
| Chen et al. (2017) | 94.8 | [Adversarial Multi-Criteria Learning for Chinese Word Segmentation](http://aclweb.org/anthology/P17-1110) | [Github](https://github.com/FudanNLP/adversarial-multi-criteria-learning-for-CWS) |

#### CityU

| Model         | F1 | Paper / Source | Code |
| ------------- | :-----: |  --- | --- |
| Huang et al. (2019) | 97.6 | [Toward Fast and Accurate Neural Chinese Word Segmentation with Multi-Criteria Learning](https://arxiv.org/pdf/1903.04190.pdf)| |
| Ma et al. (2018) | 97.2 | [State-of-the-art Chinese Word Segmentation with Bi-LSTMs](https://aclweb.org/anthology/D18-1529)| |
| Yang et al. (2017) | 96.9 | [Neural Word Segmentation with Rich Pretraining](http://aclweb.org/anthology/P17-1078) | [Github](https://github.com/jiesutd/RichWordSegmentor)|
| Cai et al. (2017) | 95.6 | [Fast and Accurate Neural Word Segmentation for Chinese](http://aclweb.org/anthology/P17-2096) | [Github](https://github.com/jcyk/greedyCWS) |
| Chen et al. (2017) | 95.6 | [Adversarial Multi-Criteria Learning for Chinese Word Segmentation](http://aclweb.org/anthology/P17-1110) | [Github](https://github.com/FudanNLP/adversarial-multi-criteria-learning-for-CWS) |

#### PKU

| Model         | F1 | Paper / Source | Code |
| ------------- | :-----: |  --- | --- |
| Huang et al. (2019) | 96.6 | [Toward Fast and Accurate Neural Chinese Word Segmentation with Multi-Criteria Learning](https://arxiv.org/pdf/1903.04190.pdf)| |
| Yang et al. (2017) | 96.3 | [Neural Word Segmentation with Rich Pretraining](http://aclweb.org/anthology/P17-1078) | [Github](https://github.com/jiesutd/RichWordSegmentor)|
| Ma et al. (2018) | 96.1 | [State-of-the-art Chinese Word Segmentation with Bi-LSTMs](https://aclweb.org/anthology/D18-1529)| |
| Yang et al. (2018) | 95.9 | [Subword Encoding in Lattice LSTM for Chinese Word Segmentation](https://arxiv.org/pdf/1810.12594.pdf) | [Github](https://github.com/jiesutd/SubwordEncoding-CWS)|
| Cai et al. (2017) | 95.8 | [Fast and Accurate Neural Word Segmentation for Chinese](http://aclweb.org/anthology/P17-2096) | [Github](https://github.com/jcyk/greedyCWS) |
| Chen et al. (2017) | 94.3 | [Adversarial Multi-Criteria Learning for Chinese Word Segmentation](http://aclweb.org/anthology/P17-1110) | [Github](https://github.com/FudanNLP/adversarial-multi-criteria-learning-for-CWS) |
| Liu et al. (2016) | 95.7 | [Exploring Segment Representations for Neural Segmentation Models](https://www.ijcai.org/Proceedings/16/Papers/409.pdf)| [Github](https://github.com/Oneplus/segrep-for-nn-semicrf) |
| Cai and Zhao (2016) | 95.7 | [Neural Word Segmentation Learning for Chinese](http://www.aclweb.org/anthology/P16-1039) | [Github](https://github.com/jcyk/CWS) |

#### MSR

| Model         | F1 | Paper / Source | Code |
| ------------- | :-----: |  --- | --- |
| Ma et al. (2018) | 98.1 | [State-of-the-art Chinese Word Segmentation with Bi-LSTMs](https://aclweb.org/anthology/D18-1529)| |
| Huang et al. (2019) | 97.9 | [Toward Fast and Accurate Neural Chinese Word Segmentation with Multi-Criteria Learning](https://arxiv.org/pdf/1903.04190.pdf)| |
| Yang et al. (2018) | 97.8 | [Subword Encoding in Lattice LSTM for Chinese Word Segmentation](https://arxiv.org/pdf/1810.12594.pdf) | [Github](https://github.com/jiesutd/SubwordEncoding-CWS)|
| Yang et al. (2017) | 97.5 | [Neural Word Segmentation with Rich Pretraining](http://aclweb.org/anthology/P17-1078) | [Github](https://github.com/jiesutd/RichWordSegmentor)|
| Cai et al. (2017) | 97.1 | [Fast and Accurate Neural Word Segmentation for Chinese](http://aclweb.org/anthology/P17-2096) | [Github](https://github.com/jcyk/greedyCWS) |
| Chen et al. (2017) | 96.0 | [Adversarial Multi-Criteria Learning for Chinese Word Segmentation](http://aclweb.org/anthology/P17-1110) | [Github](https://github.com/FudanNLP/adversarial-multi-criteria-learning-for-CWS) |
| Liu et al. (2016) | 97.6 | [Exploring Segment Representations for Neural Segmentation Models](https://www.ijcai.org/Proceedings/16/Papers/409.pdf)| [Github](https://github.com/Oneplus/segrep-for-nn-semicrf) |
| Cai and Zhao (2016) | 96.4 | [Neural Word Segmentation Learning for Chinese](http://www.aclweb.org/anthology/P16-1039) | [Github](https://github.com/jcyk/CWS) |

[Go back to the README](../README.md)
