import numpy as np
import time
from scipy import stats

def out2html(*args, **kwargs):
    '''
    parse link path data into matrix
    Input: a gene list and link path data from KEGG rest
    Output: a matrix for enrichment
    '''
    print('Saving the result to html...')
    localtime = time.asctime(time.localtime(time.time()))
    #Genes = kwargs.get('enrich', args[0])
    #Pathways = kwargs.get('GenesMat', args[1])
    GenesMat = kwargs.get('GenesMat', args[0])
    pathwayMat = kwargs.get('pathwayMat', args[1])
    enrich = kwargs.get('enrich', args[2])
    Genes = kwargs.get('Genes', args[3])
    Pathways = kwargs.get('Pathways', args[4])
    genelists = kwargs.get('genelists', args[5])
    pathwaycount = kwargs.get('pathwaycount', args[6])
    rr = kwargs.get('ratio',args[7])
    outfilename = kwargs.get('output', args[8])
    pwid2name = dict(kwargs.get('pwid2name', args[9]))
    snum = GenesMat.shape[1]
    pnum = pathwayMat.shape[1]
    gnum = GenesMat.shape[0]
    genelistscount = [len(gl) for gl in genelists]
    with open(outfilename+'-test', 'w') as fs:
        for i in range(enrich.shape[0]):
            ratio = (np.sum(enrich[i,:]>0)+0.0)/enrich.shape[1]
            if ratio > rr:
                line = str(enrich[i,:]) + '\t'+str(ratio)+'\n'
                fs.write(line)
    outfile = open(outfilename, "w")

    print >>outfile, """<!doctype html>
<html lang="en-US">
<head>
    <meta charset="utf-8">
    <title>Sharepathway Result</title>
    <meta name="author" content="Guipeng Li">
    <script type="text/javascript" src="http://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.0/jquery.min.js" ></script>
    <script type="text/javascript" src="http://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.1/js/jquery.tablesorter.min.js"></script>
    <style>
        #myTable {
          margin: 0 auto;
          font-size: 1.2em;
          margin-bottom: 10px;
          border:1px solid #cccccc;
        }
        #myTable thead {
          cursor: pointer;
          background: #c9dff0;
        }
        #myTable thead tr th {
          font-weight: bold;
          padding: 12px 30px;
          padding-left: 42px;
        }
        #myTable thead tr th span {
          padding-right: 20px;
          background-repeat: no-repeat;
          background-position: 100% 100%;
        }
        #myTable thead tr th.headerSortUp, #myTable thead tr th.headerSortDown {
          background: #acc8dd;
        }
        #myTable tbody tr {
          color: #555;
        }
        #myTable tbody tr td {
          text-align: center;
          padding: 6px 4px;
          border:1px solid #cccccc;
        }
        #myTable tbody tr td.lalign {
          text-align: left;
        }
        #footerText {
          text-align: center;
          background: #c9dff0;
        }
    </style>
    <script>
      $(document).ready(function()
        {
            $("#myTable").tablesorter( {sortList: [[5,1], [4,1]]} );
        }
      );
    </script>
</head>"""
    #summary
    print >>outfile, """
<body>
<div id='summary'>
<h1>Summary</h1>
<h2>
<ul>
    <li>Species: %s</li>
    <li>Totol number of pathway: %d</li>
    <li>Number of input samples: %d </li>
    <li>Number of input genes per sample: %s</li>
    <li>Totol number of unique input genes: %d</li>
    <li>This file is created by <a href="https://github.com/GuipengLi/SharePathway">sharepathway</a> at %s</li>
</ul>
</h2>
</div>
""" %('hsa',pnum,snum,str(genelistscount),gnum, localtime)


    print >>outfile, """
<div id='Details'>
<h1>Details</h1>
<table id="myTable" class="tablesorter">
<thead>
<tr>
    <th>Pathway</th>
    <th>Genes</th>
    <th>pCount</th>
    <th>Count</th>
    <th>Ratio</th>
    <th>-lg(P-value)</th>
    <th>Samples</th>
</tr>
</thead>
<tbody>"""
    counter = 1
    for i in range(enrich.shape[0]):
        ratio = (np.sum(enrich[i,:]>0)+0.0)/enrich.shape[1]
        if ratio > rr:
            samples = enrich[i,:]
            ratio = ratio
            # prepare the table
            pathwayid = Pathways[i]
	    if pathwayid in pwid2name:
	        pwname = pwid2name[pathwayid].split('-')[0].strip()
            genes = [g for g,p in zip(Genes,pathwayMat[:,i]) if p]
            genesid = '+'.join([g.split(':')[1] for g in genes])
            mapid = "http://www.kegg.jp/pathway/"+pathwayid.split(':')[1]+'+'+genesid
            count = len(genes)
            # get p-value
            pn = pathwaycount[i]
            x2value = 0
            j = 0
            for s in samples:
                fp = stats.fisher_exact([[s,genelistscount[j]],[pn,20000]])[1]
                #if fp<0.1:
                #    print(s,pn,genelistscount[j],fp)
                j = j+1
                x2value = x2value -2*np.log(fp)
            pvalue = -np.log10(1 - stats.chi2.cdf(x2value,2*snum)+1e-10)
            # hyperlink to mapid
            print >>outfile, '''<tr><td><a href="%s">%s</a></td><td>%s</td><td>%s</td><td>%s</td><td>%.2f</td><td>%.2f</td><td>%s</td></tr>''' % (
                mapid, pwname, genes, pn,count, ratio, pvalue, str(samples))
        counter += 1
    print >>outfile, """</tbody></table></div>"""
    print >>outfile, """<div id='footerText'>Copyright 2014-2017 by Guipeng Li. All Rights Reserved.<br></div></body></html>"""
    return enrich
