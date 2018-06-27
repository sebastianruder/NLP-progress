# Timex normalisation

Temporal expression normalisation is the grounding of a lexicalisation of a time to a calendar date or other formal temporal representation.

Example:
<TIMEX3 tid="t0" type="TIME" value="2000-10-18T21:01:00.65">10/18/2000 21:01:00.65</TIMEX3>
Dozens of Palestinians were wounded in
scattered clashes in the West Bank and Gaza Strip, <TIMEX3 tid="t1" type="DATE" value="2000-10-18" temporalFunction="true" anchorTimeID="t0">Wednesday</TIMEX3>,
despite the Sharm el-Sheikh truce accord. 

Chuck Rich reports on entertainment <TIMEX3 tid="t11" type="SET" value="XXXX-WXX-7">every Saturday</TIMEX3>

### TimeBank

TimeBank, based on the TIMEX3 standard embedded in ISO-TimeML, is a benchmark corpus containing 64K tokens of English newswire, and annotated for all asepcts of ISO-TimeML - including temporal expressions.

| Model           | F1 score  |  Paper / Source |
| ------------- | :-----:| --- |
| HeidelTime | 0.876 | [A baseline temporal tagger for all languages](http://aclweb.org/anthology/D15-1063) |
| TIMEN | 0.89 | [TIMEN: An Open Temporal Expression Normalisation Resource](http://aclweb.org/anthology/L12-1015) | 

### PNT

The [Parsing Time Normalizations corpus](https://github.com/bethard/anafora-annotations/releases) in [SCATE](http://www.lrec-conf.org/proceedings/lrec2016/pdf/288_Paper.pdf) format allows the representation of a wider variety of time expressions than previous approaches. This corpus was release with [SemEval 2018 Task 6](http://aclweb.org/anthology/S18-1011).

| Model           | F1 score  |  Paper / Source |
| ------------- | :-----:| --- |
| HeidelTime | 0.74 | [A baseline temporal tagger for all languages](http://aclweb.org/anthology/D15-1063) |
| Chrono | 0.70 | [Chrono at SemEval-2018 task 6: A system for normalizing temporal expressions](http://aclweb.org/anthology/S18-1012) | 
| Laparra et al. 2018 | 0.764 | [From Characters to Time Intervals: New Paradigms for Evaluation and Neural Parsing of Time Normalizations](http://aclweb.org/anthology/Q18-1025) |


[Go back to the README](README.md)
