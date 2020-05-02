#!/usr/bin/env python3
"""
Program:    List all CGi Script
File:       listall.py

Version:    V12.0
Date:       30.04.2020
Function:   Obtains all the entries from the BL layer and formats them for 
	    HTML display as a table.

Copyright:  (c) Maham Ahmad, Birckbeck, 2020
Author:     Maham Ahmad
            
-----------------------------------------------------------------------------------------
This program is released under the GNU Public Licence (GPL V3)
-----------------------------------------------------------------------------------------
============
Description:
============
This CGI script  displays a summary table when Genbank Accession, Gene Identifier,
Protein product or chromosomal location is searched on search html page. This CGI 
script also displays summary table of all the genes in chromosome 6, when on the 
gene summary html page, with Genbank Accession, Gene Identifier, Protein product and
chromosomal location being the column headers. 

As Genbank Accession is unique, one entry in a table will be returned whereas for 
Gene Identifier,Protein product or chromosomal location one or more entries in a table
can be returned. This CGI script also allows users to select any Genbank Accession cell
which will take user to detail page of that gene; detail page will display
Genbank Accession, Gene Identifier, Protein Product, Amino Acid sequence, Chromosomal
Location, Coding region-CDS, DNA sequences-with coding regions highlighted and star 
indicating restriction enzyme cutting site and codon frequency.

------------------------------------------------------------------------------------------

Revision History:
=================
V1.0   	10.04.20   Original   By: Maham Ahmad



"""
#*****************************************************************************************************************************************************************************************
# Import libraries

import unittest
import sys
import cgi
import blapi      # Import the Business Logic API
import htmlutils  # Import HTML utilities
import config     # Import configuration information (e.g. URLs)
# Useful debugging output
import cgitb
cgitb.enable()
class htmlTestCase(unittest.TestCase):
    def test_html(self, file = sys.stdout):
        
        
        print ("Content-Type: text/html\n")

# Add the bl sub-directory to the module path
# and the directory above to import the config file

    
        sys.path.insert(0, "/d/user6/az001/bl/")
        sys.path.insert(0, "/d/user6/az001/db/") 

    



#*****************************************************************************************************************************************************************************************

# Grab the content of the form
        form = cgi.FieldStorage()

        accession = form.getvalue("accession")
        gene_id = form.getvalue("gene_id")
        product = form.getvalue("product")
        location = form.getvalue("location")
        entries = blapi.getAllEntries(accession = accession, gene_id = gene_id, product = product,location = location)




# Header and navigation

        html    = htmlutils.header()
        html += htmlutils.navigation()


# Gene summary page table

        html += "<h3>Gene Summary Table:</h3>\n"
        html += "<div class='summary-page'>\n"
        html += "<table class ='summary'>\n"
        html += "<tr>\n"
        html += "<th>Genbank Accession</th>\n"
        html += "<th>Gene Identifier</th>\n"
        html += "<th>Protein Product</th>\n"
        html += "<th>Chromosomal Location</th>\n"
        html += "</tr>\n"
        for _ in entries:	
            html += "<tr>\n"
            html += "<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession={}' method='get'>".format(_['accession'])+ _['accession']+ "</a></td>\n" 
            html += "<td>"+_['gene_id'] + "</td>\n"	
            html += "<td>"+_['product'] + "</td>\n"
            html += "<td>"+_['location'] + "</td>\n"
            html += "</tr>\n"
        html += "</table>\n"
    
        html += htmlutils.footer()
    
        #print(html)   

if __name__ == '__main__':
    unittest.main()