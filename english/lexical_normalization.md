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
The [LexNorm](http://people.eng.unimelb.edu.au/tbaldwin/etc/lexnorm_v1.2.tgz) corpus was originally introduced by [Han and Baldwin (2011)](http://aclweb.org/anthology/P/P11/P11-1038.pdf).
Several mistakes in annotation were resolved by [Yang and Eisenstein](http://www.aclweb.org/anthology/D13-1007);
on this page, we only report results on the new dataset. For this dataset, the 2,577
tweets from [Li and Liu(2014)](http://www.aclweb.org/anthology/P14-3012) is often
used as training data, because of its similar annotation style.

This dataset is commonly evaluated with accuracy on the non-standard words. This
means that the system knows in advance which words are in need of normalization.


{% include table.html results=site.data.lexical_normalization_lexnorm scores='accuracy' %}

\* used a slightly different version of the data

#### LexNorm2015

The
[LexNorm2015](https://github.com/noisy-text/noisy-text.github.io/blob/master/2015/files/lexnorm2015.tgz)
dataset was introduced for the shared task on lexical normalization, hosted at
WNUT2015 ([Baldwin et al(2015)](http://aclweb.org/anthology/W15-4319)).  In
this dataset, 1-N and N-1 replacements are included in the annotation. The
evaluation metrics used are precision, recall and F1 score. However, this is
calculated a bit odd:

Precision: out of all necessary replacements, how many correctly found

Recall: out of all normalization by system, how many correct

This means that if the system replaces a word which is in need of normalization, 
but chooses the wrong normalization, it is penalized twice.

{% include table.html results=site.data.lexical_normalization_lexnorm2015 scores='F1' %}

[Go back to the README](../README.md)

