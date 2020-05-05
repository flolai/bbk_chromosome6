This readme contains information on how to populate the MySQL database

#### Logical Schema
 
 |**Chromosome 6** |              | 
 |-----------------|---------------|
 |Gene Identification| VARCHAR(20)|
 |Accession          | VARCHAR(20)|
 |Protein Product    | TEXT       |
 |Locus              | VARCHAR(20)|
 |CDS                | mediumtext |
 |Protein Sequence   | mediumtext |
 |DNA Sequence       | mediumtext |
  ---------------------------------
 
#### Physical Schema
 
  | **Chromosome 6** |              | 
 |-----------------|---------------|
 |gene_id            | VARCHAR(20)|
 |accession          | VARCHAR(20)|
 |product            | TEXT       |
 |locus              | VARCHAR(20)|
 |cds                | mediumtext |
 |protein_seq        | mediumtext |
 |dna_seq            | mediumtext |
  ---------------------------------
 
 
#### Table Definition
  
  **CREATE TABLE chrom6**  
( 	gene_id	VARCHAR(20) NOT NULL,  
accession	VARCHAR(20) NOT NULL,  
product	TEXT NOT NULL,  
location	VARCHAR(20) NOT NULL,  
cds		MEDIUMTEXT NOT NULL,  
protein_seq	MEDIUMTEXT NOT NULL,  
dna_seq	MEDIUMTEXT NOT NULL,  
PRIMARY KEY (accession)  
);  
	
Once data has been loaded into table add index to accession with below statement:

CREATE INDEX accession_IDX ON chrom6 (accession);  

Index added on accession as likely to be the most frequently searched on field as search tables provide the option to click through on accession to get full entry details. 

Accession is the genbank unique identifier so was used as the primary key. 


#### Load Data Statement
To load genbank data update below system path (in italics) with location of data created by the parser and run command in SQL

LOAD DATA INFILE *'/d/user6/co001/Desktop/BIOCOMP/mysql_data5.txt'*  
INTO TABLE chrom6  
FIELDS TERMINATED BY ',' ENCLOSED BY '\''  
LINES TERMINATED BY ']' STARTING BY '[';
