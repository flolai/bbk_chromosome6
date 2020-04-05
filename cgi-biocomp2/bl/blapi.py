#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 22:18:40 2020

@author: florence
"""

#import dbapi   # Import the database api
#import config  # Import configuration information 

import dbapi_dummy as dbapi
import re

def getAllEntries():
    '''
    function to return all entries fro database which contains chromosome 6
    data from the database to the front end
    >>> getAllEntries()
    [{'gene_id': 'HLA-DQA1', 'accession': 'AB006907', 'product': 'HMC class II surface glycoprotein', 'location': '6p21.3'}, {'gene_id': 'HLA-DQA1', 'accession': 'AB006908', 'product': 'MHC class II surface glycoprotein', 'location': '6p21.3'}, {'gene_id': 'HLA-DMA', 'accession': 'AB010385', 'product': 'HLA-DMA', 'location': '6p21.3'}]
    >>>
    '''
    
    return(dbapi.getAllEntries())
    
  
    
   
def getEntry(accession, rez): #remove re for now for testing
    
    '''
    getting gene id and choice of restriction enzyme information from the front end
    will return gene id, accession number, product, location,  protein sequence
    the dna sequence and the codon usage frequency with the total codon usage frequence
    of chromsome 6
    
    >>> getEntry('AB006907','EcoRI')
    {'gene_id': 'HLA-DQA1', 'accession': 'AB006907', 'product': 'HMC class II surface glycoprotein', 'location': '6p21.3', 'protein_seq': 'MILNKALMLGALALTTVMSPCGGEDIV', 'dna_seq': '<tag>ATGATCCTAAACAAAGCTCTGATGCTGGGGGCCCTTGCCCTGACCACCGTGATGAGCCCCTGTGGAGGTGAAGACATTGTGG</tag>', 'cds': '1..82', 'freq': {'CCT': '5.06', 'ATT': '1.27', 'TGT': '2.53', 'AGG': '1.27', 'AGA': '1.27', 'CGT': '1.27', 'TAA': '1.27', 'AGC': '2.53', 'GAC': '2.53', 'ACA': '2.53', 'TGA': '7.59', 'ATG': '3.80', 'AAG': '2.53', 'GAT': '3.80', 'AAC': '1.27', 'GGG': '3.80', 'CAT': '1.27', 'CTC': '1.27', 'ACC': '2.53', 'GGT': '1.27', 'TTG': '2.53', 'CCG': '1.27', 'TCT': '1.27', 'GAG': '2.53', 'GGC': '1.27', 'GGA': '1.27', 'TGC': '2.53', 'GTG': '5.06', 'CCC': '5.06', 'CTG': '5.06', 'GCC': '3.80', 'GCT': '2.53', 'ATC': '1.27', 'TCC': '1.27', 'CTA': '1.27', 'TGG': '2.53', 'CAA': '1.27', 'CAC': '1.27', 'CTT': '1.27', 'CCA': '1.27', 'AAA': '2.53', 'GAA': '1.27'}}
    '''
    
    gene_record = dbapi.getEntry(accession)
    
   
#formating cds coming from database-maynot needed, depending on whether data has been cleaned up to only contain 
#coding region in rage of numbers i the pre-agreed format. For example 1..82
    
    cds = [gene_record['cds']]
    cds = [cds.replace('<', '') for cds in cds]
    cds = [cds.replace('>', '') for cds in cds]
    cds = [cds.replace('complement(', '') for cds in cds]
    cds = [cds.replace('join(', '') for cds in cds]
    cds = [cds.replace(')', '') for cds in cds]         
    cds = cds.pop(0)   
    coding_dna = re.compile(r'\d+')  
    coding_dna = coding_dna.findall(cds)
    cds = re.sub(r'\w+\d+\.\d+:','',cds)

    dna_seq = gene_record['dna_seq']
    for d in dna_seq:
        if 'complement('  in gene_record['cds']:        
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
        
    cds_in_dna = ''
    
    for start,end in cds_pairs:
        start = start-1         
        cds_in_dna += dna_seq[start:end]
        dna_seq = dna_seq[:start]+ '<tag>' + dna_seq[start:end].lower() + '</tag>' + dna_seq[end:]
        
        
    if rez == 'EcoRI'and 'GAATTC' in dna_seq :  
        dna_seq = dna_seq.replace('GAATTC', 'G<<RE>>AATTC') 
        
    if rez == 'BamHI'and 'GGATCC' in dna_seq :  
        dna_seq = dna_seq.replace('GGATCC', 'G<<RE>>GATCC')
        
    if rez == 'BsuMI'and 'CTCGAG' in dna_seq :  
        dna_seq = dna_seq.replace('CTCGAG', '<<RE>>CTCGAG') 
        
    if rez == 'KpnI'and 'GGTACC' in dna_seq :  
        dna_seq = dna_seq.replace('GGTACC', 'GGTACC<<RE>>') 
        
    if rez == 'EcoRV'and 'GATATC' in dna_seq :  
        dna_seq = dna_seq.replace('GATATC', 'GAT<<RE>>ATC') 
        
    if rez == 'SmaI'and 'CCCGGG' in dna_seq :  
        dna_seq = dna_seq.replace('CCCGGG', 'CCC<<RE>>GGG')
        
    if rez == 'MscI'and 'TGGCCA' in dna_seq :  
        dna_seq = dna_seq.replace('TGGCCA', 'TGG<<RE>>CCA')  
      

#calculating cds codon frequency
    codon_in_gene = []        
    for n in range(len(cds_in_dna) - 3):
        codon = cds_in_dna[n: n + 3]
        codon_in_gene.append(codon)
    
    len_seq = len(codon_in_gene)
                
    codon_dict = {}    
    for i in set(codon_in_gene):
        if i in codon_dict.keys():
            codon_dict[i] += codon_in_gene.count(i)
        else:
            codon_dict[i] = codon_in_gene.count(i) 

    codon_freq = {}

    for i in codon_dict:
        codon_freq[i] = '{0:.2f}'.format(((codon_dict[i]))/len_seq*100) 
   
    r_gene_record = {}

    key = ['gene_id','accession','product','location','protein_seq','dna_seq','cds','freq']  
    value = [gene_record['gene_id'], gene_record['accession'], gene_record['product'],\
             gene_record['location'],gene_record['protein_seq'], dna_seq.upper(), cds, codon_freq]
    
    r_gene_record = dict(zip(key,value))
        
    
    
    
    return(r_gene_record)
    
print(getEntry('AB011399', 'EcoRI'))

#if __name__ == '__main__':
#    import doctest
#    doctest.testmod()  