import numpy as np

def linkpath2mat(*args, **kwargs):
    '''
    parse link path data into matrix
    Input: a gene list and link path data from KEGG rest
    Output: a matrix for enrichment
    '''
    Genes = kwargs.get('genes', args[0])
    data = kwargs.get('pathways', args[1])
    genesnum = len(Genes)
    Pathways = []
    i = 0
    # pathway genes count
    pathwaycount = []
    for line in data:
        # ('hsa:10', 'path:hsa00983')
        #gene = geneIDconv(gene)
        gene = line[0]
        pathway = line[1]
        if pathway not in Pathways:
            Pathways.append(pathway)
            pathwaycount.append(1)
        else:
            pathwaycount[Pathways.index(pathway)] = pathwaycount[Pathways.index(pathway)]+1
    pathwaysnum = len(Pathways)
    # generate matrix
    pathwayMat = np.zeros([genesnum, pathwaysnum])
    for line in data:
        gene = line[0]
        pathway = line[1]
        if gene in Genes:
            i = Genes.index(gene)
            j = Pathways.index(pathway)
            pathwayMat[i,j] = 1
    return [Pathways, pathwaycount, pathwayMat]