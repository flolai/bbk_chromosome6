#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:14:34 2020


@author: florence

updated by Oliver Cant Thurs 9th  April 21:

CDS regrex to capture new line
Entries with join included in dataset
Complement included in CDS if coding region is on complement 
Commas removed from product and protein to allow upload to database
Print output to text file for upload to database
Remove entries with accession reference in the cds entry - optional to discuss

"""
import csv
import time
t0 = time.clock()
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

## optional code below to remove entries with coding regions in other accessions entries / to discuss if to include
##for i in all_info:
##    cds_check = re.compile(r'CDS\s{13}([^\/]*)')
##    cds_check = cds_check.findall(i)
##    for k in cds_check:
##        if "a" not in k and "A" not in k and "b" not in k and "B" not in k \
##        and "x" not in k and "X" not in k and "j" not in k and "u" not in k and "f" not in k \
##        and "J" not in k and "U" not in k and "F" not in k and 'z' not in k and 'Z' not in k and 'AL' not in k \
##        and 'AP' not in k and "(Z" not in k and '(Z' not in k:
##            all_info2.append(i)
         
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
    a = a.findall(i) # print all accession number including one that has multiple accession numbers
    
    for accession in a:
        accession = accession.split( )[0:1]
        accession = accession.pop(0)
        

    loc = re.compile(r'map="(.*)')
    loc = loc.findall(i)# print all location from map=
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
   
    chrom_6_data.append(value)
              
with open('mysql_data5.txt', 'w') as f:
    for item in chrom_6_data:
        f.write("%s\n" % item)


t1 = time.clock()
print('Elapsed time: ', t1 - t0)
