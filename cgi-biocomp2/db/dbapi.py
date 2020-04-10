#!/usr/bin/python3

"""
This is the python wrapper for the MySQL database. 

It is called with two functions and passes information to the blapi:

getAllEntries() which returns a list of all the entries in the database 

getentry() which has accession number as a paramter and returns the information for this entry from database

Author: Oliver Cant
Created on March 28th 2020

"""


import time
import pymysql.cursors
import sys

sys.path.append('https://github.com/flolai/bbk_chromosome6/blob/master/cgi-biocomp2/config.py')

import config # import configuration info

def getEntry(accesion):

# Get parameters from config file

    dbname   = config.dbname
    dbhost   = config.dbhost
    dbuser   = config.dbuser
    dbpass   = config.dbpass 
    port     = config.port

# Connect to the database
    db = pymysql.connect(host=dbhost, port=port, user=dbuser, passwd=dbpass, db=dbname)

    try:
        
# Create a cursor and execute the SQL on it - search db on accession number
        cursor = db.cursor()
        nrows = cursor.execute("SELECT * FROM chrom6 WHERE accession =%s", accesion)
    
#Using the cursor as iterator, should return one entry as accession unique
        for data in cursor:
            gene_id =data[0]
            accession =data[1]
            product =data[2]
            location =data[3]
            cds =data[4]
            protein_seq =data[5]
            dna_seq =data[6]

        value = [gene_id, accession, product, location, cds, protein_seq, dna_seq]
        key = ['gene_id', 'accession', 'product', 'location', 'cds', 'protein_seq', 'dna_seq']

        gene_record = dict(zip(key,value))
        return(gene_record)
        

    except Exception as e:
        print("Exception occured:{}".format(e));

    finally:
        cursor.close()
        db.close()

def getAllEntries():

# Get parameters from config file

    dbname   = config.dbname
    dbhost   = config.dbhost
    dbuser   = config.dbuser
    dbpass   = config.dbpass 
    port     = config.port


# Connect to the database
    db = pymysql.connect(host=dbhost, port=port, user=dbuser, passwd=dbpass, db=dbname)

  
# Create a cursor and execute the SQL on it - returns all items in database
    cursor = db.cursor()
    cursor.execute("SELECT gene_id, accession, product, location FROM chrom6 WHERE accession LIKE =s% AND gene_id LIKE =s% AND product LIKE =s% AND location LIKE =%s", accession, gene_id, product, location)

    data = cursor.fetchone()

    while data is not None:    
        gene_id =data[0]
        accession =data[1]
        product =data[2]
        location =data[3]
            
        value = [gene_id, accession, product, location, cds, protein_seq, dna_seq]
        key = ['gene_id', 'accession', 'product', 'location', 'cds', 'protein_seq', 'dna_seq']

        gene_record = dict(zip(key,value))

        gene_records = append(gene_record)

        return(gene_records)


