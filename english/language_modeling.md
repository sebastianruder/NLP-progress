# Language modeling

Language modeling is the task of predicting the next word or character in a document.

\* Indicates models using dynamic evaluation.

## Word Level Models

### Penn Treebank

A common evaluation dataset for language modeling ist the Penn Treebank,
as pre-processed by [Mikolov et al. (2010)](http://www.fit.vutbr.cz/research/groups/speech/publi/2010/mikolov_interspeech2010_IS100722.pdf).
The dataset consists of 929k training words, 73k validation words, and
82k test words. As part of the pre-processing, words were lower-cased, numbers
were replaced with N, newlines were replaced with `<eos>`,
and all other punctuation was removed. The vocabulary is
the most frequent 10k words with the rest of the tokens replaced by an `<unk>` token.
Models are evaluated based on perplexity, which is the average
per-word log-probability (lower is better).

{% include table.html
  results=site.data.language_modeling.Word_Level.Penn_Treebank
  scores='Validation perplexity,Test perplexity' %}

### WikiText-2

[WikiText-2](https://arxiv.org/abs/1609.07843) has been proposed as a more realistic
benchmark for language modeling than the pre-processed Penn Treebank. WikiText-2
consists of around 2 million words extracted from Wikipedia articles.

{% include table.html
  results=site.data.language_modeling.Word_Level.WikiText_2
  scores='Validation perplexity,Test perplexity' %}

### WikiText-103

[WikiText-103](https://arxiv.org/abs/1609.07843) The WikiText-103 corpus contains 267,735 unique words and each word occurs at least three times in the training set.

{% include table.html
  results=site.data.language_modeling.Word_Level.WikiText_103
  scores='Validation perplexity,Test perplexity' %}

## Character Level Models

### Hutter Prize

[The Hutter Prize](http://prize.hutter1.net) Wikipedia dataset, also known as enwik8, is a byte-level dataset consisting of the
first 100 million bytes of a Wikipedia XML dump. For simplicity we shall refer to it as a character-level dataset.
Within these 100 million bytes are 205 unique tokens.

{% include table.html
  results=site.data.language_modeling.Char_Level.Hutter_Prize
  scores='Bits per Character (BPC),Number of params (M)' %}

### Text8
[The text8 dataset](http://mattmahoney.net/dc/textdata.html) is also derived from Wikipedia text, but has all XML removed, and is lower cased to only have 26 characters of English text plus spaces.

{% include table.html
  results=site.data.language_modeling.Char_Level.Text8
  scores='Bits per Character (BPC),Number of params (M)' %}

### Penn Treebank
The vocabulary of the words in the character-level dataset is limited to 10 000 - the same vocabulary as used in the word level dataset.  This vastly simplifies the task of character-level language modeling as character transitions will be limited to those found within the limited word level vocabulary.

{% include table.html
  results=site.data.language_modeling.Char_Level.Penn_Treebank
  scores='Bits per Character (BPC),Number of params (M)' %}

[Go back to the README](../README.md)
