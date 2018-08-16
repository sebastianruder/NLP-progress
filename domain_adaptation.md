# Domain adaptation

## Sentiment analysis

### Multi-Domain Sentiment Dataset

The [Multi-Domain Sentiment Dataset](https://www.cs.jhu.edu/~mdredze/datasets/sentiment/) is a common
evaluation dataset for domain adaptation for sentiment analysis. It contains product reviews from
Amazon.com from different product categories, which are treated as distinct domains.
Reviews contain star ratings (1 to 5 stars) that are generally converted into binary labels. Models are
typically evaluated on a target domain that is different from the source domain they were trained on, while only
having access to unlabeled examples of the target domain (unsupervised domain adaptation). The evaluation
metric is accuracy and scores are averaged across each domain.

{% include table.html
   results=site.data.domain_adaptation
   scores='DVD,Books,Electronics,Kitchen,Average' %}

[Go back to the README](README.md)
