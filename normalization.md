# Lexical Normalization

Lexical normalization is the task of translating/transforming a non standard text to a standard register.

Example:

```
new pix comming tomoroe
new pictures coming tomorrow
```

Datasets usually consists of tweets, since these naturally contain a fair amount of 
these phenomena.

For lexical normalization, only replacements on the word-level are annotated.
Some corpora include annotation for 1-N and N-1 replacements. However, word
insertion/deletion and reordering is not part of the task.

### LexNorm

v1.0 vs v1.1, we use 1.1 here.
data from chenli is often used for training, because of similar annotation style.

This dataset is commonly evaluated with accuracy on the non-standard words. This
means that the system knows in advance which words are in need of normalization.

{% include table.html
  results=site.data.normalization.lexnorm
  scores='accuracy' %}

* used a slightly different version of the data

#### LexNorm2015

Introduced in WNUT2015 shared task
In this dataset, 1-N and N-1 replacements are included in the annotation. The 
evaluation metric commonly used is F1 score. However, this is calculated a bit
odd:


{% include table.html
  results=site.data.normalization.lexnorm2015
  scores='precision,recall,F1' %}

[Go back to the README](README.md)

