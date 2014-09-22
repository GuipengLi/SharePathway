import numpy as np

def enrichment(*args, **kwargs):
    '''
    parse link path data into matrix
    Input: a gene list and link path data from KEGG rest
    Output: a matrix for enrichment
    '''
    GenesMat = kwargs.get('gMat', args[0])
    pathwayMat = kwargs.get('pMat', args[1])
    snum = GenesMat.shape[1]
    pnum = pathwayMat.shape[1]
    enrich = np.zeros([pnum,snum])
    for j in range(pnum):
        P = pathwayMat[:,j]
        # genes in pathway
        selectMat = GenesMat[P==1,:]
        # need to improve
        enrich[j,:] = selectMat.sum(axis=0)
    return enrich