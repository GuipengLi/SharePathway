def geneIDconv(*args, **kwargs):
    species = kwargs.get('species', 'hsa') #default: 'hsa'
    ngid = kwargs.get('NCBI-GeneID', 'ncbi-geneid')
    # KEGG ID conv from NCBI-GeneID to KEGG ID , though most of them are the same
    keggd=Request('conv',species,ngid)
    Kgid = {}
    for line in keggd:
        Kgid[line[0].split(':')[1]] = line[1]
    return Kgid