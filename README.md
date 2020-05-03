# Biocomputing II / cgi-biocomp2/Chromosome 6 Genome browser installation

Should any other user would like to install the genome browesr other than the current available web version, instruction are as follow.

1. Download chromosome 6 genome informaiton from GenBank follow this link: ```https://www.ncbi.nlm.nih.gov/nuccore/CM000668.2?report=genbank```
2. Clone the ```bbk_chromosome6``` repository using ```https://github.com/flolai/bbk_chromosome6.git```
3. Create a MQSQL database according to instruction given in ```bbk_chromosome6/createdb```
4. In the ```bbk_chromosome6/createdb``` directory, use ```parse.py``` and save the parsed chromosome 6 data as a text file and insert it into the MYSQL database acccording to the scheme and instruction in ```/createdb/docs``` under 'Load Data Statement'
5. Edit the ```config.py``` files with the updated database user name and password
6. In the ```cgi-biocomp2``` directory, it contains the three subdirectories for the three layers of the code
 - ```cgi-biocomp2/cgi``` contains the CGI stripts
 - ```cgi-biocomp2/bl``` contains the business layer code
 - ```cgi-biocomp2/db``` contains the database access layer code
7. If necessary, the calculation for the total codon frequency can be repeated using ```total_codon_cal.py```which is currently located in ```bbk_chromosome6/cgi-biocomp2/bl``` directory.
8. All html files, including files in the subdirectory will need to be copied to ```~/www/html/biocomp2```
9. All python files in ```bbk_chromosome6/cgi-biocomp2/cgi``` will need to be copied to ```~/www/cgi-bin/biocomp2```
10. Alternaticely, for step 8 and step 9, by running the ```install.py```, the files will be automatically copied to the correct directories
10. ```bbk_chromosome6/testing``` contains doctest code for the testing of the avialble files
11. For ```index.html```, it is necessary to update the href link for ```listall.py```. The current href link is listed below:
```sh
<li><a href="http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/listall.py"><i class="fas fa-th-list"></i> Gene Summary</a></li>
```
12. For```search.html```, it is necessary to update the href link and form action for ```listall.py```.  The current href link is listed below:
```sh
<li><a href="http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/listall.py"><i class="fas fa-th-list"></i> Gene Summary</a></li>
```
Current form action:
```sh
<form action='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/listall.py' method='get'>
```