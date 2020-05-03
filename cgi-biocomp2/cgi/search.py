#!/usr/bin/python3
"""
Program:    Search CGi Script
File:       search.py

Version:    V9.0
Date:       03.05.2020
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
This CGI script  displays the search results - a detailed page of the gene searched using
Genbank Accession,Gene Identifier, Protein Product or Chromosomal Location.

Detail page includes:
=====================

Genbank Accession, Gene Identifier, Protein Product, Amino Acid sequence, Chromosomal
Location, Coding region-CDS, DNA sequences-with coding regions highlighted and star
indicating where the restriction enzyme cuts and codon frequency.

=================
Revision History:
=================
V1.0   	15.04.20   Original   By: Maham Ahmad


"""

# Add the bl sub-directory to the module path
# and the directory above to import the config file
import sys
sys.path.insert(0, "/d/user6/az001/bl/")
sys.path.insert(0, "/d/user6/az001/db/") #Config file saved in db folder


import blapi      # Import the Business Logic API
import htmlutils  # Import HTML utilities
import config     # Import configuration information (e.g. URLs)
import dbapi      # Import the Datbase API

import pandas as pd
import cgi 

# Useful debugging output
import cgitb
cgitb.enable()  # Send errors to browser

# Grab the content of the form
form = cgi.FieldStorage()



#***********************************************************************************************************************************************************************************************

# MAIN PROGRAMME FOR DETAIL PAGE 

#***********************************************************************************************************************************************************************************************


accession = form.getvalue("accession")
enzyme = form.getvalue("rez")
entry = blapi.getEntry(accession, enzyme)




# Header and navigation

html    = htmlutils.header()
html += htmlutils.navigation()


# detail table


html += "    <h4 class = 'detail-heading'> Detail page: </h4>\n"
html += "    <div class= 'page'>\n"
html += "       <table class = 'detail'>\n"
html += "          <tr>\n"
html += "            <th>Genbank Accession</th>\n"
html += "            <th>Gene Identifier</th>\n"
html += "            <th>Protein Product</th>\n"
html += "            <th>Chromosomal Location</th>\n"
html += "            <th>Coding Region - CDS</th>\n"
html += "           </tr>\n"
html += "           <tr>\n"
html += "             <td>"+entry['accession']+ "</td>\n"
html += "             <td>"+entry['gene_id'] + "</td>\n"	
html += "             <td>"+entry['product'] + "</td>\n"
html += "             <td>"+entry['location'] + "</td>\n"
html += "             <td>"+entry['cds'] + "</td>\n"
html += "           </tr>\n"
html += "        </table>\n"

#Text area for Amino acid sequences

html += "<h4 class= 'table-heading'>Amino Acid Sequence:</h4>\n"
html += "<textarea class ='amino-acid' readonly cols='45'rows='10'>" +entry['protein_seq']+ "</textarea>\n"


#**********************************************************

# DNA sequence and resitriction enzyme 

#**********************************************************


html += "<h4 class= 'table-heading' >DNA Sequence: </h4>\n"
html += "<div class = 'dna-info'> Coding region has been highlighted. <br>By choosing a Retriction Enzyme, a star will appear in the DNA sequence below. This star will indicate that the Restriction Enzyme cuts at particular site.</div>\n"
html += "<form action='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py' method='get'>\n"
html += "<input type='hidden' id='accession' name='accession' value='" + accession + "'>\n"


#Restriction Enzyme table


#drop down for restriction enzyme

#html += "<input type='radio' id='drop' name='rez'>\n"
html += " <select name = 'rez'>\n"
html += " <option value = 'Restriction enzyme list'>Choose Restriction enzyme</option>\n"
html += " <option value = 'EcoRI'>EcoRI</option>\n"
html += " <option value = 'BamHI'>BamHI</option>\n"
html += " <option value = 'BsuMI'>BsuMI</option>\n"
html += " <option value = 'KpnI'>KpnI</option>\n"
html += " <option value = 'EcoRV'>EcoRV</option>\n"
html += " <option value = 'SmaI'>SmaI</option>\n"
html += " <option value = 'MscI'>MscI</option>\n"
html += " </select>\n"


#html += "<input type='radio' id='seq'name='rez' checked='checked''>\n"
#html += "<p><b>Sequence by sequence:</b><br /> <textarea name='rez' cols='10' rows='2'></textarea></p>\n"





html += " <input type = 'submit' value = 'Submit'/>\n"
html += "<input type='reset' value='Clear'/>\n"
html += " </form>\n"


html += "<div class = 'dna-info'>  Restriction Enzyme : " + entry['rez'] + "</div>\n"
#DNA sequence with coding region highlighted
html += "<div id = 'dna-seq'> "+ entry['dna_seq']+"</div>\n"


#******************************************************

#Total codon usasge in this Gene vs in chromosome 6

#******************************************************
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

# Frequency of codon usage in particular gene vs chromosome six

html += "<h4 class= 'table-heading'>Codon usage frequencies in this gene vs in Chromosome Six </h4>\n"

html += "<div class='codondiv'>\n"
html += "<table class= 'codon'>\n"
html += "<tbody>\n"
html += "<tr>\n"
html += "<th>Codon</th>\n"
html += "<th>Frequency</th>\n"
html += "<th>Total Frequency</th>\n"
html += "</tr><tr>\n"

html += "</tr><tr>\n"
html += "<th>Codon</th>\n"
html += "<th>Frequency</th>\n"
html += "<th>Total Frequency</th>\n"
html += "</tr><tr>\n"

html += "</tr><tr>\n"
html += "<th>Codon</th>\n"
html += "<th>Frequency</th>\n"
html += "<th>Total Frequency</th>\n"
html += "</tr>\n"

html += "</tbody>\n"
html += "</table>\n"
html += "</div>\n"


html += "<div class='codondiv'>\n"
html += "<table class = 'codon'>\n"
html += "<tbody>\n"

for _ in range(0,len(df3)):
    
   
    html += "<tr>\n"
    html += "<td>"+ df3['Codon'][_]+"</td>\n"
    html += "<td>"+ df3['Freq'][_]+"</td>\n"
    html += "<td>"+ df3['Total Freq'][_]+"</td>\n"
    html += "</tr>\n"

html += "<tr class='hiddenrow'>\n"
html += "<th>Codon</th>\n"
html += "<th>Frequency</th>\n"
html += "<th>Total Frequency</th>\n"
html += "</tr>\n"
html += "</tbody>\n"
html += "</table>\n"
html += "</div>\n"



'''

html += "<table class= 'codon'>\n"
html += "<tr>\n"
html += "<th>Codon</th>\n"
html += "<th>Frequency</th>\n"
html += "<th>Total Frequency</th>\n"
'''

html += htmlutils.footer()
print(html)



#print(df3)
