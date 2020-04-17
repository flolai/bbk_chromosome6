#!/usr/bin/python3
"""
This CGI script  displays the search results - a summary page of the gene searched using Genbank Accession,
Gene Identifier, Protein Product,Chromosomal Location and restriction enzyme.
------------------------------------------------------------------------------------------------------------------
Summary page includes:
------------------------------------------------------------------------------------------------------------------
Genbank Accession, Gene Identifier, Protein Product, Amino Acid sequence, Chromosomal Location, Coding region-CDS,
DNA sequences-with coding regions highlighted and star indicating restriction enzyme and codon frequency.

============
Author: Maham Ahmad
Created on 17th April 2020
"""

# Add the bl sub-directory to the module path
# and the directory above to import the config file
import sys
sys.path.insert(0, "/d/user6/az001/bl/")
sys.path.insert(0, "/d/user6/az001/db/") #Confif file saved in db folder


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
html    = htmlutils.header()

#SEARCH RESULTS



accession = form.getvalue('accession')
entry = blapi.getEntry(accession)


html += "<html>\n"
html += "<head>\n"
html += "<h1> Results for: </h1>\n"
html += "<li>"+accession+"</li>\n"
html+= "<p id=\"demo\"></p>"


html += "<style>"
html += "table{"
html += "width:100%;"
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

#DNA sequence with coding region highlighted
#DROP DOWN
html += "<hr\n>"
html += "<h2>DNA Sequence with coding region highlighted with star indicating restriction enzyme: </h2>\n"
html += "<form action=\"\" method=\"post\">"#
html += "<label for='Restriction Enzyme'>Choose a Restrction Enzyme:</label>"
html += "<select id='enzyme' name= 'enzyme'>"
html += "<option disabled selected value> -- select an option -- </option>"
html += "<option value='EcoRI'>EcoRI</option>"
html += "<option value='BamHI'>BamHI</option>"
html += "<option value='BsuMI'>BsuMI</option>"
html += "<option value='KpnI'>KpnI</option>"
html += "<option value='EcoRV'>EcoRV</option>"
html += "<option value='SmaI'>SmaI</option>"
html += "  <option value='MscI'>MscI</option>"
html += "</select> "
#html += "<input type=\"submit\" value=\"Submit\">"
html += "</form>"

html+= "<button type='button' onclick='myFunction()'>Try it</button>"
html+= "<p id='demo'></p>"

html+= "<script>\
function myFunction() {\
  var x = document.getElementById('enzyme').value;\
	document.getElementById('demo').innerHTML = x;\
}\
</script>"

html += "<div Class {height:auto;} style='width:1000px;font-size: 11px; word-wrap:break-word;'>"
html += entry['dna_seq']
html += "</div>"
html += "</hr\n>"

#Codon usage in this gene
html += "<style>"
html += "table{"
html += "width:50%;"
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
html += htmlutils.footer()





print(html)  
