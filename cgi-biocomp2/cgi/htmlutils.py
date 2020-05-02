#!/usr/bin/python3
"""
Program:    HTMLUTILS script
File:       htmlutils.py

Version:    V1.0
Date:       01.05.2020
Function:   Support code for generating HTML files

Copyright:  (c) Maham Ahmad, Birckbeck, 2020
Author:     Maham Ahmad
            
------------------------------------------------------------------------------------------
This program is released under the GNU Public Licence (GPL V3)
------------------------------------------------------------------------------------------
============
Description:
============
This code is the support code for CGI scripts, helping in generating HTML files.

=================
Revision History:
=================
V1.0   	01.05.20   Original   By: Maham Ahmad

"""

def header():
    """
    This function generates HTML code for the header in both search.py and listall.py
    """
    html = "Content-Type: text/html\n\n"   # MIME-Type header
    html += "<!DOCTYPE html>"
    html += "<html lang='en'>\n"
    html += "  <head>\n"
    html += "    <title>Chromosome 6 Genome Browser</title>\n"
    html += "	 <meta name='viewport' content='width=device-width, initial-scale=1'>\n"	
    html += "    <link rel='stylesheet' type='text/css' href='http://student.cryst.bbk.ac.uk/~az001/biocomp2.css' />\n"
    html += "	 <script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js'></script>\n"
    html += "    <link rel = 'stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.12.1/css/all.min.css'>\n"
    html += "    <link href='https://fonts.googleapis.com/css2?family=Poppins:wght@200&display=swap' rel='stylesheet'>\n"
    html += "  </head>\n"
    html += "  \n"
    html += "  <body>\n"


    return(html)




 
def navigation():

    """
    This function generates the HTML code for navigation bar in search.py and listall.py
    """

    html  = "    <nav>\n"
    html += "      <div class = 'logo'>\n"
    html += "        <h1>Genome<br>browser</h1>\n"
    html += "      </div>\n"
    html += "      <ul class='nav-links'>\n"
    html += "        <li><a href='http://student.cryst.bbk.ac.uk/~az001/index.html'><i class='fas fa-home home'></i> Home</a></li>\n"
    html += "        <li><a href='http://student.cryst.bbk.ac.uk/~az001/search.html'><i class='fas fa-search'></i> Search</a></li>\n"
    html += "        <li><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/listall.py'><i class='fas fa-th-list'></i> Gene Summary</a></li>\n"
    html += "      </ul>\n"
    html += "    </nav> <!-- end of navigation -->\n"

    return(html)



  
def detailtable():

    """
    This function generates HTML code for the detail page table on search.py
    """

    html  = "    <h4 class = 'detail-heading'> Detail page: </h4>\n"
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

    return(html)

def footer():

    """
    This function generates HTML code for the footer in search.py and listall.py
    """

    html = ""
    html += "    </div>\n"
    html += "  </body>\n"
    html += "</html>\n"

    return(html)

