# Grammatical Error Correction

Grammatical Error Correction (GEC) is the task of correcting grammatical mistakes in a sentence.


| Error           | Corrected     |
| -------------   | ------------- |
|She see Tom is catched by policeman in park at last night. | She saw Tom caught by a policeman in the park last night.|

### CoNLL-2014

CoNLL-14 benchmark is done on the [test split](https://www.comp.nus.edu.sg/~nlp/conll14st/conll14st-test-data.tar.gz) of [NUS Corpus of Learner English/NUCLE](https://www.comp.nus.edu.sg/~nlp/corpora.html) dataset.
CoNLL-2014 test set contains 1,312 english sentences with grammatical error correction annotations by 2 annotators. Models are evaluated with [F-score](https://en.wikipedia.org/wiki/F1_score) with β=0.5 which weighs precision twice as recall.


{% include table.html results=site.data.grammatical_error_correction.CoNLL_2014 scores='F0.5' %}

{% include chart.html results=site.data.grammatical_error_correction.CoNLL_2014 score='F0.5' %}


### CoNLL-2014 10 Annotators

[Bryant and Ng 2015](https://pdfs.semanticscholar.org/f76f/fd242c3dc88e52d1f427cdd0f5dccd814937.pdf) used 10 annotators to do grammatical error correction on CoNll-14's [1312 sentences](http://www.comp.nus.edu.sg/~nlp/sw/10gec_annotations.zip).

{% include table.html results=site.data.grammatical_error_correction.CoNLL_2014_10_Annotators scores='F0.5' %}

{% include chart.html results=site.data.grammatical_error_correction.CoNLL_2014_10_Annotators score='F0.5' %}


### JFLEG

[JFLEG corpus](https://github.com/keisks/jfleg) by [Napoles et al., 2017](https://arxiv.org/abs/1702.04066) consists of 1,511 english sentences with annotations. Models are evaluated with [GLEU metric](https://arxiv.org/abs/1609.08144).

{% include table.html results=site.data.grammatical_error_correction.JFLEG scores='GLEU' %}

{% include chart.html results=site.data.grammatical_error_correction.JFLEG score='GLEU' %}
