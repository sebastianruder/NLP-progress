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

| Model           | Accuracy  |  Paper / Source | Code | 
| ------------- | :-----:| --- | --- | 
| MoNoise (van der Goot & van Noord, 2017) | 87.63 | [MoNoise: Modeling Noise Using a Modular Normalization System](http://www.let.rug.nl/rob/doc/clin27.paper.pdf) | [Official](https://bitbucket.org/robvanderg/monoise/) | 
| Joint POS + Norm in a Viterbi decoding (Li & Liu, 2015) | 87.58* | [Joint POS Tagging and Text Normalization for Informal Text](http://www.aaai.org/ocs/index.php/IJCAI/IJCAI15/paper/download/10839/10838) | |
| Syllable based (Xu et al., 2015) | 86.08 | [Tweet Normalization with Syllables](http://www.aclweb.org/anthology/P15-1089) | |
| unLOL (Yang & Eisenstein, 2013) | 82.06 | [A Log-Linear Model for Unsupervised Text Normalization](http://www.aclweb.org/anthology/D13-1007) | |

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

| Model           | F1  | Precision | Recall | Paper / Source | Code | 
| ------------- | :-----:| :-----:| :-----:| --- | --- | 
| MoNoise (van der Goot & van Noord, 2017) | 86.39 | 93.53 | 80.26 | [MoNoise: Modeling Noise Using a Modular Normalization System](http://www.let.rug.nl/rob/doc/clin27.paper.pdf) | [Official](https://bitbucket.org/robvanderg/monoise/) | 
| Random Forest + novel similarity metric (Jin, 2017) | 84.21 | 90.61 | 78.65 | [NCSU-SAS-Ning: Candidate Generation and Feature Engineering for Supervised Lexical Normalization](http://www.aclweb.org/anthology/W15-4313) | |

[Go back to the README](../README.md)
