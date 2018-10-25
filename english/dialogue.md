# Dialogue

Dialogue is notoriously hard to evaluate. Past approaches have used human evaluation.

## Dialogue state tracking

Dialogue state tacking consists of determining at each turn of a dialogue the
full representation of what the user wants at that point in the dialogue,
which contains a goal constraint, a set of requested slots, and the user's dialogue act.

### Second dialogue state tracking challenge

For goal-oriented dialogue, the dataset of the [second dialogue state tracking challenge](http://www.aclweb.org/anthology/W14-4337)
(DSTC2) is a common evaluation dataset. The DSTC2 focuses on the restaurant search domain. Models are
evaluated based on accuracy on both individual and joint slot tracking.

| Model           | Area  |  Food  |  Price  |  Joint  |  Paper / Source |
| ------------- | :-----:| :-----:| :-----:| :-----:| --- |
| Liu et al. (2018) | 90 | 84 | 92 | 72 | [Dialogue Learning with Human Teaching and Feedback in End-to-End Trainable Task-Oriented Dialogue Systems](https://arxiv.org/abs/1804.06512) |
| Neural belief tracker (Mrkšić et al., 2017) | 90 | 84 | 94 | 72 | [Neural Belief Tracker: Data-Driven Dialogue State Tracking](https://arxiv.org/abs/1606.03777) |
| RNN (Henderson et al., 2014) |﻿92 | 86 | 86 | 69 | [Robust dialog state tracking using delexicalised recurrent neural networks and unsupervised gate](http://svr-ftp.eng.cam.ac.uk/~sjy/papers/htyo14.pdf) | 

[Go back to the README](../README.md)
