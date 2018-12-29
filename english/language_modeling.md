# Language modeling

Language modeling is the task of predicting the next word or character in a document.

\* indicates models using dynamic evaluation; where, at test time, models may adapt to seen tokens in order to improve performance on following tokens. ([Mikolov et al., (2010)](https://www.fit.vutbr.cz/research/groups/speech/publi/2010/mikolov_interspeech2010_IS100722.pdf), [Kraus et al., (2017)](https://arxiv.org/pdf/1709.07432))

## Word Level Models

### Penn Treebank

A common evaluation dataset for language modeling ist the Penn Treebank,
as pre-processed by [Mikolov et al., (2010)](http://www.fit.vutbr.cz/research/groups/speech/publi/2010/mikolov_interspeech2010_IS100722.pdf).
The dataset consists of 929k training words, 73k validation words, and
82k test words. As part of the pre-processing, words were lower-cased, numbers
were replaced with N, newlines were replaced with `<eos>`,
and all other punctuation was removed. The vocabulary is
the most frequent 10k words with the rest of the tokens replaced by an `<unk>` token.
Models are evaluated based on perplexity, which is the average
per-word log-probability (lower is better).

| Model           | Validation perplexity | Test perplexity |  Paper / Source |
| ------------- | :-----:| :-----:| --- |
| AWD-LSTM-MoS + dynamic eval (Yang et al., 2018)* | 48.33 | 47.69 | [Breaking the Softmax Bottleneck: A High-Rank RNN Language Model](https://arxiv.org/abs/1711.03953) |
| AWD-LSTM + dynamic eval (Krause et al., 2017)* | 51.6 | 51.1 | [Dynamic Evaluation of Neural Sequence Models](https://arxiv.org/abs/1709.07432) |
| AWD-LSTM + continuous cache pointer (Merity et al., 2017)* | 53.9 | 52.8 | [Regularizing and Optimizing LSTM Language Models](https://arxiv.org/abs/1708.02182) |
| AWD-LSTM-DOC (Takase et al., 2018) | 54.12 | 52.38 | [Direct Output Connection for a High-Rank Language Model](https://arxiv.org/abs/1808.10143) |
| AWD-LSTM-MoS (Yang et al., 2018) | 56.54 | 54.44 | [Breaking the Softmax Bottleneck: A High-Rank RNN Language Model](https://arxiv.org/abs/1711.03953) |
| Transformer-XL (Dai et al., 2018) ***under review*** | 56.72 | 54.55 | [Transformer-XL: Language Modeling with Longer-Term Dependency](https://openreview.net/pdf?id=HJePno0cYm) |
| AWD-LSTM (Merity et al., 2017) | 60.0 | 57.3 | [Regularizing and Optimizing LSTM Language Models](https://arxiv.org/abs/1708.02182) | 

### WikiText-2

[WikiText-2](https://arxiv.org/abs/1609.07843) has been proposed as a more realistic
benchmark for language modeling than the pre-processed Penn Treebank. WikiText-2
consists of around 2 million words extracted from Wikipedia articles.

| Model           | Validation perplexity | Test perplexity |  Paper / Source |
| ------------- | :-----:| :-----:| --- |
| AWD-LSTM-MoS + dynamic eval (Yang et al., 2018)* | 42.41 | 40.68 | [Breaking the Softmax Bottleneck: A High-Rank RNN Language Model](https://arxiv.org/abs/1711.03953) |
| AWD-LSTM + dynamic eval (Krause et al., 2017)* | 46.4 | 44.3 | [Dynamic Evaluation of Neural Sequence Models](https://arxiv.org/abs/1709.07432) |
| AWD-LSTM + continuous cache pointer (Merity et al., 2017)* | 53.8 | 52.0 | [Regularizing and Optimizing LSTM Language Models](https://arxiv.org/abs/1708.02182) | 
| AWD-LSTM-DOC (Takase et al., 2018) | 60.29 | 58.03 | [Direct Output Connection for a High-Rank Language Model](https://arxiv.org/abs/1808.10143) |
| AWD-LSTM-MoS (Yang et al., 2018) | 63.88 | 61.45 | [Breaking the Softmax Bottleneck: A High-Rank RNN Language Model](https://arxiv.org/abs/1711.03953) |
| AWD-LSTM (Merity et al., 2017) | 68.6 | 65.8 | [Regularizing and Optimizing LSTM Language Models](https://arxiv.org/abs/1708.02182) | 

### WikiText-103

[WikiText-103](https://arxiv.org/abs/1609.07843) The WikiText-103 corpus contains 267,735 unique words and each word occurs at least three times in the training set.

{% include table.html
  results=site.data.language_modeling.Word_Level.WikiText_103
  scores='Validation perplexity,Test perplexity' %}
  
| Model           | Validation perplexity | Test perplexity | Number of params | Paper / Source | Code |
| ------------- | :-----: | :-----: | :-----: | --- | --- |
| Transformer-XL Large (Dai et al., 2018) ***under review*** | 18.2 | 18.9 | 257M | [Transformer-XL: Language Modeling with Longer-Term Dependency](https://openreview.net/pdf?id=HJePno0cYm) ||
| Transformer-XL Standard (Dai et al., 2018) ***under review*** | 23.1 | 24.0 | 151M | [Transformer-XL: Language Modeling with Longer-Term Dependency](https://openreview.net/pdf?id=HJePno0cYm) ||
| LSTM + Hebbian + Cache + MbPA (Rae et al., 2018) | 29.0 | 29.2 | | [Fast Parametric Learning with Activation Memorization](http://arxiv.org/abs/1803.10049) | |
| LSTM + Hebbian (Rae et al., 2018) | 34.1 | 34.3 | | [Fast Parametric Learning with Activation Memorization](http://arxiv.org/abs/1803.10049) | |
| LSTM (Rae et al., 2018) | 36.0 | 36.4 | | [Fast Parametric Learning with Activation Memorization](http://arxiv.org/abs/1803.10049) | |
| Gated CNN (Dauphin et al., 2016) | - | 37.2 | | [Language modeling with gated convolutional networks](https://arxiv.org/abs/1612.08083) | | 
| Temporal CNN (Bai et al., 2018) | - | 45.2 | | [Convolutional sequence modeling revisited](https://openreview.net/forum?id=BJEX-H1Pf) | |
| LSTM (Graves et al., 2014) | - | 48.7 | | [Neural turing machines](https://arxiv.org/abs/1410.5401) | |

## Character Level Models

### Hutter Prize

[The Hutter Prize](http://prize.hutter1.net) Wikipedia dataset, also known as enwiki8, is a byte-level dataset consisting of the
first 100 million bytes of a Wikipedia XML dump. For simplicity we shall refer to it as a character-level dataset.
Within these 100 million bytes are 205 unique tokens.

| Model           | Bit per Character (BPC) |  Number of params | Paper / Source |
| ---------------- | :-----: | :-----: | --- |
| 24-layer Transformer-XL (Dai et al., 2018) ***under review*** | 0.99 | 277M | [Transformer-XL: Language Modeling with Longer-Term Dependency](https://openreview.net/pdf?id=HJePno0cYm) ||
| 18-layer Transformer-XL (Dai et al., 2018) ***under review*** | 1.03 | 88M | [Transformer-XL: Language Modeling with Longer-Term Dependency](https://openreview.net/pdf?id=HJePno0cYm) ||
| Character Transformer Model (Al-Rfou et al., 2018) | 1.06 | 235M | [Character-Level Language Modeling with Deeper Self-Attention](https://arxiv.org/abs/1808.04444)
| mLSTM + dynamic eval (Krause et al., 2017)* | 1.08 | 46M | [Dynamic Evaluation of Neural Sequence Models](https://arxiv.org/abs/1709.07432)
| 3 layer AWD-LSTM (Merity et al., 2018)  | 1.232 | 47M | [An Analysis of Neural Language Modeling at Multiple Scales](https://arxiv.org/abs/1803.08240) |
| Large FS-LSTM-4 (Mujika et al., 2017) | 1.245 | 47M | [Fast-Slow Recurrent Neural Networks](https://arxiv.org/abs/1705.08639) |
| Large mLSTM +emb +WN +VD (Krause et al., 2017) | 1.24 | 46M | [Multiplicative LSTM for sequence modelling](https://arxiv.org/abs/1609.07959)
| FS-LSTM-4 (Mujika et al., 2017) | 1.277 | 27M | [Fast-Slow Recurrent Neural Networks](https://arxiv.org/abs/1705.08639) |
| Large RHN (Zilly et al., 2016) | 1.27 | 46M | [Recurrent Highway Networks](https://arxiv.org/abs/1607.03474)

### Text8
[The text8 dataset](http://mattmahoney.net/dc/textdata.html) is also derived from Wikipedia text, but has all XML removed, and is lower cased to only have 26 characters of English text plus spaces.

| Model           | Bit per Character (BPC) |  Number of params | Paper / Source |
| ---------------- | :-----: | :-----: | --- |
| Character Transformer Model (Al-Rfou et al., 2018) | 1.13 | 235M | [Character-Level Language Modeling with Deeper Self-Attention](https://arxiv.org/abs/1808.04444)
| mLSTM + dynamic eval (Krause et al., 2017)* | 1.19 | 45M | [Dynamic Evaluation of Neural Sequence Models](https://arxiv.org/abs/1709.07432)
| Large mLSTM +emb +WN +VD (Krause et al., 2016) | 1.27 | 45M | [Multiplicative LSTM for sequence modelling](https://arxiv.org/abs/1609.07959)
| Large RHN (Zilly et al., 2016) | 1.27 | 46M | [Recurrent Highway Networks](https://arxiv.org/abs/1607.03474)
| LayerNorm HM-LSTM (Chung et al., 2017) | 1.29 |  35M | [Hierarchical Multiscale Recurrent Neural Networks](https://arxiv.org/abs/1609.01704)
| BN LSTM (Cooijmans et al., 2016) | 1.36 | 16M | [Recurrent Batch Normalization](https://arxiv.org/abs/1603.09025)
| Unregularised mLSTM (Krause et al., 2016) | 1.40 | 45M | [Multiplicative LSTM for sequence modelling](https://arxiv.org/abs/1609.07959)

### Penn Treebank
The vocabulary of the words in the character-level dataset is limited to 10 000 - the same vocabulary as used in the word level dataset.  This vastly simplifies the task of character-level language modeling as character transitions will be limited to those found within the limited word level vocabulary.

| Model           | Bit per Character (BPC) |  Number of params | Paper / Source |
| ---------------- | :-----: | :-----: | --- |
| 3 layer AWD-LSTM (Merity et al., 2018)  | 1.175 | 13.8M | [An Analysis of Neural Language Modeling at Multiple Scales](https://arxiv.org/abs/1803.08240) |
| 6 layer QRNN (Merity et al., 2018)  | 1.187 | 13.8M | [An Analysis of Neural Language Modeling at Multiple Scales](https://arxiv.org/abs/1803.08240) |
| FS-LSTM-4 (Mujika et al., 2017) | 1.190 | 27M | [Fast-Slow Recurrent Neural Networks](https://arxiv.org/abs/1705.08639) |
| FS-LSTM-2 (Mujika et al., 2017) | 1.193 | 27M | [Fast-Slow Recurrent Neural Networks](https://arxiv.org/abs/1705.08639) |
| NASCell (Zoph & Le, 2016) | 1.214 |  16.3M | [Neural Architecture Search with Reinforcement Learning](https://arxiv.org/abs/1611.01578)
| 2-Layer Norm HyperLSTM (Ha et al., 2016) |  1.219 | 14.4M | [HyperNetworks](https://arxiv.org/abs/1609.09106)

[Go back to the README](../README.md)
