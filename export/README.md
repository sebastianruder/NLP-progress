# Exporting NLP-progress into a machine-readable structure format

Parse and export the unstructured information from Markdown into a structured JSON format. 

## Installation

Requires Python 3.6+.

Create a virtualenv and install requirements (you can also use conda):

```shell
virtualenv -p python3 venv
source venv/bin/activate

pip install -r requirements.txt
```

## Running

From the NLP-progress root directly (where the LICENCE file is), run:

```shell
python export/export.py <one or more languages>
```

For example, to export all the english data:

```shell
python export/export.py english
```

or for multiple languages:

```shell
python export/export.py chinese english hindi spanish vietnamese
```

By default the output will be written into `export.json`, but you can override this with the `--output` parameter. 


