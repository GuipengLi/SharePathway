def readfiles(*args, **kwargs):
    '''
    parse gene list files into genelists
    Input: N gene lists, NCBI-GeneID
    Output: list of lists (genelists)'''
    files = kwargs.get('files', args[0])
    KGID = kwargs.get('kgid', args[1])
    Genes = []
    tmpset = set()
    genelists = []
    j = 0
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
    return [Genes, genelists]
