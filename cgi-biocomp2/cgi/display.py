#!/usr/bin/python3
"""
This CGI script  displays the search results:

Accession number, Gene ID, Protein sequences, chromosomal location, DNA sequences-with coding regions highlighted, CDS, restiction enzyme, codon frequency.
============
Author: Maham Ahmad
Created on 15th April 2020
"""

# Add the bl sub-directory to the module path
# and the directory above to import the config file
import sys
sys.path.insert(0, "../bl/")
sys.path.insert(0, "../db")

import cgi
import blapi      # Import the Business Logic API
import htmlutils  # Import HTML utilities
import config     # Import configuration information (e.g. URLs)
import dbapi

# Useful debugging output
import cgitb
cgitb.enable()  # Send errors to browser

# Grab the content of the form
form = cgi.FieldStorage()


#SEARCH RESULTS

html    = htmlutils.header()
keyword = form.getvalue('keyword')
keyword2 = form.getvalue('keyword2')
entry = blapi.getEntry(keyword,keyword2)

html += "<html\n>"
html += "<head>"
html += "<h1> Results for: </h2>\n"
html += "<li>"+keyword+"</li>"
html += "<style>"
html += "table{width:100%;}, table-layout: fixed table,th,td {border: 1px solid black;  border-collapse: collapse;}th, td {  padding: 15px;  text-align: left;}table#t01 tr:nth-child(even) {background-color: #eee;}table#t01 tr:nth-child(odd) { background-color: #fff;}table#t01 th {background-color: black; color: white;}"
html += "</style>"
html += "</head>"
html += "<body>"
html += "<table id =\"t01\">"
html += "<tr><th>Genbank Accession</th>"
html += "<th>Gene Identifier</th>"
html += "<th>Protein Product</th>"
html += "<th>Chromosomal Location</th>"
html += "<th>Coding Region - CDS</th>"
html += "<th>Restriction Enzyme</th>"
html += "</tr>\n"
html += "<tr>"
html += "<td>"+entry['accession']+ "</td>"
html += "<td>"+entry['gene_id'] + "</td>"	
html += "<td>"+entry['product'] + "</td>"
html += "<td>"+entry['location'] + "</td>"
html += "<td>"+entry['cds'] + "</td>"
html += "<td>"+entry['rez'] + "</td>"
html += "</tr>"
html += "</table>"

#Text area for Amino acid sequences
html += "<hr>"
html += "<h2>Amino Acid Sequence:</h2>\n"
html += "<textarea readonly style=\"width:500px; height:100px; word-wrap:break-word;\">"
html += entry['protein_seq']
html += "</textarea>\n"
html += "</hr>"

#DNA sequence with coding region highlighted
html += "<h2>DNA Sequence with coding region highlighted with star indicating restriction enzyme: </h2>\n"
html += "<div Class {height:auto;} style=\"width:1000px;font-size: 11px; word-wrap:break-word;\">"
html += entry['dna_seq']
html += "</div>"

#Codon Frequency
html += "<table id =\"t01\">"
html += "<tr><th>Codon</th>"
html += "<th>Frequency</th>"
temp = []
for key, value in entry['freq'].items():    

    html += "<tr>"
    html += "<td>"+key+ "</td>"
    html += "<td>"+ value+"</td>"
    html += "</tr>"
html += "</table>"
html += "</body>"
html += htmlutils.footer()

print(html)  
