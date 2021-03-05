# Language modeling

Language modeling is the task of predicting the next word or character in a document.

\* indicates models using dynamic evaluation; where, at test time, models may adapt to seen tokens in order to improve performance on following tokens. ([Mikolov et al., (2010)](https://www.fit.vutbr.cz/research/groups/speech/publi/2010/mikolov_interspeech2010_IS100722.pdf), [Krause et al., (2017)](https://arxiv.org/pdf/1709.07432))

## Word Level Models

### Penn Treebank

A common evaluation dataset for language modeling ist the Penn Treebank,
as pre-processed by [Mikolov et al., (2011)](https://www.isca-speech.org/archive/archive_papers/interspeech_2011/i11_0605.pdf).
The dataset consists of 929k training words, 73k validation words, and
82k test words. As part of the pre-processing, words were lower-cased, numbers
were replaced with N, newlines were replaced with `<eos>`,
and all other punctuation was removed. The vocabulary is
the most frequent 10k words with the rest of the tokens replaced by an `<unk>` token.
Models are evaluated based on perplexity, which is the average
per-word log-probability (lower is better).

| Model           | Validation perplexity | Test perplexity | Number of params |  Paper / Source | Code |
| ------------- | :-----:| :-----: | :-----: | -------------- | ---- |
| Mogrifier LSTM + dynamic eval (Melis et al., 2019)      | 44.9  | 44.8  | 24M | [Mogrifier LSTM](http://arxiv.org/abs/1909.01792) | [Official](https://github.com/deepmind/lamb) |
| AdvSoft + AWD-LSTM-MoS + dynamic eval (Wang et al., 2019) | 46.63 | 46.01 | 22M | [Improving Neural Language Modeling via Adversarial Training](http://proceedings.mlr.press/v97/wang19f/wang19f.pdf) | [Official](https://github.com/ChengyueGongR/advsoft) |
| FRAGE + AWD-LSTM-MoS + dynamic eval (Gong et al., 2018) | 47.38 | 46.54 | 22M | [FRAGE: Frequency-Agnostic Word Representation](https://arxiv.org/abs/1809.06858) | [Official](https://github.com/ChengyueGongR/Frequency-Agnostic) |
| AWD-LSTM-DOC x5 (Takase et al., 2018) | 48.63 | 47.17 | 185M | [Direct Output Connection for a High-Rank Language Model](https://arxiv.org/abs/1808.10143) | [Official](https://github.com/nttcslab-nlp/doc_lm) |
| AWD-LSTM-MoS + dynamic eval (Yang et al., 2018)* | 48.33 | 47.69 | 22M | [Breaking the Softmax Bottleneck: A High-Rank RNN Language Model](https://arxiv.org/abs/1711.03953) | [Official](https://github.com/zihangdai/mos) |
| Mogrifier LSTM (Melis et al., 2019)                     | 51.4  | 50.1  | 24M | [Mogrifier LSTM](http://arxiv.org/abs/1909.01792) | [Official](https://github.com/deepmind/lamb) |
| AWD-LSTM + dynamic eval (Krause et al., 2017)* | 51.6 | 51.1 | 24M | [Dynamic Evaluation of Neural Sequence Models](https://arxiv.org/abs/1709.07432) | [Official](https://github.com/benkrause/dynamic-evaluation) |
| AWD-LSTM-DOC + Partial Shuffle (Press, 2019) ***preprint*** | 53.79 | 52.00 | 23M | [Partially Shuffling the Training Data to Improve Language Models](https://arxiv.org/abs/1903.04167) | [Official](https://github.com/ofirpress/PartialShuffle) |
| AWD-LSTM-DOC (Takase et al., 2018) | 54.12 | 52.38 | 23M | [Direct Output Connection for a High-Rank Language Model](https://arxiv.org/abs/1808.10143) | [Official](https://github.com/nttcslab-nlp/doc_lm) |
| AWD-LSTM + continuous cache pointer (Merity et al., 2017)* | 53.9 | 52.8 | 24M | [Regularizing and Optimizing LSTM Language Models](https://arxiv.org/abs/1708.02182) | [Official](https://github.com/salesforce/awd-lstm-lm) |
| Trellis Network (Bai et al., 2019) |   -   | 54.19 | 34M | [Trellis Networks for Sequence Modeling](https://openreview.net/pdf?id=HyeVtoRqtQ) | [Official](https://github.com/locuslab/trellisnet)
| AWD-LSTM-MoS + ATOI (Kocher et al., 2019) | 56.44 | 54.33 | 22M | [Alleviating Sequence Information Loss with Data Overlapping and Prime Batch Sizes](https://arxiv.org/abs/1909.08700) | [Official](https://github.com/nkcr/overlap-ml) |
| AWD-LSTM-MoS + finetune (Yang et al., 2018) | 56.54 | 54.44 | 22M | [Breaking the Softmax Bottleneck: A High-Rank RNN Language Model](https://arxiv.org/abs/1711.03953) | [Official](https://github.com/zihangdai/mos) |
| Transformer-XL (Dai et al., 2018) ***under review*** | 56.72 | 54.52 | 24M | [Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context](https://arxiv.org/pdf/1901.02860.pdf) | [Official](https://github.com/kimiyoung/transformer-xl) |
| AWD-LSTM-MoS (Yang et al., 2018) | 58.08 | 55.97 | 22M | [Breaking the Softmax Bottleneck: A High-Rank RNN Language Model](https://arxiv.org/abs/1711.03953) | [Official](https://github.com/zihangdai/mos) |
| AWD-LSTM 3-layer with Fraternal dropout (Zołna et al., 2018) |  58.9 | 56.8 | 24M | [Fraternal dropout](https://arxiv.org/pdf/1711.00066.pdf) | [Official](https://github.com/kondiz/fraternal-dropout) |
| AWD-LSTM (Merity et al., 2017) | 60.0 | 57.3 | 24M | [Regularizing and Optimizing LSTM Language Models](https://arxiv.org/abs/1708.02182) | [Official](https://github.com/salesforce/awd-lstm-lm) |

### WikiText-2

[WikiText-2](https://arxiv.org/abs/1609.07843) has been proposed as a more realistic
benchmark for language modeling than the pre-processed Penn Treebank. WikiText-2
consists of around 2 million words extracted from Wikipedia articles.

| Model           | Validation perplexity | Test perplexity | Number of params | Paper / Source | Code |
| ------------- | :-----:| :-----: | :-----: | -------------- | ---- |
| Mogrifier LSTM + dynamic eval (Melis et al., 2019)      | 40.2  | 38.6  | 35M | [Mogrifier LSTM](http://arxiv.org/abs/1909.01792) | [Official](https://github.com/deepmind/lamb) |
| AdvSoft + AWD-LSTM-MoS + dynamic eval (Wang et al., 2019) | 40.27 | 38.65 | 35M | [Improving Neural Language Modeling via Adversarial Training](http://proceedings.mlr.press/v97/wang19f/wang19f.pdf) | [Official](https://github.com/ChengyueGongR/advsoft) |
| FRAGE + AWD-LSTM-MoS + dynamic eval (Gong et al., 2018) | 40.85 | 39.14 | 35M | [FRAGE: Frequency-Agnostic Word Representation](https://arxiv.org/abs/1809.06858) | [Official](https://github.com/ChengyueGongR/Frequency-Agnostic) |
| AWD-LSTM-MoS + dynamic eval (Yang et al., 2018)* | 42.41 | 40.68 | 35M | [Breaking the Softmax Bottleneck: A High-Rank RNN Language Model](https://arxiv.org/abs/1711.03953) | [Official](https://github.com/zihangdai/mos) |
| AWD-LSTM + dynamic eval (Krause et al., 2017)* | 46.4 | 44.3 | 33M | [Dynamic Evaluation of Neural Sequence Models](https://arxiv.org/abs/1709.07432) | [Official](https://github.com/benkrause/dynamic-evaluation) |
| AWD-LSTM + continuous cache pointer (Merity et al., 2017)* | 53.8 | 52.0 | 33M | [Regularizing and Optimizing LSTM Language Models](https://arxiv.org/abs/1708.02182) | [Official](https://github.com/salesforce/awd-lstm-lm) |
| AWD-LSTM-DOC x5 (Takase et al., 2018) | 54.19 | 53.09 | 185M | [Direct Output Connection for a High-Rank Language Model](https://arxiv.org/abs/1808.10143) | [Official](https://github.com/nttcslab-nlp/doc_lm) |
| Mogrifier LSTM (Melis et al., 2019)                     | 57.3  | 55.1  | 35M | [Mogrifier LSTM](http://arxiv.org/abs/1909.01792) | [Official](https://github.com/deepmind/lamb) |
| AWD-LSTM-DOC + Partial Shuffle (Press, 2019) ***preprint*** | 60.16 | 57.85 | 37M | [Partially Shuffling the Training Data to Improve Language Models](https://arxiv.org/abs/1903.04167) | [Official](https://github.com/ofirpress/PartialShuffle) |
| AWD-LSTM-DOC (Takase et al., 2018) | 60.29 | 58.03 | 37M | [Direct Output Connection for a High-Rank Language Model](https://arxiv.org/abs/1808.10143) | [Official](https://github.com/nttcslab-nlp/doc_lm) |
| AWD-LSTM-MoS (Yang et al., 2018) | 63.88 | 61.45 | 35M | [Breaking the Softmax Bottleneck: A High-Rank RNN Language Model](https://arxiv.org/abs/1711.03953) | [Official](https://github.com/zihangdai/mos) |
| AWD-LSTM 3-layer with Fraternal dropout (Zołna et al., 2018) |  66.8 | 64.1 | 34M | [Fraternal dropout](https://arxiv.org/pdf/1711.00066.pdf) | [Official](https://github.com/kondiz/fraternal-dropout) |
| AWD-LSTM + ATOI (Kocher et al., 2019) | 67.47 | 64.73 | 33M | [Alleviating Sequence Information Loss with Data Overlapping and Prime Batch Sizes](https://arxiv.org/abs/1909.08700) | [Official](https://github.com/nkcr/overlap-ml) |
| AWD-LSTM (Merity et al., 2017) | 68.6 | 65.8 | 33M | [Regularizing and Optimizing LSTM Language Models](https://arxiv.org/abs/1708.02182) | [Official](https://github.com/salesforce/awd-lstm-lm) |

### WikiText-103

[WikiText-103](https://arxiv.org/abs/1609.07843) The WikiText-103 corpus contains 267,735 unique words and each word occurs at least three times in the training set.

| Model           | Validation perplexity | Test perplexity | Number of params | Paper / Source | Code |
| ------------- | :---:| :---:| :---:| -------- | --- |
| Routing Transformer (Roy et al., 2020)* ***arxiv preprint*** | - | 15.8 | - | [Efficient Content-Based Sparse Attention with Routing Transformers](https://arxiv.org/pdf/2003.05997.pdf) | - |
| Transformer-XL + RMS dynamic eval (Krause et al., 2019)* ***arxiv preprint*** | 15.8 | 16.4 | 257M | [Dynamic Evaluation of Transformer Language Models](https://arxiv.org/pdf/1904.08378.pdf) | [Official](https://github.com/benkrause/dynamiceval-transformer) |
| Compressive Transformer (Rae et al., 2019)* ***arxiv preprint*** | 16.0 | 17.1(16.1 with basic dynamic evaluation) | ~257M | [Compressive Transformers for Long-Range Sequence Modelling](https://arxiv.org/pdf/1911.05507.pdf) | - |
| SegaTransformer-XL (Bai et al., 2020) | - | 17.1 | 257M | [Segatron: Segment-Aware Transformer for Language Modeling and Understanding](https://arxiv.org/abs/2004.14996) | [Official](https://github.com/rsvp-ai/segatron_aaai) |
| Transformer-XL Large (Dai et al., 2018) ***under review*** | 17.7 | 18.3 | 257M | [Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context](https://arxiv.org/pdf/1901.02860.pdf) | [Official](https://github.com/kimiyoung/transformer-xl) |
| Transformer with tied adaptive embeddings (Baevski and Auli, 2018) | 19.8 | 20.5 | 247M | [Adaptive Input Representations for Neural Language Modeling](https://arxiv.org/pdf/1809.10853.pdf) | [Link](https://github.com/AranKomat/adapinp) |
| TaLK Convolutions (Lioutas et al., 2020)| - | 23.3 | 240M | [Time-aware Large Kernel Convolutions](https://arxiv.org/abs/2002.03184) | [Official](https://github.com/lioutasb/TaLKConvolutions) |
| Transformer-XL Standard (Dai et al., 2018) ***under review*** | 23.1 | 24.0 | 151M | [Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context](https://arxiv.org/pdf/1901.02860.pdf) | [Official](https://github.com/kimiyoung/transformer-xl) |
| AdvSoft + 4 layer QRNN + dynamic eval (Wang et al., 2019) | 27.2 | 28.0 |  | [Improving Neural Language Modeling via Adversarial Training](http://proceedings.mlr.press/v97/wang19f/wang19f.pdf) | [Official](https://github.com/ChengyueGongR/advsoft) |
| LSTM + Hebbian + Cache + MbPA (Rae et al., 2018) | 29.0 | 29.2 | | [Fast Parametric Learning with Activation Memorization](http://arxiv.org/abs/1803.10049) ||
| Trellis Network (Bai et al., 2019) |   -   | 30.35 | 180M | [Trellis Networks for Sequence Modeling](https://openreview.net/pdf?id=HyeVtoRqtQ) | [Official](https://github.com/locuslab/trellisnet)
| AWD-LSTM-MoS + ATOI (Kocher et al., 2019) | 31.92 | 32.85 | | [Alleviating Sequence Information Loss with Data Overlapping and Prime Batch Sizes](https://arxiv.org/abs/1909.08700) | [Official](https://github.com/nkcr/overlap-ml) |
| LSTM + Hebbian (Rae et al., 2018) | 34.1 | 34.3 | | [Fast Parametric Learning with Activation Memorization](http://arxiv.org/abs/1803.10049) ||
| LSTM (Rae et al., 2018) | 36.0 | 36.4 | | [Fast Parametric Learning with Activation Memorization](http://arxiv.org/abs/1803.10049) ||
| Gated CNN (Dauphin et al., 2016) | - | 37.2 | | [Language modeling with gated convolutional networks](https://arxiv.org/abs/1612.08083) ||
| Neural cache model (size = 2,000) (Grave et al., 2017) | - | 40.8 | | [Improving Neural Language Models with a Continuous Cache](https://arxiv.org/pdf/1612.04426.pdf) | [Link](https://github.com/kaishengtai/torch-ntm) |
| Temporal CNN (Bai et al., 2018) | - | 45.2 | | [Convolutional sequence modeling revisited](https://openreview.net/forum?id=BJEX-H1Pf) ||
| LSTM (Grave et al., 2017) | - | 48.7 | | [Improving Neural Language Models with a Continuous Cache](https://arxiv.org/pdf/1612.04426.pdf) | [Link](https://github.com/kaishengtai/torch-ntm) |

### 1B Words / Google Billion Word benchmark

[The One-Billion Word benchmark](https://arxiv.org/pdf/1312.3005.pdf) is a large dataset derived from a news-commentary site.
The dataset consists of 829,250,940 tokens over a vocabulary of 793,471 words.
Importantly, sentences in this model are shuffled and hence context is limited.

| Model         | Test perplexity | Number of params | Paper / Source | Code |
| ------------- | :-----:| :-----:| --------- | --- |
| Transformer-XL Large (Dai et al., 2018) ***under review*** | 21.8 | 0.8B | [Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context](https://arxiv.org/pdf/1901.02860.pdf) | [Official](https://github.com/kimiyoung/transformer-xl) |
| Transformer-XL Base (Dai et al., 2018) ***under review*** | 23.5 | 0.46B | [Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context](https://arxiv.org/pdf/1901.02860.pdf) | [Official](https://github.com/kimiyoung/transformer-xl) |
| Transformer with shared adaptive embeddings - Very large (Baevski and Auli, 2018) | 23.7 | 0.8B | [Adaptive Input Representations for Neural Language Modeling](https://arxiv.org/pdf/1809.10853.pdf) | [Link](https://github.com/AranKomat/adapinp) 
| 10 LSTM+CNN inputs + SNM10-SKIP (Jozefowicz et al., 2016) ***ensemble*** | 23.7 | 43B? | [Exploring the Limits of Language Modeling](https://arxiv.org/pdf/1602.02410.pdf) | [Official](https://github.com/rafaljozefowicz/lm) |
| Transformer with shared adaptive embeddings (Baevski and Auli, 2018) | 24.1 | 0.46B | [Adaptive Input Representations for Neural Language Modeling](https://arxiv.org/pdf/1809.10853.pdf) | [Link](https://github.com/AranKomat/adapinp) 
| Big LSTM+CNN inputs (Jozefowicz et al., 2016) | 30.0 | 1.04B | [Exploring the Limits of Language Modeling](https://arxiv.org/pdf/1602.02410.pdf) ||
| Gated CNN-14Bottleneck (Dauphin et al., 2017) | 31.9 | ? | [Language Modeling with Gated Convolutional Networks](https://arxiv.org/pdf/1612.08083.pdf) ||
| BIGLSTM baseline (Kuchaiev and Ginsburg, 2018) | 35.1 | 0.151B | [Factorization tricks for LSTM networks](https://arxiv.org/pdf/1703.10722.pdf) | [Official](https://github.com/okuchaiev/f-lm) |
| BIG F-LSTM F512 (Kuchaiev and Ginsburg, 2018) | 36.3 | 0.052B | [Factorization tricks for LSTM networks](https://arxiv.org/pdf/1703.10722.pdf) | [Official](https://github.com/okuchaiev/f-lm) |
| BIG G-LSTM G-8 (Kuchaiev and Ginsburg, 2018) | 39.4 | 0.035B | [Factorization tricks for LSTM networks](https://arxiv.org/pdf/1703.10722.pdf) | [Official](https://github.com/okuchaiev/f-lm) |


## Character Level Models

### Hutter Prize

[The Hutter Prize](http://prize.hutter1.net) Wikipedia dataset, also known as enwiki8, is a byte-level dataset consisting of the
first 100 million bytes of a Wikipedia XML dump. For simplicity we shall refer to it as a character-level dataset.
Within these 100 million bytes are 205 unique tokens.

| Model           | Bit per Character (BPC) |  Number of params | Paper / Source | Code |
| ---------------- | :-----: | :-----: | -------------- | ---- |
| Transformer-XL + RMS dynamic eval (Krause et al., 2019)* ***arxiv preprint*** | 0.94 | 277M | [Dynamic Evaluation of Transformer Language Models](https://arxiv.org/pdf/1904.08378.pdf) | [Official](https://github.com/benkrause/dynamiceval-transformer) |
| Compressive Transformer (Rae et al., 2019) ***arxiv preprint*** | 0.97 | - | [Compressive Transformers for Long-Range Sequence Modelling](https://arxiv.org/pdf/1911.05507.pdf) | - |
| Mogrifier LSTM + dynamic eval (Melis et al., 2019)            | 0.988 | 96M | [Mogrifier LSTM](http://arxiv.org/abs/1909.01792) | [Official](https://github.com/deepmind/lamb) |
| 24-layer Transformer-XL (Dai et al., 2018) ***under review*** | 0.99 | 277M | [Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context](https://arxiv.org/pdf/1901.02860.pdf) | [Official](https://github.com/kimiyoung/transformer-xl) |
| Longformer Large (Beltagy, Peters, and Cohan; 2020) | 0.99 | 102M | [Longformer: The Long-Document Transformer](https://arxiv.org/pdf/2004.05150.pdf) | [Official](https://github.com/allenai/longformer) |
| Longformer Small (Beltagy, Peters, and Cohan; 2020) | 1.00 | 41M | [Longformer: The Long-Document Transformer](https://arxiv.org/pdf/2004.05150.pdf) | [Official](https://github.com/allenai/longformer) |
| 18-layer Transformer-XL (Dai et al., 2018) ***under review*** | 1.03 | 88M | [Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context](https://arxiv.org/pdf/1901.02860.pdf) | [Official](https://github.com/kimiyoung/transformer-xl) |
| 12-layer Transformer-XL (Dai et al., 2018) ***under review*** | 1.06 | 41M | [Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context](https://arxiv.org/pdf/1901.02860.pdf) | [Official](https://github.com/kimiyoung/transformer-xl) |
| 64-layer Character Transformer Model (Al-Rfou et al., 2018) | 1.06 | 235M | [Character-Level Language Modeling with Deeper Self-Attention](https://arxiv.org/abs/1808.04444) ||
| mLSTM + dynamic eval (Krause et al., 2017)* | 1.08 | 46M | [Dynamic Evaluation of Neural Sequence Models](https://arxiv.org/abs/1709.07432) | [Official](https://github.com/benkrause/dynamic-evaluation) |
| 12-layer Character Transformer Model (Al-Rfou et al., 2018) | 1.11 | 44M | [Character-Level Language Modeling with Deeper Self-Attention](https://arxiv.org/abs/1808.04444) ||
| Mogrifier LSTM (Melis et al., 2019)            | 1.122 | 96M | [Mogrifier LSTM](http://arxiv.org/abs/1909.01792) | [Official](https://github.com/deepmind/lamb) |
| 3-layer AWD-LSTM (Merity et al., 2018)  | 1.232 | 47M | [An Analysis of Neural Language Modeling at Multiple Scales](https://arxiv.org/abs/1803.08240) | [Official](https://github.com/salesforce/awd-lstm-lm) |
| Large mLSTM +emb +WN +VD (Krause et al., 2017) | 1.24 | 46M | [Multiplicative LSTM for sequence modelling](https://arxiv.org/abs/1609.07959) | [Official](https://github.com/benkrause/mLSTM) |
| Large FS-LSTM-4 (Mujika et al., 2017) | 1.245 | 47M | [Fast-Slow Recurrent Neural Networks](https://arxiv.org/abs/1705.08639) | [Official](https://github.com/amujika/Fast-Slow-LSTM) |
| Large RHN (Zilly et al., 2016) | 1.27 | 46M | [Recurrent Highway Networks](https://arxiv.org/abs/1607.03474) | [Official](https://github.com/jzilly/RecurrentHighwayNetworks) |
| FS-LSTM-4 (Mujika et al., 2017) | 1.277 | 27M | [Fast-Slow Recurrent Neural Networks](https://arxiv.org/abs/1705.08639) | [Official](https://github.com/amujika/Fast-Slow-LSTM) |

### Text8
[The text8 dataset](http://mattmahoney.net/dc/textdata.html) is also derived from Wikipedia text, but has all XML removed, and is lower cased to only have 26 characters of English text plus spaces.

| Model           | Bit per Character (BPC) |  Number of params | Paper / Source | Code |
| ---------------- | :-----: | :-----: | -------------- | ---- |
| Transformer-XL + RMS dynamic eval (Krause et al., 2019)* ***arxiv preprint*** | 1.038 | 277M | [Dynamic Evaluation of Transformer Language Models](https://arxiv.org/pdf/1904.08378.pdf) | [Official](https://github.com/benkrause/dynamiceval-transformer) |
| Transformer-XL Large (Dai et al., 2018) ***under review*** | 1.08 | 277M | [Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context](https://arxiv.org/pdf/1901.02860.pdf) | [Official](https://github.com/kimiyoung/transformer-xl) |
| Longformer Small (Beltagy, Peters, and Cohan; 2020) | 1.10 | 41M | [Longformer: The Long-Document Transformer](https://arxiv.org/pdf/2004.05150.pdf) | [Official](https://github.com/allenai/longformer) |
| 64-layer Character Transformer Model (Al-Rfou et al., 2018) | 1.13 | 235M | [Character-Level Language Modeling with Deeper Self-Attention](https://arxiv.org/abs/1808.04444) ||
| 12-layer Character Transformer Model (Al-Rfou et al., 2018) | 1.18 | 44M | [Character-Level Language Modeling with Deeper Self-Attention](https://arxiv.org/abs/1808.04444) ||
| mLSTM + dynamic eval (Krause et al., 2017)* | 1.19 | 45M | [Dynamic Evaluation of Neural Sequence Models](https://arxiv.org/abs/1709.07432) | [Official](https://github.com/benkrause/dynamic-evaluation) |
| Large mLSTM +emb +WN +VD (Krause et al., 2016) | 1.27 | 45M | [Multiplicative LSTM for sequence modelling](https://arxiv.org/abs/1609.07959) | [Official](https://github.com/benkrause/mLSTM) |
| Large RHN (Zilly et al., 2016) | 1.27 | 46M | [Recurrent Highway Networks](https://arxiv.org/abs/1607.03474) | [Official](https://github.com/jzilly/RecurrentHighwayNetworks) |
| LayerNorm HM-LSTM (Chung et al., 2017) | 1.29 |  35M | [Hierarchical Multiscale Recurrent Neural Networks](https://arxiv.org/abs/1609.01704) ||
| BN LSTM (Cooijmans et al., 2016) | 1.36 | 16M | [Recurrent Batch Normalization](https://arxiv.org/abs/1603.09025) | [Official](https://github.com/cooijmanstim/recurrent-batch-normalization) |
| Unregularised mLSTM (Krause et al., 2016) | 1.40 | 45M | [Multiplicative LSTM for sequence modelling](https://arxiv.org/abs/1609.07959) | [Official](https://github.com/benkrause/mLSTM) |

### Penn Treebank
The vocabulary of the words in the character-level dataset is limited to 10 000 - the same vocabulary as used in the word level dataset.  This vastly simplifies the task of character-level language modeling as character transitions will be limited to those found within the limited word level vocabulary.

| Model           | Bit per Character (BPC) |  Number of params | Paper / Source | Code |
| ---------------- | :-----: | :-----: | -------------- | ---- |
| Mogrifier LSTM + dynamic eval (Melis et al., 2019)| 1.083 | 24M | [Mogrifier LSTM](http://arxiv.org/abs/1909.01792) | [Official](https://github.com/deepmind/lamb) |
| Mogrifier LSTM (Melis et al., 2019)               | 1.120 | 24M | [Mogrifier LSTM](http://arxiv.org/abs/1909.01792) | [Official](https://github.com/deepmind/lamb) |
| Trellis Network (Bai et al., 2019) | 1.159 | 13.4M | [Trellis Networks for Sequence Modeling](https://openreview.net/pdf?id=HyeVtoRqtQ) | [Official](https://github.com/locuslab/trellisnet)
| 3-layer AWD-LSTM (Merity et al., 2018)  | 1.175 | 13.8M | [An Analysis of Neural Language Modeling at Multiple Scales](https://arxiv.org/abs/1803.08240) | [Official](https://github.com/salesforce/awd-lstm-lm) |
| 6-layer QRNN (Merity et al., 2018)  | 1.187 | 13.8M | [An Analysis of Neural Language Modeling at Multiple Scales](https://arxiv.org/abs/1803.08240) | [Official](https://github.com/salesforce/awd-lstm-lm) |
| FS-LSTM-4 (Mujika et al., 2017) | 1.190 | 27M | [Fast-Slow Recurrent Neural Networks](https://arxiv.org/abs/1705.08639) | [Official](https://github.com/amujika/Fast-Slow-LSTM) |
| FS-LSTM-2 (Mujika et al., 2017) | 1.193 | 27M | [Fast-Slow Recurrent Neural Networks](https://arxiv.org/abs/1705.08639) | [Official](https://github.com/amujika/Fast-Slow-LSTM) |
| NASCell (Zoph & Le, 2016) | 1.214 |  16.3M | [Neural Architecture Search with Reinforcement Learning](https://arxiv.org/abs/1611.01578) ||
| 2-layer Norm HyperLSTM (Ha et al., 2016) |  1.219 | 14.4M | [HyperNetworks](https://arxiv.org/abs/1609.09106) ||

### Multilingual Wikipedia Corpus

The character-based [MWC](http://k-kawakami.com/research/mwc) dataset is a collection of Wikipedia pages available in a number of languages. Markup and rare characters were removed, but otherwise no preprocessing was applied.

#### MWC English in the single text, large setting.

| Model           | Validation BPC | Test BPC | Number of params |  Paper / Source | Code |
| ------------- | :-----:| :-----: | :-----: | -------------- | ---- |
| Mogrifier LSTM + dynamic eval (Melis et al., 2019)| 1.200 | 1.187 | 24M | [Mogrifier LSTM](http://arxiv.org/abs/1909.01792) | [Official](https://github.com/deepmind/lamb) |
| Mogrifier LSTM (Melis et al., 2019)               | 1.312 | 1.298 | 24M | [Mogrifier LSTM](http://arxiv.org/abs/1909.01792) | [Official](https://github.com/deepmind/lamb) |
| HCLM with Cache (Kawakami et al. 2017)            | 1.591 | 1.538 |  8M | [Learning to Create and Reuse Words in Open-Vocabulary Neural Language Modeling](https://arxiv.org/abs/1704.06986) |  |
| LSTM (Kawakami et al. 2017)                       | 1.793 | 1.736 |  8M | [Learning to Create and Reuse Words in Open-Vocabulary Neural Language Modeling](https://arxiv.org/abs/1704.06986) |  |

#### MWC Finnish in the single text, large setting.

| Model           | Validation BPC | Test BPC | Number of params |  Paper / Source | Code |
| ------------- | :-----:| :-----: | :-----: | -------------- | ---- |
| Mogrifier LSTM + dynamic eval (Melis et al., 2019)| 1.202 | 1.191 | 24M | [Mogrifier LSTM](http://arxiv.org/abs/1909.01792) | [Official](https://github.com/deepmind/lamb) |
| Mogrifier LSTM (Melis et al., 2019)               | 1.327 | 1.313 | 24M | [Mogrifier LSTM](http://arxiv.org/abs/1909.01792) | [Official](https://github.com/deepmind/lamb) |
| HCLM with Cache (Kawakami et al. 2017)            | 1.754 | 1.711 |  8M | [Learning to Create and Reuse Words in Open-Vocabulary Neural Language Modeling](https://arxiv.org/abs/1704.06986) |  |
| LSTM (Kawakami et al. 2017)                       | 1.943 | 1.913 |  8M | [Learning to Create and Reuse Words in Open-Vocabulary Neural Language Modeling](https://arxiv.org/abs/1704.06986) |  |

[Go back to the README](../README.md)
