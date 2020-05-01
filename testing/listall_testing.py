#!/usr/bin/env python3
"""
This CGI script  displays a summary table when Genbank Accession, Gene Identifier, Protein product
or chromosomal location is searched on search html page. This CGI script also displays summary table of all 
the genes in chromosome 6, when on the gene summary html page, with Genbank Accession, Gene Identifier,
Protein product and chromosomal location being the column headers. 

As Genbank Accession is unique, one entry in a table will be returned whereas for Gene Identifier,Protein
product or chromosomal location one or more entries in a table can be returned. This CGI script also allows
users to select any Genbank Accession cell which will take user to detail page of that gene; detail page
will display Genbank Accession, Gene Identifier, Protein Product, Amino Acid sequence, Chromosomal Location,
Coding region-CDS,DNA sequences-with coding regions highlighted and star indicating restriction enzyme and 
codon frequency.
============
Program: List all CGI script
Author: Maham Ahmad
Date Created: 19 April 2020
"""
import cgi
#print ("Content-Type: text/html\n")

# Add the bl sub-directory to the module path
# and the directory above to import the config file

import sys
sys.path.insert(0, "/d/user6/az001/bl/")
sys.path.insert(0, "/d/user6/az001/db/") 

import blapi      # Import the Business Logic API
import htmlutils  # Import HTML utilities
import config     # Import configuration information (e.g. URLs)


# Useful debugging output
import cgitb
cgitb.enable()

# Grab the content of the form
form = cgi.FieldStorage()

accession = form.getvalue("accession")
gene_id = form.getvalue("gene_id")
product = form.getvalue("product")
location = form.getvalue("location")
entries = blapi.getAllEntries(accession = accession, gene_id = gene_id, product = product,location = location)
html    = htmlutils.header()


#Table Design

html += "<html>\n"
html += "<head>\n"
html += "<title>Gene Summary Table</title>\n"
html += "</head>"
html += "<body>\n"
html += "<h1>Gene Summary Table:</h1>\n"
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


#Gene summary table page: Genbank Accession, Gene Identifier, Protein product and chromosomal location with Genbank Accession linking to detail page of gene

html += "<table id =\"t01\">"
html += "<tr><th>Genbank Accession</th>"
html += "<th>Gene Identifier</th>"
html += "<th>Protein Product</th>"
html += "<th>Chromosomal Location</th>"
html += "</tr>\n"
for _ in entries:	
	html += "<tr>\n"
	html += "<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession={}' method='get'>".format(_['accession'])+ _['accession']+ "</a></td>" 
	html += "<td>"+_['gene_id'] + "</td>"	
	html += "<td>"+_['product'] + "</td>"
	html += "<td>"+_['location'] + "</td>"
	html += "</tr>\n"

	
html += "</table>\n"

html += "</body>\n"
html += "</html>\n"
html += htmlutils.footer()

print(html)   
