#!/usr/bin/env python3

"""
Program: Parser
Date Created: 2nd April 2020

Author: Florence Lai / Oliver Cant 
Programe: Genbank parser 
Function: Read Genbank download and greps relevant information to and create upload file for MYSQL database

Description
-----------
This program reads the Genbank chromosome 6 download and greps the following for each entry:

accession
gene_id
location 
product
CDS
protein_seq
dna_seq

Return
------
List of lists:
[[‘accession1’, ’gene_id1’, ’location1’, ’product1’, ’CDS1’, ’Protein Sequence1’, ’dna_seq1’]
[  ‘accessionX’, ’gene_idX’, ’location X’, ’product X’, ’CDS X’, ’Protein SequenceX’, ’dna_seqX’]]

"""

import re
all_info = []
all_info2 = []
record = []

with open('C:/Users/user/Documents/BBK/Biocomputing/chrom_CDS_6.txt', 'r') as f:
    info = f.read().split('//\n')[:-1]
    
#removing all records with non-standard dna sequences   
for i in info:     
    seq_check = re.compile(r'\nORIGIN(.*)', re.DOTALL)
    seq_check = seq_check.findall(i)
    for k in seq_check:
        if 'y' not in k and 'r' not in k and 'n' not in k and 'w' not in k and 's' not in k \
        and 'm' not in k and 'k' not in k and 'k' not in k and 'r'  not in k and 'b' not in k \
        and 'd' not in k and 'h' not in k and 'v' not in k and 'z' not in k:
            all_info.append(i)


#filter out entries with allele
for i in all_info:
    if 'gene=' in i and 'map=' in i and '/translation=' in i\
    and  '/product=' in i and '/allele=' not in i:
        record.append(i)

chrom_6_data = []
        
for i in record:  
    dsq = re.compile(r'\nORIGIN(.*)', re.DOTALL)
    dsq = dsq.findall(i)    
    for k in dsq:
        dna_seq = re.compile(r'[a-z]+', re.DOTALL)
        dna_seq = dna_seq.findall(k)
        dna_seq = ''.join(dna_seq)
        dna_seq = dna_seq.upper()
   
    a = re.compile(r'ACCESSION\s+(.*)')
    a = a.findall(i) 
    
    for accession in a:
        accession = accession.split( )[0:1]
        accession = accession.pop(0)
        

    loc = re.compile(r'map="(.*)')
    loc = loc.findall(i) # print all location from map=
    loc = [loc.replace('"', '') for loc in loc]
    location = loc.pop(0)
    
    gn = re.compile(r'gene="(.*)') # greping gene CDS id
    gn = gn.findall(i)
    gn = [gn.replace('"', '') for gn in gn]
    gene = gn.pop(0)
    
           
    prt = re.compile(r'product="(.*)')
    prt = prt.findall(i)    
    prt = [prt.replace('"', '') for prt in prt]
    prt = [prt.replace(',','') for prt in prt] # remove commas from protein product for import to sql
    product = prt.pop(0)

             
    prot_seq = re.compile(r'translation="([A-Z\s]+)"', re.DOTALL)
    prot_seq = prot_seq.findall(i)  
    prot_seq = [prot_seq.replace('\n','') for prot_seq in prot_seq]
    prot_seq = [prot_seq.replace(" ",'') for prot_seq in prot_seq]
    protein_seq = prot_seq.pop(0)
    
    cds = re.compile(r'CDS\s{13}([^\/]*)')
    cds = cds.findall(i)
    cds = [cds.replace('<', '') for cds in cds]
    cds = [cds.replace('>', '') for cds in cds]
    cds = [cds.replace(')', '') for cds in cds]
    cds = [cds.replace('\n', '') for cds in cds]
    cds = [cds.replace(' ', '') for cds in cds]
    cds = [cds.replace(',', ';') for cds in cds]
    cds = cds.pop(0)
    all_cds.append(cds)    
     
    value = [gene, accession, product, location, cds, protein_seq, dna_seq]
   
    chrom_6_data.append(value) # create list of lists 
              
# write data to text file "chrom_6_data"

with open('mysql_data.txt', 'w') as f:
    for item in chrom_6_data:
        f.write("%s\n" % item)

