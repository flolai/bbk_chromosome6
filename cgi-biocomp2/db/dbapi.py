"""
Program: dbapi
File: dbapi.py

Version: V2.0
Date Crated: 11-Apr 2020
Function: Python wrapper for MySQL Genebank chromosome 6 database. Searches databaseand returns
matching entry details to the blapi.py 

Description:
------------

This program takes Genbank accession number, gene_id, protein product and location from the blapi
and returns all matching entries from the Genebank database.
The program contains two functions:
    getEntry()      - takes accession number as a parameter and returns one entry.
                      Returns accession number, gene_id, protein, location, DNA sequence
                      and protein sequence. 
    getAllEntries() - takes accession, gene_id, protein and or location as a parameter
                      and returns all matching entries in database. Returns accession,
                      gene_id, location and product.
                      If no parameters entered all entries in the database are returned.

Updates
-------
V2 - update to allow searches on gene_id, protein and location.
    
"""

#***************************************************************************************************
#import libraries
import pymysql.cursors
import sys

sys.path.insert(0, "../db/")
sys.path.insert(0, "../")

import config # import configuration information
#***************************************************************************************************


def getEntry(accession):
    '''
    Takes accession number from blapi.py, connects to MySQL database and returns accession number,
    Gene ID, protein, location on chromosome 6, DNA sequence and protein sequence of matching gene
    bank entry
    to the blapi.

    Parameters
    ----------
    accession: this is the genebank accession number that the user has selected in the front end.
                It is passed from the front end to the blapi which calls this function

    Return
    -------
    {'gene_id': 'XXX', 'accession': 'XXX', 'product': 'XXX', 'location': 'XXX', 
     'cds': 'XXX', 'protein_seq': 'XXX', 'dna_seq': 'XXX'}

    Returns: 'Exception occured: e' if error   
    '''
    
# Get database connection parameters from config file

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
    '''
    This function take accession, gene_id, location and or product
    from the blapi, connects to the MySQL Database containing chromosome 6 genebank
    entries and returns accession, gene_id, location and product of any matching entries.
        
    Parameters are selected by the user in the front end. They are passed from the front end to the blapi which call this function. Depending on user
    data any one or more of the following. If no parameters entered 
    Parameters
    ----------
    accession: Genebank accession number selected by the user in the front end
    gene_id: Genebank gene_id selected by the user in the front end
    location: Chromosome 6 location of genebank entry selected by the user in the front end
    product: Gene product selected by the user in the front end

    Return
    ------
    List of dictionaries:
    [{'gene_id' : 'XXX', 'accession': 'XXX','product' :'XXX','location' :' XXX'}]
    Returns: 'Exception occured: e' if error
    '''
    
    gene_records = []

    accession = '%' if kwargs['accession'] == 'None' else kwargs['accession']
    product = '%' if kwargs['product'] == 'None' else kwargs['product']
    location = '%' if kwargs['location'] == 'None' else kwargs['location']
    gene_id = '%' if kwargs['gene_id'] == 'None' else kwargs['gene_id']

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


