#!/usr/bin/python3
"""
Program:    HTML UTILS script
File:       htmlutils.py

Version:    V3.0
Date:       04.05.2020
Function:   Support code for generating HTML files

Copyright:  (c) Maham Ahmad, Birckbeck, 2020
Author:     Maham Ahmad
            
------------------------------------------------------------------------------------------
This program is released under the GNU Public Licence (GPL V3)
------------------------------------------------------------------------------------------

Revision History:
=================
V1.0   	01.05.2020   Original   By: Maham Ahmad
V2.0   	02.05.2020
V3.0    04.05.2020     

"""
#******************************************************************************************************************************************************************

def header():
    """
    This function generates HTML code for the header in both search.py and listall.py
    """
    html = "Content-Type: text/html\n\n"   # MIME-Type header
    html += "<!DOCTYPE html>\n"
    html += "<html lang='en'>\n"
    html += "  <head>\n"
    html += "    <title>Chromosome 6 Genome Browser</title>\n"
    html += "	 <meta name='viewport' content='width=device-width, initial-scale=1'>\n"	
    html += "    <link rel='stylesheet' type='text/css' href='http://student.cryst.bbk.ac.uk/~az001/biocomp2.css' />\n"
    html += "    <link rel = 'stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.12.1/css/all.min.css'>\n"
    html += "    <link href='https://fonts.googleapis.com/css2?family=Poppins:wght@200&display=swap' rel='stylesheet'>\n"
    html += "  </head>\n"
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



def footer():

    """
    This function generates HTML code for the footer in search.py and listall.py
    """

    html = ""
    html += "    </div>\n"
    html += "  </body>\n"
    html += "</html>\n"

    return(html)

