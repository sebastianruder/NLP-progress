# Paraphrase Generation
[Paraphrase generation](https://arxiv.org/abs/1908.07831) is the task to generate an output sentence which is sementically identical to the input sentence but contains variations in lexicon or syntext. See the example given below:

| Input (Erroneous)          | Output (Corrected)     |
| -------------------------  | ---------------------- |
|The need for investors to earn a commercial return may put upward pressure on prices| The need for profit is likely to push up prices|

### Opusparcus
The [Opusparcus dataset](https://arxiv.org/pdf/1809.06142v1.pdf) is a paraphrase corpus for six European languages: German, English, Finnish, French, Russian, and Swedish. The paraphrases are extracted from the OpenSubtitles2016 corpus, which contains subtitles from movies and TV shows.

For each target language, the Opusparcus data have been partitioned into three types of data sets: training, development and test sets. The training sets are large, consisting of millions of sentence pairs, and have been compiled automatically, with the help of probabilistic ranking functions. The development and test sets consist of sentence pairs that have been annotated manually; each set contains approximately 1000 sentence pairs that have been verified to be acceptable paraphrases by two annotators.

