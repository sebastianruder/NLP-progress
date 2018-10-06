# Vietnamese NLP tasks

## Word segmentation 

* Training data: 75k manually word-segmented training sentences from the [VLSP](http://vlsp.org.vn/) 2013 word segmentation shared task.
* Test data: 2120 test sentences from the VLSP 2013 POS tagging shared task.

| Model           | F1  |  Paper / Source | Code | 
| ------------- | :-----:| --- | --- | 
| VnCoreNLP-RDRsegmenter (2018) | 97.90 | [A Fast and Accurate Vietnamese Word Segmenter](http://www.lrec-conf.org/proceedings/lrec2018/pdf/55.pdf) | [Official](https://github.com/datquocnguyen/RDRsegmenter) | 
| UETsegmenter (2016) | 97.87 | [A hybrid approach to Vietnamese word segmentation](http://doi.org/10.1109/RIVF.2016.7800279) | [Official](https://github.com/phongnt570/UETsegmenter) |
| vnTokenizer (2008) | 97.33 | [A Hybrid Approach to Word Segmentation of Vietnamese Texts](https://link.springer.com/chapter/10.1007/978-3-540-88282-4_23) |  |
| JVnSegmenter (2006) | 97.06 | [Vietnamese Word Segmentation with CRFs and SVMs: An Investigation](http://www.aclweb.org/anthology/Y06-1028) |  |
| DongDu (2012) | 96.90 |  Ứng dụng phương pháp Pointwise vào bài toán tách từ cho tiếng Việt |  |

* Results for VnTokenizer, JVnSegmenter and DongDu are reported in "[A hybrid approach to Vietnamese word segmentation](http://doi.org/10.1109/RIVF.2016.7800279)."

## POS tagging 

* 27,870 sentences for training and development from the VLSP 2013 POS tagging shared task:
  *  27k sentences are used for training.
  *  870 sentences are used for development.
* Test data: 2120 test sentences from the VLSP 2013 POS tagging shared task.

| Model           | Accuracy  |  Paper / Source | Code | 
| ------------- | :-----:| --- | --- | 
| VnCoreNLP-VnMarMoT (2017) | 95.88 | [From Word Segmentation to POS Tagging for Vietnamese](http://aclweb.org/anthology/U17-1013) | [Official](https://github.com/datquocnguyen/vnmarmot) | 
| BiLSTM-CRF + CNN-char  (2016) | 95.40 | [End-to-end Sequence Labeling via Bi-directional LSTM-CNNs-CRF](http://www.aclweb.org/anthology/P16-1101) | [Link](https://github.com/UKPLab/emnlp2017-bilstm-cnn-crf/) | 
| BiLSTM-CRF + LSTM-char (2016) | 95.31 | / [Neural Architectures for Named Entity Recognition](http://www.aclweb.org/anthology/N16-1030) | [Link](https://github.com/UKPLab/emnlp2017-bilstm-cnn-crf/) | 
| BiLSTM-CRF (2015) | 95.06 | [Bidirectional LSTM-CRF Models for Sequence Tagging](https://arxiv.org/abs/1508.01991) | [Link](https://github.com/UKPLab/emnlp2017-bilstm-cnn-crf/) | 
| RDRPOSTagger (2014) | 95.11 |  [RDRPOSTagger: A Ripple Down Rules-based Part-Of-Speech Tagger](http://www.aclweb.org/anthology/E14-2005) | [Official](https://github.com/datquocnguyen/rdrpostagger) | 

* Results for BiLSTM-CRF-based models and RDRPOSTagger are reported in  "[From Word Segmentation to POS Tagging for Vietnamese](http://aclweb.org/anthology/U17-1013)."

## Named entity recognition
* 16,861 sentences for training and development from the VLSP 2016 NER shared task:
  *  14,861 sentences are used for training.
  *  2k sentences are used for development.
* Test data: 2,831 test sentences from the VLSP 2016 NER  shared task.
* **NOTE** that in the VLSP 2016 NER data, each word representing a full personal name are separated into syllables that constitute the word. The VLSP 2016 NER data also consists of gold POS and chunking tags as [reconfirmed by VLSP 2016 organizers](https://drive.google.com/file/d/1XzrgPw13N4C_B6yrQy_7qIxl8Bqf7Uqi/view?usp=sharing). This scheme results in an unrealistic scenario for a pipeline evaluation: 
  * The standard annotation for Vietnamese word segmentation and POS tagging forms each full name as a word token, thus all   word segmenters have been trained to output a full name as a word and all POS taggers have been trained to assign a POS label to the entire full-name.
  * Gold POS and chunking tags are NOT available in a real-world application.
* For a realistic scenario, we merge those contiguous syllables constituting a full name to form a word. Then to obtain predicted POS tags for training, developement and test sentences, we perform POS tagging by using VnCoreNLP-VnMarMoT. 

<table>
    <tr>
    <td><b>Model<b></td>
    <td><b>F1</td>
    <td><b>Speed</td>
  </tr>
  <tr>
    <td>VnCoreNLP</td>
    <td><b>88.55</td>
    <td><b>18k</td>
  </tr>
  <tr>
    <td>BiLSTM-CRF</td>
    <td>86.48</td>
    <td> 2.8k</td>
  </tr>
   <tr>
    <td>BiLSTM-CRF + CNN-char</td>
    <td>88.28</td>
    <td> 1.8k</td>
  </tr>
  <tr>
    <td>BiLSTM-CRF + LSTM-char</td>
    <td>87.71</td>
    <td> 1.3k</td>
  </tr>
  <tr>
    <td>BiLSTM-CRF + predicted POS</td>
    <td>86.12</td>
    <td> _ </td>
  </tr>
   <tr>
    <td>BiLSTM-CRF + CNN-char + predicted POS </td>
    <td>88.06</td>
    <td> _</td>
  </tr>
  <tr>
    <td>BiLSTM-CRF + LSTM-char + predicted POS</td>
    <td>87.43</td>
    <td> _ </td>
  </tr>
</table>

* Here, for VnCoreNLP, we include the time POS tagging takes in the speed.
* See paper [1] for more details.

## Dependency parsing

* We use the Vietnamese dependency treebank [VnDT](http://vndp.sourceforge.net)  consisting of 10,200 sentences. We use the last 1020 sentences of VnDT for test while the remaining sentences are used for training.

<table>
  <tr>
    <th colspan="2"><b>Model</b></th>
    <th> <b>LAS</b> (%)</th>
    <th><b>UAS</b> (%)</th>
    <th><b>Speed</th>
  </tr>
  <tr>
    <td rowspan="5">Gold POS</td>
    <td>VnCoreNLP</td>
    <td><b>73.39</td>
    <td>79.02</td>
    <td>_</td>
  </tr>
  <tr>
    <td>BIST-bmstparser</td>
    <td>73.17</td>
    <td><b>79.39</td>
    <td>_</td>
  </tr>
  <tr>
    <td>BIST-barchybrid</td>
    <td>72.53</td>
    <td>79.33</td>
    <td>_</td>
  </tr>
  <tr>
    <td>MSTparser</td>
    <td>70.29</td>
    <td>76.47</td>
    <td>_</td>
  </tr>
  <tr>
    <td>MaltParser</td>
    <td>69.10</td>
    <td>74.91</td>
    <td>_</td>
  </tr>
  <tr>
    <td rowspan="2">Predicted POS</td>
    <td>VnCoreNLP</td>
    <td><b>70.23</td>
    <td>76.93</td>
    <td><b>8k</td>
  </tr>
  <tr>
    <td>jPTDP</td>
    <td>69.49</td>
    <td><b>77.68</td>
    <td>700</td>
  </tr>
</table>
