# Common sense

Common sense reasoning tasks are intended to require the model to go beyond pattern 
recognition. Instead, the model should use "common sense" or world knowledge
to make inferences.

### Event2Mind

Event2Mind is a crowdsourced corpus of 25,000 event phrases covering a diverse range of everyday events and situations.
Given an event described in a short free-form text, a model should reason about the likely intents and reactions of the
event's participants. Models are evaluated based on average cross-entropy (lower is better).

| Model           | Dev  | Test  |  Paper / Source | Code | 
| ------------- | :-----:| :-----:|--- | --- | 
| BiRNN 100d (Rashkin et al., 2018) | 4.25 | 4.22 | [Event2Mind: Commonsense Inference on Events, Intents, and Reactions](https://arxiv.org/abs/1805.06939) | |
| ConvNet (Rashkin et al., 2018) | 4.44 | 4.40 | [Event2Mind: Commonsense Inference on Events, Intents, and Reactions](https://arxiv.org/abs/1805.06939) | |

### SWAG

Situations with Adversarial Generations (SWAG) is a dataset consisting of 113k multiple
choice questions about a rich spectrum of grounded situations.

| Model           | Dev  | Test  |  Paper / Source | Code | 
| ------------- | :-----:| :-----:|--- | --- | 
| BERT Large (Devlin et al., 2018) | 86.6 | 86.3 | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) | |
| BERT Base (Devlin et al., 2018) | 81.6 | - | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) | |
| ESIM + ELMo (Zellers et al., 2018) | 59.1 | 59.2 | [SWAG: A Large-Scale Adversarial Dataset for Grounded Commonsense Inference](http://arxiv.org/abs/1808.05326) |  |
| ESIM + GloVe (Zellers et al., 2018) | 51.9 | 52.7 | [SWAG: A Large-Scale Adversarial Dataset for Grounded Commonsense Inference](http://arxiv.org/abs/1808.05326) |  |

### Winograd Schema Challenge

The [Winograd Schema Challenge](https://www.aaai.org/ocs/index.php/KR/KR12/paper/view/4492)
is a dataset for common sense reasoning. It employs Winograd Schema questions that
require the resolution of anaphora: the system must identify the antecedent of an ambiguous pronoun in a statement. Models
are evaluated based on accuracy.

Example:

The trophy doesn’t fit in the suitcase because _it_ is too big. What is too big?
Answer 0: the trophy. Answer 1: the suitcase

| Model           | Score  |  Paper / Source | Code |
| ------------- | :-----:| --- | --- |
| XLNet-Large (ensemble) (Yang et al., 2019) | 90.4 | [XLNet: Generalized Autoregressive Pretraining for Language Understanding](https://arxiv.org/pdf/1906.08237.pdf) | [Official](https://github.com/zihangdai/xlnet/) |
| MT-DNN-ensemble (Liu et al., 2019) | 89.0 | [Improving Multi-Task Deep Neural Networks via Knowledge Distillation for Natural Language Understanding](https://arxiv.org/pdf/1904.09482.pdf) | [Official](https://github.com/namisan/mt-dnn/) |
| Snorkel MeTaL(ensemble) (Ratner et al., 2018) | 65.1 | [Training Complex Models with Multi-Task Weak Supervision](https://arxiv.org/pdf/1810.02840.pdf) | [Official](https://github.com/HazyResearch/metal) |
| Word-LM-partial (Trinh and Le, 2018) | 62.6 | [A Simple Method for Commonsense Reasoning](https://arxiv.org/abs/1806.02847) | |
| Char-LM-partial (Trinh and Le, 2018) | 57.9 | [A Simple Method for Commonsense Reasoning](https://arxiv.org/abs/1806.02847) | |
| USSM + Supervised DeepNet + KB (Liu et al., 2017) | 52.8 | [Combing Context and Commonsense Knowledge Through Neural Networks for Solving Winograd Schema Problems](https://aaai.org/ocs/index.php/SSS/SSS17/paper/view/15392) | |

### Visual Common Sense

Visual Commonsense Reasoning (VCR) is a new task and large-scale dataset for cognition-level visual understanding.
With one glance at an image, we can effortlessly imagine the world beyond the pixels (e.g. that [person1] ordered 
pancakes). While this task is easy for humans, it is tremendously difficult for today's vision systems, requiring 
higher-order cognition and commonsense reasoning about the world. We formalize this task as Visual Commonsense 
Reasoning. In addition to answering challenging visual questions expressed in natural language, a model must provide a 
rationale explaining why its answer is true.

| Model | Q->A  | QA->R  | Q->AR  | Paper / Source | Code |
| ------ | :-------:| :-------: | :-------:| ------ |  ------ | 
| Human Performance University of Washington (Zellers et al. '18) | 91.0 | 93.0 | 85.0 | [From Recognition to Cognition: Visual Commonsense Reasoning](https://arxiv.org/abs/1811.10830) | | 
| Recognition to Cognition Networks University of Washington | 65.1 | 67.3 | 44.0 | [From Recognition to Cognition: Visual Commonsense Reasoning](https://arxiv.org/abs/1811.10830) |  https://github.com/rowanz/r2c |
| BERT-Base Google AI Language (experiment by Rowan) | 53.9 | 64.5 | 35.0 | | https://github.com/google-research/bert |
| MLB Seoul National University (experiment by Rowan) | 46.2 | 36.8 | 17.2 | | https://github.com/jnhwkim/MulLowBiVQA |
| Random Performance | 25.0 | 25.0 | 6.2 | | | 
