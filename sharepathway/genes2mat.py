import numpy as np
def genes2mat(*args, **kwargs):
    '''
    parse gene lists into matrix
    Input: N gene lists, NCBI-GeneID
    Output: a matrix'''
    genelists = kwargs.get('glists', args[0])
    Genes = kwargs.get('genes', args[1])
    samplesnum = kwargs.get('N', 10)

    genesnum = len(Genes)
    samplesnum = len(genelists)
    GenesMat = np.zeros([genesnum,samplesnum])
    j = 0
    for gl in genelists:
        for g in gl:
            GenesMat[Genes.index(g),j] = 1
        j = j+1
    return GenesMat

