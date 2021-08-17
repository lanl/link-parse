# Link Parse

[Python](https://www.python.org/) library for parsing memento link headers.


## Installation

Installation of the library requires [pip](https://pip.pypa.io/en/stable/) package installer for Python. 

Install pip: [https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/)



### 1. Using Git 

```shell
pip install https://github.com/mahanama94/link-parser
```

### 2. Local copy

```shell
pip install path/to/package/directory
```

## Usage

```python
# sample.py

from linkparse.regex_parser import RegexLinkParser

parser = RegexLinkParser()

parser_results = parser.parse("link-header string")

```

```shell
$ python sample.py
```