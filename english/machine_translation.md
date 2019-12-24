# Machine translation

Machine translation is the task of translating a sentence in a source language to a different target language. 

Results with a * indicate that the mean test score over the the best window based on average dev-set BLEU score over 
21 consecutive evaluations is reported as in [Chen et al. (2018)](https://arxiv.org/abs/1804.09849).

### WMT 2014 EN-DE

Models are evaluated on the English-German dataset of the Ninth Workshop on Statistical Machine Translation (WMT 2014) based
on BLEU.

| Model           | BLEU  |  Paper / Source |
| ------------- | :-----:| --- |
| Transformer Big + BT (Edunov et al., 2018) | 35.0 | [Understanding Back-Translation at Scale](https://arxiv.org/pdf/1808.09381.pdf) |
| DeepL | 33.3 | [DeepL Press release](https://www.deepl.com/press.html) |
| DynamicConv (Wu et al., 2019)| 29.7 | [Pay Less Attention With Lightweight and Dynamic Convolutions](https://arxiv.org/abs/1901.10430) |
| AdvSoft + Transformer Big (Wang et al., 2019)| 29.52 | [Improving Neural Language Modeling via Adversarial Training](http://proceedings.mlr.press/v97/wang19f/wang19f.pdf) |
| Transformer Big (Ott et al., 2018) | 29.3 | [Scaling Neural Machine Translation](https://arxiv.org/abs/1806.00187) |
| RNMT+ (Chen et al., 2018) | 28.5* | [The Best of Both Worlds: Combining Recent Advances in Neural Machine Translation](https://arxiv.org/abs/1804.09849) |
| Transformer Big (Vaswani et al., 2017) | 28.4 | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) |
| Transformer Base (Vaswani et al., 2017) | 27.3 | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) |
| MoE (Shazeer et al., 2017) | 26.03 | [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538) |
| ConvS2S (Gehring et al., 2017) | 25.16 | [Convolutional Sequence to Sequence Learning](https://arxiv.org/abs/1705.03122) | 

### WMT 2014 EN-FR

Similarly, models are evaluated on the English-French dataset of the Ninth Workshop on Statistical Machine Translation (WMT 2014) based
on BLEU.

| Model           | BLEU  |  Paper / Source |
| ------------- | :-----:| --- |
| DeepL | 45.9 | [DeepL Press release](https://www.deepl.com/press.html) |
| Transformer Big + BT (Edunov et al., 2018) | 45.6 | [Understanding Back-Translation at Scale](https://arxiv.org/pdf/1808.09381.pdf) |
| DynamicConv (Wu et al., 2019)| 43.2 | [Pay Less Attention With Lightweight and Dynamic Convolutions](https://arxiv.org/abs/1901.10430) |
| Transformer Big (Ott et al., 2018) | 43.2 | [Scaling Neural Machine Translation](https://arxiv.org/abs/1806.00187) |
| RNMT+ (Chen et al., 2018) | 41.0* | [The Best of Both Worlds: Combining Recent Advances in Neural Machine Translation](https://arxiv.org/abs/1804.09849) |
| Transformer Big (Vaswani et al., 2017) | 41.0 | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) |
| MoE (Shazeer et al., 2017) | 40.56 | [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538) |
| ConvS2S (Gehring et al., 2017) | 40.46 | [Convolutional Sequence to Sequence Learning](https://arxiv.org/abs/1705.03122) | 
| Transformer Base (Vaswani et al., 2017) | 38.1 | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) |

[Go back to the README](../README.md)
