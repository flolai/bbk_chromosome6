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
Testing:    Florence Lai
Edited:     Nini Nguyen
            
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



#************************************************************************
#import libraries
import sys 

sys.path.insert(0, "../db/")
sys.path.insert(0, "../")

import re  
import dbapi   # Import the database api
#import config  # Import configuration information

from config import total_codon_freq
#*************************************************************************

def getAllEntries(accession = None, gene_id = None, product = None, location = None):
    '''
    function to return all entries from database which contains chromosome 6
    data from Genbank to the front end
    
    Input: All of the following parameters.
    accession: Genbank accession number
    gene_id: Gene identifier
    product: protein product name
    location: chromasomal location
    If none was returned, full database information for chromasome 6 
    will return to front page.
    
    Return: [{'gene_id' : 'XXX', 'accession': 'XXX','product' :'XXX','location' :' XXX'}]
    -- A list of dictionaries containing Genbank accession numbers, Gene identifiers,
       protein product names and chromosomal locations within chromosome 6
       
   #Doctesting blapi 
   
       """ To test the getAllEntries function and return list of dictionaries after gene_id input.
           ----------------------------------------
           Verification:
           OK
       """     
       >>> getAllEntries(None,'NOTCH4', None, None)
       [{'gene_id': 'NOTCH4', 'accession': 'AB023961', 'product': 'notch4', 'location': '6p21.3'}, {'gene_id': 'NOTCH4', 'accession': 'D86566', 'product': 'notch related protein', 'location': '6p21.3'}, {'gene_id': 'NOTCH4', 'accession': 'U89335', 'product': 'notch4', 'location': '6p21'}, {'gene_id': 'NOTCH4', 'accession': 'U89336', 'product': 'G18', 'location': '6p21'}]

       """ To test the getAllEntries function and return list of dictionaries after accession input.
           -----------------------------------------
           Verification:
           OK
       """
       >>> getAllEntries('Z95326',None, None, None)
       [{'gene_id': 'SLC35F1', 'accession': 'Z95326', 'product': 'solute carrier family 35 member F1', 'location': 'q22.1-22.33'}]
       
       """ To test the getAllEntries function and return list of dictionaries after location input.
           -----------------------------------------
           Verification:
           OK
       """
       >>> getAllEntries(None,None, None,'6q22-q23')
       [{'gene_id': 'PDNP1', 'accession': 'AB032016', 'product': 'phosphodiesterase I/nucleotide pyrophosphatase', 'location': '6q22-q23'}]
       
       """
    
    '''
    
    return(dbapi.getAllEntries(accession = accession, gene_id = gene_id, \
                               product = product , location = location))
    
#************************************************************************     
def getEntry(accession, rez = ''): 
    '''
    This function will first taking accession number from 
    the front end. After processing, this function will return Genbank 
    accession numbers, Gene identifiers, protein product names and chromosomal 
    locations within chromosome 6.
    Additionally, the coding region will be marked with tags for highlighting. 
    The codon usage frequency of that gene together with the total codon usage 
    frequenceof chromsome 6 will also be returned.
    Should the user of the browser selected the choice of restriction enzymes
    available, the DNA sequence will then be further processed and return
    the same DNA sequence with restriction enzyme marked with star.
    
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
    -- {'gene_id' : 'XXX', 'accession': 'XXX','product' : 'XXX','location' : 'XXX', 
    'protein_seq': 'xxx', 'dna_seq': '[xx|x]', 
    'cds':'xxx','codon_freq':{'AAA':'0'..'GGG':'0'}, 'total_codon_freq':{'AAA': '0'..'GGG':'0'}}
    
        """ To test the getEntry function with accession input and to return list of dictionaries, restriction enzyme sites marked with stars on DNA sequence and total codon frequency.
            ---------------------------------------
            Verification:
            OK
        """
       
        >>> getEntry('AB023961')
        {'gene_id': 'NOTCH4', 'accession': 'AB023961', 'product': 'notch4', 'location': '6p21.3', 'protein_seq': 'MQPPSLLLLLLLLLLCVSVVRPRGLLCGSFPEPCANGGTCLSLSLGQGTCQCAPGFLGETCQFPDPCQNAQLCQNGGSCQALLPAPLGLPSSPSPLTPSFLCTCLPGFTGERCQAKLEDPCPPSFCSKRGRCHIQASGRPQCSCMPGWTGEQCQLRDFCSANPCVNGGVCLATYPQIQCHCPPGFEGHACERDVNECFQDPGPCPKGTSCHNTLGSFQCLCPVGQEGPRCELRAGPCPPRGCSNGGTCQLMPEKDSTFHLCLCPPGFIGPGCEVNPDNCVSHQCQNGGTCQDGLDTYTCLCPETWTGWDCSEDVDECEAQGPPHCRNGGTCQNSAGSFHCVCVSGWGGTSCEENLDDCIAATCAPGSTCIDRVGSFSCLCPPGRTGLLCHLEDMCLSQPCHGDAQCSTNPLTGSTLCLCQPGYSGPTCHQDLDECLMAQQGPSPCEHGGSCLNTPGSFNCLCPPGYTGSRCEADHNECLSQPCHPGSTCLDLLATFHCLCPP', 'dna_seq': '[ATGCAGCCCCCTTCACTGCTGCTGCTGCTGCTGCTGCTGCTGCTATGTGTCTCAGTGGTCAGACCCAGAG]GTGAGGCATGGCGTGGGTGAGGTGAGGGGACCCAGCTCCCTTAGGAGGATGATCAGTGGGGTGGGGGAAGAGGGCCAAGCCCCAGGCCGTGTGAGGGATGCTGGATGGAGGAGATTCTCACTGCCCAAATAGAGACGGCCTCCAGGGAAAGACGGCTCTGCCCATGGAGCTGCTTTGGGCCTGGTGCCAGGGGTGGTGACTGCTGGGGGATGGGTGAGAGGGTGCCCACCTCCAGGAAGAACCTCGTCAGCACTGGCACTGGAGGACTCTTGCAGCCATAGGGAAGAGGGGAAGAGGGAACACACTGACCACCTGCTTGGGGAGGAGATGAGAGGGAAGCAGGAGATGGGGACATGAAAGGTCAGGCCTACTAAGCCCTTTCTTAGTCCAGCTGTCCCCACCCCCCGGATGGCTCAATGCTCGGCCTTTCCGGGAGGAAATCTCTTCGAAGTCTCAGCCATTCACCTCCCGGGAGCCACCTCCGCCCCTCTTCTGACCCCTGTTGTCTTGCTTCCGAGAGATGGAGTCCGAGGCTGGACTTGGGAGGCCAGAGAATAAACAGGAAAGGGGGGTAGGGATTAGTAACTGGGACGGAGGGCACTGGGGCTGGGGCTGGGTACCATGTGGAGAGTGGGGACAGATGTGAAGAAGAGGTGGTTTAGAGTACCTGTGGGAGCTGCTGTGGGCAGGTCTCTCAGGAGCACCTAGAAGAGGAAAGGTGGAGGCACAGCACCCAGGGCTTCCATTGCGCCTGCCTCTCCTCCCTCAG[GGCTGCTGTGTGGGAGTTTCCCAGAACCCTGTGCCAATGGAGGCACCTGCCTGAGCCTGTCTCTGGGACAAGGGACCTGCCA]GTGAGTGTGCCTTGCAGGAGTGGGAGACTGGAGAGAAAGGGGGAGGGAGAGCAGGGGGGGAGAGGTGAGGAAGTGAGACCAAAGAAGAAAGAGAGGAAGTGAAGGAGATGAAGGGAAACAAATGAAGGCAGAGGAGGGAGTGGGCAAGAATAGGAAGAGGGGCCAGTGATGTGAGTTTTCCTCTCCTCCCCTGCCCAG[GTGTGCCCCTGGCTTCCTGGGTGAGACGTGCCAGTTTCCTGACCCCTGCCAGAACGCCCAGCTCTGCCAAAATGGAGGCAGCTGCCAAGCCCTGCTTCCCGCTCCCCTAGGGCTCCCCAGCTCTCCCTCTCCATTGACACCCAGCTTCTTGTGCACTTGCCTCCCTGGCTTCACTGGCGAGAGATGCCAGGCCAAGCTTGAAGACCCTTGTCCTCCCTCCTTCTGTTCCAAAAGGGGCCGCTGCCACATCCAGGCCTCGGGCCGCCCACAGTGCTCCTGCATGCCTGGATGGACAG]GTAAGCGCTGCTGGGGGCAGCCAGGAGGGGACAGGCAGGAGCAATGGGCTAGGCTGTGGGTGGGGAAGATAGAACTGGAGCCTGAGAAACTGCAAGCCCTTTGAAGACAGAAGCCATGAGAATCAACATGCCAATTCTTGGCAATCCACTTACCCACAACCAACATTCACCAGCATGGTTGTACTGATTGCTAAAATGTTAAAATATTTCCAAATTAAGGGTGCCATGAGCCCCCTTTGTGCACCATCCTGATGCCTGTCCTAGCCCCTTTAATCTCCCCATTGCCTAGCAGCTAGAAGAGGGTCATTGCTCTGCATACCAGGGGTCCTCCAGACTTTTGCATTCTGAGCATCTGAATGGCTCCCATTCTGAGTGGAGGGAGCCATTATATCACCTGGGAAGACTGCAGTGGTGGGAGGGGCACCGGGAAGGGAAGGATGTGACCCAGAGAGTGGATTGGGGGCCGCCCCAGGAGGAGGGGTGTAACCCTGGGGCAAGCTTAGTGCTTCATTCTAGGGGCTCTGCACCAGCCCCTGGATCCAAATGCTAGCTCTGCCACTGATCAGCTACATGACCTCATATAAGATATTTTAGCTTTCTGGTGTTCAGTTGTCAGCTGACAAACAGGGAGAGTAATGGTCACACTTCATAAGGTTGCTGAGAGGACAGAAGGGGCCGATGCTCAGGAGATGCTTGCTCAGCTCAGCACCTGGCACCTCCACTGCTGCCGCCATTACCACTGGTGCACATGGACTGTGAAGTGAGTCTCCAGGTGCCTAAACCCACTTAAAGATTAGGAAATGAGGTTCAGAAAGGCAAAGTGGCTCACCCAAGGGTATACAACCAGTTGTGGCACAGCATGGTGCCACCTGAGTCTCCTGCCTGCAGACGTGGGGTGCTTTTCACCTCCCCCAAGATCACCCACGTCCCAGATTTTCTCAGGCAAGGCCAATTTGCAATACTCTCATCATCACTTTAGAAGATATGGTCACTCCAGATAAACCCTCCCAAGCCATGACATCGCTCAGAGCAGGGGTGATGGAACAGAGCAAAGAAAGTATGGTAATAAAGGGAAGGAAATATGAAAATGAGACCCAGAGATAATCCAGAGTGAGCACTGGGTAACCTCAGATGGGCTAGAATTCGTACAATGCTAGAAACGGCTCCCTCTGTCCTCTGCCTCAG[GTGAGCAGTGCCAGCTTCGGGACTTCTGTTCAGCCAACCCATGTGTTAATGGAGGGGTGTGTCTGGCCACGTACCCCCAGATCCAGTGCCACTGCCCACCGGGCTTCGAGGGCCATGCCTGTGAACGTGATGTCAACGAGTGCTTCCAGGACCCAGGACCCTGCCCCAAAGGCACCTCCTGCCATAACACCCTGGGCTCCTTCCAGTGCCTCTGCCCTGTGGGGCAGGAGGGTCCACGTTGTGAGCTGCGGGCAGGACCCTGCCCTCCTAGGGGCTGTTCGAATGGGGGCACCTGCCAGCTGATGCCAGAGAAAGACTCCACCTTTCACCTCTGCCTCTGTCCCCCAG]GTGTGTCCTCACAGGGGCTCTCCGGCCGCCCCTCTCTCTGGGCAGGGCAGGATGTCTCCGTTGGAGCCTCCTCCCACAGCTGATCCATGACCCTGTCAG[GTTTCATAGGCCCGGGCTGTGAGGTGAATCCAGACAACTGTGTCAGCCACCAATGTCAGAATGGGGGCACTTGCCAGGATGGGCTGGACACCTACACCTGCCTCTGCCCAGAAACCTGGACAG]GTGAGTTGTTTAAGCCACATCCATGACACCCATGGCCCAGAGAGTTGGCCCCTGGCCTCCCCTACTCATAGGGCTCCCAGCCTTAGCCCTCGTCCCCTCCCCAACCCCCTGCAG[GCTGGGACTGCTCCGAAGATGTGGATGAGTGTGAGGCCCAGGGTCCCCCTCACTGCAGAAACGGGGGCACCTGCCAGAACTCTGCTGGTAGCTTTCACTGCGTGTGTGTGAGTGGCTGGGGGGGCACAAGCTGTGAGGAGAACCTGGATGACTGTATTGCTGCCACCTGTGCCCCGGGATCCACCTGCATTGACCGGGTGGGCTCTTTCTCCTGCCTCTGCCCACCTGGACGCACAG]GTATGGGGGTAGAGGGTATCAGGAGGTGGGAGGTAGAGAAGGAGGGTGAGAGAAGCACCAGGAGGACTGCTAGGAGCTTCAAATGGCCTTTGAGAGCCTCACCCCCTCTTACCCCTCCAG[GACTCCTGTGCCACTTGGAAGACATGTGTCTGAGCCAGCCGTGCCATGGGGATGCCCAATGCAGCACCAACCCCCTCACAGGCTCCACACTCTGCCTGTGTCAGCCTGGCTATTCGGGGCCCACCTGCCACCAGGACCTGGACGAGTGTCTGATGG]GTGAGGCCACTCCCACTTCAGAGCCTCTCTGAGCCTCAGACAGGCCTCTGCACTGAAGACAGAAAAGGGGGCAGATTGCTTTTCCAATTAAAAAACCAAACATCTTTTTCCTTGAATTTGCCCAGATTTGGCATCTCTTGCCTACATGACCCTCTCTCCAATGTTCAGCCCCTCAGTCCCCATGAATTTGGTCCCTTATTTCCTTTCCATCTTAAAGACACAAGCCCCTTCCCCAATTTGGTCTCGTCTGCCACACGCAGGCCCCCACACCTTCCCTGACAGTCTCACCTCCTTGCCCTTCCTGCCCTGACCCCTGTGGACTCCCAGCTCTTCTCTCCTCCCAG[CCCAGCAAGGCCCAAGTCCCTGTGAACATGGCGGTTCCTGCCTCAACACTCCTGGCTCCTTCAACTGCCTCTGTCCACCTGGCTACACAGGCTCCCGTTGTGAGGCTGATCACAATGAGTGCCTCTCCCAGCCCTGCCACCCAGGAAGCACCTGTCTGGACCTACTTGCCACCTTCCACTGCCTCTGCCCGCCAG]GTATCAGCTGGATGGGGCCTTGGGTGGGGAAAACAGGGAACTAGTCCTGAACCCACTAGGAATGCCCCCTCCAGAGTAAGGACAGCTTCAGGCCAATTGGCGTAAGTTACCACAGATGCT', 'cds': '1..70;840..921;1120..1415;2601..2948;3048..3170;3285..3521;3642..3797;4142..4336', 'freq': {'AAA': '0.53', 'AAC': '1.00', 'AAG': '0.86', 'AAT': '0.66', 'ACA': '1.33', 'ACC': '2.53', 'ACG': '0.60', 'ACT': '1.33', 'AGA': '1.33', 'AGC': '1.53', 'AGG': '2.19', 'AGT': '0.86', 'ATA': '0.13', 'ATC': '0.33', 'ATG': '1.73', 'ATT': '0.27', 'CAA': '1.33', 'CAC': '2.86', 'CAG': '3.19', 'CAT': '0.73', 'CCA': '4.32', 'CCC': '4.06', 'CCG': '0.73', 'CCT': '4.52', 'CGA': '0.40', 'CGC': '0.40', 'CGG': '0.66', 'CGT': '0.47', 'CTA': '0.47', 'CTC': '2.66', 'CTG': '5.92', 'CTT': '1.53', 'GAA': '1.06', 'GAC': '1.66', 'GAG': '1.60', 'GAT': '0.86', 'GCA': '1.33', 'GCC': '4.39', 'GCG': '0.27', 'GCT': '3.06', 'GGA': '1.93', 'GGC': '2.59', 'GGG': '3.12', 'GGT': '0.80', 'GTA': '0.20', 'GTC': '1.13', 'GTG': '2.99', 'GTT': '0.66', 'TAA': '0.13', 'TAC': '0.27', 'TAG': '0.27', 'TAT': '0.20', 'TCA': '1.13', 'TCC': '2.59', 'TCG': '0.33', 'TCT': '1.66', 'TGA': '1.60', 'TGC': '4.52', 'TGG': '2.46', 'TGT': '2.86', 'TTA': '0.07', 'TTC': '1.60', 'TTG': '0.80', 'TTT': '0.40'}, 'total_freq': {'AAA': '3.66', 'AAC': '1.67', 'AAG': '1.95', 'AAT': '2.21', 'ACA': '1.94', 'ACC': '1.53', 'ACG': '0.92', 'ACT': '1.77', 'AGA': '2.17', 'AGC': '0.83', 'AGG': '1.68', 'AGT': '1.78', 'ATA': '1.94', 'ATC': '1.31', 'ATG': '1.45', 'ATT': '2.23', 'CAA': '1.63', 'CAC': '1.49', 'CAG': '1.46', 'CAT': '1.45', 'CCA': '1.49', 'CCC': '1.38', 'CCG': '0.84', 'CCT': '1.67', 'CGA': '0.90', 'CGC': '0.32', 'CGG': '0.84', 'CGT': '0.92', 'CTA': '1.31', 'CTC': '1.71', 'CTG': '1.46', 'CTT': '1.96', 'GAA': '1.98', 'GAC': '1.55', 'GAG': '1.73', 'GAT': '1.32', 'GCA': '0.83', 'GCC': '0.77', 'GCG': '0.33', 'GCT': '0.83', 'GGA': '1.72', 'GGC': '0.76', 'GGG': '1.39', 'GGT': '1.54', 'GTA': '1.46', 'GTC': '1.54', 'GTG': '1.51', 'GTT': '1.69', 'TAA': '2.22', 'TAC': '1.46', 'TAG': '1.32', 'TAT': '1.95', 'TCA': '1.77', 'TCC': '1.71', 'TCG': '0.90', 'TCT': '2.17', 'TGA': '1.79', 'TGC': '0.84', 'TGG': '1.50', 'TGT': '1.97', 'TTA': '2.23', 'TTC': '1.99', 'TTG': '1.66', 'TTT': '3.73'}, 'rez': ''}

        """ To test the getEntry function with restriction enzyme and accession input and to return list of dictionaries with selected restriction enzyme sites on the DNA sequence marked with stars and total codon frequncy.
            ---------------------------------------
            Verification:
            OK
        """
        >>> getEntry('AB023961', 'EcoRI')
        {'gene_id': 'NOTCH4', 'accession': 'AB023961', 'product': 'notch4', 'location': '6p21.3', 'protein_seq': 'MQPPSLLLLLLLLLLCVSVVRPRGLLCGSFPEPCANGGTCLSLSLGQGTCQCAPGFLGETCQFPDPCQNAQLCQNGGSCQALLPAPLGLPSSPSPLTPSFLCTCLPGFTGERCQAKLEDPCPPSFCSKRGRCHIQASGRPQCSCMPGWTGEQCQLRDFCSANPCVNGGVCLATYPQIQCHCPPGFEGHACERDVNECFQDPGPCPKGTSCHNTLGSFQCLCPVGQEGPRCELRAGPCPPRGCSNGGTCQLMPEKDSTFHLCLCPPGFIGPGCEVNPDNCVSHQCQNGGTCQDGLDTYTCLCPETWTGWDCSEDVDECEAQGPPHCRNGGTCQNSAGSFHCVCVSGWGGTSCEENLDDCIAATCAPGSTCIDRVGSFSCLCPPGRTGLLCHLEDMCLSQPCHGDAQCSTNPLTGSTLCLCQPGYSGPTCHQDLDECLMAQQGPSPCEHGGSCLNTPGSFNCLCPPGYTGSRCEADHNECLSQPCHPGSTCLDLLATFHCLCPP', 'dna_seq': '[ATGCAGCCCCCTTCACTGCTGCTGCTGCTGCTGCTGCTGCTGCTATGTGTCTCAGTGGTCAGACCCAGAG]GTGAGGCATGGCGTGGGTGAGGTGAGGGGACCCAGCTCCCTTAGGAGGATGATCAGTGGGGTGGGGGAAGAGGGCCAAGCCCCAGGCCGTGTGAGGGATGCTGGATGGAGGAGATTCTCACTGCCCAAATAGAGACGGCCTCCAGGGAAAGACGGCTCTGCCCATGGAGCTGCTTTGGGCCTGGTGCCAGGGGTGGTGACTGCTGGGGGATGGGTGAGAGGGTGCCCACCTCCAGGAAGAACCTCGTCAGCACTGGCACTGGAGGACTCTTGCAGCCATAGGGAAGAGGGGAAGAGGGAACACACTGACCACCTGCTTGGGGAGGAGATGAGAGGGAAGCAGGAGATGGGGACATGAAAGGTCAGGCCTACTAAGCCCTTTCTTAGTCCAGCTGTCCCCACCCCCCGGATGGCTCAATGCTCGGCCTTTCCGGGAGGAAATCTCTTCGAAGTCTCAGCCATTCACCTCCCGGGAGCCACCTCCGCCCCTCTTCTGACCCCTGTTGTCTTGCTTCCGAGAGATGGAGTCCGAGGCTGGACTTGGGAGGCCAGAGAATAAACAGGAAAGGGGGGTAGGGATTAGTAACTGGGACGGAGGGCACTGGGGCTGGGGCTGGGTACCATGTGGAGAGTGGGGACAGATGTGAAGAAGAGGTGGTTTAGAGTACCTGTGGGAGCTGCTGTGGGCAGGTCTCTCAGGAGCACCTAGAAGAGGAAAGGTGGAGGCACAGCACCCAGGGCTTCCATTGCGCCTGCCTCTCCTCCCTCAG[GGCTGCTGTGTGGGAGTTTCCCAGAACCCTGTGCCAATGGAGGCACCTGCCTGAGCCTGTCTCTGGGACAAGGGACCTGCCA]GTGAGTGTGCCTTGCAGGAGTGGGAGACTGGAGAGAAAGGGGGAGGGAGAGCAGGGGGGGAGAGGTGAGGAAGTGAGACCAAAGAAGAAAGAGAGGAAGTGAAGGAGATGAAGGGAAACAAATGAAGGCAGAGGAGGGAGTGGGCAAGAATAGGAAGAGGGGCCAGTGATGTGAGTTTTCCTCTCCTCCCCTGCCCAG[GTGTGCCCCTGGCTTCCTGGGTGAGACGTGCCAGTTTCCTGACCCCTGCCAGAACGCCCAGCTCTGCCAAAATGGAGGCAGCTGCCAAGCCCTGCTTCCCGCTCCCCTAGGGCTCCCCAGCTCTCCCTCTCCATTGACACCCAGCTTCTTGTGCACTTGCCTCCCTGGCTTCACTGGCGAGAGATGCCAGGCCAAGCTTGAAGACCCTTGTCCTCCCTCCTTCTGTTCCAAAAGGGGCCGCTGCCACATCCAGGCCTCGGGCCGCCCACAGTGCTCCTGCATGCCTGGATGGACAG]GTAAGCGCTGCTGGGGGCAGCCAGGAGGGGACAGGCAGGAGCAATGGGCTAGGCTGTGGGTGGGGAAGATAGAACTGGAGCCTGAGAAACTGCAAGCCCTTTGAAGACAGAAGCCATGAGAATCAACATGCCAATTCTTGGCAATCCACTTACCCACAACCAACATTCACCAGCATGGTTGTACTGATTGCTAAAATGTTAAAATATTTCCAAATTAAGGGTGCCATGAGCCCCCTTTGTGCACCATCCTGATGCCTGTCCTAGCCCCTTTAATCTCCCCATTGCCTAGCAGCTAGAAGAGGGTCATTGCTCTGCATACCAGGGGTCCTCCAGACTTTTGCATTCTGAGCATCTGAATGGCTCCCATTCTGAGTGGAGGGAGCCATTATATCACCTGGGAAGACTGCAGTGGTGGGAGGGGCACCGGGAAGGGAAGGATGTGACCCAGAGAGTGGATTGGGGGCCGCCCCAGGAGGAGGGGTGTAACCCTGGGGCAAGCTTAGTGCTTCATTCTAGGGGCTCTGCACCAGCCCCTGGATCCAAATGCTAGCTCTGCCACTGATCAGCTACATGACCTCATATAAGATATTTTAGCTTTCTGGTGTTCAGTTGTCAGCTGACAAACAGGGAGAGTAATGGTCACACTTCATAAGGTTGCTGAGAGGACAGAAGGGGCCGATGCTCAGGAGATGCTTGCTCAGCTCAGCACCTGGCACCTCCACTGCTGCCGCCATTACCACTGGTGCACATGGACTGTGAAGTGAGTCTCCAGGTGCCTAAACCCACTTAAAGATTAGGAAATGAGGTTCAGAAAGGCAAAGTGGCTCACCCAAGGGTATACAACCAGTTGTGGCACAGCATGGTGCCACCTGAGTCTCCTGCCTGCAGACGTGGGGTGCTTTTCACCTCCCCCAAGATCACCCACGTCCCAGATTTTCTCAGGCAAGGCCAATTTGCAATACTCTCATCATCACTTTAGAAGATATGGTCACTCCAGATAAACCCTCCCAAGCCATGACATCGCTCAGAGCAGGGGTGATGGAACAGAGCAAAGAAAGTATGGTAATAAAGGGAAGGAAATATGAAAATGAGACCCAGAGATAATCCAGAGTGAGCACTGGGTAACCTCAGATGGGCTAG|AATTCGTACAATGCTAGAAACGGCTCCCTCTGTCCTCTGCCTCAG[GTGAGCAGTGCCAGCTTCGGGACTTCTGTTCAGCCAACCCATGTGTTAATGGAGGGGTGTGTCTGGCCACGTACCCCCAGATCCAGTGCCACTGCCCACCGGGCTTCGAGGGCCATGCCTGTGAACGTGATGTCAACGAGTGCTTCCAGGACCCAGGACCCTGCCCCAAAGGCACCTCCTGCCATAACACCCTGGGCTCCTTCCAGTGCCTCTGCCCTGTGGGGCAGGAGGGTCCACGTTGTGAGCTGCGGGCAGGACCCTGCCCTCCTAGGGGCTGTTCGAATGGGGGCACCTGCCAGCTGATGCCAGAGAAAGACTCCACCTTTCACCTCTGCCTCTGTCCCCCAG]GTGTGTCCTCACAGGGGCTCTCCGGCCGCCCCTCTCTCTGGGCAGGGCAGGATGTCTCCGTTGGAGCCTCCTCCCACAGCTGATCCATGACCCTGTCAG[GTTTCATAGGCCCGGGCTGTGAGGTGAATCCAGACAACTGTGTCAGCCACCAATGTCAGAATGGGGGCACTTGCCAGGATGGGCTGGACACCTACACCTGCCTCTGCCCAGAAACCTGGACAG]GTGAGTTGTTTAAGCCACATCCATGACACCCATGGCCCAGAGAGTTGGCCCCTGGCCTCCCCTACTCATAGGGCTCCCAGCCTTAGCCCTCGTCCCCTCCCCAACCCCCTGCAG[GCTGGGACTGCTCCGAAGATGTGGATGAGTGTGAGGCCCAGGGTCCCCCTCACTGCAGAAACGGGGGCACCTGCCAGAACTCTGCTGGTAGCTTTCACTGCGTGTGTGTGAGTGGCTGGGGGGGCACAAGCTGTGAGGAGAACCTGGATGACTGTATTGCTGCCACCTGTGCCCCGGGATCCACCTGCATTGACCGGGTGGGCTCTTTCTCCTGCCTCTGCCCACCTGGACGCACAG]GTATGGGGGTAGAGGGTATCAGGAGGTGGGAGGTAGAGAAGGAGGGTGAGAGAAGCACCAGGAGGACTGCTAGGAGCTTCAAATGGCCTTTGAGAGCCTCACCCCCTCTTACCCCTCCAG[GACTCCTGTGCCACTTGGAAGACATGTGTCTGAGCCAGCCGTGCCATGGGGATGCCCAATGCAGCACCAACCCCCTCACAGGCTCCACACTCTGCCTGTGTCAGCCTGGCTATTCGGGGCCCACCTGCCACCAGGACCTGGACGAGTGTCTGATGG]GTGAGGCCACTCCCACTTCAGAGCCTCTCTGAGCCTCAGACAGGCCTCTGCACTGAAGACAGAAAAGGGGGCAGATTGCTTTTCCAATTAAAAAACCAAACATCTTTTTCCTTGAATTTGCCCAGATTTGGCATCTCTTGCCTACATGACCCTCTCTCCAATGTTCAGCCCCTCAGTCCCCATGAATTTGGTCCCTTATTTCCTTTCCATCTTAAAGACACAAGCCCCTTCCCCAATTTGGTCTCGTCTGCCACACGCAGGCCCCCACACCTTCCCTGACAGTCTCACCTCCTTGCCCTTCCTGCCCTGACCCCTGTGGACTCCCAGCTCTTCTCTCCTCCCAG[CCCAGCAAGGCCCAAGTCCCTGTGAACATGGCGGTTCCTGCCTCAACACTCCTGGCTCCTTCAACTGCCTCTGTCCACCTGGCTACACAGGCTCCCGTTGTGAGGCTGATCACAATGAGTGCCTCTCCCAGCCCTGCCACCCAGGAAGCACCTGTCTGGACCTACTTGCCACCTTCCACTGCCTCTGCCCGCCAG]GTATCAGCTGGATGGGGCCTTGGGTGGGGAAAACAGGGAACTAGTCCTGAACCCACTAGGAATGCCCCCTCCAGAGTAAGGACAGCTTCAGGCCAATTGGCGTAAGTTACCACAGATGCT', 'cds': '1..70;840..921;1120..1415;2601..2948;3048..3170;3285..3521;3642..3797;4142..4336', 'freq': {'AAA': '0.53', 'AAC': '1.00', 'AAG': '0.86', 'AAT': '0.66', 'ACA': '1.33', 'ACC': '2.53', 'ACG': '0.60', 'ACT': '1.33', 'AGA': '1.33', 'AGC': '1.53', 'AGG': '2.19', 'AGT': '0.86', 'ATA': '0.13', 'ATC': '0.33', 'ATG': '1.73', 'ATT': '0.27', 'CAA': '1.33', 'CAC': '2.86', 'CAG': '3.19', 'CAT': '0.73', 'CCA': '4.32', 'CCC': '4.06', 'CCG': '0.73', 'CCT': '4.52', 'CGA': '0.40', 'CGC': '0.40', 'CGG': '0.66', 'CGT': '0.47', 'CTA': '0.47', 'CTC': '2.66', 'CTG': '5.92', 'CTT': '1.53', 'GAA': '1.06', 'GAC': '1.66', 'GAG': '1.60', 'GAT': '0.86', 'GCA': '1.33', 'GCC': '4.39', 'GCG': '0.27', 'GCT': '3.06', 'GGA': '1.93', 'GGC': '2.59', 'GGG': '3.12', 'GGT': '0.80', 'GTA': '0.20', 'GTC': '1.13', 'GTG': '2.99', 'GTT': '0.66', 'TAA': '0.13', 'TAC': '0.27', 'TAG': '0.27', 'TAT': '0.20', 'TCA': '1.13', 'TCC': '2.59', 'TCG': '0.33', 'TCT': '1.66', 'TGA': '1.60', 'TGC': '4.52', 'TGG': '2.46', 'TGT': '2.86', 'TTA': '0.07', 'TTC': '1.60', 'TTG': '0.80', 'TTT': '0.40'}, 'total_freq': {'AAA': '3.66', 'AAC': '1.67', 'AAG': '1.95', 'AAT': '2.21', 'ACA': '1.94', 'ACC': '1.53', 'ACG': '0.92', 'ACT': '1.77', 'AGA': '2.17', 'AGC': '0.83', 'AGG': '1.68', 'AGT': '1.78', 'ATA': '1.94', 'ATC': '1.31', 'ATG': '1.45', 'ATT': '2.23', 'CAA': '1.63', 'CAC': '1.49', 'CAG': '1.46', 'CAT': '1.45', 'CCA': '1.49', 'CCC': '1.38', 'CCG': '0.84', 'CCT': '1.67', 'CGA': '0.90', 'CGC': '0.32', 'CGG': '0.84', 'CGT': '0.92', 'CTA': '1.31', 'CTC': '1.71', 'CTG': '1.46', 'CTT': '1.96', 'GAA': '1.98', 'GAC': '1.55', 'GAG': '1.73', 'GAT': '1.32', 'GCA': '0.83', 'GCC': '0.77', 'GCG': '0.33', 'GCT': '0.83', 'GGA': '1.72', 'GGC': '0.76', 'GGG': '1.39', 'GGT': '1.54', 'GTA': '1.46', 'GTC': '1.54', 'GTG': '1.51', 'GTT': '1.69', 'TAA': '2.22', 'TAC': '1.46', 'TAG': '1.32', 'TAT': '1.95', 'TCA': '1.77', 'TCC': '1.71', 'TCG': '0.90', 'TCT': '2.17', 'TGA': '1.79', 'TGC': '0.84', 'TGG': '1.50', 'TGT': '1.97', 'TTA': '2.23', 'TTC': '1.99', 'TTG': '1.66', 'TTT': '3.73'}, 'rez': 'EcoRI'}

         """ To test the getEntry function with accession input and to return list of dictionaries, restriction enzyme sites marked with stars on DNA sequence and total codon frequency.
            ---------------------------------------
            Verification:
            OK
        """
        >>> getEntry('X68272')
        {'gene_id': 'HLA-DBR1', 'accession': 'X68272', 'product': 'HLA-DRbeta-chain', 'location': 'locus HLA-DBR1', 'protein_seq': 'RFLEQVKHECHFFNGTERVRFLDRYFYHQEEYVRFDSDVGEYRAVTELGRPDEEYWNSQKDFLEDRRAAVDTYCRHNYGVVE', 'dna_seq': '[CACGTTTCTTGGAGCAGGTTAAACATGAGTGTCATTTCTTCAACGGGACGGAGCGGGTGCGGTTCCTGGACAGATACTTCTATCACCAAGAGGAGTACGTGCGCTTCGACAGCGACGTGGGGGAGTACCGGGCGGTGACGGAGCTGGGGCGGCCTGATGAGGAGTACTGGAACAGCCAGAAGGACTTCCTGGAAGACAGGCGGGCCGCGGTGGACACCTACTGCAGACACAACTACGGGGTTGTGGAGAG]', 'cds': '1..250', 'freq': {'AAA': '0.40', 'AAC': '1.62', 'AAG': '1.21', 'ACA': '3.24', 'ACC': '1.21', 'ACG': '2.83', 'ACT': '2.02', 'AGA': '2.43', 'AGC': '2.02', 'AGG': '2.02', 'AGT': '1.62', 'ATA': '0.40', 'ATC': '0.40', 'ATG': '0.81', 'ATT': '0.40', 'CAA': '1.21', 'CAC': '1.62', 'CAG': '2.83', 'CAT': '0.81', 'CCA': '0.81', 'CCG': '0.81', 'CCT': '1.62', 'CGA': '0.81', 'CGC': '0.81', 'CGG': '4.45', 'CGT': '1.21', 'CTA': '1.21', 'CTG': '2.43', 'CTT': '2.02', 'GAA': '1.21', 'GAC': '3.64', 'GAG': '4.05', 'GAT': '0.81', 'GCA': '0.81', 'GCC': '1.21', 'GCG': '3.24', 'GCT': '0.81', 'GGA': '5.26', 'GGC': '2.02', 'GGG': '4.45', 'GGT': '2.43', 'GTA': '1.21', 'GTC': '0.40', 'GTG': '2.83', 'GTT': '1.62', 'TAA': '0.40', 'TAC': '2.43', 'TAT': '0.40', 'TCA': '1.21', 'TCC': '0.81', 'TCG': '0.40', 'TCT': '1.21', 'TGA': '1.62', 'TGC': '1.21', 'TGG': '3.24', 'TGT': '0.81', 'TTA': '0.40', 'TTC': '2.83', 'TTG': '0.81', 'TTT': '0.81'}, 'total_freq': {'AAA': '3.66', 'AAC': '1.67', 'AAG': '1.95', 'AAT': '2.21', 'ACA': '1.94', 'ACC': '1.53', 'ACG': '0.92', 'ACT': '1.77', 'AGA': '2.17', 'AGC': '0.83', 'AGG': '1.68', 'AGT': '1.78', 'ATA': '1.94', 'ATC': '1.31', 'ATG': '1.45', 'ATT': '2.23', 'CAA': '1.63', 'CAC': '1.49', 'CAG': '1.46', 'CAT': '1.45', 'CCA': '1.49', 'CCC': '1.38', 'CCG': '0.84', 'CCT': '1.67', 'CGA': '0.90', 'CGC': '0.32', 'CGG': '0.84', 'CGT': '0.92', 'CTA': '1.31', 'CTC': '1.71', 'CTG': '1.46', 'CTT': '1.96', 'GAA': '1.98', 'GAC': '1.55', 'GAG': '1.73', 'GAT': '1.32', 'GCA': '0.83', 'GCC': '0.77', 'GCG': '0.33', 'GCT': '0.83', 'GGA': '1.72', 'GGC': '0.76', 'GGG': '1.39', 'GGT': '1.54', 'GTA': '1.46', 'GTC': '1.54', 'GTG': '1.51', 'GTT': '1.69', 'TAA': '2.22', 'TAC': '1.46', 'TAG': '1.32', 'TAT': '1.95', 'TCA': '1.77', 'TCC': '1.71', 'TCG': '0.90', 'TCT': '2.17', 'TGA': '1.79', 'TGC': '0.84', 'TGG': '1.50', 'TGT': '1.97', 'TTA': '2.23', 'TTC': '1.99', 'TTG': '1.66', 'TTT': '3.73'}, 'rez': ''}

         """ To test the getEntry function with accession input and to return list of dictionaries, restriction enzyme sites marked with stars on DNA sequence and total codon frequency.
            ---------------------------------------
            Verification:
            OK
        """
        >>> getEntry('X64545')
        {'gene_id': 'HLA-DRB2', 'accession': 'X64545', 'product': 'MHC class II antigen', 'location': '6p21.3', 'protein_seq': 'MVCLKPPGGSCMAALTVTLMVLSSPLALA', 'dna_seq': 'CATACAGCATCTCTGACCAGCAACTGATGATGCTATTGAACTCAGACGCTGATTCATTCTCCAACACTAGATTACCCAATCCAGGAGCAAGGAAATCAGTAACTTCCTCCCTATAATTTGGAATATGGGTGGAGCAGGGTCATAGTTCTCGCTGAGTGAGACTTGACTGCCCCTCTGGGCCCTGGACCTGTCATGCTCCTTAGC[ATGGTGTGTCTGAAGCCCCCTGGAGGCTCCTGCATGGCAGCTCTGACAGTGACACTGATGGTGCTGAGCTCCCCACTGGCTTTGGCTG]', 'cds': '205..292', 'freq': {'AAG': '1.18', 'ACA': '2.35', 'ACT': '2.35', 'AGC': '3.53', 'AGG': '1.18', 'AGT': '1.18', 'ATG': '3.53', 'CAC': '2.35', 'CAG': '2.35', 'CAT': '1.18', 'CCA': '1.18', 'CCC': '5.88', 'CCT': '2.35', 'CTC': '3.53', 'CTG': '8.24', 'CTT': '1.18', 'GAA': '1.18', 'GAC': '2.35', 'GAG': '2.35', 'GAT': '1.18', 'GCA': '2.35', 'GCC': '1.18', 'GCT': '7.06', 'GGA': '1.18', 'GGC': '4.71', 'GGT': '2.35', 'GTC': '1.18', 'GTG': '4.71', 'TCC': '2.35', 'TCT': '2.35', 'TGA': '5.88', 'TGC': '2.35', 'TGG': '7.06', 'TGT': '2.35', 'TTG': '1.18', 'TTT': '1.18'}, 'total_freq': {'AAA': '3.66', 'AAC': '1.67', 'AAG': '1.95', 'AAT': '2.21', 'ACA': '1.94', 'ACC': '1.53', 'ACG': '0.92', 'ACT': '1.77', 'AGA': '2.17', 'AGC': '0.83', 'AGG': '1.68', 'AGT': '1.78', 'ATA': '1.94', 'ATC': '1.31', 'ATG': '1.45', 'ATT': '2.23', 'CAA': '1.63', 'CAC': '1.49', 'CAG': '1.46', 'CAT': '1.45', 'CCA': '1.49', 'CCC': '1.38', 'CCG': '0.84', 'CCT': '1.67', 'CGA': '0.90', 'CGC': '0.32', 'CGG': '0.84', 'CGT': '0.92', 'CTA': '1.31', 'CTC': '1.71', 'CTG': '1.46', 'CTT': '1.96', 'GAA': '1.98', 'GAC': '1.55', 'GAG': '1.73', 'GAT': '1.32', 'GCA': '0.83', 'GCC': '0.77', 'GCG': '0.33', 'GCT': '0.83', 'GGA': '1.72', 'GGC': '0.76', 'GGG': '1.39', 'GGT': '1.54', 'GTA': '1.46', 'GTC': '1.54', 'GTG': '1.51', 'GTT': '1.69', 'TAA': '2.22', 'TAC': '1.46', 'TAG': '1.32', 'TAT': '1.95', 'TCA': '1.77', 'TCC': '1.71', 'TCG': '0.90', 'TCT': '2.17', 'TGA': '1.79', 'TGC': '0.84', 'TGG': '1.50', 'TGT': '1.97', 'TTA': '2.23', 'TTC': '1.99', 'TTG': '1.66', 'TTT': '3.73'}, 'rez': ''}
   
        """
        
    '''

    rez = '' if rez == None else rez
    
    gene_record = dbapi.getEntry(accession) 
    
   
#formating cds coming from database - removing non numerical strings
    
    cds = [gene_record['cds']]
    cds = [cds.replace('complement(', '') for cds in cds]
    cds = [cds.replace('join(', '') for cds in cds]         
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
        dna_seq = dna_seq[:start]+ '[' + dna_seq[start:end].lower() + ']' + dna_seq[end:]
        
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
#    dna_seq = dna_seq.replace('|', '|')
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

if __name__ == "__main__":
   import doctest
   doctest.testmod()
