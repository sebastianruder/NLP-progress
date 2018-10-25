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

| Model           | Score  |  Paper / Source |
| ------------- | :-----:| --- |
| Word-LM-partial (Trinh and Le, 2018) | 62.6 | [A Simple Method for Commonsense Reasoning](https://arxiv.org/abs/1806.02847) |
| Char-LM-partial (Trinh and Le, 2018) | 57.9 | [A Simple Method for Commonsense Reasoning](https://arxiv.org/abs/1806.02847) |
| USSM + Supervised DeepNet + KB (Liu et al., 2017) | 52.8 | [Combing Context and Commonsense Knowledge Through Neural Networks for Solving Winograd Schema Problems](https://aaai.org/ocs/index.php/SSS/SSS17/paper/view/15392) |
