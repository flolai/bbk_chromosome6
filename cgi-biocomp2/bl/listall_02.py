
"""
Created on Wed Apr  1 22:59:57 2020

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
#import sys
#sys.path.insert(0, "../bl/")
#sys.path.insert(0, "../")

#import blapi      # Import the Business Logic API
#import cgi
#import htmlutils  # Import HTML utilities
#import config     # Import configuration information (e.g. URLs)

#entries = blapi.getAllEntries()
#html    = htmlutils.header()

entries = [{'gene_id': 'IGF2R',
  'accession': 'X83700',
  'product': 'insulin-like growth factor type II receptor',
  'location': '6q25-27'},
 {'gene_id': 'IGF2R',
  'accession': 'X83701',
  'product': 'insulin-like growth factor II receptor',
  'location': '6q25-27'},
 {'gene_id': 'IGF2R',
  'accession': 'X83702',
  'product': 'insulin-like growth factor type II receptor',
  'location': '6q25-27'},
 {'gene_id': 'DRB1*1116',
  'accession': 'X87200',
  'product': 'Beta 1 domain of MHC Class II HLA DRB1 molecule',
  'location': 'p21.3'},
 {'gene_id': 'PPP1R11',
  'accession': 'X89902',
  'product': 'protein phosphatase 1, regulatory (inhibitor)',
  'location': 'p21.3 mu'}]


html = "<html>\n"
html += "<head>\n"
html += "<h1>Python cgi to return entries from chromosome 6 database</h1>\n"
html += "</head>"
html += "<body>"
html += "<h2>Please click your gene of interest by its Genbank accession, the coding region will then be highlighted</h2>"
html += "<style>table,th, td {border: 1px solid black;}"
html += "</style>"
html += "<table>"
html += "<tr>"
html += "<th>Genbank accession</th>"
html += "<th>Gene Identifier</th>"
html += "<th>Protein product name</th>"
html += "<th>Chromosomal location</th>"
html += "</tr>"



for entry in entries:
    html += "<tr>"
    html += "        <td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/lc001/search_02.py?accession=" \
            + entry['accession'] + "'>" + entry['accession'] + "</a></td>"
    html += "        <td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/lc001/search_02.py?accession=" \
            + entry['accession'] + "'>" + entry['gene_id'] + "</a></td>"  
    html += "        <td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/lc001/search_02.py?accession=" \
            + entry['accession'] + "'>" + entry['product'] + "</a></td>" 
    html += "        <td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/lc001/search_02.py?accession=" \
            + entry['accession'] + "'>" + entry['location'] + "</a></td>"        
    html +=        "</tr>\n"
         

html += "      </ul>\n"

html += "</html>\n"
#html += htmlutils.footer()

print(html)

