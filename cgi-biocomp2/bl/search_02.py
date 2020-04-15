#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:36:41 2020

@author: florence
"""

#!/usr/bin/python3
"""
...Comment header goes here...
This CGI script obtains all the entries from the BL layer and formats them for 
HTML display as a table
"""

# Add the bl sub-directory to the module path
# and the directory above to import the config file
import sys
sys.path.insert(0, "/d/user6/lc001/biocomp2/bbk_chromosome6/cgi-biocomp2/bl/")
sys.path.insert(0, "/d/user6/lc001/biocomp2/bbk_chromosome6/cgi-biocomp2/")
import cgi
import blapi      # Import the Business Logic API
import htmlutils  # Import HTML utilities
import config     # Import configuration information (e.g. URLs)

'''
entry = {'gene_id': 'HLA-DQA1',
 'accession': 'AB006907',
 'product': 'HMC class II surface glycoprotein',
 'location': '6p21.3',
 'protein_seq': 'MILNKALMLGALALTTVMSPCGGEDIV',
 'dna_seq': '<mark>ATGATCCTAAACAAAGCTCTGATGCTGGGGGCCCTTGCCCTGACCACCGTG</mark>ATGAGCCCCTGTGGAGGTGAA<span class = "re">&star;</span>GACATTGTGG',
 'cds': '1..82', 'freq': {'AAA': '2.53','AAC': '1.27','AAG': '2.53','ACA': '2.53',
  'ACC': '2.53','AGA': '1.27','AGC': '2.53','AGG': '1.27','ATC': '1.27','ATG': '3.80',
  'ATT': '1.27','CAA': '1.27','CAC': '1.27','CAT': '1.27','CCA': '1.27','CCC': '5.06',
  'CCG': '1.27','CCT': '5.06','CGT': '1.27','CTA': '1.27','CTC': '1.27','CTG': '5.06',
  'CTT': '1.27','GAA': '1.27','GAC': '2.53','GAG': '2.53','GAT': '3.80','GCC': '3.80',
  'GCT': '2.53','GGA': '1.27','GGC': '1.27','GGG': '3.80','GGT': '1.27','GTG': '5.06',
  'TAA': '1.27','TCC': '1.27','TCT': '1.27','TGA': '7.59','TGC': '2.53','TGG': '2.53',
  'TGT': '2.53','TTG': '2.53'}, 'total_freq': {'AAA': '3.73','AAC': '1.66','AAG': '1.96',
  'AAT': '2.17','ACA': '1.96','ACC': '1.58','ACG': '0.92','ACT': '1.78','AGA': '2.20',
  'AGC': '0.77','AGG': '1.70','AGT': '1.79','ATA': '1.91','ATC': '1.28','ATG': '1.43',
  'ATT': '2.19','CAA': '1.61','CAC': '1.51','CAG': '1.45','CAT': '1.42','CCA': '1.49',
  'CCC': '1.39','CCG': '0.86','CCT': '1.69','CGA': '0.91','CGC': '0.28','CGG': '0.86',
  'CGT': '0.92','CTA': '1.29','CTC': '1.74','CTG': '1.45','CTT': '1.96','GAA': '1.98',
  'GAC': '1.61','GAG': '1.75','GAT': '1.29','GCA': '0.79','GCC': '0.72','GCG': '0.29',
  'GCT': '0.77','GGA': '1.75','GGC': '0.72','GGG': '1.40','GGT': '1.58','GTA': '1.47',
  'GTC': '1.60','GTG': '1.54','GTT': '1.68','TAA': '2.20','TAC': '1.47','TAG': '1.30',
  'TAT': '1.93','TCA': '1.76','TCC': '1.74','TCG': '0.91','TCT': '2.20','TGA': '1.78',
  'TGC': '0.79','TGG': '1.49','TGT': '1.99','TTA': '2.22','TTC': '1.99','TTG': '1.64',
  'TTT': '3.80'}, 'rez': 'EcoRI'}

'''
form = cgi.FieldStorage()
accession = form.getvalue("accession")
rez = form.getvalue("rez")
entry = blapi.getEntry(accession)

html  = htmlutils.header()
html += "<html>\n"
html += "<head>\n"
html += "<h1>Cgi script to return entries of chromosome 6 and adding tags to coding region</h1>\n"
html += "      <ul>\n"
html += "<body>"
html += "<h2>Genbank information from your selection</h2>"
html += "<style>table,th, td {border: 1px solid black;}"
html += "</style>"
html += "<table>"
html += "<tr>"
html += "<th>Genbank accession</th>"
html += "<th>Gene Identifier</th>"
html += "<th>Protein product name</th>"
html += "<th>Chromosomal location</th>"
html += "<th>coding region - cds</th>"
html += "<th>Restriction enzyme</th>"
html += "</tr>"
html += "<tr>"
html += "<td>" + entry['accession'] + "</a></td>"
html += " <td>" + entry['gene_id'] + "</a></td>"  
html += "<td>" + entry['product'] + "</a></td>" 
html += "<td>" + entry['location'] + "</a></td>"     
html += "<td>" + entry['cds'] + "</a></td>"
html += "<td>" + entry['rez'] + "</a></td>"       
html += "</tr>\n"
html += "<h2>The protein sequence coded by this gene is listed below: </h2>\n"
html += entry['protein_seq']
html += "<h2>The dna sequence is shown below with coding region highlighted, where restriction enzyme choice is given, the region of binding site will also be marked : </h2>\n"
html += entry['dna_seq']
html += "<h2>Codon usage of current record</h2>"
html += "<table>\n"

#Table = []
for key, value in entry['freq'].items():    
    temp = []
    temp.extend([key,value])
    #Table.append(temp)
    html += "<tr>"
    html += "<td>"
    html += key
    html += "</td>"
    html += "<td>"
    html += value
    html += "</td>"
    html += "</tr>"
    
html += "</table>\n"
html += "<h2>Codon usage of all gene in chromosome 6</h2>"
for k, v in entry['total_freq'].items():    
    t = []
    t.extend([k,v])
    #Table.append(temp)
    html += "<tr>"
    html += "<td>"
    html += k
    html += "</td>"
    html += "<td>"
    html += v
    html += "</td>"
    html += "</tr>"
    

html += "</table>\n"

html += "      </ul>\n"


html += "</html>\n"


html += htmlutils.footer()

print(html)
