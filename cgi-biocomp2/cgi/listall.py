#!/usr/bin/env python3
"""
This CGI script  displays summary of the genes:

Accession number, Gene ID, Protein sequences, chromosomal location.
============
Author: Maham Ahmad
Created on 15th April 2020
"""
import cgi

#print ("Content-Type: text/html\n")

# Add the bl sub-directory to the module path
# and the directory above to import the config file

import sys
sys.path.insert(0, "../bl/")
sys.path.insert(0, "../")


import blapi      # Import the Business Logic API
import htmlutils  # Import HTML utilities
import config     # Import configuration information (e.g. URLs)

# Useful debugging output
import cgitb
cgitb.enable()


entries = []
entries = blapi.getAllEntries()
html    = htmlutils.header()

#html += "<title>Gene Summary</title>"

#Table Design

html += "<html>"
html += "<head>"
html += "<h1>Gene Summary</h1>"
html += "<style>"
html += "table {width:100%;}table, th, td {border: 1px solid black;  border-collapse: collapse;}th, td {  padding: 15px;  text-align: left;} table#t01 tr:nth-child(even) {background-color: #eee;}table#t01 tr:nth-child(odd) { background-color: #fff;}table#t01 th {  background-color: black;  color: white;}"
html += "</style>"
html += "</head>"
html += "<body>"


#Gene summary table page

html += "<table>"
html += "<tr><th>Genbank Accession</th>"
html += "<th>Gene Identifier</th>"
html += "<th>Protein Product</th>"
html += "<th>Chromosomal Location</th>"
html += "</tr>\n"
for _ in entries:	
	html += "<tr>"
	html += "<td>"+ _['accession']+ "</td>"
	html += "<td>"+_['gene_id'] + "</td>"	
	html += "<td>"+_['product'] + "</td>"
	html += "<td>"+_['location'] + "</td>"
	html += "</tr>"
	
	
html += "<table>"
#html += "      </ul>\n"
html += htmlutils.footer()


print(html) 
 
