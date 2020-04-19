#!/usr/bin/python3
"""
This CGI script  displays the search results - a detailed page of the gene searched using Genbank Accession,
Gene Identifier, Protein Product or Chromosomal Location and restriction enzyme.
------------------------------------------------------------------------------------------------------------------
Detail page includes:
------------------------------------------------------------------------------------------------------------------
Genbank Accession, Gene Identifier, Protein Product, Amino Acid sequence, Chromosomal Location, Coding region-CDS,
DNA sequences-with coding regions highlighted and star indicating restriction enzyme and codon frequency.

============
Program: Search CGI script
Author: Maham Ahmad
Date Created: 19 April 2020
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


#*********************
# DETAIL PAGE 
#*********************


accession = form.getvalue("accession")
enzyme = form.getvalue("rez")
entry = blapi.getEntry(accession, enzyme)


html    = htmlutils.header()
html += "<html>\n"
html += "<head>\n"
html += "<h1> Results for: </h1>\n"
html += "<li>"+accession+"</li>\n"



html += "<style>"
html += "table{"
html += "width:150px;"
html += "}"
html += "table, {"
html += "border: 1px solid black;"
html += "border-collapse: collapse;"
html += "}"
html += "th, td {"
html += "border: 1px white;"
html += "padding: 15px;"
html += "text-align: left;"
html += "}"
html += "table#t01 tr:nth-child(even){"
html += "background-color: #eee;"
html += "}"
html += "table#t01 tr:nth-child(odd){"
html += "background-color: #fff;"
html += "}"
html += "table#t01 th {"
html += "background-color: black;"
html += "color: white;"
html += "}"
html += "</style>"
html += "</head>"
html += "<body>"
html += "<table id ='t01'>"
html += "<tr><th>Genbank Accession</th>"
html += "<th>Gene Identifier</th>"
html += "<th>Protein Product</th>"
html += "<th>Chromosomal Location</th>"
html += "<th>Coding Region - CDS</th>"
html += "</tr>\n"
html += "<tr>"
html += "<td>"+entry['accession']+ "</td>"
html += "<td>"+entry['gene_id'] + "</td>"	
html += "<td>"+entry['product'] + "</td>"
html += "<td>"+entry['location'] + "</td>"
html += "<td>"+entry['cds'] + "</td>"
html += "</tr>"
html += "</table>"

#Text area for Amino acid sequences
html += "<hr\n>"
html += "<h2>Amino Acid Sequence:</h2>\n"
html += "<textarea readonly style='width:500px; height:100px; word-wrap:break-word;'>"
html += entry['protein_seq']
html += "</textarea>\n"
html += "</hr\n>"


#DNA sequence

html += "<hr\n>"
html += "<h2>DNA Sequence with coding region highlighted with star indicating restriction enzyme: </h2>\n"

html += "<form action='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py' method='get'>"
html += "<input type='hidden' id='accession' name='accession' value='" + accession + "'>"

#Restriction Enzyme table
html += "<table id ='t01'>"
html += "<tr><th>Restriction enzyme</th>"
html += "</tr>\n"
html += "<tr>"
html += "<td>" + entry['rez'] + "</td>"
html += "</tr>"
html += "</table>"

#drop down for restriction enzyme
html += """
	<select name = "rez">
        <option value = "Restriction enzyme list">Choose Restriction enzyme</option>
	<option value = "EcoRI">EcoRI</option>
	<option value = "BamHI">BamHI</option>
	<option value = "BsuMI">BsuMI</option>
	<option value = "KpnI">KpnI</option>
	<option value = "EcoRV">EcoRV</option>
	<option value = "SmaI">SmaI</option>
	<option value = "MscI">MscI</option>
	</select>
	<input type = "submit" value = "Submit"/>
	</form>
"""
#DNA sequence with coding region highlighted
html += "<div Class {height:auto;} style='width:1000px;font-size: 11px; word-wrap:break-word;'>"
html += entry['dna_seq']
html += "</div>"
html += "</hr\n>"


#Total codon usasge in this Gene
html += "<hr\n>"
html += "<h2>Codon usage in this Gene </h2>"
html += "<table id ='t01'>"
html += "<tr><th>Codon</th>"
html += "<th>Frequency</th>"
temp = []
for key, value in entry['freq'].items():    

    html += "<tr>"
    html += "<td>"+key+ "</td>"
    html += "<td>"+ value+"</td>"
    html += "</tr>"
html += "</table>\n"
html += "</body>"
html += htmlutils.footer()

#Total codon usasge in this Chromosome
html += "<h2>Total Codon usage in Chromosome 6</h2>"
html += "<table id ='t01'>"
html += "<tr><th>Codon</th>"
html += "<th>Frequency</th>"
cod = []
for key, value in entry['total_freq'].items():    

    html += "<tr>"
    html += "<td>"+key+ "</td>"
    html += "<td>"+ value+"</td>"
    html += "</tr>"
html += "</table>\n"

html += "</body>\n"
html += "</html>\n>"
html += htmlutils.footer()


print(html)  
