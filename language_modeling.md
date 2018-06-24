# Language modeling

Language modeling is the task of predicting the next word in a document. * indicates models using dynamic evaluation.

### Penn Treebank

A common evaluation dataset for language modeling ist the Penn Treebank,
as pre-processed by [Mikolov et al. (2010)](http://www.fit.vutbr.cz/research/groups/speech/publi/2010/mikolov_interspeech2010_IS100722.pdf).
The dataset consists of 929k training words, 73k validation words, and
82k test words. As part of the pre-processing, words were lower-cased, numbers
were replaced with N, newlines were replaced with <eos>,
and all other punctuation was removed. The vocabulary is
the most frequent 10k words with the rest of the tokens replaced by an <unk> token.
Models are evaluated based on perplexity, which is the average
per-word log-probability (lower is better).

| Model           | Validation perplexity | Test perplexity |  Paper / Source |
| ------------- | :-----:| :-----:| --- |
| AWD-LSTM-MoS + dynamic eval (Yang et al., 2018)* | 48.33 | 47.69 | [Breaking the Softmax Bottleneck: A High-Rank RNN Language Model](https://arxiv.org/abs/1711.03953) |
| AWD-LSTM + dynamic eval (Krause et al., 2017)* | 51.6 | 51.1 | [Dynamic Evaluation of Neural Sequence Models](https://arxiv.org/abs/1709.07432) |
| AWD-LSTM + continuous cache pointer (Merity et al., 2017)* | 53.9 | 52.8 | [Regularizing and Optimizing LSTM Language Models](https://arxiv.org/abs/1708.02182) | 
| AWD-LSTM-MoS (Yang et al., 2018) | 56.54 | 54.44 | [Breaking the Softmax Bottleneck: A High-Rank RNN Language Model](https://arxiv.org/abs/1711.03953) |
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
| AWD-LSTM-MoS (Yang et al., 2018) | 63.88 | 61.45 | [Breaking the Softmax Bottleneck: A High-Rank RNN Language Model](https://arxiv.org/abs/1711.03953) |
| AWD-LSTM (Merity et al., 2017) | 68.6 | 65.8 | [Regularizing and Optimizing LSTM Language Models](https://arxiv.org/abs/1708.02182) | 

[Go back to the README](README.md)
