# Dialogue

Dialogue is notoriously hard to evaluate. Past approaches have used human evaluation.

## Dialogue act classification

Dialogue act classification is the task of classifying an utterance with respect to the fuction it serves in a dialogue, i.e. the act the speaker is performing. Dialogue acts are a type of speech acts (for Speech Act Theory, see [Austin (1975)](http://www.hup.harvard.edu/catalog.php?isbn=9780674411524) and [Searle (1969)](https://www.cambridge.org/core/books/speech-acts/D2D7B03E472C8A390ED60B86E08640E7)).

### Switchboard corpus
The [Switchboard-1 corpus](https://catalog.ldc.upenn.edu/ldc97s62) is a telephone speech corpus, consisting of about 2,400 two-sided telephone conversation among 543 speakers with about 70 provided conversation topics. The dataset includes the audio files and the transcription files, as well as information about the speakers and the calls.

The Switchboard Dialogue Act Corpus (SwDA) [[download](https://web.stanford.edu/~jurafsky/swb1_dialogact_annot.tar.gz)] extends the Switchboard-1 corpus with tags from the [SWBD-DAMSL tagset](https://web.stanford.edu/~jurafsky/ws97/manual.august1.html), which is an augmentation to the Discourse Annotation and Markup System of Labeling (DAMSL) tagset. The 220 tags were reduced to 42 tags by clustering in order to improve the language model on the Switchboard corpus. A subset of the Switchboard-1 corpus consisting of 1155 conversations was used. The resulting tags include dialogue acts like statement-non-opinion, acknowledge, statement-opinion, agree/accept, etc.  
Annotated example:  
*Speaker:* A, *Dialogue Act:* Yes-No-Question, *Utterance:* So do you go to college right now?  

| Model           | Accuracy  |  Paper / Source | Code | 
| ------------- | :-----:| --- | --- |
| CRF-ASN (Chen et al., 2018) | 81.3 | [Dialogue Act Recognition via CRF-Attentive Structured Network](https://arxiv.org/abs/1711.05568) | |
| Bi-LSTM-CRF (Kumar et al., 2017) | 79.2 | [Dialogue Act Sequence Labeling using Hierarchical encoder with CRF](https://arxiv.org/abs/1709.04250) | [Link](https://github.com/YanWenqiang/HBLSTM-CRF) |
| RNN with 3 utterances in context (Bothe et al., 2018) | 77.34 | [A Context-based Approach for Dialogue Act Recognition using Simple Recurrent Neural Networks](https://arxiv.org/abs/1805.06280) | | 


### ICSI Meeting Recorder Dialog Act (MRDA) corpus
The [MRDA corpus](http://www1.icsi.berkeley.edu/Speech/mr/) [[download](http://www.icsi.berkeley.edu/~ees/dadb/icsi_mrda+hs_corpus_050512.tar.gz)] consists of about 75 hours of speech from 75 naturally-occurring meetings among 53 speakers. The tagset used for labeling is a modified version of the SWBD-DAMSL tagset. It is annotated with three types of information: marking of the dialogue act segment boundaries, marking of the dialogue acts and marking of correspondences between dialogue acts.   
Annotated example:  
*Time:* 2804-2810, *Speaker:* c6, *Dialogue Act:* s^bd, *Transcript:* i mean these are just discriminative.  
Multiple dialogue acts are separated by "^".

| Model           | Accuracy  |  Paper / Source | Code | 
| ------------- | :-----:| --- | --- | 
| CRF-ASN (Chen et al., 2018) | 91.7 | [Dialogue Act Recognition via CRF-Attentive Structured Network](https://arxiv.org/abs/1711.05568) | |
| Bi-LSTM-CRF (Kumar et al., 2017) | 90.9 | [Dialogue Act Sequence Labeling using Hierarchical encoder with CRF](https://arxiv.org/abs/1709.04250) | [Link](https://github.com/YanWenqiang/HBLSTM-CRF) |

## Dialogue state tracking

Dialogue state tacking consists of determining at each turn of a dialogue the
full representation of what the user wants at that point in the dialogue,
which contains a goal constraint, a set of requested slots, and the user's dialogue act.

### Second dialogue state tracking challenge

For goal-oriented dialogue, the dataset of the [second Dialogue Systems Technology Challenges](http://www.aclweb.org/anthology/W14-4337)
(DSTC2) is a common evaluation dataset. The DSTC2 focuses on the restaurant search domain. Models are
evaluated based on accuracy on both individual and joint slot tracking.

| Model           | Request | Area  |  Food  |  Price  |  Joint  |  Paper / Source |
| ------------- | :-----: | :-----:| :-----:| :-----:| :-----:| --- |
| Zhong et al. (2018) | 97.5 | - | - | - | 74.5| [Global-locally Self-attentive Dialogue State Tracker](https://arxiv.org/abs/1805.09655) |
| Liu et al. (2018) | - | 90 | 84 | 92 | 72 | [Dialogue Learning with Human Teaching and Feedback in End-to-End Trainable Task-Oriented Dialogue Systems](https://arxiv.org/abs/1804.06512) |
| Neural belief tracker (Mrkšić et al., 2017) | 96.5 | 90 | 84 | 94 | 73.4 | [Neural Belief Tracker: Data-Driven Dialogue State Tracking](https://arxiv.org/abs/1606.03777) |
| RNN (Henderson et al., 2014) | 95.7 | 92 | 86 | 86 | 69 | [Robust dialog state tracking using delexicalised recurrent neural networks and unsupervised gate](http://svr-ftp.eng.cam.ac.uk/~sjy/papers/htyo14.pdf) | 

[Go back to the README](../README.md)

### Wizard-of-Oz

The [WoZ 2.0 dataset](https://arxiv.org/pdf/1606.03777.pdf) is a newer dialogue state tracking dataset whose evaluation is detached from the noisy output of speech recognition systems. Similar to DSTC2, it covers the restaurant search domain and has identical evaluation.


| Model           | Request  |  Joint  |  Paper / Source |
| ------------- |  :-----:| :-----:| --- |
| Zhong et al. (2018) | 97.1 | 88.1 | [Global-locally Self-attentive Dialogue State Tracker](https://arxiv.org/abs/1805.09655) |
| Neural belief tracker (Mrkšić et al., 2017) | 96.5 | 84.4 | [Neural Belief Tracker: Data-Driven Dialogue State Tracking](https://arxiv.org/abs/1606.03777) |
| RNN (Henderson et al., 2014) | 87.1 | 70.8 | [Robust dialog state tracking using delexicalised recurrent neural networks and unsupervised gate](http://svr-ftp.eng.cam.ac.uk/~sjy/papers/htyo14.pdf) | 
