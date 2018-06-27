# Temporal Information Extraction

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

##### Temporal relations

| Model           | F1 score  |  Paper / Source |
| ------------- | :-----:| --- |
| Catena | 0.511 |  [CATENA: CAusal and TEmporal relation extraction from NAtural language texts](http://www.aclweb.org/anthology/C16-1007) |
| CAEVO | 0.507 | [Dense Event Ordering with a Multi-Pass Architecture](https://www.transacl.org/ojs/index.php/tacl/article/download/255/50) | 


### TempEval-3

The TempEval-3 corpus accompanied the shared [TempEval-3](http://www.aclweb.org/anthology/S13-2001) SemEval task in 2013. This uses a timelines-based metric to assess temporal relation structure. The corpus is fresh and somewhat more varied than TimeBank, though markedly smaller. [TempEval-3 data](https://www.cs.york.ac.uk/semeval-2013/task1/index.php%3Fid=data.html)

##### Temporal relations

| Model           | Temporal awareness  |  Paper / Source |
| ------------- | :-----:| --- |
| ClearTK | 30.98 | [Cleartk-timeml: A minimalist approach to tempeval 2013](http://www.aclweb.org/anthology/S13-2002) |
| Ning et al. | | [A Structured Learning Approach to Temporal Relation Extraction](http://www.aclweb.org/anthology/D17-1108) | 


[Go back to the README](README.md)
