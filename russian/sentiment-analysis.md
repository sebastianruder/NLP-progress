# Sentiment Analysis

Sentiment analysis is the task of classifying the polarity of a given text.

## RuSentRel

The [RuSentRel](https://github.com/nicolay-r/RuSentRel) dataset
consisted of analytical articles from Internet-portal inosmi.ru. These are translated into Russian texts in the domain of international politics obtained from foreign authoritative sources.
The collected articles contain both the author's opinion on the subject matter of the article and a large number of references mentioned between the participants of the described situations. 
The dataset contains 73 large analytical texts, labeled with about 2000 relations.
 
**Sentiment Attitude Extraction task:** Given a subset of documents, in which every document includes: (1) text, (2) a list of mentioned named entities. 
For each document it is required to complete a list of labeled entity pairs [(s<sub>1</sub>->o<sub>1</sub>, l<sub>1</sub>), ... (s<sub>n</sub>->o<sub>n</sub>, l<sub>n</sub>)], 
for which text conveys the presence of the sentiment relation expressed by the subject towards the object (s<sub>i</sub>->o<sub>i</sub>) with sentiment l<sub>i</sub> ∈ [neg, pos] (see the example below).

Task paper: https://arxiv.org/pdf/1808.08932.pdf

The public leaderboard is available at [github repository](https://github.com/nicolay-r/RuSentRel-Leaderboard)

| Example                                                                                                                                                                                                                                                     |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ... Meanwhile <ins>Moscow</ins> has repeatedly emphasized that its activity in the <ins>Baltic Sea</ins> is a response precisely to actions of **<ins>NATO</ins>** and the escalation of the hostile approach to **<ins>Russia</ins>** near its eastern borders ...
| (NATO->Russia, neg), (Russia->NATO, neg)                                                                                                                                                                                                                    |

## RuSentNE-2023

The dataset for RuSentNE-2023 evaluation is based on the Russian news corpus RuSentNE having rich sentiment-related annotation. The corpus
is annotated with named entities and sentiments towards these entities, along with related effects and emotional states. The dataset contains over 11000 sentences from 400+ large texts.

**Entity-Oriented Sentiment Analysis task:** Given a subset of sentences, in which every sentence includes one or several named entities. For each sentence all of the named entities should be classified into one of three sentiment classes: positive, negative or neutral within the context of a single sentence.

Task paper: https://arxiv.org/pdf/2305.17679.pdf

The public leaderboard is available at [github repository](https://github.com/dialogue-evaluation/RuSentNE-evaluation)

| Example                                                                                                                                                                                                                                                     |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Notorious figure in the country - <ins>Berlusconi</ins> has been repeatedly accused of financial fraud
| (Berlusconi-> neg)

