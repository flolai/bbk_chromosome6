
# CGI code documentation

There are two CGI scripts, listall.py and search.py

## listall.py CGI script
### Grabbing the contents of the form

```sh
form = cgi.FieldStorage()

accession = form.getvalue("accession")
gene_id = form.getvalue("gene_id")
product = form.getvalue("product")
location = form.getvalue("location")
entries = blapi.getAllEntries(accession = accession, gene_id = gene_id, product = product, location = location)
```

The form.getvalue allows users to search on the search HTML page by: 

* **Gene Identifier**
* **Chromosomal location**
* **Protein Product**
* **GenBank Accession** 
 
When the user searches something on the search HTML page (this is the input), the function, entries = blapi.getAllEntries(accession = accession, gene_id = gene_id, product = product, location = location), returns all entries for what is searched. If there is no input and users click the search button, then all the records from the database will returned.

This is the form and method used on search HTML page:

```sh
<form action='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/listall.py' method='get'>
  ```

The listall.py CGI script is also used on the gene summary page of the browser. On this page, all the genes in Chromosome 6 are displayed in a table.

A hyperlink is created so you can select any GenBank accession to take you to the detail page, search.py. The hyperlink is created by using Python String format - .format(_['accession']).

* A for loop has been created so that the hyperlink is created for the whole GenBank Accession column. 

```sh
for _ in entries:
	
	html += "<tr>\n"
	html += "<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession={}' method='get'>".format(_['accession'])+ _['accession']+ "</a></td>\n" 
	html += "<td>"+_['gene_id'] + "</td>\n"	
	html += "<td>"+_['product'] + "</td>\n"
	html += "<td>"+_['location'] + "</td>\n"
	html += "</tr>\n"
html += "</table><!-- end of summary table -->\n"
```

Listall CGI call tree:
function:
```sh
entries = blapi.getAllEntries(accession = accession, gene_id = gene_id, product = product, location = location)
```
![image](https://github.com/flolai/bbk_chromosome6/blob/master/cgi-biocomp2/cgi/docs/listall.py%20call%20tree.png)



## Search.py CGI script
### Grabbing the contents of the form

```sh
form = cgi.FieldStorage()

accession = form.getvalue("accession")
enzyme = form.getvalue("rez")
entry = blapi.getEntry(accession, enzyme)
```
form.getvalue and getEntry has been used in this CGI script 

A form and get method is used

```sh
html += "<form action='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py' method='get'>\n"
html += "<input type='hidden' id='accession' name='accession' value='" + accession + "'>\n"



# Drop down for restriction enzyme

html += "<div class= 'dropdown'><!-- Dropdown for restriction enzyme -->\n"
html += "<select name = 'rez'>\n"
html += "<option value = 'Restriction enzyme list'>Choose Restriction enzyme</option>\n"
html += "<option value = 'EcoRI'>EcoRI</option>\n"
html += "<option value = 'BamHI'>BamHI</option>\n"
html += "<option value = 'BsuMI'>BsuMI</option>\n"
html += "<option value = 'KpnI'>KpnI</option>\n"
html += "<option value = 'EcoRV'>EcoRV</option>\n"
html += "<option value = 'SmaI'>SmaI</option>\n"
html += "<option value = 'MscI'>MscI</option>\n"
html += "</select>\n"
html += "<input type = 'submit' value = 'Submit'/>\n"
html += "</div>\n"
html += "</form>\n"
```

* On the detail page (search.py) of the chosen GenBank Accession by user, the restriction enzyme be chosen by the dropdown menu. The restriction enzyme chosen may be used to cut the gene at specific location. 

* Restriction enzyme which is returned as a string is passed to this function, def getEntry(accession, rez = ''), used in BLAPI, the DNA sequence is processed and location of the cutting site will be pre-tagged with | and returned back to the front end for display.

Search CGI call tree:

Function:

```sh
entry = blapi.getEntry(accession, rez)

```
![image](https://github.com/flolai/bbk_chromosome6/blob/master/cgi-biocomp2/cgi/docs/search.py%20call%20tree.png)




## semantic markup used
   
  * <mark>
  * <nav>
  * <div>
  * <header>
  * <footer>
  
   




