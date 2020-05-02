#!/usr/bin/python3
"""
This file data contains the database connection info for the dbapi.

Author: Oliver Cant
Created on 4th April 2020

"""

# Set parameters for connection to MySQL database

dbname   = "co001"
dbhost   = "localhost"
dbuser   = "co001"
dbpass   = "nz8mjl6ft"   
port     = 3306

# Precalculated total codon frequency to return

total_codon_freq = {'AAA': '3.66','AAC': '1.67','AAG': '1.95',
                    'AAT': '2.21','ACA': '1.94','ACC': '1.53',
                    'ACG': '0.92','ACT': '1.77','AGA': '2.17',
                    'AGC': '0.83','AGG': '1.68','AGT': '1.78',
                    'ATA': '1.94','ATC': '1.31','ATG': '1.45',
                    'ATT': '2.23','CAA': '1.63','CAC': '1.49',
                    'CAG': '1.46','CAT': '1.45','CCA': '1.49',
                    'CCC': '1.38','CCG': '0.84','CCT': '1.67',
                    'CGA': '0.90','CGC': '0.32','CGG': '0.84',
                    'CGT': '0.92','CTA': '1.31','CTC': '1.71',
                    'CTG': '1.46','CTT': '1.96','GAA': '1.98',
                    'GAC': '1.55','GAG': '1.73','GAT': '1.32',
                    'GCA': '0.83','GCC': '0.77','GCG': '0.33',
                    'GCT': '0.83','GGA': '1.72','GGC': '0.76',
                    'GGG': '1.39','GGT': '1.54','GTA': '1.46',
                    'GTC': '1.54','GTG': '1.51','GTT': '1.69',
                    'TAA': '2.22','TAC': '1.46','TAG': '1.32',
                    'TAT': '1.95','TCA': '1.77','TCC': '1.71',
                    'TCG': '0.90','TCT': '2.17','TGA': '1.79',
                    'TGC': '0.84','TGG': '1.50','TGT': '1.97',
                    'TTA': '2.23','TTC': '1.99','TTG': '1.66',
                    'TTT': '3.73'}