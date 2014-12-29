SharePathway
============

SharePathway is a python package for KEGG pathway enrichment analysis with multiple gene lists.

There have been dozens of tools or web servers for enrichment analysis using a list of candidate genes from some kinds of high throughput experiments,such as Exome-Seq and RNA-Seq. But the reality is that we usually get multiple gene lists, each from one sample or patient. We can do enrichment analysis for each sample then check which pathway or module is enrich. This strategy is simple and commonly used in cancer study. But we may miss some important driver genes.

SharePathway is motivated at providing users a simple and easy-to-use tool for enrichment analysis on multiple lists of genes simultaneously.

Installation
------------

This version is for both python2 and python3.
The first step is to install Python. Python is available from the `Python project page <https://www.python.org/>`_ . The next step is install sharepathway.

Install from PyPi using `pip <http://www.pip-installer.org/en/latest/>`_, a
package manager for Python::

    $ pip install sharepathway

Or, you can download the source code at `Github <https://github.com/GuipengLi/SharePathway>`_  or at `PyPi <https://pypi.python.org/pypi/sharepathway>`_ for SharePathway, and then run::

    $ python setup.py install

Usage
-----

Assume you have put all the path of your gene list files in one summary file genelists.txt (one path per line) in the directory ~/data/. Go into this directory,open python and run the scripts below. The result will be saved in the result.html file::

	import sharepathway as sp
	filein="genelists.txt"
	fileout="result"
	sp.Run(fi=filein,fo=fileout)

Entrez Gene ID is supported. The result will be output to a html file.


Output Description
------------------

.. list-tables::
   :widths: 30 200
   :header-rows: 1

   * - Column
     - Description
   * - Pathway
     - Pathway name and hyperlink to modified KEGG map
   * - Genes
     - KEGG¡¡ID of the genes in the pathway
   * - pCount
     - Total number of genes in the pathway
   * - Count
     - The number of recognized genes from user input
   * - Ratio
     - The percentage of lists that containing genes in the corresponding pathway
   * - Pvalue
     - The combined p valude from Fisher's Method
   * - EASE
     - EASE¡¡score defined by DAVID, from merged gene list
   * - FET
     - P value of the Fisher Exact Test, from merged gene list Samples The number of genes in the pathway in each list

Test data
---------

See the gene list files and genelists.txt file in data/


Contact
-------

Author: Guipeng Li

Email:  guipeng.lee@gmail.com
