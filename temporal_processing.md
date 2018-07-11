# Temporal Processing

## Document Dating (Time-stamping)

Document Dating is the problem of automatically predicting the date of a document based on its content. Date of a document, also referred to as the Document Creation Time (DCT), is at the core of many important tasks, such as, information retrieval, temporal reasoning, text summarization, event detection, and analysis of historical text, among others. 

For example, in the following document, the correct creation year is 1999. This can be inferred by the presence of terms *1995* and *Four years after*.

*Swiss adopted that form of taxation in 1995. The concession was approved by the govt last September. Four years after, the IOC….*

### Datasets 

|                 Datasets                 | # Docs | Start Year | End Year |
| :--------------------------------------: | :----: | :--------: | :------: |
| [APW](https://drive.google.com/file/d/1tll04ZBooB3Mohm6It-v8MBcjMCC3Y1w/view) |  675k  |    1995    |   2010   |
| [NYT](https://drive.google.com/file/d/1wqQRFeA1ESAOJqrwUNakfa77n_S9cmBi/view?usp=sharing) |  647k  |    1987    |   1996   |

### Comparison on year level granularity:

|                                        | APW Dataset | NYT Dataset | Paper/Source                             |
| -------------------------------------- | :---------: | :---------: | ---------------------------------------- |
| NeuralDater (Vashishth et. al, 2018)   |    64.1     |    58.9     | [Document Dating using Graph Convolution Networks](https://github.com/malllabiisc/NeuralDater) |
| Chambers (2012)                        |    52.5     |    42.3     | [Labeling Documents with Timestamps: Learning from their Time Expressions](https://pdfs.semanticscholar.org/87af/a0cb4f829ce861da0c721ca666d48a62c404.pdf) |
| BurstySimDater (Kotsakos et. al, 2014) |    45.9     |    38.5     | [A Burstiness-aware Approach for Document Dating](https://www.idi.ntnu.no/~noervaag/papers/SIGIR2014short.pdf) |


## Temporal Information Extraction

Temporal information extraction is the identification of chunks/tokens corresponding to temporal intervals, and the extraction and determination of the temporal relations between those. The entities extracted may be temporal expressions (timexes), eventualities (events), or auxiliary signals that support the interpretation of an entity or relation. Relations may be temporal links (tlinks), describing the order of events and times, or subordinate links (slinks) describing modality and other subordinative activity, or aspectual links (alinks) around the various influences aspectuality has on event structure.

The markup scheme used for temporal information extraction is well-described in the ISO-TimeML standard, and also on [www.timeml.org](http://www.timeml.org).

```
<?xml version="1.0" ?>

<TimeML xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://timeml.org/timeMLdocs/TimeML_1.2.1.xsd">
<TEXT>


 PRI20001020.2000.0127 
 NEWS STORY 
 <TIMEX3 tid="t0" type="TIME" value="2000-10-20T20:02:07.85">10/20/2000 20:02:07.85</TIMEX3> 


 The Navy has changed its account of the attack on the USS Cole in Yemen.
 Officials <TIMEX3 tid="t1" type="DATE" value="PRESENT_REF" temporalFunction="true" anchorTimeID="t0">now</TIMEX3> say the ship was hit <TIMEX3 tid="t2" type="DURATION" value="PT2H">nearly two hours </TIMEX3>after it had docked.
 Initially the Navy said the explosion occurred while several boats were helping
 the ship to tie up. The change raises new questions about how the attackers
 were able to get past the Navy security.


 <TIMEX3 tid="t3" type="TIME" value="2000-10-20T20:02:28.05">10/20/2000 20:02:28.05</TIMEX3> 



<TLINK timeID="t2" relatedToTime="t0" relType="BEFORE"/>
</TEXT>
</TimeML>
```

To avoid leaking knowledge about temporal structure, train, dev and test splits must be made at document level for temporal information extraction.

### TimeBank

TimeBank, based on the TIMEX3 standard embedded in ISO-TimeML, is a benchmark corpus containing 64K tokens of English newswire, and annotated for all asepcts of ISO-TimeML - including temporal expressions. TimeBank is freely distributed by the LDC: [TimeBank 1.2](https://catalog.ldc.upenn.edu/LDC2006T08)

Evaluation is for both entity chunking and attribute annotation, as well as temporal relation accuracy, typically measured with F1 -- although this metric is not sensitive to inconsistencies or free wins from interval logic induction over the whole set.

| Model           | F1 score  |  Paper / Source |
| ------------- | :-----:| --- |
| Catena | 0.511 |  [CATENA: CAusal and TEmporal relation extraction from NAtural language texts](http://www.aclweb.org/anthology/C16-1007) |
| CAEVO | 0.507 | [Dense Event Ordering with a Multi-Pass Architecture](https://www.transacl.org/ojs/index.php/tacl/article/download/255/50) | 

### TempEval-3

The TempEval-3 corpus accompanied the shared [TempEval-3](http://www.aclweb.org/anthology/S13-2001) SemEval task in 2013. This uses a timelines-based metric to assess temporal relation structure. The corpus is fresh and somewhat more varied than TimeBank, though markedly smaller. [TempEval-3 data](https://www.cs.york.ac.uk/semeval-2013/task1/index.php%3Fid=data.html)

| Model           | Temporal awareness  |  Paper / Source |
| ------------- | :-----:| --- |
| Ning et al. | 67.2 | [A Structured Learning Approach to Temporal Relation Extraction](http://www.aclweb.org/anthology/D17-1108) | 
| ClearTK | 30.98 | [Cleartk-timeml: A minimalist approach to tempeval 2013](http://www.aclweb.org/anthology/S13-2002) |

## Timex normalisation

Temporal expression normalisation is the grounding of a lexicalisation of a time to a calendar date or other formal temporal representation.

Example:
<TIMEX3 tid="t0" type="TIME" value="2000-10-18T21:01:00.65">10/18/2000 21:01:00.65</TIMEX3>
Dozens of Palestinians were wounded in
scattered clashes in the West Bank and Gaza Strip, <TIMEX3 tid="t1" type="DATE" value="2000-10-18" temporalFunction="true" anchorTimeID="t0">Wednesday</TIMEX3>,
despite the Sharm el-Sheikh truce accord. 

Chuck Rich reports on entertainment <TIMEX3 tid="t11" type="SET" value="XXXX-WXX-7">every Saturday</TIMEX3>

### TimeBank

TimeBank, based on the TIMEX3 standard embedded in ISO-TimeML, is a benchmark corpus containing 64K tokens of English newswire, and annotated for all asepcts of ISO-TimeML - including temporal expressions. TimeBank is freely distributed by the LDC: [TimeBank 1.2](https://catalog.ldc.upenn.edu/LDC2006T08)

| Model           | F1 score  |  Paper / Source |
| ------------- | :-----:| --- |
| TIMEN | 0.89 | [TIMEN: An Open Temporal Expression Normalisation Resource](http://aclweb.org/anthology/L12-1015) | 
| HeidelTime | 0.876 | [A baseline temporal tagger for all languages](http://aclweb.org/anthology/D15-1063) |

### PNT

The [Parsing Time Normalizations corpus](https://github.com/bethard/anafora-annotations/releases) in [SCATE](http://www.lrec-conf.org/proceedings/lrec2016/pdf/288_Paper.pdf) format allows the representation of a wider variety of time expressions than previous approaches. This corpus was release with [SemEval 2018 Task 6](http://aclweb.org/anthology/S18-1011).

| Model           | F1 score  |  Paper / Source |
| ------------- | :-----:| --- |
| Laparra et al. 2018 | 0.764 | [From Characters to Time Intervals: New Paradigms for Evaluation and Neural Parsing of Time Normalizations](http://aclweb.org/anthology/Q18-1025) |
| HeidelTime | 0.74 | [A baseline temporal tagger for all languages](http://aclweb.org/anthology/D15-1063) |
| Chrono | 0.70 | [Chrono at SemEval-2018 task 6: A system for normalizing temporal expressions](http://aclweb.org/anthology/S18-1012) | 


[Go back to the README](README.md)
