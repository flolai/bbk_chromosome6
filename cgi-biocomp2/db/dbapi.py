#!/usr/bin/python3

"""
This is the python wrapper for the MySQL database. 

Queries chrom6 database and returns entries to blapi 

getAllEntries() parameters = accession, location, gene_id, product. Returns list of dictionaries. 

getentry() parameters = accession, returns dictionary

Author: Oliver Cant
Created on March 28th 2020

11th April 2020 Updated get all entries function to allow searching on multiple categories 
"""


import time
import pymysql.cursors
import sys

import config # import configuration info

sys.path.insert(0, "../db/")
sys.path.insert(0, "../")

def getEntry(accession):

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
        nrows = cursor.execute("SELECT * FROM chrom6 WHERE accession =%s", accession)
    
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
        return("Exception occured:{}".format(e));

    finally:
        cursor.close()
        db.close()

def getAllEntries(**kwargs):

    gene_records = []

    accession = '%' if kwargs['accession'] == '' else kwargs['accession']
    product = '%' if kwargs['product'] == '' else kwargs['product']
    location = '%' if kwargs['location'] == '' else kwargs['location']
    gene_id = '%' if kwargs['gene_id'] == '' else kwargs['gene_id']

# Get parameters from config file

    dbname   = config.dbname
    dbhost   = config.dbhost
    dbuser   = config.dbuser
    dbpass   = config.dbpass 
    port     = config.port


# Connect to the database
    db = pymysql.connect(host=dbhost, port=port, user=dbuser, passwd=dbpass, db=dbname)

    try:
        
        SQL = "SELECT gene_id, accession, product, location FROM chrom6 WHERE accession LIKE %s AND gene_id LIKE %s AND product LIKE %s AND location LIKE %s "
    
# Create a cursor and execute the SQL on it - returns all items in database
        cursor = db.cursor()
        nrows = cursor.execute(SQL, (accession, gene_id, product, location))

        data = cursor.fetchall()

        for row in data:
            key = ['gene_id', 'accession', 'product', 'location']
            gene_record = dict(zip(key,row))
            gene_records.append(gene_record)
        return(gene_records)
        
    except Exception as e:
        return("Exception occured:{}".format(e));

    finally:
        cursor.close()
        db.close()


