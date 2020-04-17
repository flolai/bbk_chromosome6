#!/usr/bin/env python3

"""
Program:    blapi
File:       blapi.py

Version:    V1.0
Date Created:       11.03.20
Function:   Obtain Genbank Chromosome 6 Accession number, Gene ID, protein sequences
            and dna sequences from dbapi.py to the front end

Copyright:  Florence Lai, Birkbeck, 2020
Author:     Florence Lai
            
--------------------------------------------------------------------------

This program is released under the GNU Public Licence (GPL V3)

--------------------------------------------------------------------------
Description:
============
This program takes Genbank accession number from the front end and pass it
to the database layer for Genbank data query. Relavent information like protein
sequence and dna sequence with coding region ready to be highlighted by the
front end. 

"""

#*************************************************************************
# Precalculated total codon frequency to return

total_codon_freq = {'AAA': '3.73','AAC': '1.66','AAG': '1.96','AAT': '2.17',
 'ACA': '1.96','ACC': '1.58','ACG': '0.92','ACT': '1.78','AGA': '2.20',
 'AGC': '0.77','AGG': '1.70','AGT': '1.79','ATA': '1.91','ATC': '1.28',
 'ATG': '1.43','ATT': '2.19','CAA': '1.61','CAC': '1.51','CAG': '1.45',
 'CAT': '1.42','CCA': '1.49','CCC': '1.39','CCG': '0.86','CCT': '1.69',
 'CGA': '0.91','CGC': '0.28','CGG': '0.86','CGT': '0.92','CTA': '1.29',
 'CTC': '1.74','CTG': '1.45','CTT': '1.96','GAA': '1.98','GAC': '1.61',
 'GAG': '1.75','GAT': '1.29','GCA': '0.79','GCC': '0.72','GCG': '0.29',
 'GCT': '0.77','GGA': '1.75','GGC': '0.72','GGG': '1.40','GGT': '1.58',
 'GTA': '1.47','GTC': '1.60','GTG': '1.54','GTT': '1.68','TAA': '2.20',
 'TAC': '1.47','TAG': '1.30','TAT': '1.93','TCA': '1.76','TCC': '1.74',
 'TCG': '0.91','TCT': '2.20','TGA': '1.78','TGC': '0.79','TGG': '1.49',
 'TGT': '1.99','TTA': '2.22','TTC': '1.99','TTG': '1.64','TTT': '3.80'}

#************************************************************************
#import libraries
import sys 

sys.path.insert(0, "../db/")
sys.path.insert(0, "../")

import re  
import dbapi   # Import the database api
import config  # Import configuration information


#*************************************************************************

def getAllEntries(accession = '', gene_id = '', product = '',\
             location = ''):
    '''
    function to return all entries from database which contains chromosome 6
    data from Genbank to the front end
    
    Input: depending on user data input could be any of the following.
    accession: Genbank accession number
    gene_id: Gene identifier
    product: protein product name
    location: chromasomal location
    If none was returned, full database information for chromasome 6 
    will return to front page.
    
    Return: [{'gene_id' : 'XXX', 'accession': 'XXX','product' :'XXX','location' :' XXX'}]
    -- A list of dictionaries containing Genbank accession numbers, Gene identifiers,
       protein product names adn chromosomal locations within chromosome 6
    
    '''
    
    accession = '' if accession == None else accession
    gene_id = '' if gene_id == None else gene_id
    product = '' if product == None else product
    location = '' if location == None else location
    
    return(dbapi.getAllEntries(accession = accession, gene_id = gene_id, \
                               product = product , location = location))
    
#************************************************************************     
def getEntry(accession = '', rez = ''): 
    rez = '' if rez == None else rez
    '''
    Taking accession number and a choice of restriction enzyme information from 
    the front end. After processing, this function will return Genbank 
    accession numbers, Gene identifiers, protein product names and chromosomal 
    locations within chromosome 6.
    Additionally, teh coding region will be marked with tags for front end to 
    process for highlighting. The codon usage frequency of that particular 
    gene and together with the total codon usage frequenceof chromsome 6 
    will also be returned.
    
    Input:
    accession: Genbank accession number
    rez: restriction enzyme choice of 7
    1.  EcoRI
    2.  BamHI
    3.  BsuMI
    4.  KpnI
    5.  EcoRV
    6.  SmaI
    7.  MscI
    
    Return:
    {'gene_id' : 'XXX', 'accession': 'XXX','product' : 'XXX','location' : 'XXX', 
    'protein_seq': 'xxx', 'dna_seq': '<tag>xx><<RE>>x</tag>', 'cds':'xxx',
    'freq':{AAA:0..'GGG':0}, 'total_freq':{AAA:0..'GGG':0}}
        
    '''
    
    gene_record = dbapi.getEntry(accession) 
    
   
#formating cds coming from database - removing non numerical strings
    
    cds = [gene_record['cds']]
#    cds = [cds.replace('<', '') for cds in cds]
#    cds = [cds.replace('>', '') for cds in cds]
    cds = [cds.replace('complement(', '') for cds in cds]
    cds = [cds.replace('join(', '') for cds in cds]
#    cds = [cds.replace(')', '') for cds in cds]         
    cds = cds.pop(0)   
    coding_dna = re.compile(r'\d+')  
    coding_dna = coding_dna.findall(cds)
    cds = re.sub(r'\w+\d+\.\d+:','',cds)

#formating dna sequences if it was on the complement strand
    
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
            dna_seq = dna_seq[::-1] # reversing the order of the sequence in order to match the cds range
            dna_seq = ''.join(dna_seq)
            

    bases = []
    
    for i in coding_dna:
        base = int(i)
        bases.append(base)
        cds_pairs = [bases[i:i + 2] for i in range(0, len(bases), 2)]
        cds_pairs = cds_pairs[::-1]
        
    cds_in_dna = ''

#adding tags on dna coding sequence based on coding pairs formatted from cds
    
    for start,end in cds_pairs:
        start = start-1         
        cds_in_dna += dna_seq[start:end]
        dna_seq = dna_seq[:start]+ '<mark>' + dna_seq[start:end].lower() + '</mark>' + dna_seq[end:]
        
#adding tags for restriction enzymes
        
    if rez == 'EcoRI'and 'GAATTC' in dna_seq :  
        dna_seq = dna_seq.replace('GAATTC', 'G|AATTC') 
        
    if rez == 'BamHI'and 'GGATCC' in dna_seq :  
        dna_seq = dna_seq.replace('GGATCC', 'G|GATCC')
        
    if rez == 'BsuMI'and 'CTCGAG' in dna_seq :  
        dna_seq = dna_seq.replace('CTCGAG', '|CTCGAG') 
        
    if rez == 'KpnI'and 'GGTACC' in dna_seq :  
        dna_seq = dna_seq.replace('GGTACC', 'GGTACC|') 
        
    if rez == 'EcoRV'and 'GATATC' in dna_seq :  
        dna_seq = dna_seq.replace('GATATC', 'GAT|ATC') 
        
    if rez == 'SmaI'and 'CCCGGG' in dna_seq :  
        dna_seq = dna_seq.replace('CCCGGG', 'CCC|GGG')
        
    if rez == 'MscI'and 'TGGCCA' in dna_seq :  
        dna_seq = dna_seq.replace('TGGCCA', 'TGG|CCA')  
      
    dna_seq = dna_seq.upper()
    dna_seq = dna_seq.replace('|', '<span class = "re">&starf;</span>')
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
        codon_freq = dict(sorted(codon_freq.items()))
   
    r_gene_record = {}

    key = ['gene_id','accession','product','location','protein_seq','dna_seq',\
           'cds','freq', 'total_freq', 'rez']  
    value = [gene_record['gene_id'], gene_record['accession'], gene_record['product'],\
             gene_record['location'],gene_record['protein_seq'], dna_seq, \
             cds, codon_freq, total_codon_freq, rez]
    
    r_gene_record = dict(zip(key,value))
                
    return(r_gene_record)    

