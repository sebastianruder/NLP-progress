# Chunking

Chunking is a shallow form of parsing that identifies continuous spans of tokens that form syntactic units such as noun phrases or verb phrases.

Example:

| Vinken | , | 61 | years | old |
| --- | ---| --- | --- | --- |
| B-NLP| I-NP | I-NP | I-NP | I-NP |

### Penn Treebank

The [Penn Treebank](https://catalog.ldc.upenn.edu/LDC99T42) is typically used for evaluating chunking.
Sections 15-18 are used for training, section 19 for development, and and section 20
for testing. Models are evaluated based on F1.

{% include table.html results=site.data.chunking score='F1 score' %}

{% include chart.html results=site.data.chunking score='F1 score' %}

[Go back to the README](README.md)
