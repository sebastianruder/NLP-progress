# Dependency parsing

Dependency parsing is the task of extracting a dependency parse of a sentence that represents its grammatical
structure and defines the relationships between "head" words and words, which modify those heads.

Example:

```
     root
      |
      | +-------dobj---------+
      | |                    |
nsubj | |   +------det-----+ | +-----nmod------+
+--+  | |   |              | | |               |
|  |  | |   |      +-nmod-+| | |      +-case-+ |
+  |  + |   +      +      || + |      +      | |
I  prefer  the  morning   flight  through  Denver
```

Relations among the words are illustrated above the sentence with directed, labeled
arcs from heads to dependents (+ indicates the dependent).

### Penn Treebank

Models are evaluated on the [Stanford Dependency](https://nlp.stanford.edu/software/dependencies_manual.pdf)
conversion (**v3.3.0**) of the Penn Treebank with __predicted__ POS-tags. Punctuation symbols
are excluded from the evaluation. Evaluation metrics are unlabeled attachment score (UAS) and
labeled attachment score (LAS). Here, we also mention the predicted POS tagging accuracy.

{% include table.html
  results=site.data.dependency_parsing.Penn_Treebank
  scores='POS,UAS,LAS' %}

The following results are just for references:

{% include table.html
  results=site.data.dependency_parsing.Reference
  scores='POS,UAS,comment' %}

[Go back to the README](README.md)
