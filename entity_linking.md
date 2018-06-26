# Entity Linking

Entity Linking (EL) can be defined in two approaches:
* first approach (End-to-End): processing a piece of text to extract the entities (i.e. Named Entity Recognition) and then link these extracted entities to their counterpart in a given knowledge base (i.e. Wikipedia).
* second approach: contrary to the first approach, this one directly takes the annotated entities as input and then has just to link them against their counterpart in a given knowledge base (i.e. Wikipedia).

Example:

| Barack | Obama | was | born | in | Hawaï |
| --- | ---| --- | --- | --- | --- |
| https://en.wikipedia.org/wiki/Barack_Obama | https://en.wikipedia.org/wiki/Barack_Obama | O | O | O | https://en.wikipedia.org/wiki/Hawaii |

More in details in this [survey](http://dbgroup.cs.tsinghua.edu.cn/wangjy/papers/TKDE14-entitylinking.pdf)

### AIDA CoNLL-YAGO Dataset

The AIDA CoNLL-YAGO Dataset contains assignments of entities to the mentions of named entities annotated for the original [CoNLL 2003 NER task](http://www.aclweb.org/anthology/W03-0419.pdf). The entities are identified by [YAGO2](http://yago-knowledge.org/) entity name, by [Wikipedia URL](https://en.wikipedia.org/), or by [Freebase mid](http://wiki.freebase.com/wiki/Machine_ID). Approaches are evaluated based on span-based F1.

| Approach           | F1  |  Paper / Source |
| ------------- | :-----:| --- |
| Radhakrishnan et al. (2018) | 93.7 | [ELDEN: Improved Entity Linking using Densified Knowledge Graphs](http://aclweb.org/anthology/N18-1167) |
| Le et al. (2018) | 93.07 | [Improving Entity Linking by Modeling Latent Relations between Mentions](https://arxiv.org/abs/1804.10637) |

[Go back to the README](README.md)
