# Entity Linking

## Task

Entity Linking (EL) is the task of recognizing (cf. [Named Entity Recognition](named_entity_recognition.md)) and disambiguating (Named Entity Disambiguation) named entities to a knowledge base (e.g. Wikidata, DBpedia, or YAGO). It is sometimes also simply known as Named Entity Recognition and Disambiguation.

EL can be split into two classes of approaches:
* *End-to-End*: processing a piece of text to extract the entities (i.e. Named Entity Recognition) and then disambiguate these extracted entities to the correct entry in a given knowledge base (e.g. Wikidata, DBpedia, YAGO).
* *Disambiguation-Only*: contrary to the first approach, this one directly takes gold standard named entities as input and only disambiguates them to the correct entry in a given knowledge base.

Example:

| Barack | Obama | was | born | in | Hawaï |
| --- | ---| --- | --- | --- | --- |
| https://en.wikipedia.org/wiki/Barack_Obama | https://en.wikipedia.org/wiki/Barack_Obama | O | O | O | https://en.wikipedia.org/wiki/Hawaii |

More in details can be found in this [survey](http://dbgroup.cs.tsinghua.edu.cn/wangjy/papers/TKDE14-entitylinking.pdf).

## Evaluation

### Metrics 

#### Disambiguation-Only Approach

* Micro-Precision: Fraction of correctly disambiguated named entities in the full corpus.
* Macro-Precision: Fraction of correctly disambiguated named entities, averaged by document.

### Datasets

#### AIDA CoNLL-YAGO Dataset

The [AIDA CoNLL-YAGO][AIDACoNLLYAGO] Dataset by [[Hoffart]](http://www.aclweb.org/anthology/D11-1072) contains assignments of entities to the mentions of named entities annotated for the original [[CoNLL]](http://www.aclweb.org/anthology/W03-0419.pdf) 2003 NER task. The entities are identified by [YAGO2](http://yago-knowledge.org/) entity identifier, by [Wikipedia URL](https://en.wikipedia.org/), or by [Freebase mid](http://wiki.freebase.com/wiki/Machine_ID).

| Micro-Precision | Macro-Precision  |  Paper / Source |
| ------------- | :-----:| :----: | --- |
| 93.0 | 93.7 | [Radhakrishnan et al. ELDEN: Improved Entity Linking using Densified Knowledge Graphs. NAACL-HLT 2018](http://aclweb.org/anthology/N18-1167) |
| 93.07 | - | [Le et al. Improving Entity Linking by Modeling Latent Relations between Mentions. ACL 2018](http://aclweb.org/anthology/P18-1148) |
| 82.29 | 82.02 | [Hoffart et al. Robust Disambiguation of Named Entities in Text. EMNLP 2011](http://www.aclweb.org/anthology/D11-1072)

### Platforms

Evaluating Entity Linking systems in a manner that allows for direct comparison of performance can be difficult. The precise definition of a "correct" annotation can be somewhat subjective and it is easy to make mistakes. To provide a simple example, given the input surface form **"Tom Waits"**, an evaluation dataset might record the dbpedia resource `http://dbpedia.org/resource/Tom_Waits` as the correct referent. Yet an annotation system which returns a reference to `http://dbpedia.org/resource/PEHDTSCKJBMA` has technically provided an appropriate annotation as this resource is a redirect to `http://dbpedia.org/resource/Tom_Waits`. Alternatively if evaluating an End-to-End EL system, then accuracy with respect to word boundaries must be considered e.g. if a system only annotates **"Obama"** with the URI `http://dbpedia.org/resource/Barack_Obama` in the surface form **"Barack Obama"**, then is the system correct or incorrect in its annotation?

Furthermore, the performance of an EL system can be strongly affected by the nature of the content on which the evaluation is performed e.g. news content versus Tweets. Hence comparing the relative performance of two EL systems which have been tested on two different corpora can be fallicious. Rather than allowing these little subjective points to creep into the evaluation of EL systems, it is better to make use of a standard evaluation platform where these assumptions are known and made explicit in the configuration of the experiment.

[GERBIL][GERBIL], developed by [AKSW][AKSW] is an evaluation platform that is based on the [BAT framework][Cornolti]. It defines a number of standard experiments which may be run for any given EL service. These experiment types determine how strict the evaluation is with respect to measures such as word boundary alignment and also dictates how much responsibility is assigned to the EL service with respect to Entity Recognition, etc. GERBIL hosts 38 evaluation datasets obtained from a variety of different EL challenges. At present it also has hooks for 17 different EL services which may be included in an experiment.

GERBIL may be used to test your own EL system either by downloading the source code and deploying GERBAL locally, or by making your service available on the web and giving GERBIL a link to your API endpoint. The only condition is that your API must accept input and respond with output in [NIF][NIF] format. It is also possible to upload your own evaluation dataset if you would like to test these services on your own content. Note the dataset must also be in NIF format. The [DBpedia Spotlight evaluation dataset][SpotlightEvaluation] is a good example of how to structure your content.

GERBIL does have a number of shortcomings, the most notable of which are:
1. There is no way to view the annotations returned by each system you test. These are handled internally by GERBIL and then discarded. This can make it difficult to determine the source of error with an EL system.
2. There is no way to observe the candidate list considered for each surface form. This is, of course, a standard problem with any third party EL API, but if one is conducting a detailed investigation into the performance of an EL system, it is important to know if the source of error was the EL algorithm itself, or the candidate retrieval process which failed to identify the correct referent as a candidate. This was listed as an important consideration by [Hachey et al][Hachey].

Nevertheless, GERBIL is an excellent resource for standardising how EL systems are tested and compared. It is also a good starting point for anyone new to Entity Linking as it contains links to a wide variety of EL resources. For more information, see the research paper by [[Usbeck]](http://svn.aksw.org/papers/2015/WWW_GERBIL/public.pdf).

## References

[Hoffart] Johannes Hoffart, Mohamed Amir Yosef, Ilaria Bordino, Hagen Fürstenau, Manfred Pinkal, Marc Spaniol, Bilyana Taneva, Stefan Thater, and Gerhard Weikum. Robust Disambiguation of Named Entities in Text. EMNLP 2011. http://www.aclweb.org/anthology/D11-1072

[CoNLL] Erik F Tjong Kim Sang and Fien De Meulder. Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition. CoNLL 2003. http://www.aclweb.org/anthology/W03-0419.pdf

[Usbeck] Usbeck et al. GERBIL - General Entity Annotator Benchmarking Framework. WWW 2015. http://svn.aksw.org/papers/2015/WWW_GERBIL/public.pdf

[Go back to the README](README.md)

[Shen]: http://dbgroup.cs.tsinghua.edu.cn/wangjy/papers/TKDE14-entitylinking.pdf "Entity Linking with a Knowledge Base: Issues, Techniques, and Solutions"
[AIDACoNLLYAGO]: https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/yago-naga/aida/downloads/ "AIDA CoNLL-YAGO Dataset"
[YAGO2]: http://yago-knowledge.org/ "YAGO2"
[Wikipedia]: https://en.wikipedia.org/ "Wikipedia"
[Freebase]: http://wiki.freebase.com/wiki/Machine_ID "Freebase"
[Radhakrishnan]: http://aclweb.org/anthology/N18-1167 "ELDEN: Improved Entity Linking using Densified Knowledge Graphs"
[Le]: https://arxiv.org/abs/1804.10637
[NIF]: http://persistence.uni-leipzig.org/nlp2rdf/ "NLP Interchange Formt"
[SpotlightEvaluation]: http://apps.yovisto.com/labs/ner-benchmarks/data/dbpedia-spotlight-nif.ttl "GERBIL DBpedia Spotlight Dataset"
[Cornolti]: https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/40749.pdf "A Framework for Benchmarking Entity-Annotation Systems"
[GERBIL]: http://aksw.org/Projects/GERBIL.html "General Entity Annotator Benchmarking framework"
[AKSW]: http://aksw.org/About.html "Agile Knowledge Engineering and Semantic Web"
[Hachey]: http://benhachey.info/pubs/hachey-aij12-evaluating.pdf "Evaluating Entity Linking with Wikipedia"