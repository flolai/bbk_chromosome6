#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Program:    Total codon frequency calculation for records from Genbank
File:       tolal_codon_cal.py

Version:    V1.0
Date Created:       11.03.20
Function:   Calculation of total codon frequency in chromosome 6.

Copyright:  Florence Lai, Birkbeck, 2020
Author:     Florence Lai
            
--------------------------------------------------------------------------

This program is released under the GNU Public Licence (GPL V3)

--------------------------------------------------------------------------
Description:
============
Parsing of Genbank DNA sequence from 'ORIGIN' section of the 
Genbank record and using this information to calculate the usage
of codon in chromosome 6.
 

'''

import re
all_info = []

with open('/home/florence/Documents/Bioinformatics_MSc/biocomputing_2/chrom_CDS_6', 'r') as f:
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



record_no_comp = []
record_comp = []
new_records = []

#spliting data into two part, complementing strand data and non-complementing normal sequences
for i in all_info:
    if 'gene=' in i and 'map=' in i and '/translation=' in i\
    and  '/product=' in i and '/allele=' not in i and \
    'CDS             complement('  not in i:
        record_no_comp.append(i)
        
for i in all_info:
    if 'gene=' in i and 'map=' in i and '/translation=' in i\
    and 'CDS             complement('  in i and '/product=' in i and \
    '/allele=' not in i:
        record_comp.append(i)        

        

#reversing complement strand, also reversing the order of the sequence to make 
#all sequence direction from 5' to 3'
        
for i in record_comp:
    dsq_comp = re.compile(r'\nORIGIN(.*)', re.DOTALL)
    dsq_comp = dsq_comp.findall(i)
    
    for k in dsq_comp:
        comp_seq = re.compile(r'[a-z]+', re.DOTALL)
        comp_seq = comp_seq.findall(k)
        comp_seq = [comp_seq.replace('a', '1') for comp_seq in comp_seq]
        comp_seq = [comp_seq.replace('t', '2') for comp_seq in comp_seq]
        comp_seq = [comp_seq.replace('c', '3') for comp_seq in comp_seq]
        comp_seq = [comp_seq.replace('g', '4') for comp_seq in comp_seq]
        comp_seq = [comp_seq.replace('1', 't') for comp_seq in comp_seq]
        comp_seq = [comp_seq.replace('2', 'a') for comp_seq in comp_seq]
        comp_seq = [comp_seq.replace('3', 'g') for comp_seq in comp_seq]
        comp_seq = [comp_seq.replace('4', 'c') for comp_seq in comp_seq]
        comp_seq = comp_seq[::-1]
        comp_seq = ''.join(comp_seq)

    dsq_comp = dsq_comp.pop()
    new_record = i.replace(dsq_comp, comp_seq)
    
    new_records.append(new_record)

#combining records of 'normal' DNA sequence and the processed complement strand
    
full_record = record_no_comp + new_records


total_len = 0
codon_dict = {}
     
for i in full_record:
    dsq = re.compile(r'\nORIGIN(.*)', re.DOTALL)
    dsq = dsq.findall(i)    
    for k in dsq:
        dna_seq = re.compile(r'[a-z]+', re.DOTALL)
        dna_seq = dna_seq.findall(k)
        dna_seq = ''.join(dna_seq)
        dna_seq = dna_seq.upper() # making sequence in upper case for consistancy with blapi
        
        codon_in_gene = []
   
        for n in range(len(dna_seq) - 3):
            codon = dna_seq[n: n + 3]
            codon_in_gene.append(codon)
    
        len_seq = len(codon_in_gene)
        total_len +=  len_seq
        
        
        for i in set(codon_in_gene):
            if i in codon_dict.keys():
                codon_dict[i] += codon_in_gene.count(i)
            else:
                codon_dict[i] = codon_in_gene.count(i)
                

codon_freq = {}

#calculating total codon usage for chromosome 6
for i in codon_dict:
    codon_freq[i] = '{0:.2f}'.format(((codon_dict[i]))/total_len*100)
    

codon_freq = dict(sorted(codon_freq.items()))

  

