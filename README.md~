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
from pprint import pprint

link_header = '<http://www.mementoweb.org:80/>; rel="original", '\
'<https://web.archive.org/web/timemap/link/http://www.mementoweb.org:80/>; rel="timemap"; '\
'type="application/link-format", <https://web.archive.org/web/http://www.mementoweb.org:80/>; '\
'rel="timegate", <https://web.archive.org/web/20090930115825/http://www.mementoweb.org/>; rel="first '\
'memento"; datetime="Wed, 30 Sep 2009 11:58:25 GMT" '

parser = RegexLinkParser()

parser_results = parser.parse(link_header)

for result in parser_results:
    pprint(result.__dict__)

```

```shell
$ python sample.py

{'datetime': '',
 'link_from': '',
 'link_type': '',
 'link_until': '',
 'relationship': 'original',
 'title': '',
 'uri': 'http://www.mementoweb.org:80/'}
{'datetime': '',
 'link_from': '',
 'link_type': 'application/link-format',
 'link_until': '',
 'relationship': 'timemap',
 'title': '',
 'uri': 'https://web.archive.org/web/timemap/link/http://www.mementoweb.org:80/'}
{'datetime': '',
 'link_from': '',
 'link_type': '',
 'link_until': '',
 'relationship': 'timegate',
 'title': '',
 'uri': 'https://web.archive.org/web/http://www.mementoweb.org:80/'}
{'datetime': 'Wed, 30 Sep 2009 11:58:25 GMT',
 'link_from': '',
 'link_type': '',
 'link_until': '',
 'relationship': 'first memento',
 'title': '',
 'uri': 'https://web.archive.org/web/20090930115825/http://www.mementoweb.org/'}

```