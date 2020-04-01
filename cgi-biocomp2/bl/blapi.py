#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 22:18:40 2020

@author: florence
"""

#import dbapi   # Import the database api
#import config  # Import configuration information 

import dbapi_dummy as dbapi




def getAllEntries():
    '''
    function to return all entries fro database which contains chromosome 6
    data from the database to the front end
    >>> getAllEntries()
    [{'gene_id': 'HLA-DQA1', 'accession': 'AB006907', 'product': 'HMC class II surface glycoprotein', 'location': '6p21.3'}, {'gene_id': 'HLA-DQA1', 'accession': 'AB006908', 'product': 'MHC class II surface glycoprotein', 'location': '6p21.3'}, {'gene_id': 'HLA-DMA', 'accession': 'AB010385', 'product': 'HLA-DMA', 'location': '6p21.3'}]
    >>>
    '''
    
    return(dbapi.getAllEntries())
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()    
    
   
def getEntry(accession, re):
    
    '''
    getting gene id and choice of restriction enzyme information from the front end
    will return gene id, accession number, product, location,  protein sequence
    the dna sequence and the codon usage frequency with the total codon usage frequence
    of chromsome 6#    
    '''
    
    gene_record = dbapi.getEntry("accession" = accession)
#formating cds coming from database-maynot needed, depending on whether data has been cleaned up to only contain 
#coding region in rage of numbers i the pre-agreed format. For example 1..82
    for i in cds: 
        cds = [i.replace('<', '') for i in i]
        cds = [i.replace('>', '') for i in i]
        cds = [i.replace('complement(', '') for i in i]
        cds = [i.replace('join(', '') for i in i]
        cds = [i.replace(')', '') for i in i]         
        cds = cds.pop(0)   
        coding_dna = re.compile(r'\d+')  
        coding_dna = coding_dna.findall(cds)
        cds = re.sub(r'\w+\d+\.\d+:','',cds)

    for d in dna_seq:
        if 'CDS             complement('  in i:        
            dna_seq = [dna_seq.replace('A', '1') for dna_seq in dna_seq]
            dna_seq = [dna_seq.replace('T', '2') for dna_seq in dna_seq]
            dna_seq = [dna_seq.replace('C', '3') for dna_seq in dna_seq]
            dna_seq = [dna_seq.replace('G', '4') for dna_seq in dna_seq]
            dna_seq = [dna_seq.replace('1', 'T') for dna_seq in dna_seq]
            dna_seq = [dna_seq.replace('2', 'A') for dna_seq in dna_seq]
            dna_seq = [dna_seq.replace('3', 'G') for dna_seq in dna_seq]
            dna_seq = [dna_seq.replace('4', 'C') for dna_seq in dna_seq]
            dna_seq = dna_seq[::-1]
            dna_seq = ''.join(dna_seq)
            

        bases = []
        for i in coding_dna:
            base = int(i)
            bases.append(base)
            cds_pairs = [bases[i:i + 2] for i in range(0, len(bases), 2)]
         
            
            cds_pairs = cds_pairs[::-1] 
            for i,k in cds_pairs:   
                dna_seq = dna_seq.replace(dna_seq[i:], '<<tag>>' + dna_seq[i:]).replace(dna_seq[k:], '<<tag>>' + dna_seq[k:])
        
        
    
    return(r_gene_record)

#'''