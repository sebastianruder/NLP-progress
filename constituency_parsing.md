# Constituency parsing

Consituency parsing aims to extract a constituency-based parse tree from a sentence that
represents its syntactic structure according to a [phrase structure grammar](https://en.wikipedia.org/wiki/Phrase_structure_grammar).

Example:

                 Sentence (S)
                     |
       +-------------+------------+
       |                          |
     Noun (N)                Verb Phrase (VP)
       |                          |
     John                 +-------+--------+
                          |                |
                        Verb (V)         Noun (N)
                          |                |
                        sees              Bill

[Recent approaches](https://papers.nips.cc/paper/5635-grammar-as-a-foreign-language.pdf)
convert the parse tree into a sequence following a depth-first traversal in order to
be able to apply sequence-to-sequence models to it. The linearized version of the
above parse tree looks as follows: (S (N) (VP V N)).

### Penn Treebank

The Wall Street Journal section of the [Penn Treebank](https://catalog.ldc.upenn.edu/LDC99T42) is used for
evaluating constituency parsers. Section 22 is used for development and Section 23 is used for evaluation.
Models are evaluated based on F1. Most of the below models incorporate external data or features.
For a comparison of single models trained only on WSJ, refer to [Kitaev and Klein (2018)](https://arxiv.org/abs/1805.01052).

{% include table.html results=site.data.constituency_parsing scores='F1 score' %}

{% include chart.html results=site.data.constituency_parsing score='F1 score' %}

[Go back to the README](README.md)
