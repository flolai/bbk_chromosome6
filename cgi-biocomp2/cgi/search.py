#!/usr/bin/python3
"""
This CGI script allows user to search using Acession Number and  Restriction Enzyme of your choice
============
Author: Maham Ahmad
Created on 15th April 2020
"""

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
cgitb.enable()  # Send errors to browser

html    = htmlutils.header()

#Acession = form["accession"]

html += "<html>"
html += "<h1>Search</h1>"
html += "<form action= 'http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/nextcgi.py' method='get>"
html += "<label for= 'keyword'> Keyword </label>"
html += "Keyword: <input type= 'text' id= 'keyword' name= 'keyword' placeholder=\"Search the site...\">  <br/>"
html += "<label for = 'keyword2'> second name: </label>"
html += "Keyword2: <input type = 'text' id = 'keyword2' name = 'keyword2'>  <br/>"
html += "<input type = 'submit' value = 'Submit' />"
html += "</form>"
html += "</html>"


html += htmlutils.footer()

print(html)  


