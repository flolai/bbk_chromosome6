import time
import pymysql.cursors

def getEntry(x):

    t0 = time.clock()

# Set parameters – to move these to config file

    dbname   = "co001"
    dbhost   = "localhost"
    dbuser   = "co001"
    dbpass   = "nz8mjl6ft"   
    port     = 3306

# Connect to the database
    db = pymysql.connect(host=dbhost, port=port, user=dbuser, passwd=dbpass, db=dbname)

    try:
        
# Create a cursor and execute the SQL on it - search db on accession number
        cursor = db.cursor()
        nrows = cursor.execute("SELECT * FROM chrom6 WHERE accession =%s", x)
    
#Using the cursor as iterator, should return one entry as accession unique
        for data in cursor:
            gene_id =data[0]
            accession =data[1]
            product =data[2]
            location =data[3]
            cds =data[4]
            protein_seq =data[5]
            dna_seq =data[6]

        t1 = time.clock()

        print("gene_id: ", gene_id,"\naccession:", accession,"\nproduct: ",product,"\nlocation: ",location,"\ncds: ",cds,"\nprotein_seq: ", protein_seq,"\ndna_seq: ", dna_seq,",")
        print('elapsed time: ', t1-t0)

    except Exception as e:
        print("Exception occured:{}".format(e));

    finally:
        cursor.close()
        db.close()

def getAllEntries():

# Set parameters – to move these to config file

    dbname   = "co001"
    dbhost   = "localhost"
    dbuser   = "co001"
    dbpass   = "nz8mjl6ft"   
    port     = 3306

# Connect to the database
    db = pymysql.connect(host=dbhost, port=port, user=dbuser, passwd=dbpass, db=dbname)


    sql = 'SELECT * FROM chrom6'
    
# Create a cursor and execute the SQL on it - returns all items in database
    cursor = db.cursor()
    cursor.execute(sql)

    data = cursor.fetchone()

    while data is not None:    
        gene_id =data[0]
        accession =data[1]
        product =data[2]
        location =data[3]
            
        print("gene_id: ", gene_id,"\naccession:", accession,"\nproduct: ",product,"\nlocation: ",location,",\n")
        data = cursor.fetchone()


