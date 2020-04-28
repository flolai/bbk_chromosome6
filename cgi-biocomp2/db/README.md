Biocomputing II / cgi-biocomp2/db
=================================

Description
-----------

This directory contains the python code to access the MySQL database. It connects to the MySQL database using PyMySQL and executes a MySQL query based on data from the BLAPI. It returns information from matching entries in the database to the blapi as either a dictionary, or list of dictionaries. 


Connecting to Database
----------------------
The Chromosome 6 genbank entries are held in a MySQL database. (see create DB for information on database). The dbapi connects to the database using PyMySQL library. Database connection parameters are held in the config file (cgi-biocomp2/config.py).


Functions
----------
The dbapi contains two functions:

### getEntry(accession)*
This function takes accession number from the blapi and returns accession number, gene identifier, protein product, chromosome 6 location, protein sequence and dna sequence from the genbank database as a dictionary

#### Input:

Accession: Genbank accession number e.g (‘AB000905’). 

#### Return:

{'gene_id': 'XXX', 'accession': 'XXX', 'product': 'XXX', 'location': 'XXX', 
  'cds': 'XXX', 'protein_seq': 'XXX', 'dna_seq': 'XXX'}



## getAllEntries(**kwargs)

This function takes any combination of accession, gene identified, chromosome location or protein product from the the blapi and returns accession number, gene identifier, protein product, chromosome 6 location from the genbank database.
The parameters are keyword arguments so the keyword should be entered before the search value e.g “accession = ‘AB000905’”.
Keywords must be entered for all search fields whether the user has supplied data or not. Where the user has not supplied data into the search field the search value should be ‘none’: e.g “accession = none”. 

Example 1, search based on one parameter:

getAllEntries(accession= ‘AF065210’, product= ‘None’, location= ‘None’, gene_id= ‘None’)


Example 2, search based on two parameters 

getAllEntries(accession= ‘AF065210’, product= ‘None’, location= ‘None’, gene_id= ‘Rage’)
Searches based on all four parameters are possible. Where all search fields are ‘none’ all entries in the database are returned. 

#### Input

Accession – Genbank accession number 
Product – protein product
Location – Chromosome 6 location
Gene_id – Gene identifier

#### Return

List of dictionaries:
[{'gene_id' : 'XXX', 'accession': 'XXX','product' :'XXX','location' :' XXX'}]

