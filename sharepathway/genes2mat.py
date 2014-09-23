import numpy as np
def genes2mat(*args, **kwargs):
    '''
    parse gene lists into matrix
    Input: N gene lists, NCBI-GeneID
    Output: a matrix'''
    files = kwargs.get('files', args[0]) #default: 'hsa'
    KGID = kwargs.get('kgid', args[1])
    samplesnum = kwargs.get('N', 10)
    Genes = []
    tmpset = set()
    genelists = []
    i = 0
    j = 0
    k = 0
    with open(files, 'r') as fs:
        for f in fs:
            print(("Loading the file " + files))
            f = f.strip()
            genelists.append([])
            with open(f,'r') as genelist:
                for gene in genelist:
                    gene = gene.strip()
                    if gene in KGID:
                        gene = KGID[gene]
                        #gene = geneIDconv(gene)
                        genelists[j].append(gene)
                        if gene not in tmpset:
                            Genes.append(gene)
                            tmpset.add(gene)
            j = j+1
        genesnum = len(Genes)
        samplesnum = len(genelists)
        GenesMat = np.zeros([genesnum,samplesnum])
        j = 0
        for gl in genelists:
            for g in gl:
                GenesMat[Genes.index(g),j] = 1
            j = j+1
    return [Genes, genelists, GenesMat]

