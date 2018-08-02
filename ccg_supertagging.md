# CCG supertagging

Combinatory Categorical Grammar (CCG; [Steedman, 2000](http://www.citeulike.org/group/14833/article/8971002)) is a
highly lexicalized formalism. The standard parsing model of [Clark and Curran (2007)](https://www.mitpressjournals.org/doi/abs/10.1162/coli.2007.33.4.493)
uses over 400 lexical categories (or _supertags_), compared to about 50 part-of-speech tags for typical parsers.

Example:

| Vinken | , | 61 | years | old |
| --- | ---| --- | --- | --- |
| N| , | N/N | N | (S[adj]\ NP)\ NP |

### CCGBank

The CCGBank is a corpus of CCG derivations and dependency structures extracted from the Penn Treebank by
[Hockenmaier and Steedman (2007)](http://www.aclweb.org/anthology/J07-3004). Sections 2-21 are used for training,
section 00 for development, and section 23 as in-domain test set.
Performance is only calculated on the 425 most frequent labels. Models are evaluated based on accuracy.

{% include table.html results=site.data.ccg_supertagging score='accuracy' %}

{% include chart.html results=site.data.ccg_supertagging score='accuracy' %}

[Go back to the README](README.md)
