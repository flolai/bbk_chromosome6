Biocomputing II / createdb
==========================

This directory contains the parser to populate the database from the
provided Genbank file.

## Contents
1.	Genbank Parser 
2.	Genebank Database

## 1.	Genbank Parser
The parser reads all the genbank entries for chromosome 6 and for each entry extracts the following:
Accession number    
Gene identification number   
Locus  
Protein product  
CDS   
Protein Sequence  
DNA sequence  

The data is returned as list of lists, with each item enclosed by ‘’ and ended with a comma. The start and end of each list is delimited by square brackets:  
[[‘accession1’, ’gene_id1’, ’location1’, ’product1’, ’CDS1’, ’Protein Sequence1’, ’dna_seq1’][  ‘accessionX’, ’gene_idX’, ’location X’, ’product X’, ’CDS X’, ’Protein SequenceX’, ’dna_seqX’]]  

#### Filtering
The following entries are filtered out of the database by the parser:  
1.	Entries with non-standard amino acids in the DNA sequence   
2.	For entries with multiple CDS features only the first CDS feature is taken  
3.	Entries with mutations and variations and alternative splicing  

#### Modifications to Genbank entries  
###### Non-Standard Characters
CDS – Commas where used to separate exons in the genbank data. These are switched to semi-colons by the parser as commas are used as delimiters when the data is loaded into MySQL. Newlines, <, >, ), (, whitespace are removed from the CDS field to return a string detailing start and end bases in each exon and the annotation ‘complement’ where the exon occurs on the complement strand. Complement annotation was left in the entry so the bases in these entries could be swapped and sequence reversed in the business layer.  
Product – Commas are removed from this field by the parser as they are used as a delimiter when loading the data to the database. New lines are removed and whitespace was reduced to just one character to improve readability of the output from the database.

#### Running the parser 
1.	Genbank data was downloaded from:  
http://www.bioinf.org.uk/teaching/bbk/biocomp2/project/data/chrom_CDS_6.gz  
2.	Update parser with system path with file location from Genbank data  
3.	Run parser in python, this will generate the following text file “chrom6_data.txt” which contains data to be uploaded to MySQL Database  

## 2.	Genbank Database

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
( 	gene_id	VARCHAR(20a) NOT NULL,  
accession	VARCHAR(20) NOT NULL,  
product	TEXT NOT NULL,  
location	VARCHAR(20) NOT NULL,  
cds		MEDIUMTEXT NOT NULL,  
protein_seq	MEDIUMTEXT NOT NULL,  
dna_seq	MEDIUMTEXT NOT NULL,  
PRIMARY KEY (accession),  
INDEX (accession)   
);  
	
Once data has been loaded into table add index with below statements:  
CREATE INDEX accession_x ON chrom6 (accession);  


#### Load Data Statement
Updated below system path (highlighted in blue) with location of data created by the parser  

LOAD DATA INFILE '/d/user6/co001/Desktop/BIOCOMP/mysql_data5.txt'  
INTO TABLE chrom6  
FIELDS TERMINATED BY ',' ENCLOSED BY '\''  
LINES TERMINATED BY ']' STARTING BY '['  
