
#!/usr/bin/env python3


import cgi

#print ("Content-Type: text/html\n")

# Add the bl sub-directory to the module path
# and the directory above to import the config file

import sys
sys.path.insert(0, "/d/user6/az001/bl/")
sys.path.insert(0, "d/user6/az001/WWW/cgi-bin/")

import blapi      # Import the Business Logic API
import htmlutils  # Import HTML utilities
import config     # Import configuration information (e.g. URLs)

# Useful debugging output
import cgitb
cgitb.enable()




entries = []
entries = blapi.getAllEntries()
html    = htmlutils.header()

html += "<title>Gene Summary</title>"

#Table Design

html += "<html><head><style>table {  width:100%;}table, th, td {border: 1px solid black;  border-collapse: collapse;}th, td {  padding: 15px;  text-align: left;}table#t01 tr:nth-child(even) {background-color: #eee;}table#t01 tr:nth-child(odd) { background-color: #fff;}table#t01 th {  background-color: black;  color: white;}</style></head><body>"


#Gene summary table page

html += "<table >"
html += "<tr><th>Accession</th><th>Gene Identifier</th><th>Protein Product</th><th>Chromosome location</th></tr>\n"
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
 
