# SharePathway

SharePathway is a python package for KEGG pathway enrichment analysis with multiple gene lists.

There have been dozens of tools or web servers for enrichment analysis using a list of candidate genes from some kinds of high throughput experiments,such as Exome-Seq and RNA-Seq. But the reality is that we usually get multiple gene lists, each from one sample or patient. We can do enrichment analysis for each sample then check which pathway or module is enrich. This strategy is simple and commonly used in cancer study. But we may miss some important driver genes.

SharePathway is motivated at providing users a simple and easy-to-use tool for enrichment analysis on multiple lists of genes simultaneously.

## Installation

The first step is to install Python if you haven't already. Python is available from the [Python project page](https://www.python.org/). The next step is install sharepathway.

Install from PyPi using [pip](http://www.pip-installer.org/en/latest/), a
package manager for Python.

    pip install sharepathway

Or, you can [download the source code
(ZIP)](https://github.com/GuipengLi/SharePathway/zipball/master "SharePathway
source code") for `SharePathway`, and then run:

    python setup.py install

## Usage
Assume you have put all the path of your gene list files in one summary file genelists.txt (one path per line). And the result will be saved in file result.html

```python
import sharepathway as sp
filein="genelists.txt"
fileout="result"
sp.run(fi=files,fo=fileout)
```

The result will be output to a html file

## Contact

Author: Guipeng Li

Email:  guipenglee@gmail.com