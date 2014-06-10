# -*- coding: utf-8 -*-
from itertools import chain, groupby
from collections import defaultdict
import pickle
import urllib2
import numpy as np

from sharepathway.enrichment import enrichment
from sharepathway.geneIDconv import geneIDconv
from sharepathway.genes2mat import genes2mat
from sharepathway.linkpath2mat import linkpath2mat
from sharepathway.out2html import out2html
from parse_kegg import Request

def Run(*args, **kwargs):

    species = kwargs.get('species', 'hsa') #default: 'hsa'
    filein = kwargs.get('fi')
    fileout = kwargs.get('fo')

    fileout = fileout+'.html'
    ratio = kwargs.get('r',0.01)
    # parse gene lists into matrix
    KGID = geneIDconv(species=species)
    [Genes, genelists, GenesMat] = genes2mat(filein,KGID)
    # load KEGG data
    data=Request('link','path',species)
    # parse KEGG into matrix
    [Pathways, pathwaycount, pathwayMat] = linkpath2mat(Genes, data)
    enrich = enrichment(GenesMat, pathwayMat)
    result = out2html(GenesMat, pathwayMat,enrich,Genes,Pathways,genelists,pathwaycount,ratio,fileout)
