#!/usr/bin/python3
"""
Program:    Search CGi Script
File:       search.py

Version:    V8.0
Date:       04.05.2020
Function:   Obtains accession and rez entries from the BL layer and formats them for 
	    HTML display.

Copyright:  (c) Maham Ahmad, Birckbeck, 2020
Author:     Maham Ahmad
            
------------------------------------------------------------------------------------------
This program is released under the GNU Public Licence (GPL V3)
------------------------------------------------------------------------------------------
============
Description:
============
This CGI script  displays the search results - a detailed page of the gene that is searched
using Genbank Accession, Gene Identifier, Protein Product or Chromosomal Location.

Detail page includes:
=====================

Genbank Accession, Gene Identifier, Protein Product, Amino Acid sequence, Chromosomal
Location, Coding region-CDS, DNA sequence-with coding regions highlighted and star
indicating where the restriction enzyme cuts and codon frequencies.

=================
Revision History:
=================
V1.0   	10.04.2020  Original   By: Maham Ahmad
V2.0   	15.04.2020   
V3.0   	16.04.2020   
V4.0   	16.04.2020   
V5.0   	17.04.2020   
V6.0   	18.04.2020     
V7.0   	02.05.2020
V8.0    04.05.2020      


"""
#******************************************************************************************************************************************************************
import cgi 

# Add the bl sub-directory to the module path
# and the directory above to import the config file
import sys
sys.path.insert(0, "/d/user6/az001/bl/")
sys.path.insert(0, "/d/user6/az001/db/") #Config file saved in db folder


import blapi      # Import the Business Logic API
import htmlutils  # Import HTML utilities
import config     # Import configuration information (e.g. URLs)
import dbapi      # Import the Datbase API

import pandas as pd #Import panda for table merge

# Useful debugging output
import cgitb
cgitb.enable()  # Send errors to browser

#******************************************************************************************************************************************************************
# Grab the content of the form
form = cgi.FieldStorage()

accession = form.getvalue("accession")
enzyme = form.getvalue("rez")
entry = blapi.getEntry(accession, enzyme)


#******************************************************************************************************************************************************************
# MAIN PROGRAMME FOR DETAIL PAGE 

#******************************************************************************************************************************************************************

# Header and navigation

html  = htmlutils.header()
html += htmlutils.navigation()


# detail table


html += "<h4 class = 'detail-heading'> Detail page: </h4>\n" 
html += "<div class= 'page'>\n"
html += "<table class = 'detail'>\n" 
html += "<tr>\n"
html += "<th>Genbank Accession</th>\n"
html += "<th>Gene Identifier</th>\n"
html += "<th>Protein Product</th>\n"
html += "<th>Chromosomal Location</th>\n"
html += "<th>Coding Region - CDS</th>\n"
html += "</tr>\n"
html += "<tr>\n"
html += "<td>"+entry['accession']+ "</td>\n"
html += "<td>"+entry['gene_id'] + "</td>\n"	
html += "<td>"+entry['product'] + "</td>\n"
html += "<td>"+entry['location'] + "</td>\n"
html += "<td>"+entry['cds'] + "</td>\n"
html += "</tr>\n"
html += "</table><!-- end of detail table -->\n"

#Text area for Amino acid sequences

html += "<h4 class= 'table-heading'>Amino Acid Sequence:</h4>\n"
html += "<textarea class ='amino-acid' readonly cols='45' rows='10'>" +entry['protein_seq']+ "</textarea><!-- Amino Acid Sequence -->\n"


#******************************************************************************************************************************************************************

# DNA sequence and restriction enzyme 

#******************************************************************************************************************************************************************


html += "<h4 class= 'table-heading' >DNA Sequence: </h4>\n"
html += "<div class = 'info'> Coding region has been highlighted.\n"
html += "<ul>\n"
html += "<li>By choosing a Retriction Enzyme, a star will appear in the DNA sequence below</li>\n"
html += "<li>This star will indicate that the chosen Restriction Enzyme cuts at this specific sequence locations</li>\n"
html += "</ul>\n"
html += "</div>\n"
html += "<form action='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py' method='get'>\n"
html += "<input type='hidden' id='accession' name='accession' value='" + accession + "'>\n"



# Drop down for restriction enzyme

html += "<div class= 'dropdown'><!-- Dropdown for restriction enzyme -->\n"
html += "<select name = 'rez'>\n"
html += "<option value = 'Restriction enzyme list'>Choose Restriction enzyme</option>\n"
html += "<option value = 'EcoRI'>EcoRI</option>\n"
html += "<option value = 'BamHI'>BamHI</option>\n"
html += "<option value = 'BsuMI'>BsuMI</option>\n"
html += "<option value = 'KpnI'>KpnI</option>\n"
html += "<option value = 'EcoRV'>EcoRV</option>\n"
html += "<option value = 'SmaI'>SmaI</option>\n"
html += "<option value = 'MscI'>MscI</option>\n"
html += "</select>\n"
html += "<input type = 'submit' value = 'Submit'/>\n"
html += "</div>\n"
html += "</form>\n"

# Display name of enzyme searched 

html += "<div class = 'rezinfo'>  RESTRICTION ENZYME : "+ entry['rez'] + "</div>\n"

# DNA sequence with coding region highlighted
entry['dna_seq'] = entry['dna_seq'].replace('|', '<span class = "re">&starf;</span>') 
entry['dna_seq'] = entry['dna_seq'].replace('[', '<mark>')
entry['dna_seq'] = entry['dna_seq'].replace(']', '</mark>')
html += "<div id = 'dna-seq'> "+ entry['dna_seq']+"</div><!-- end of DNA sequence -->\n"



#******************************************************************************************************************************************************************

#Total codon usasge in this Gene vs in chromosome 6

#******************************************************************************************************************************************************************

# Merging frequencies of chosen gene with frequencies in chromosome 6 using dataframes

dictlist = []
for key, value in entry['freq'].items(): 
	cod = key
	dictlist.append(cod)
	 
df = pd.DataFrame()
df['Codon'] = dictlist
df['Freq'] = df['Codon'].map(entry['freq'])
dictlist2 = []
for key, value in entry['total_freq'].items(): 
	cod = key
	dictlist2.append(cod)

	 
df2 = pd.DataFrame()
df2['Codon'] = dictlist2
df2['Total Freq'] = df2['Codon'].map(entry['total_freq'])


df['Codon'] = df['Codon'].str.strip()
df2['Codon'] = df2['Codon'].str.strip()

df3 = df.merge(df2, left_on ='Codon', right_on='Codon')
df3 = df3[['Codon', 'Freq', 'Total Freq']]

# Frequency of codon usage in chosen gene vs in chromosome six

html += "<h4 class= 'table-heading'>Codon usage frequencies in this gene vs in Chromosome Six </h4>\n"
html += "<table class= 'codon'>\n"
html += "<tr>\n"
html += "<th>Codon</th>\n"
html += "<th>Frequency</th>\n"
html += "<th>Total Frequency</th>\n"

for _ in range(0,len(df3)):

    html += "<tr>\n"
    html += "<td>"+ df3['Codon'][_]+"</td>\n"
    html += "<td>"+ df3['Freq'][_]+"</td>\n"
    html += "<td>"+ df3['Total Freq'][_]+"</td>\n"
    html += "</tr>\n"
html += "</table><!-- end of codon usage table -->\n"

# Footer

html += htmlutils.footer()
print(html)



