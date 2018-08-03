# Dialog

Dialogue is notoriously hard to evaluate. Past approaches have used human evaluation.

## Dialog state tracking

Dialogue state tacking consists of determining at each turn of a dialog the
full representation of what the user wants at that point in the dialog,
which contains a goal constraint, a set of requested slots, and the user's dialog act.

### Second dialog state tracking challenge

For goal-oriented dialogue, the dataset of the [second dialog state tracking challenge](http://www.aclweb.org/anthology/W14-4337)
(DSTC2) is a common evaluation dataset. The DSTC2 focuses on the restaurant search domain. Models are
evaluated based on accuracy on both individual and joint slot tracking.

{% include table.html results=site.data.dialog scores='Area,Food,Price,Joint' %}

{% include chart.html results=site.data.dialog score='Joint' %}

[Go back to the README](README.md)
