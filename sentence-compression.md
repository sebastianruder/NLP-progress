# Sentence Compression

Sentence compression produces a shorter sentence by removing redundant information,
preserving the grammatically and the important content of the original sentence. 

### Google Dataset

The [Google Dataset](https://github.com/google-research-datasets/sentence-compression) was built by Filippova et al., 2013([Overcoming the Lack of Parallel Data in Sentence Compression](https://www.aclweb.org/anthology/D/D13/D13-1155.pdf)). The first dataset released contained only 10,000 sentence-compression pairs, but last year was released an additional 200,000 pairs. 

Example of a sentence-compression pair:
> Sentence: Floyd Mayweather is open to fighting Amir Khan in the future, despite snubbing the Bolton-born boxer in favour of a May bout with Argentine Marcos Maidana, according to promoters Golden Boy

> Compression: Floyd Mayweather is open to fighting Amir Khan in the future. 

In short, this is a deletion-based task where the compression is a subsequence from the original sentence. From the 10,000 pairs of the eval portion([repository](https://github.com/google-research-datasets/sentence-compression/tree/master/data)) it is used the very first 1,000 sentence for automatic evaluation and the 200,000 pairs for training.

Models are evaluated using the following metrics:
* F1 - compute the recall and precision in terms of tokens kept in the golden and the generated compressions.
* Compression rate (CR) - the length of the compression in characters divided over the sentence length. 

| Model           | F1 | CR |Paper / Source | Code |
| -------------   | :-----:| --- | --- | --- |
| LSTM (Filippova et al., 2015) | 0.82 | 0.38 | [Sentence Compression by Deletion with LSTMs](https://research.google.com/pubs/archive/43852.pdf) | |
| BiLSTM (Wang et al., 2017) | 0.8 | 0.43 | [Can Syntax Help? Improving an LSTM-based Sentence Compression Model for New Domains](www.aclweb.org/anthology/P17-1127) |  | 


[Go back to the README](README.md)
