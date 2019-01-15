# Exporting NLP-progress into a structure format

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
python structured/export.py <one or more directories or files>
```

For example, to export all the data in the `english/` directory:

```shell
python structured/export.py english
```

By default the output will be written into `structured.json`, but you can override this with the `--output` parameter. 


