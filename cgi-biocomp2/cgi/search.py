#!/usr/bin/python3
"""
Program:    Search CGi Script
File:       search.py

Version:    V8.0
Date:       01.05.2020
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
Genbank Accession,Gene Identifier, Protein Product or Chromosomal Location and restriction
enzyme.

Detail page includes:
=====================

Genbank Accession, Gene Identifier, Protein Product, Amino Acid sequence, Chromosomal
Location, Coding region-CDS, DNA sequences-with coding regions highlighted and star
indicating where the restriction enzyme cuts and codon frequency.

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



# Summary table

html += htmlutils.detailtable()
html += "<td>"+entry['accession']+ "</td>\n"
html += "<td>"+entry['gene_id'] + "</td>\n"	
html += "<td>"+entry['product'] + "</td>\n"
html += "<td>"+entry['location'] + "</td>\n"
html += "<td>"+entry['cds'] + "</td>\n"
html += "</tr>\n"
html += "</table>\n"

#Text area for Amino acid sequences

html += "<h4 class= 'table-heading'>Amino Acid Sequence:</h4>\n"
html += "<textarea readonly>\n"
html += entry['protein_seq']
html += "</textarea>\n"


#**********************************************************

# DNA sequence and resitriction enzyme 

#**********************************************************


html += "<h4 class= 'table-heading' >DNA Sequence: </h4>\n"
html += "<p1> Coding region has been highlighted. <br>By choosing a Retriction Enzyme, a star will appear in the DNA sequence below. This star will indicate that the Restriction Enzyme cuts at particular site.</p1>\n"
html += "<form action='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py' method='get'>\n"
html += "<input type='hidden' id='accession' name='accession' value='" + accession + "'>\n"


#Restriction Enzyme table

html += "<table class = 'reztable'>\n"
html += "<tr>\n"
html += "<th>Restriction enzyme</th>\n"
html += "</tr>\n"
html += "<tr>\n"
html += "<td>" + entry['rez'] + "</td>\n"
html += "</tr>\n"
html += "</table>\n"


#drop down for restriction enzyme

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
html += " <input type = 'submit' value = 'Submit'/>\n"
html += " </form>\n"



#DNA sequence with coding region highlighted
html += "<div id = 'dna-seq'>\n"
html += entry['dna_seq']
html += "</div>\n"



#Total codon usasge in this Gene

html += "<h4 class= 'table-heading'>Codon usage in this Gene </h4>\n"
html += "<table class= 'codon'>\n"
html += "<tr>\n"
html += "<th>Codon</th>\n"
html += "<th>Frequency</th>\n"
#temp = []
for key, value in entry['freq'].items():    

    html += "<tr>\n"
    html += "<td>"+key+ "</td>\n"
    html += "<td>"+ value+"</td>\n"
    html += "</tr>\n"
html += "</table>\n"



#Total codon usasge in this Chromosome

html += "<h4 class= 'table-heading' >Total Codon usage in Chromosome 6</h4>\n"
html += "<table class= 'codon'>\n"
html += "<tr>\n"
html += "<th>Codon</th>\n"
html += "<th>Frequency</th>\n"
#cod = []
for key, value in entry['total_freq'].items():    

    html += "<tr>\n"
    html += "<td>"+key+ "</td>\n"
    html += "<td>"+ value+"</td>\n"
    html += "</tr>\n"
html += "</table>\n"

html += htmlutils.footer()
print(html)
