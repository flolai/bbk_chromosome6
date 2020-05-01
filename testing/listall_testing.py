#!/usr/bin/env python3
def bar(self, MSG, file=sys.stdout):
'''
    """
    >>> Content-Type: text/html

<!DOCTYPE html><html>
  <head>
    <title>Biocomputing II - framework</title>
    <link rel='stylesheet' type='text/css' href='css/biocomp2.css' />
  </head>
  
  <body>
    <div class='content'>
<html>
<head>
<title>Gene Summary Table</title>
</head><body>
<h1>Gene Summary Table:</h1>
<style>table{width:100%;}table, {border: 1px solid black;border-collapse: collapse;}th, td {border: 1px white;padding: 15px;text-align: left;}table#t01 tr:nth-child(even){background-color: #eee;}table#t01 tr:nth-child(odd){background-color: #fff;}table#t01 th {background-color: black;color: white;}</style><table id ="t01"><tr><th>Genbank Accession</th><th>Gene Identifier</th><th>Protein Product</th><th>Chromosomal Location</th></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB006907' method='get'>AB006907</a></td><td>HLA-DQA1</td><td>HMC class II surface glycoprotein</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB006908' method='get'>AB006908</a></td><td>HLA-DQA1</td><td>MHC class II surface glycoprotein</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB010385' method='get'>AB010385</a></td><td>HLA-DMA</td><td>HLA-DMA</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB018045' method='get'>AB018045</a></td><td>HSP70-Hom</td><td>heat shock protein 72</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB023961' method='get'>AB023961</a></td><td>NOTCH4</td><td>notch4</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB032016' method='get'>AB032016</a></td><td>PDNP1</td><td>phosphodiesterase I/nucleotide pyrophosphatase</td><td>6q22-q23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB051339' method='get'>AB051339</a></td><td>MRPL14</td><td>mitochondrial ribosomal protein L14</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB051617' method='get'>AB051617</a></td><td>MRPL2</td><td>mitochondrial ribosomal protein L2</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB061840' method='get'>AB061840</a></td><td>RPS12</td><td>ribosomal protein S12</td><td>6q23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088082' method='get'>AB088082</a></td><td>HLA-F</td><td>major histocompatibility complex class I F</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088083' method='get'>AB088083</a></td><td>HLA-G</td><td>HLA-G histocompatibility antigen class I G</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088084' method='get'>AB088084</a></td><td>HLA-A</td><td>major histocompatibility complex class I A</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088085' method='get'>AB088085</a></td><td>HCGIX-4</td><td>hypothetical protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088087' method='get'>AB088087</a></td><td>HCGVII</td><td>homologue of yeast omnipotent supressor 45</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088089' method='get'>AB088089</a></td><td>RNF9</td><td>tripartite motif-containing 10</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088090' method='get'>AB088090</a></td><td>ZNF173</td><td>tripartite motif-containing 26</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088093' method='get'>AB088093</a></td><td>TC4</td><td>RAN</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088094' method='get'>AB088094</a></td><td>HLA-E</td><td>major histocompatibility complex class I E</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088095' method='get'>AB088095</a></td><td>CAT56</td><td>proline rich protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088096' method='get'>AB088096</a></td><td>ABC50</td><td>ATP-binding cassette sub-family F (GCN20)</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088097' method='get'>AB088097</a></td><td>FB19</td><td>protein phosphatase 1 regulatory subunit 10</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088098' method='get'>AB088098</a></td><td>DBP2</td><td>DEAD/H (Asp-Glu-Ala-Asp/His) box polypeptide 16</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088099' method='get'>AB088099</a></td><td>KIAA0170</td><td>homologue to Drosophila photoreceptor protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088100' method='get'>AB088100</a></td><td>TUBB</td><td>tubulin beta polypeptide</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088101' method='get'>AB088101</a></td><td>PRG1</td><td>immediate early response 3</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088102' method='get'>AB088102</a></td><td>DDR</td><td>receptor tyrosine kinase</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088103' method='get'>AB088103</a></td><td>TFIIH</td><td>transcription factor II H</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088104' method='get'>AB088104</a></td><td>HCR</td><td>tricohyalin homologue</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088106' method='get'>AB088106</a></td><td>LTB</td><td>lymphotoxin beta</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088107' method='get'>AB088107</a></td><td>MICB</td><td>MHC class I polypeptide-related sequence B</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088108' method='get'>AB088108</a></td><td>MICA</td><td>MHC class I polypeptide-related sequence A</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088110' method='get'>AB088110</a></td><td>HLA-B</td><td>major histocompatibility complex class I B</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088111' method='get'>AB088111</a></td><td>HLA-C</td><td>major histocompatibility complex class I C</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088112' method='get'>AB088112</a></td><td>LTA</td><td>lymphotoxin alpha</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088113' method='get'>AB088113</a></td><td>SC1</td><td>transcription factor 19</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088114' method='get'>AB088114</a></td><td>STG</td><td>hypothetical protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB088115' method='get'>AB088115</a></td><td>IKBL</td><td>nuclear factor of kappa light polypeptide gene</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103588' method='get'>AB103588</a></td><td>HLA-F</td><td>HLA-F protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103589' method='get'>AB103589</a></td><td>HLA-G</td><td>HLA-G protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103590' method='get'>AB103590</a></td><td>HLA-A</td><td>HLA-A protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103591' method='get'>AB103591</a></td><td>HCGIX-4</td><td>hypothetical protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103595' method='get'>AB103595</a></td><td>RNF9</td><td>Zn-finger protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103596' method='get'>AB103596</a></td><td>ZNF173</td><td>Zn-finger protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103599' method='get'>AB103599</a></td><td>TC4</td><td>TC4 protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103600' method='get'>AB103600</a></td><td>HLA-E</td><td>HLA-E protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103601' method='get'>AB103601</a></td><td>CAT56</td><td>hypothetical protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103602' method='get'>AB103602</a></td><td>ABC50</td><td>ABC50 protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103603' method='get'>AB103603</a></td><td>FB19</td><td>FB19 protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103604' method='get'>AB103604</a></td><td>DBP2</td><td>DBP2 protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103605' method='get'>AB103605</a></td><td>KIAA0170</td><td>KIAA0170 protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103606' method='get'>AB103606</a></td><td>TUBB</td><td>beta-tubulin protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103607' method='get'>AB103607</a></td><td>PRG1</td><td>PRG1 protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103608' method='get'>AB103608</a></td><td>DDR</td><td>DDR protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103609' method='get'>AB103609</a></td><td>TFIIH</td><td>TFIIH protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103610' method='get'>AB103610</a></td><td>HCR</td><td>HCR protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103612' method='get'>AB103612</a></td><td>LTB</td><td>LTB protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103613' method='get'>AB103613</a></td><td>MICB</td><td>MICB protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103614' method='get'>AB103614</a></td><td>MICA</td><td>MICA protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103616' method='get'>AB103616</a></td><td>HLA-B</td><td>HLA-B protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103617' method='get'>AB103617</a></td><td>HLA-C</td><td>HLA-C protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103618' method='get'>AB103618</a></td><td>LTA</td><td>LTA protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103619' method='get'>AB103619</a></td><td>SC1</td><td>SC1 protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103620' method='get'>AB103620</a></td><td>STG</td><td>hypothetical protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB103621' method='get'>AB103621</a></td><td>IKBL</td><td>IKBL protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB110931' method='get'>AB110931</a></td><td>DPCR1</td><td>DPCR protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB110932' method='get'>AB110932</a></td><td>DPCR1</td><td>DPCR1 protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB110933' method='get'>AB110933</a></td><td>MRPS18B</td><td>MRPS18B protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB110934' method='get'>AB110934</a></td><td>MRPS18B</td><td>MRPS18B protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB110935' method='get'>AB110935</a></td><td>NRM</td><td>nuclear envelope membrane protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB110936' method='get'>AB110936</a></td><td>NRM</td><td>nuclear envelope membrane protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB110937' method='get'>AB110937</a></td><td>TRIM39</td><td>TRIM39 protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB110938' method='get'>AB110938</a></td><td>TRIM39</td><td>TRIM39 protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB110939' method='get'>AB110939</a></td><td>TRIM40</td><td>TRIM40 protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB110940' method='get'>AB110940</a></td><td>TRIM40</td><td>TRIM40 protein</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB112911' method='get'>AB112911</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB112912' method='get'>AB112912</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB112913' method='get'>AB112913</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF001450' method='get'>AF001450</a></td><td>CBFA1</td><td>core binding factor alpha1 subunit</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF006004' method='get'>AF006004</a></td><td>BZF1</td><td>BZF1</td><td>6p23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF017776' method='get'>AF017776</a></td><td>IPM150</td><td>interphotoreceptor matrix</td><td>6q14.2-q15</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF019369' method='get'>AF019369</a></td><td>TPMT</td><td>thiopurine S-methyltransferase</td><td>6p22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF019413' method='get'>AF019413</a></td><td>tenascin-X</td><td>tenascin X</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF020714' method='get'>AF020714</a></td><td>HLA-G</td><td>MHC class I antigen</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF024516' method='get'>AF024516</a></td><td>OPRM1</td><td>mu opioid receptor</td><td>6q24-q25</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF035426' method='get'>AF035426</a></td><td>TPMT</td><td>thiopurine S-methyltransferase</td><td>6p22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF036130' method='get'>AF036130</a></td><td>COL9A1</td><td>collagen type IX alpha I chain long form</td><td>6q12-q14</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF047350' method='get'>AF047350</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>between D6s8 and D6s5</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF048688' method='get'>AF048688</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>between D6S8 and D6S5</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF048693' method='get'>AF048693</a></td><td>FKHL7</td><td>transcription factor forkhead-like 7</td><td>6p25</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF048991' method='get'>AF048991</a></td><td>MSH5</td><td>MutS homolog 5</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF059197' method='get'>AF059197</a></td><td>SOD2</td><td>manganese superoxide dismutase</td><td>6q25</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF059675' method='get'>AF059675</a></td><td>SKI2W</td><td>putative RNA helicase Ski2w</td><td>6p21.3; between RP1 and DOM3Z</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF065210' method='get'>AF065210</a></td><td>RAGE</td><td>advanced glycosylation end product-specific</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF065211' method='get'>AF065211</a></td><td>RAGE</td><td>advanced glycosylation end product-specific</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF065212' method='get'>AF065212</a></td><td>RAGE</td><td>advanced glycosylation end product-specific</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF068859' method='get'>AF068859</a></td><td>prolactin</td><td>prolactin</td><td>6p22.2-p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF069067' method='get'>AF069067</a></td><td>CD73</td><td>"ecto-5-nucleotidase"</td><td>6q14-q21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF069333' method='get'>AF069333</a></td><td>IGF2R</td><td>insulin-like growth factor II receptor</td><td>6q26-27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF070079' method='get'>AF070079</a></td><td>MSH5</td><td>MutS homolog</td><td>6p22.3-p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF072680' method='get'>AF072680</a></td><td>HLA-DMB</td><td>MHC class II antigen</td><td>6p21.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF077015' method='get'>AF077015</a></td><td>HLA-DPB1</td><td>MHC class II antigen</td><td>6p21.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF078096' method='get'>AF078096</a></td><td>FKHL7</td><td>forkhead/winged helix-like transcription factor</td><td>6p25</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF084939' method='get'>AF084939</a></td><td>FREAC2</td><td>forkhead transcription factor</td><td>6p25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF086641' method='get'>AF086641</a></td><td>TNXB</td><td>truncated tenascin XB</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF092125' method='get'>AF092125</a></td><td>VEGF</td><td>vascular endothelial growth factor</td><td>6p12-p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF095785' method='get'>AF095785</a></td><td>VEGF</td><td>vascular endothelial growth factor</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF097026' method='get'>AF097026</a></td><td>AHCP</td><td>autosomal highly conserved protein</td><td>6p22-p23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF098794' method='get'>AF098794</a></td><td>HLA-DPA1</td><td>MHC class II antigen</td><td>6p21.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF107699' method='get'>AF107699</a></td><td>RING3</td><td>RING3 protein</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF108098' method='get'>AF108098</a></td><td>PEX6</td><td>peroxisome assembly factor-2</td><td>6p21.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF112460' method='get'>AF112460</a></td><td>GPR58</td><td>G protein-coupled receptor 58</td><td>6q24</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF117221' method='get'>AF117221</a></td><td>KE4</td><td>KE4 protein</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF119714' method='get'>AF119714</a></td><td>PDNP3</td><td>phosphodiesterase I/nucleotide pyrophosphatase</td><td>6q22</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF120161' method='get'>AF120161</a></td><td>RXRB</td><td>retinoic X receptor beta</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF134890' method='get'>AF134890</a></td><td>HLA-DMB</td><td>MHC class antigen HLA-DM beta</td><td>6q22</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF153836' method='get'>AF153836</a></td><td>HIVEP2</td><td>human immunodeficiency virus type I</td><td>6q23-q24</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF158656' method='get'>AF158656</a></td><td>APOA</td><td>apolipoprotein(a)</td><td>6q26-q27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF158657' method='get'>AF158657</a></td><td>APOA</td><td>apolipoprotein(a)</td><td>6q26-q27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF158659' method='get'>AF158659</a></td><td>APOA</td><td>apolipoprotein(a)</td><td>6q26-q27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF158661' method='get'>AF158661</a></td><td>APOA</td><td>apolipoprotein(a)</td><td>6q26-q27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF158663' method='get'>AF158663</a></td><td>APOA</td><td>apolipoprotein(a)</td><td>6q26-q27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF178842' method='get'>AF178842</a></td><td>RHAG</td><td>Rhesus blood group-associated glycoprotein</td><td>6p11-p21.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF180814' method='get'>AF180814</a></td><td>PEX7</td><td>peroxisomal PTS2 receptor</td><td>6q22-q24</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF184234' method='get'>AF184234</a></td><td>HFE</td><td>hereditary haemochromatosis protein precursor</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF190884' method='get'>AF190884</a></td><td>ENT1</td><td>equilibrative nucleoside transporter 1</td><td>6p21.1-p21.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF211939' method='get'>AF211939</a></td><td>OR2H3</td><td>olfactory receptor</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF211940' method='get'>AF211940</a></td><td>OR2H3</td><td>olfactory receptor</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF211941' method='get'>AF211941</a></td><td>OR2H3</td><td>olfactory receptor</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF211942' method='get'>AF211942</a></td><td>OR2H3</td><td>olfactory receptor</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF218234' method='get'>AF218234</a></td><td>F13A1</td><td>blood coagulation factor XIII a subunit</td><td>6p25-p24</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF222310' method='get'>AF222310</a></td><td>DLL1</td><td>Delta1</td><td>6q27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF225950' method='get'>AF225950</a></td><td>HFH1</td><td>HNF-3/forkhead-like protein 1</td><td>6p23-25</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF227518' method='get'>AF227518</a></td><td>HLA-DRB4</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF280405' method='get'>AF280405</a></td><td>HLA-DPB1</td><td>MHC class II anitgen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF293078' method='get'>AF293078</a></td><td>MRS2</td><td>putative magnesium transporter</td><td>6p22.3-22.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF317654' method='get'>AF317654</a></td><td>GPR63</td><td>G protein-coupled receptor</td><td>6q16.1-q16.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF326912' method='get'>AF326912</a></td><td>ESR1</td><td>estrogen receptor 1</td><td>between D6S440 and D6S442</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF331065' method='get'>AF331065</a></td><td>HFE</td><td>hereditary hemochromatosis protein precursor</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF362494' method='get'>AF362494</a></td><td>SLC17A1</td><td>sodium/phosphate type I cotransporter</td><td>6p23-p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF362495' method='get'>AF362495</a></td><td>SLC17A1</td><td>sodium/phosphate type I cotransporter</td><td>6p23-p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF362500' method='get'>AF362500</a></td><td>SLC17A1</td><td>sodium/phosphate type I cotransporter</td><td>6p23-p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF362502' method='get'>AF362502</a></td><td>SLC17A1</td><td>sodium/phosphate type I cotransporter</td><td>6p23-p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF362504' method='get'>AF362504</a></td><td>SLC17A1</td><td>sodium/phosphate type I cotransporter</td><td>6p23-p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF362505' method='get'>AF362505</a></td><td>SLC17A1</td><td>sodium/phosphate type I cotransporter</td><td>6p23-p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF372451' method='get'>AF372451</a></td><td>HLA-DPB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF372452' method='get'>AF372452</a></td><td>HLA-DPB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF380185' method='get'>AF380185</a></td><td>TA1</td><td>trace amine receptor 1</td><td>6q23.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF380189' method='get'>AF380189</a></td><td>TA3</td><td>trace amine receptor 3</td><td>6q23.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF380192' method='get'>AF380192</a></td><td>TA4</td><td>trace amine receptor 4</td><td>6q23.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF380193' method='get'>AF380193</a></td><td>TA5</td><td>trace amine receptor 5</td><td>6q23.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF386792' method='get'>AF386792</a></td><td>PIM1</td><td>proto-oncogene PIM1</td><td>6p21.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF407166' method='get'>AF407166</a></td><td>KEPI</td><td>PKC-potentiated PP1 inhibitory protein</td><td>6q24.3-q25.3; 159mb</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF438327' method='get'>AF438327</a></td><td>COL21A1</td><td>alpha 1 type XXI collagen precursor</td><td>6p12.3-p11.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF447176' method='get'>AF447176</a></td><td>PTK7</td><td>protein tyrosine kinase-7</td><td>6p21.1-p12.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF463516' method='get'>AF463516</a></td><td>HLA-DQB1</td><td>MHC class II antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF479569' method='get'>AF479569</a></td><td>HLA-DQB1</td><td>MHC class II antigen</td><td>6p23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF479570' method='get'>AF479570</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF480612' method='get'>AF480612</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF480613' method='get'>AF480613</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF480614' method='get'>AF480614</a></td><td>HLA-C</td><td>MHC class I antigen</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF480841' method='get'>AF480841</a></td><td>HLA-A</td><td>MHC class I antigen</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF495730' method='get'>AF495730</a></td><td>SLC29A1</td><td>equilibrative nucleoside transporter 1</td><td>6p21.2-21.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF525359' method='get'>AF525359</a></td><td>HFE</td><td>hereditary hemochromatosis protein HLA-H</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF525499' method='get'>AF525499</a></td><td>HFE</td><td>hereditary hemochromatosis protein precursor</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AF547997' method='get'>AF547997</a></td><td>OPRM1</td><td>mu opioid receptor MOR-1O</td><td>6q24-6q25</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ000512' method='get'>AJ000512</a></td><td>sgk</td><td>serine/threonine protein kinase</td><td>q23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ001590' method='get'>AJ001590</a></td><td>AF6q21</td><td>fork head protein</td><td>6q21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ005590' method='get'>AJ005590</a></td><td>HLA-B*5111N</td><td>alpha 1 domain</td><td>6p21.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ007603' method='get'>AJ007603</a></td><td>HLA-B*15UL</td><td>HLA-B15UL protein</td><td>p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ007605' method='get'>AJ007605</a></td><td>HLA-B*15IL</td><td>HLA-B15IL protein</td><td>p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ009866' method='get'>AJ009866</a></td><td>pex3</td><td>Pex3p</td><td>q23-24</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ010322' method='get'>AJ010322</a></td><td>HLA-Cw*15P</td><td>human leukocyte antigen-C alpha chain</td><td>p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ010323' method='get'>AJ010323</a></td><td>HLA-Cw*15P</td><td>human leukocyte antigen-C alpha chain</td><td>p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ010982' method='get'>AJ010982</a></td><td>HLA-DRB1*14JW</td><td>HLA-DR14 protein</td><td>p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ012384' method='get'>AJ012384</a></td><td>HLA-A</td><td>human leucocyte antigen A alpha chain</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ012753' method='get'>AJ012753</a></td><td>RAGE</td><td>RAGE protein</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ131193' method='get'>AJ131193</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ131194' method='get'>AJ131194</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ131789' method='get'>AJ131789</a></td><td>HLA-DRB4</td><td>human leucocyte antigen DRB4</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ131852' method='get'>AJ131852</a></td><td>HLA-B</td><td>human leucocyte antigen B</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ131853' method='get'>AJ131853</a></td><td>HLA-B</td><td>human lecocyte antigen B</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ133492' method='get'>AJ133492</a></td><td>HLA-DRB1</td><td>human leucocyte antigen DRB1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ133773' method='get'>AJ133773</a></td><td>HLA-B</td><td>human leucocyte antigen B</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ223319' method='get'>AJ223319</a></td><td>rps18</td><td>ribosomal protein S18</td><td>p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ237964' method='get'>AJ237964</a></td><td>HLA-DRB1</td><td>human leucocyte antigen DRB</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ238151' method='get'>AJ238151</a></td><td>HLA-A</td><td>human leucocyte antigen A alpha chain</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ238154' method='get'>AJ238154</a></td><td>HLA-DRB1</td><td>human leucocyte antigen DR beta 1 chain</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ238155' method='get'>AJ238155</a></td><td>HLA-DRB3</td><td>human leucocyte antigen DR52 beta 1 chain</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ238523' method='get'>AJ238523</a></td><td>HLA-A</td><td>human leucocyte antigen A</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ242020' method='get'>AJ242020</a></td><td>PC-1</td><td>plasma cell membrane glycoprotein</td><td>6q22</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ242860' method='get'>AJ242860</a></td><td>HLA-DRB3</td><td>human leucocyte antigen DRB3</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ242861' method='get'>AJ242861</a></td><td>HLA-DRB3</td><td>human leucocyte antigen DRB3</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ242862' method='get'>AJ242862</a></td><td>HLA-DRB3</td><td>human leucocyte antigen DRB3</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ243701' method='get'>AJ243701</a></td><td>HLA-DRB4</td><td>human leucocyte antigen DRB4</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ243737' method='get'>AJ243737</a></td><td>HLA-B</td><td>human leucocyte antigen B</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ243738' method='get'>AJ243738</a></td><td>HLA-B</td><td>human leucocyte antigen B</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ245869' method='get'>AJ245869</a></td><td>HLA-B</td><td>human leucocyte antigen B</td><td>6p23.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ249394' method='get'>AJ249394</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ249724' method='get'>AJ249724</a></td><td>HLA-B</td><td>human leucocyte antigen B</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ249726' method='get'>AJ249726</a></td><td>HLA-DRB1</td><td>human leucocyte antigen DRB1</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ250499' method='get'>AJ250499</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ250500' method='get'>AJ250500</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ250501' method='get'>AJ250501</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ250502' method='get'>AJ250502</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ250503' method='get'>AJ250503</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ250504' method='get'>AJ250504</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ250505' method='get'>AJ250505</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ250506' method='get'>AJ250506</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ250507' method='get'>AJ250507</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ250802' method='get'>AJ250802</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ250803' method='get'>AJ250803</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ250804' method='get'>AJ250804</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ250805' method='get'>AJ250805</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ250990' method='get'>AJ250990</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ250991' method='get'>AJ250991</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ251156' method='get'>AJ251156</a></td><td>MICB</td><td>MHC class I chain-related protein B</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ251158' method='get'>AJ251158</a></td><td>MICB</td><td>MHC class I chain-related protein B</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ251160' method='get'>AJ251160</a></td><td>MICB</td><td>MHC class I chain-related protein B</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ251884' method='get'>AJ251884</a></td><td>SLC22A3</td><td>extraneuronal monoamine transporter (EMT)</td><td>6q27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ251885' method='get'>AJ251885</a></td><td>SLC22A2</td><td>organic cation transporter (OCT2)</td><td>6q26</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ251984' method='get'>AJ251984</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ251985' method='get'>AJ251985</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ269496' method='get'>AJ269496</a></td><td>HLA-B</td><td>human leucocyte antigen B</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ270944' method='get'>AJ270944</a></td><td>TNFa</td><td>tumor necrosis factor alpha</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ271340' method='get'>AJ271340</a></td><td>HLA-A</td><td>human leucocyte antigen A</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ271789' method='get'>AJ271789</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ272506' method='get'>AJ272506</a></td><td>KCNQ5</td><td>potassium channel protein</td><td>6q14</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ275937' method='get'>AJ275937</a></td><td>HLA</td><td>human leucocyte antigen</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ278043' method='get'>AJ278043</a></td><td>HLA-B</td><td>human leucocyte antigen B</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ278044' method='get'>AJ278044</a></td><td>HLA-B</td><td>human leucocyte antigen B</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ278494' method='get'>AJ278494</a></td><td>HLA-Cw</td><td>human leucocyte antigen Cw</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ278744' method='get'>AJ278744</a></td><td>HLA-B*3531</td><td>MHC Class I antigen alpha 1 domain</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ278746' method='get'>AJ278746</a></td><td>HLA-B*35SRE</td><td>MHC Class I antigen alpha 1 domain</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ289123' method='get'>AJ289123</a></td><td>HLA-DRB1</td><td>human leucocyte antigen DRB1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ289124' method='get'>AJ289124</a></td><td>HLA-DRB1</td><td>human leucocyte antigen DRB1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ290949' method='get'>AJ290949</a></td><td>HLA-B</td><td>human leucocyte antigen B</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ291815' method='get'>AJ291815</a></td><td>HLA-Cw</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ292253' method='get'>AJ292253</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ293577' method='get'>AJ293577</a></td><td>MOCS1</td><td>MOCS1A enzyme</td><td>6p21.1-2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ295250' method='get'>AJ295250</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ295293' method='get'>AJ295293</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ295294' method='get'>AJ295294</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ297317' method='get'>AJ297317</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ297476' method='get'>AJ297476</a></td><td>HLA-A</td><td>human leucocyte antigen A</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ297499' method='get'>AJ297499</a></td><td>HLA-A</td><td>human leucocyte antigen A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ297503' method='get'>AJ297503</a></td><td>HLA-DRB4</td><td>human leucocyte antigen DRB4</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ297934' method='get'>AJ297934</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ297940' method='get'>AJ297940</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ297942' method='get'>AJ297942</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ298116' method='get'>AJ298116</a></td><td>HLA-C</td><td>MHC class I antigen</td><td>p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ301657' method='get'>AJ301657</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ308397' method='get'>AJ308397</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ308399' method='get'>AJ308399</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ309139' method='get'>AJ309139</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ309192' method='get'>AJ309192</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ309194' method='get'>AJ309194</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ310358' method='get'>AJ310358</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ311599' method='get'>AJ311599</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ311600' method='get'>AJ311600</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ311601' method='get'>AJ311601</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ315477' method='get'>AJ315477</a></td><td>HLA-DRB3</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ401085' method='get'>AJ401085</a></td><td>HLA-A</td><td>human leucocyte antigen A</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ401086' method='get'>AJ401086</a></td><td>HLA-A</td><td>human leucocyte antigen A</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ401087' method='get'>AJ401087</a></td><td>HLA-A</td><td>human leucocyte antigen A</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ401236' method='get'>AJ401236</a></td><td>HLA-DRB1</td><td>human leucocyte antigen DRB1</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ403946' method='get'>AJ403946</a></td><td>SLC22A3</td><td>organic cation transporter 3</td><td>6q26-27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ404846' method='get'>AJ404846</a></td><td>HLA-B</td><td>human leucocyte antigen B</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ404969' method='get'>AJ404969</a></td><td>MOCS1</td><td>MOCS1B Protein</td><td>6p21.1-2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ418708' method='get'>AJ418708</a></td><td>HLA-Cw</td><td>MHC class I antigen</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ420238' method='get'>AJ420238</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ420239' method='get'>AJ420239</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ420240' method='get'>AJ420240</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ420241' method='get'>AJ420241</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ420242' method='get'>AJ420242</a></td><td>HLA-C</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ420243' method='get'>AJ420243</a></td><td>HLA-C</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ420244' method='get'>AJ420244</a></td><td>HLA-C</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ420245' method='get'>AJ420245</a></td><td>HLA-C</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ420246' method='get'>AJ420246</a></td><td>HLA-C</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ420247' method='get'>AJ420247</a></td><td>HLA-C</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ420248' method='get'>AJ420248</a></td><td>HLA-C</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ420249' method='get'>AJ420249</a></td><td>HLA-C</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ420250' method='get'>AJ420250</a></td><td>HLA-C</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ420251' method='get'>AJ420251</a></td><td>HLA-C</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ420252' method='get'>AJ420252</a></td><td>HLA-C</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ420253' method='get'>AJ420253</a></td><td>HLA-C</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ420288' method='get'>AJ420288</a></td><td>HLA DRB1</td><td>MHC class II antigen</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ426561' method='get'>AJ426561</a></td><td>HLA-A</td><td>MHC class I antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ490331' method='get'>AJ490331</a></td><td>IFNGR1</td><td>interferon gamma receptor 1</td><td>6q23-24</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ490332' method='get'>AJ490332</a></td><td>IFNGR1</td><td>interferon gamma receptor 1</td><td>6q23-24</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AJ507149' method='get'>AJ507149</a></td><td>HLA-A</td><td>MHC class I antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL008628' method='get'>AL008628</a></td><td>PSMB1</td><td>proteasome (prosome macropain) subunit beta</td><td>q26-27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL008729' method='get'>AL008729</a></td><td>RPEL</td><td>RPEL repeat containing 1</td><td>p24</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL008730' method='get'>AL008730</a></td><td>TRAF3IP2</td><td>novel transcript</td><td>q21-22.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL009031' method='get'>AL009031</a></td><td>ATXN1</td><td>ataxin 1</td><td>p22.3-24.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL009178' method='get'>AL009178</a></td><td>MLLT4</td><td>myeloid/lymphoid or mixed-lineage leukemia</td><td>q27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL009179' method='get'>AL009179</a></td><td>HIST1H2BL</td><td>novel pseudogene</td><td>p21.3-22.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL021331' method='get'>AL021331</a></td><td>UNC93A</td><td>unc-93 homolog A (C. elegans)</td><td>q27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL021366' method='get'>AL021366</a></td><td>cICK0721Q.1</td><td>cICK0721Q.3 (Kinesin related protein)</td><td>p21.1-21.32</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL021407' method='get'>AL021407</a></td><td>MYLIP</td><td>mitochondrial 28S ribosomal protein S32</td><td>p22.3-23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL021807' method='get'>AL021807</a></td><td>HIST1H2BJ</td><td>vomeronasal olfactory 1 receptor chromosome 6-2</td><td>p21.31-22.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL021808' method='get'>AL021808</a></td><td>PRSS16</td><td>protease serine 16 (thymus)</td><td>p21.31-22.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL021917' method='get'>AL021917</a></td><td>HIST1H4H</td><td>histone 1 H4h</td><td>p21.3-22.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL021918' method='get'>AL021918</a></td><td>ZNF184</td><td>zinc finger protein 184</td><td>p21.3-22.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL021938' method='get'>AL021938</a></td><td>JARID2</td><td>jumonji AT rich interactive domain 2</td><td>p22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL021939' method='get'>AL021939</a></td><td>ALDH8A1</td><td>novel pseudogene</td><td>q24.1-25.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL021978' method='get'>AL021978</a></td><td>DTNBP1</td><td>dystrobrevin binding protein 1</td><td>p22.1-22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL021997' method='get'>AL021997</a></td><td>ZNF323</td><td>novel protein similar to zinc finger protein 306</td><td>p22.1-22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL022067' method='get'>AL022067</a></td><td>PRDM1</td><td>PR domain containing 1 with ZNF domain</td><td>q21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL022069' method='get'>AL022069</a></td><td>RPS6KA2</td><td>ribosomal protein S6 kinase 90kDa polypeptide</td><td>q26-27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL022097' method='get'>AL022097</a></td><td>FARS2</td><td>heterogeneous nuclear ribonucleoprotein A0</td><td>p24.1-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL022098' method='get'>AL022098</a></td><td>NEDD9</td><td>neural precursor cell expressed developmentally</td><td>p24.1-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL022170' method='get'>AL022170</a></td><td>LRRC16</td><td>leucine rich repeat containing 16</td><td>p22.1-22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL022343' method='get'>AL022343</a></td><td>DTNBP1</td><td>dystrobrevin binding protein 1</td><td>p22.1-22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL022393' method='get'>AL022393</a></td><td>ZNF193</td><td>novel C2H2 type zinc finger protein</td><td>p21.31-21.33</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL022395' method='get'>AL022395</a></td><td>FBXL4</td><td>F-box and leucine-rich repeat protein 4</td><td>q16.1-16.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL022396' method='get'>AL022396</a></td><td>CD83</td><td>novel transcript</td><td>p22.3-24</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL022717' method='get'>AL022717</a></td><td>CDKAL1</td><td>CDK5 regulatory subunit associated protein</td><td>p22.1-22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL022721' method='get'>AL022721</a></td><td>TEAD3</td><td>TEA domain family member 3</td><td>p21.2-21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL022722' method='get'>AL022722</a></td><td>MAN1A1</td><td>cytochrome c oxidase polypeptide I (COX)</td><td>q22</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL022723' method='get'>AL022723</a></td><td>HLA-G</td><td>HLA-G histocompatibility antigen class I G</td><td>p21.32-22.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL022724' method='get'>AL022724</a></td><td>RP3-413H6.1</td><td>novel transcript</td><td>p22.3-24.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL022725' method='get'>AL022725</a></td><td>CDYL</td><td>chromodomain protein Y-like</td><td>p24.1-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL022726' method='get'>AL022726</a></td><td>ID4</td><td>inhibitor of DNA binding 4 dominant negative</td><td>p22.2-23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL022727' method='get'>AL022727</a></td><td>OR2J1</td><td>olfactory receptor family 2 subfamily B</td><td>p21.31-22.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL023284' method='get'>AL023284</a></td><td>MAP7</td><td>pseudogene similar to Elongation Factor 1-Alpha</td><td>q23-24</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL023578' method='get'>AL023578</a></td><td>MOXD1</td><td>monooxygenase DBH-like 1</td><td>q23.1-23.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL023580' method='get'>AL023580</a></td><td>OLIG3</td><td>basic transcription factor 3 (BTF3) pseudogene</td><td>q24</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL023581' method='get'>AL023581</a></td><td>AIG1</td><td>novel transcript</td><td>q24.1-24.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL023582' method='get'>AL023582</a></td><td>RP3-496H19.1</td><td>p53-induced protein PIGPC1 (PERP)</td><td>q24</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL023583' method='get'>AL023583</a></td><td>CCDC90A</td><td>coiled-coil domain containing 90A</td><td>p23-24.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL023584' method='get'>AL023584</a></td><td>HIVEP2</td><td>putative novel transcript</td><td>q24.1-24.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL023656' method='get'>AL023656</a></td><td>KLHL32</td><td>kelch-like 32 (Drosophila)</td><td>q16</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL023693' method='get'>AL023693</a></td><td>MYB</td><td>v-myb myeloblastosis viral oncogene homolog</td><td>q22.33-23.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL023694' method='get'>AL023694</a></td><td>EEF1E1</td><td>eukaryotic translation elongation factor 1</td><td>p24.3-25.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL023806' method='get'>AL023806</a></td><td>EPM2A</td><td>epilepsy progressive myoclonus type 2A Lafora</td><td>q24</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL023807' method='get'>AL023807</a></td><td>KIF13A</td><td>kinesin family member 13A</td><td>p22.3-23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL023883' method='get'>AL023883</a></td><td>PRL</td><td>prolactin</td><td>p22.2-22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL024474' method='get'>AL024474</a></td><td>UTRN</td><td>pseudogene similar to single-stranded</td><td>q24</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL024497' method='get'>AL024497</a></td><td>EYA4</td><td>novel transcript</td><td>q23.1-24.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL024498' method='get'>AL024498</a></td><td>GCM2</td><td>novel protein</td><td>p23-25.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL024507' method='get'>AL024507</a></td><td>SEC63</td><td>pseudogene similar to part of methylene</td><td>q16.1-22.33</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL024508' method='get'>AL024508</a></td><td>MAP7</td><td>microtubule-associated protein 7</td><td>q23.1-24.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL024509' method='get'>AL024509</a></td><td>LRRC16</td><td>novel transcript</td><td>p21.31-22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031003' method='get'>AL031003</a></td><td>RP3-422G23.1</td><td>macrophage myristoylated alanine-rich C kinase</td><td>q24</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031010' method='get'>AL031010</a></td><td>IYD</td><td>iodotyrosine deiodinase</td><td>q24.1-25.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031058' method='get'>AL031058</a></td><td>DSP</td><td>desmoplakin</td><td>p24-25</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031118' method='get'>AL031118</a></td><td>ZNF184</td><td>novel C2H2 type Zinc Finger protein</td><td>p21.3-22.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031119' method='get'>AL031119</a></td><td>EPM2A</td><td>BTB/POZ domain zinc finger protein pseudogene</td><td>q24</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031121' method='get'>AL031121</a></td><td>PACRG</td><td>PARK2 co-regulated</td><td>q26-27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031123' method='get'>AL031123</a></td><td>RP3-398D13.3</td><td>novel transcript</td><td>p24.1-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031133' method='get'>AL031133</a></td><td>ZC3H12D</td><td>novel pseudogene</td><td>q25.1-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031178' method='get'>AL031178</a></td><td>ICK</td><td>intestinal cell (MAK-like) kinase</td><td>p11.2-12.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031224' method='get'>AL031224</a></td><td>TFAP2B</td><td>transcription factor AP-2 beta (activating</td><td>p12.1-21.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031228' method='get'>AL031228</a></td><td>C6orf11</td><td>chromosome 6 open reading frame 11</td><td>p21.2-21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031230' method='get'>AL031230</a></td><td>GPLD1</td><td>glycosylphosphatidylinositol specific</td><td>p22.2-22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031259' method='get'>AL031259</a></td><td>PDCD2</td><td>7 transmembrane receptor (rhodopsin family)</td><td>q27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031320' method='get'>AL031320</a></td><td>PEX3</td><td>novel protein similar to yeast and bacterial</td><td>q24</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031321' method='get'>AL031321</a></td><td>BAG2</td><td>BCL2-associated athanogene 2</td><td>p11.2-12.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031390' method='get'>AL031390</a></td><td>SF3B5</td><td>novel pseudogene</td><td>q24.1-25.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031433' method='get'>AL031433</a></td><td>KIAA1244</td><td>KIAA1244</td><td>q23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031577' method='get'>AL031577</a></td><td>RP3-391O22.4</td><td>ribosomal protein L44 (RPL44) pseudogene</td><td>p21.2-21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031770' method='get'>AL031770</a></td><td>EXOC2</td><td>novel transcript</td><td>p25.1-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031772' method='get'>AL031772</a></td><td>RP1-225E12.1</td><td>novel transcript</td><td>q24</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031773' method='get'>AL031773</a></td><td>NOX3</td><td>putative novel transcript</td><td>q25.1-26</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031774' method='get'>AL031774</a></td><td>DEK</td><td>DEK oncogene (DNA binding)</td><td>p22.3-23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031775' method='get'>AL031775</a></td><td>C6orf62</td><td>chromosome 6 open reading frame 62</td><td>p22.1-22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031776' method='get'>AL031776</a></td><td>RSPO3</td><td>R-spondin 3 homolog (Xenopus laevis)</td><td>q22.2-23.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031777' method='get'>AL031777</a></td><td>HIST1H3D</td><td>histone 1 H1 pseudogene 1</td><td>p21.31-22.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031778' method='get'>AL031778</a></td><td>APOBEC2</td><td>novel protein</td><td>p12.1-21.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031781' method='get'>AL031781</a></td><td>QKI</td><td>quaking homolog KH domain RNA binding (mouse)</td><td>q26-27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031782' method='get'>AL031782</a></td><td>COL21A1</td><td>collagen type XXI alpha 1</td><td>p11.2-12.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031963' method='get'>AL031963</a></td><td>RIPK1</td><td>family with sequence similarity 136 member B</td><td>p24.1-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL031983' method='get'>AL031983</a></td><td>UBD</td><td>G protein-coupled receptor 53 pseudogene</td><td>p21.31-22.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL032821' method='get'>AL032821</a></td><td>VNN1</td><td>pseudogene similar to part of hepatic leukemia</td><td>q22.3-23.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL033375' method='get'>AL033375</a></td><td>KLHL32</td><td>kelch-like 32 (Drosophila)</td><td>q16.1-21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL033377' method='get'>AL033377</a></td><td>GPR126</td><td>novel transcript</td><td>q23.1-24.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL033378' method='get'>AL033378</a></td><td>SASH1</td><td>SAM and SH3 domain containing 1</td><td>q24.1-25.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL033379' method='get'>AL033379</a></td><td>GPR63</td><td>eukaryotic translation elongation factor 1 gamma</td><td>q16.1-16.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL033383' method='get'>AL033383</a></td><td>PRPF4B</td><td>PRP4 pre-mRNA processing factor 4 homolog B</td><td>p24.1-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL033384' method='get'>AL033384</a></td><td>LRRC1</td><td>leucine rich repeat containing 1</td><td>p11.2-12.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL033392' method='get'>AL033392</a></td><td>AKAP12</td><td>A kinase (PRKA) anchor protein (gravin) 12</td><td>q24.1-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL033517' method='get'>AL033517</a></td><td>GMDS</td><td>GDP-mannose 46-dehydratase</td><td>p24.1-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL033519' method='get'>AL033519</a></td><td>TEAD3</td><td>TEA domain family member 3</td><td>p21.2-21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL033520' method='get'>AL033520</a></td><td>RP3-349A12.1</td><td>novel protein</td><td>p21.31-22.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL033521' method='get'>AL033521</a></td><td>CDKAL1</td><td>CDK5 regulatory subunit associated protein</td><td>p22.3-23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL033522' method='get'>AL033522</a></td><td>VTA1</td><td>novel transcript</td><td>q24</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL033539' method='get'>AL033539</a></td><td>HDGFL1</td><td>hepatoma derived growth factor-like 1</td><td>p22.1-22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL034343' method='get'>AL034343</a></td><td>MCM3</td><td>minichromosome maintenance complex component 3</td><td>p12.1-21.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL034344' method='get'>AL034344</a></td><td>FOXC1</td><td>forkhead box C1</td><td>p24.1-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL034345' method='get'>AL034345</a></td><td>DNAH8</td><td>dynein axonemal heavy chain 8</td><td>p21.1-21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL034346' method='get'>AL034346</a></td><td>FOXF2</td><td>forkhead box F2</td><td>p25.1-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL034347' method='get'>AL034347</a></td><td>CYB5R4</td><td>novel transcript</td><td>q14</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL034349' method='get'>AL034349</a></td><td>PTPRK</td><td>novel transcript</td><td>q22.2-23.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL034350' method='get'>AL034350</a></td><td>SAMD5</td><td>sterile alpha motif domain containing 5</td><td>q24.1-25.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL034371' method='get'>AL034371</a></td><td>C6orf168</td><td>chromosome 6 open reading frame 168</td><td>q16.1-16.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL034372' method='get'>AL034372</a></td><td>CAP2</td><td>ESD (esterase D/formylglutathione hydrolase)</td><td>p22.3-23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL034373' method='get'>AL034373</a></td><td>RIMS1</td><td>regulating synaptic membrane exocytosis 1</td><td>q12-13</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL034374' method='get'>AL034374</a></td><td>RP3-483K16.1</td><td>novel protein</td><td>p12.1-21.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL034394' method='get'>AL034394</a></td><td>BTNL2</td><td>butyrophilin-like 2 (MHC class II associated)</td><td>p21.2-21.32</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL034452' method='get'>AL034452</a></td><td>COL21A1</td><td>collagen type XXI alpha 1</td><td>p11.2-12.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035086' method='get'>AL035086</a></td><td>MTHFD1L</td><td>methylenetetrahydrofolate dehydrogenase (NADP+</td><td>q23.1-24.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035087' method='get'>AL035087</a></td><td>PRDM13</td><td>PR domain containing 13</td><td>q16.1-21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035090' method='get'>AL035090</a></td><td>CDKAL1</td><td>novel transcript</td><td>p22.1-22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035445' method='get'>AL035445</a></td><td>C6orf10</td><td>heterogeneous nuclear ribonucleoprotein A1</td><td>p21.2-22.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035464' method='get'>AL035464</a></td><td>KIF6</td><td>kinesin family member 6</td><td>p21.1-21.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035465' method='get'>AL035465</a></td><td>PTPRK</td><td>novel transcript</td><td>q22.2-23.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035470' method='get'>AL035470</a></td><td>PTPRK</td><td>protein tyrosine phosphatase receptor type K</td><td>q22.2-23.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035530' method='get'>AL035530</a></td><td>TAGAP</td><td>putative novel transcript</td><td>q25.3-27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035542' method='get'>AL035542</a></td><td>MAS1L</td><td>olfactory receptor family 12 subfamily D</td><td>p21.31-22.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035555' method='get'>AL035555</a></td><td>DNAH8</td><td>dynein axonemal heavy chain 8</td><td>p21.1-21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035587' method='get'>AL035587</a></td><td>PTCRA</td><td>novel transcript</td><td>p12.3-21.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035588' method='get'>AL035588</a></td><td>TFEB</td><td>transcription factor EB</td><td>p12.3-21.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035593' method='get'>AL035593</a></td><td>C6orf170</td><td>chromosome 6 open reading frame 170</td><td>q22.1-22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035594' method='get'>AL035594</a></td><td>PTPRK</td><td>protein tyrosine phosphatase receptor type K</td><td>q22.31-22.33</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035633' method='get'>AL035633</a></td><td>RIMS1</td><td>regulating synaptic membrane exocytosis 1</td><td>q12-13</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035634' method='get'>AL035634</a></td><td>SNX9</td><td>sorting nexin 9</td><td>q25.1-26</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035670' method='get'>AL035670</a></td><td>CYP39A1</td><td>cytochrome P450 family 39 subfamily A</td><td>p11.2-21.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035689' method='get'>AL035689</a></td><td>TRMT11</td><td>tRNA methyltransferase 11 homolog (S.</td><td>q11.1-22.33</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035690' method='get'>AL035690</a></td><td>C6orf64</td><td>chromosome 6 open reading frame 64</td><td>p21.1-21.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035691' method='get'>AL035691</a></td><td>IGF2R</td><td>insulin-like growth factor 2 receptor</td><td>q26-27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035693' method='get'>AL035693</a></td><td>GMDS</td><td>GDP-mannose 46-dehydratase</td><td>p24.1-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035694' method='get'>AL035694</a></td><td>TBX18</td><td>T-box 18</td><td>q14.1-15</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035697' method='get'>AL035697</a></td><td>PARK2</td><td>Parkinson disease (autosomal recessive</td><td>q25.3-27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035698' method='get'>AL035698</a></td><td>GRM1</td><td>glutamate receptor metabotropic 1</td><td>q24.1-25.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035699' method='get'>AL035699</a></td><td>SLC2A12</td><td>solute carrier family 2 (facilitated glucose</td><td>q23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035700' method='get'>AL035700</a></td><td>SH3BGRL2</td><td>SH3 domain binding glutamic acid-rich protein</td><td>q13-15</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL035701' method='get'>AL035701</a></td><td>ENPP5</td><td>actin gamma pseudogene 9</td><td>p11.2-21.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL049543' method='get'>AL049543</a></td><td>dJ1186N24.3</td><td>dJ1186N24.3 (novel zinc finger protein)</td><td>p21.2-22.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL049547' method='get'>AL049547</a></td><td>dJ34F7.2</td><td>dJ34F7.2 (CREB-RP (G13))</td><td>p21.2-21.33</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL049548' method='get'>AL049548</a></td><td>SYNE1</td><td>spectrin repeat containing nuclear envelope 1</td><td>q25.1-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL049553' method='get'>AL049553</a></td><td>MDGA1</td><td>MAM domain containing</td><td>p21.1-21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL049595' method='get'>AL049595</a></td><td>HTR1B</td><td>5-hydroxytryptamine (serotonin) receptor 1B</td><td>q13-14.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL049611' method='get'>AL049611</a></td><td>TRAM2</td><td>novel protein with possible Calmodulin like</td><td>p11.2-12.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL049693' method='get'>AL049693</a></td><td>TFAP2B</td><td>transcription factor AP-2 beta (activating</td><td>p12.1-12.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL049694' method='get'>AL049694</a></td><td>MTHFD1L</td><td>methylenetetrahydrofolate dehydrogenase (NADP+</td><td>q25.1-26</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL049696' method='get'>AL049696</a></td><td>BCKDHB</td><td>branched chain keto acid dehydrogenase E1 beta</td><td>q13-15</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL049697' method='get'>AL049697</a></td><td>SLC35A1</td><td>novel protein</td><td>q14.3-15</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL049698' method='get'>AL049698</a></td><td>MLLT4</td><td>novel transcript</td><td>q26-27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL049699' method='get'>AL049699</a></td><td>ME1</td><td>malic enzyme 1 NADP(+)-dependent cytosolic</td><td>q13-15</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL049820' method='get'>AL049820</a></td><td>RP11-419L10.1</td><td>novel protein</td><td>q25.1-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL049821' method='get'>AL049821</a></td><td>ESR1</td><td>estrogen receptor 1</td><td>q25.1-26</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL049822' method='get'>AL049822</a></td><td>HIST1H2AJ</td><td>histone cluster 1 H2aj</td><td>p21.2-22.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL049843' method='get'>AL049843</a></td><td>PRPH2</td><td>novel protein similar to ATPase H+</td><td>p12.3-21.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL049844' method='get'>AL049844</a></td><td>PHACTR2</td><td>phosphatase and actin regulator 2</td><td>q24.1-24.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL050329' method='get'>AL050329</a></td><td>PHF3</td><td>PHD finger protein 3</td><td>q11.1-12</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL050330' method='get'>AL050330</a></td><td>BTN2A1</td><td>butyrophilin subfamily 2 member A1</td><td>p21.23-22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL050331' method='get'>AL050331</a></td><td>TSPYL1</td><td>novel protein</td><td>q22.1-22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL050333' method='get'>AL050333</a></td><td>RP1-93K22.1</td><td>novel BTB/POZ domain containing protein</td><td>q14.1-15.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL050336' method='get'>AL050336</a></td><td>CLIC5</td><td>chloride intracellular channel 5</td><td>p12.1-21.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL050337' method='get'>AL050337</a></td><td>IL22RA2</td><td>interleukin 22 receptor alpha 2</td><td>q24.1-25.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL050350' method='get'>AL050350</a></td><td>SLC22A16</td><td>solute carrier family 22 (organic</td><td>q21-22.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL078581' method='get'>AL078581</a></td><td>PPIL4</td><td>peptidylprolyl isomerase (cyclophilin)-like 4</td><td>q24.1-25.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL078582' method='get'>AL078582</a></td><td>ESR1</td><td>estrogen receptor 1</td><td>q24.2-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL078584' method='get'>AL078584</a></td><td>FAM65B</td><td>cytochrome c oxidase polypeptide II pseudogene</td><td>p21.32-22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL078591' method='get'>AL078591</a></td><td>KIAA1411</td><td>KIAA1411</td><td>q12-13</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL078593' method='get'>AL078593</a></td><td>PHACTR2</td><td>phosphatase and actin regulator 2</td><td>q23.3-25.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL078594' method='get'>AL078594</a></td><td>HEY2</td><td>novel transcript</td><td>q22.2-22.33</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL078596' method='get'>AL078596</a></td><td>OSTM1</td><td>putative novel transcript</td><td>q21-22.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL078599' method='get'>AL078599</a></td><td>FAM46A</td><td>novel transcript</td><td>q14.1-15</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL078600' method='get'>AL078600</a></td><td>MAN1A1</td><td>mannosidase alpha class 1A member 1</td><td>q21-22.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL078605' method='get'>AL078605</a></td><td>DLL1</td><td>novel protein (KIAA1838)</td><td>q26-27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL080250' method='get'>AL080250</a></td><td>COL12A1</td><td>collagen type XII alpha 1</td><td>q13-14.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL080275' method='get'>AL080275</a></td><td>COL9A1</td><td>collagen type IX alpha 1</td><td>q12-13</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL080276' method='get'>AL080276</a></td><td>FBXO5</td><td>novel pseudogene</td><td>q25-26</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL080317' method='get'>AL080317</a></td><td>KIAA1919</td><td>novel transcript</td><td>q21-22.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL096678' method='get'>AL096678</a></td><td>ANKRD6</td><td>ankyrin repeat domain 6</td><td>q14.2-16.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL096708' method='get'>AL096708</a></td><td>PPP1R14C</td><td>protein phosphatase 1 regulatory (inhibitor)</td><td>q24.3-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL096710' method='get'>AL096710</a></td><td>DST</td><td>dystonin</td><td>p11.2-12.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL096711' method='get'>AL096711</a></td><td>C6orf174</td><td>60S Ribosomal protein L23 (RPL23) pseudogene</td><td>q22.31-23.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL096712' method='get'>AL096712</a></td><td>RNF8</td><td>ring finger protein 8</td><td>p12.1-21.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL096771' method='get'>AL096771</a></td><td>COL12A1</td><td>collagen type XII alpha 1</td><td>q12-14.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL096801' method='get'>AL096801</a></td><td>TNFRSF21</td><td>tumor necrosis factor receptor superfamily</td><td>p12.2-21.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL096814' method='get'>AL096814</a></td><td>TRERF1</td><td>transcriptional regulating factor 1</td><td>p12.1-21.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL096816' method='get'>AL096816</a></td><td>SCML4</td><td>sex comb on midleg-like 4 (Drosophila)</td><td>q16.2-21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL096817' method='get'>AL096817</a></td><td>C6orf162</td><td>heat shock 60kDa protein 1 (chaperonin) (HSPD1)</td><td>q15-16.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL096865' method='get'>AL096865</a></td><td>RUNX2</td><td>runt-related transcription factor 2</td><td>p12.3-21.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL096867' method='get'>AL096867</a></td><td>GRM1</td><td>glutamate receptor metabotropic 1</td><td>q23.1-24.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL096868' method='get'>AL096868</a></td><td>RNGTT</td><td>"RNA guanylyltransferase and 5-phosphatase"</td><td>q14.3-16.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL109612' method='get'>AL109612</a></td><td>EYS</td><td>eyes shut homolog (Drosophila)</td><td>q12-13</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL109615' method='get'>AL109615</a></td><td>MRPL14</td><td>novel transcript</td><td>p12.3-21.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL109897' method='get'>AL109897</a></td><td>SENP6</td><td>SUMO1/sentrin specific peptidase 6</td><td>q13-14.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL109915' method='get'>AL109915</a></td><td>SNAP91</td><td>synaptosomal-associated protein 91kDa homolog</td><td>q13-15</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL109918' method='get'>AL109918</a></td><td>TMEM14A</td><td>HNRNP A/B related protein pseudogene</td><td>p11.2-12.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL109933' method='get'>AL109933</a></td><td>LPA</td><td>lipoprotein Lp(a)</td><td>q25.3-26</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL109939' method='get'>AL109939</a></td><td>RP3-351K20.1</td><td>dactilydin</td><td>q22.1-22.33</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL109942' method='get'>AL109942</a></td><td>MAP3K4</td><td>mitogen-activated protein kinase kinase kinase</td><td>q25.3-26</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL109947' method='get'>AL109947</a></td><td>PPIL6</td><td>peptidylprolyl isomerase (cyclophilin)-like 6</td><td>q16.3-22.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL117344' method='get'>AL117344</a></td><td>ZDHHC14</td><td>novel pseudogene</td><td>q25.2-26</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL117345' method='get'>AL117345</a></td><td>PDE10A</td><td>phosphodiesterase 10A</td><td>q26-27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL117378' method='get'>AL117378</a></td><td>ENPP1</td><td>T-cell activation leucine repeat-rich protein</td><td>q22.33-23.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL118519' method='get'>AL118519</a></td><td>COL19A1</td><td>collagen type XIX alpha 1</td><td>q11.2-13</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121575' method='get'>AL121575</a></td><td>ARG1</td><td>arginase liver</td><td>q22.33-24.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121716' method='get'>AL121716</a></td><td>PGM3</td><td>phosphoglucomutase 3</td><td>q14.1-15</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121787' method='get'>AL121787</a></td><td>BACH2</td><td>BTB and CNC homology 1 basic leucine zipper</td><td>q14.3-16.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121788' method='get'>AL121788</a></td><td>RP1-70A9.1</td><td>novel protein</td><td>q16.3-22.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121833' method='get'>AL121833</a></td><td>GABRR2</td><td>gamma-aminobutyric acid (GABA) receptor rho 2</td><td>q15-16.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121834' method='get'>AL121834</a></td><td>CCDC28A</td><td>coiled-coil domain containing 28A</td><td>q23.1-24.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121837' method='get'>AL121837</a></td><td>MAP3K7</td><td>mitogen-activated protein kinase kinase kinase</td><td>q16.1-16.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121938' method='get'>AL121938</a></td><td>TPD52L1</td><td>tumor protein D52-like 1</td><td>q22.1-23.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121946' method='get'>AL121946</a></td><td>PKHD1</td><td>polycystic kidney and hepatic disease 1</td><td>p12.1-12.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121949' method='get'>AL121949</a></td><td>GLULD1</td><td>glutamate-ammonia ligase (glutamine synthetase)</td><td>q12-13</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121952' method='get'>AL121952</a></td><td>RBM16</td><td>RNA binding motif protein 16</td><td>q25.1-26</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121953' method='get'>AL121953</a></td><td>FAM26E</td><td>family with sequence similarity 26 member E</td><td>q22.1-22.33</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121954' method='get'>AL121954</a></td><td>HSF2</td><td>heat shock transcription factor 2</td><td>q22.31-23.33</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121957' method='get'>AL121957</a></td><td>SOBP</td><td>sine oculis binding protein homolog</td><td>q16.2-21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121959' method='get'>AL121959</a></td><td>EYA4</td><td>novel transcript</td><td>q22.33-23.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121961' method='get'>AL121961</a></td><td>SMAP1</td><td>small ArfGAP 1</td><td>q12-13</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121963' method='get'>AL121963</a></td><td>COL10A1</td><td>collagen type X alpha 1</td><td>q21-22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121964' method='get'>AL121964</a></td><td>MAP3K7</td><td>mitogen-activated protein kinase kinase kinase</td><td>q15-16.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121965' method='get'>AL121965</a></td><td>RP1-121G13.4</td><td>novel RNA helicase family (RNAH) protein</td><td>q16.1-16.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121966' method='get'>AL121966</a></td><td>EPHA7</td><td>EPH receptor A7</td><td>q15-16.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121968' method='get'>AL121968</a></td><td>TCBA1</td><td>T-cell lymphoma breakpoint associated target 1</td><td>q22.2-22.33</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121969' method='get'>AL121969</a></td><td>GSTA3</td><td>glutathione S-transferase A3</td><td>p12.1-12.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121972' method='get'>AL121972</a></td><td>SLC17A5</td><td>novel transcript</td><td>q12-14.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121974' method='get'>AL121974</a></td><td>CRISP3</td><td>cysteine-rich secretory protein 3</td><td>p12-21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121977' method='get'>AL121977</a></td><td>TPBG</td><td>single stranded DNA binding protein pseudogene</td><td>q13-15</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL121978' method='get'>AL121978</a></td><td>FARS2</td><td>putative novel transcript</td><td>p24.1-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL122017' method='get'>AL122017</a></td><td>FAM46A</td><td>family with sequence similarity 46 member A</td><td>q13-14</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL132660' method='get'>AL132660</a></td><td>MARCKS</td><td>putative novel transcript</td><td>q21-22.32</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL132767' method='get'>AL132767</a></td><td>EYS</td><td>eyes shut homolog (Drosophila)</td><td>q12-13</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL132774' method='get'>AL132774</a></td><td>OPRM1</td><td>opioid receptor mu 1</td><td>q25-26.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL132775' method='get'>AL132775</a></td><td>E2F3</td><td>E2F transcription factor 3</td><td>p22.2-23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL132776' method='get'>AL132776</a></td><td>RP3-393D12.1</td><td>novel protein</td><td>q16.1-16.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL132795' method='get'>AL132795</a></td><td>RP3-412I7.3</td><td>novel protein similar to murine radial</td><td>q22.1-22.33</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL132874' method='get'>AL132874</a></td><td>ASF1A</td><td>ASF1 anti-silencing function 1 homolog A (S.</td><td>q22.1-22.33</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL132875' method='get'>AL132875</a></td><td>ELOVL4</td><td>novel pseudogene</td><td>q14.1-15</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL133211' method='get'>AL133211</a></td><td>ORC3L</td><td>putative novel transcript</td><td>q14.3-16.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL133257' method='get'>AL133257</a></td><td>TRDN</td><td>triadin</td><td>q22.1-22.33</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL133260' method='get'>AL133260</a></td><td>MTHFD1L</td><td>methylenetetrahydrofolate dehydrogenase (NADP+</td><td>q24.3-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL133264' method='get'>AL133264</a></td><td>C6orf62</td><td>chromosome 6 open reading frame 62</td><td>p22.1-22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL133268' method='get'>AL133268</a></td><td>CMAH</td><td>novel transcript</td><td>p21.33-22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL133326' method='get'>AL133326</a></td><td>F13A1</td><td>coagulation factor XIII A1 polypeptide</td><td>p24.3-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL133338' method='get'>AL133338</a></td><td>RP1-121G13.4</td><td>novel RNA helicase family (RNAH) protein</td><td>q16.1-16.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL133351' method='get'>AL133351</a></td><td>SERPINB9</td><td>novel transcript</td><td>p24.1-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL133356' method='get'>AL133356</a></td><td>VIP</td><td>vasoactive intestinal peptide</td><td>q24.3-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL133378' method='get'>AL133378</a></td><td>BAI3</td><td>brain-specific angiogenesis inhibitor 3</td><td>q13-14.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL133379' method='get'>AL133379</a></td><td>SLC35F1</td><td>solute carrier family 35 member F1</td><td>q22.1-22.33</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL133386' method='get'>AL133386</a></td><td>BMP5</td><td>bone morphogenetic protein 5</td><td>p11.1-12.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL133388' method='get'>AL133388</a></td><td>COL19A1</td><td>collagen type XIX alpha 1</td><td>q11.1-13</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL133406' method='get'>AL133406</a></td><td>PREP</td><td>prolyl endopeptidase</td><td>q16.3-21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL133510' method='get'>AL133510</a></td><td>ZDHHC14</td><td>zinc finger DHHC-type containing 14</td><td>q25.1-26</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL135839' method='get'>AL135839</a></td><td>SGK1</td><td>serum/glucocorticoid regulated kinase 1</td><td>q22.22-23.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL135911' method='get'>AL135911</a></td><td>C6orf220</td><td>chromosome 6 open reading frame 220</td><td>q16.3-22.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL136079' method='get'>AL136079</a></td><td>SYNE1</td><td>spectrin repeat containing nuclear envelope 1</td><td>q24.3-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL136082' method='get'>AL136082</a></td><td>SNX14</td><td>sorting nexin 14</td><td>q14.3-16.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL136087' method='get'>AL136087</a></td><td>KCNK17</td><td>potassium channel subfamily K member 17</td><td>p21.1-21.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL136093' method='get'>AL136093</a></td><td>MYO6</td><td>myosin VI</td><td>q13-14.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL136096' method='get'>AL136096</a></td><td>SPACA1</td><td>sperm acrosome associated 1</td><td>q15-16.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL136130' method='get'>AL136130</a></td><td>PDE10A</td><td>phosphodiesterase 10A</td><td>q26-27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL136131' method='get'>AL136131</a></td><td>RP1-261G23.6</td><td>novel protein</td><td>p12.2-21.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL136163' method='get'>AL136163</a></td><td>ESNA1</td><td>estrogen nuclear receptor coactivator 1</td><td>q22.1-22.33</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL136223' method='get'>AL136223</a></td><td>UBR2</td><td>ubiquitin protein ligase E3 component n-recognin</td><td>p21.1-21.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL136304' method='get'>AL136304</a></td><td>PPP2R5D</td><td>"protein phosphatase 2 regulatory subunit B"</td><td>p12.3-21.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL136307' method='get'>AL136307</a></td><td>RP3-380B8.2</td><td>Putative novel transcript</td><td>p24.1-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL136445' method='get'>AL136445</a></td><td>COL19A1</td><td>collagen type XIX alpha 1</td><td>q12-13</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL136478' method='get'>AL136478</a></td><td>SLC35F1</td><td>solute carrier family 35 member F1</td><td>q22.33-23.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL138832' method='get'>AL138832</a></td><td>SYNE1</td><td>spectrin repeat containing nuclear envelope 1</td><td>q25.1-26</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL138916' method='get'>AL138916</a></td><td>C6orf103</td><td>chromosome 6 open reading frame 103</td><td>q24.2-25.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL139191' method='get'>AL139191</a></td><td>PREP</td><td>prolyl endopeptidase</td><td>q22.33-23.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL139330' method='get'>AL139330</a></td><td>SYNJ2</td><td>synaptojanin 2</td><td>q25.2-26</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL139392' method='get'>AL139392</a></td><td>SLC29A1</td><td>solute carrier family 29 (nucleoside</td><td>p11.2-21.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL139393' method='get'>AL139393</a></td><td>MAP3K4</td><td>novel transcript</td><td>q26-27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL158051' method='get'>AL158051</a></td><td>BAI3</td><td>brain-specific angiogenesis inhibitor 3</td><td>q12-13</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL160163' method='get'>AL160163</a></td><td>USP49</td><td>putative novel transcript</td><td>p12.3-21.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL354680' method='get'>AL354680</a></td><td>RPEL</td><td>RPEL repeat containing 1</td><td>p23-24.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB201549' method='get'>AB201549</a></td><td>HLA-F</td><td>major histocompatibility complex class I F</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB201550' method='get'>AB201550</a></td><td>HLA-G</td><td>major histocompatibility complex class I G</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202079' method='get'>AB202079</a></td><td>HLA-A</td><td>major histocompatibility complex class I A</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202080' method='get'>AB202080</a></td><td>HCG9</td><td>HLA complex group 9</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202082' method='get'>AB202082</a></td><td>C6orf12</td><td>chromosome 6 open reading frame 12</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202083' method='get'>AB202083</a></td><td>TRIM31</td><td>tripartite motif-containing 31</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202084' method='get'>AB202084</a></td><td>TRIM40</td><td>ring finger protein 40</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202085' method='get'>AB202085</a></td><td>TRIM10</td><td>tripartite motif-containing 10</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202086' method='get'>AB202086</a></td><td>TRIM26</td><td>tripartite motif-containing 26</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202089' method='get'>AB202089</a></td><td>TRIM39</td><td>tripartite motif-containing 39</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202091' method='get'>AB202091</a></td><td>HLA-E</td><td>major histocompatibility complex class I E</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202092' method='get'>AB202092</a></td><td>PRR3</td><td>proline-rich polypeptide 3</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202093' method='get'>AB202093</a></td><td>ABCF1</td><td>ATP-binding cassette sub-family F (GCN20)</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202094' method='get'>AB202094</a></td><td>PPP1R10</td><td>protein phosphatase 1 regulatory subunit 10</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202095' method='get'>AB202095</a></td><td>DHX16</td><td>DEAD/H (Asp-Glu-Ala-Asp/His) box polypeptide 16</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202096' method='get'>AB202096</a></td><td>NRM</td><td>nurim (nuclear envelope membrane protein)</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202097' method='get'>AB202097</a></td><td>MDC1</td><td>mediator of DNA damage checkpoint 1</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202098' method='get'>AB202098</a></td><td>OK/SW-cl.56</td><td>beta 5-tubulin</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202099' method='get'>AB202099</a></td><td>IER3</td><td>immediate early response 3</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202100' method='get'>AB202100</a></td><td>DDR1</td><td>discoidin domain receptor family member 1</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202101' method='get'>AB202101</a></td><td>GTF2H4</td><td>general transcription factor IIH polypeptide 4</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202102' method='get'>AB202102</a></td><td>DPCR1</td><td>diffuse panbronchiolitis critical region</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202103' method='get'>AB202103</a></td><td>C6orf15</td><td>chromosome 6 open reading frame 15</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202104' method='get'>AB202104</a></td><td>C6orf18</td><td>chromosome 6 open reading frame 18</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202105' method='get'>AB202105</a></td><td>TCF19</td><td>transcription factor 19 (SC1)</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202106' method='get'>AB202106</a></td><td>HLA-C</td><td>major histocompatibility complex class I C</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202107' method='get'>AB202107</a></td><td>HLA-B</td><td>major histocompatibility complex class I B</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202108' method='get'>AB202108</a></td><td>MICA</td><td>MHC class I polypeptide-related sequence A</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202111' method='get'>AB202111</a></td><td>MICB</td><td>MHC class I polypeptide-related sequence B</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202112' method='get'>AB202112</a></td><td>NFKBIL1</td><td>nuclear factor of kappa light polypeptide gene</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202113' method='get'>AB202113</a></td><td>LTA</td><td>lymphotoxin alpha (TNF superfamily member 1)</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB202114' method='get'>AB202114</a></td><td>LTB</td><td>lymphotoxin beta (TNF superfamily member 3)</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB470629' method='get'>AB470629</a></td><td>REV3L</td><td>REV3-like catalytic subunit of DNA polymerase</td><td>6q21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB505437' method='get'>AB505437</a></td><td>REV3L</td><td>REV3-like catalytic subunit of DNA polymerase</td><td>6q21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB505438' method='get'>AB505438</a></td><td>REV3L</td><td>REV3-like catalytic subunit of DNA polymerase</td><td>6q21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB505621' method='get'>AB505621</a></td><td>REV3L</td><td>REV3-like catalytic subunit of DNA polymerase</td><td>6q21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB510591' method='get'>AB510591</a></td><td>HLA-DRB4</td><td>MHC Class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AB601768' method='get'>AB601768</a></td><td>TREM2</td><td>triggering receptor expressed on myeloid cells</td><td>6p21.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL355506' method='get'>AL355506</a></td><td>SLC22A3</td><td>solute carrier family 22 (extraneuronal</td><td>q25.3-26</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL355586' method='get'>AL355586</a></td><td>RP11-59I9.1</td><td>novel protein</td><td>q16.3-21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL356415' method='get'>AL356415</a></td><td>STXBP5</td><td>syntaxin binding protein 5 (tomosyn)</td><td>q23.3-25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL359813' method='get'>AL359813</a></td><td>ABCC10</td><td>ATP-binding cassette sub-family C (CFTR/MRP)</td><td>p12.3-21.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL390955' method='get'>AL390955</a></td><td>C6orf35</td><td>chromosome 6 open reading frame 35</td><td>q25.2-26</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL513015' method='get'>AL513015</a></td><td>CDKAL1</td><td>CDK5 regulatory subunit associated protein</td><td>p22.1-22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL589931' method='get'>AL589931</a></td><td>DYNLT1</td><td>dynein light chain Tctex-type 1</td><td>q25.2-26</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL590489' method='get'>AL590489</a></td><td>PDSS2</td><td>prenyl (decaprenyl) diphosphate synthase</td><td>q16.2-21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL591069' method='get'>AL591069</a></td><td>SLC22A3</td><td>solute carrier family 22 (extraneuronal</td><td>q25.2-26</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL591516' method='get'>AL591516</a></td><td>PDSS2</td><td>prenyl (decaprenyl) diphosphate synthase</td><td>q16.3-21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AL591545' method='get'>AL591545</a></td><td>RP11-419L10.1</td><td>novel protein</td><td>q25.2-26</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AM992866' method='get'>AM992866</a></td><td>DDX11L4</td><td>DEAD/H box polypeptide 11 like 4</td><td>6p25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY033075' method='get'>AY033075</a></td><td>HLA-DPBI</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY062031' method='get'>AY062031</a></td><td>HCRTR2</td><td>hypocretin receptor 2</td><td>6p11-q11</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY228704' method='get'>AY228704</a></td><td>FOXC1</td><td>forkhead winged/helix transcription factor</td><td>6p25</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY259125' method='get'>AY259125</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY259126' method='get'>AY259126</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY259127' method='get'>AY259127</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY259128' method='get'>AY259128</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.31</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY291205' method='get'>AY291205</a></td><td>HLA-DRB3</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY297539' method='get'>AY297539</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY297540' method='get'>AY297540</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY299456' method='get'>AY299456</a></td><td>NQO2</td><td>NRH:quinone oxidoreductase 2</td><td>6p25</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY299483' method='get'>AY299483</a></td><td>OPRMI</td><td>mu opioid receptor</td><td>6q25.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY304505' method='get'>AY304505</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY323834' method='get'>AY323834</a></td><td>HLA-Cw</td><td>MHC class I antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY328474' method='get'>AY328474</a></td><td>CDSN</td><td>corneodesmosin</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY328475' method='get'>AY328475</a></td><td>CDSN</td><td>corneodesmosin</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY335522' method='get'>AY335522</a></td><td>HLA-DPB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY349134' method='get'>AY349134</a></td><td>TAP1</td><td>transporter 1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY368204' method='get'>AY368204</a></td><td>TBP</td><td>TATA box binding protein</td><td>6q27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379860' method='get'>AY379860</a></td><td>C4B</td><td>C4B1</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379861' method='get'>AY379861</a></td><td>C4B</td><td>C4B1</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379862' method='get'>AY379862</a></td><td>C4B</td><td>C4B1</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379863' method='get'>AY379863</a></td><td>C4B</td><td>C4B1</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379864' method='get'>AY379864</a></td><td>C4B</td><td>C4B</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379866' method='get'>AY379866</a></td><td>C4B</td><td>C4B5</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379867' method='get'>AY379867</a></td><td>C4B</td><td>C4B5</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379868' method='get'>AY379868</a></td><td>C4B</td><td>C4B</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379870' method='get'>AY379870</a></td><td>C4B</td><td>C4B1</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379871' method='get'>AY379871</a></td><td>C4B</td><td>C4B1</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379872' method='get'>AY379872</a></td><td>C4B</td><td>C4B1</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379873' method='get'>AY379873</a></td><td>C4B</td><td>C4B1</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379874' method='get'>AY379874</a></td><td>C4B</td><td>C4B3</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379875' method='get'>AY379875</a></td><td>C4B</td><td>C4B3</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379876' method='get'>AY379876</a></td><td>C4B</td><td>C4B1</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379877' method='get'>AY379877</a></td><td>C4B</td><td>C4B1</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379878' method='get'>AY379878</a></td><td>C4B</td><td>C4B1</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379879' method='get'>AY379879</a></td><td>C4B</td><td>C4B1</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379880' method='get'>AY379880</a></td><td>C4A</td><td>C4A3</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379881' method='get'>AY379881</a></td><td>C4A</td><td>C4A3</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379882' method='get'>AY379882</a></td><td>C4A</td><td>C4A3</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379883' method='get'>AY379883</a></td><td>C4A</td><td>C4A3</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379884' method='get'>AY379884</a></td><td>C4A</td><td>C4A2</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379885' method='get'>AY379885</a></td><td>C4A</td><td>C4A2</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379886' method='get'>AY379886</a></td><td>C4A</td><td>C4A2</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379887' method='get'>AY379887</a></td><td>C4A</td><td>C4A2</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379888' method='get'>AY379888</a></td><td>C4A</td><td>C4A3</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379889' method='get'>AY379889</a></td><td>C4A</td><td>C4B1</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379890' method='get'>AY379890</a></td><td>C4A</td><td>C4A3</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379891' method='get'>AY379891</a></td><td>C4A</td><td>C4A3</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379892' method='get'>AY379892</a></td><td>C4A</td><td>C4A3</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379893' method='get'>AY379893</a></td><td>C4A</td><td>C4A3</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379894' method='get'>AY379894</a></td><td>C4A</td><td>C4A3</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379895' method='get'>AY379895</a></td><td>C4A</td><td>C4A3</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379896' method='get'>AY379896</a></td><td>C4A</td><td>C4A3</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379897' method='get'>AY379897</a></td><td>C4A</td><td>C4A3</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379898' method='get'>AY379898</a></td><td>C4A</td><td>C4A3</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379899' method='get'>AY379899</a></td><td>C4A</td><td>C4A3</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379900' method='get'>AY379900</a></td><td>C4B</td><td>C4B5</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379901' method='get'>AY379901</a></td><td>C4B</td><td>C4B5</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379902' method='get'>AY379902</a></td><td>C4B</td><td>C4B2</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379903' method='get'>AY379903</a></td><td>C4B</td><td>C4B2</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379904' method='get'>AY379904</a></td><td>C4B</td><td>C4B2</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379905' method='get'>AY379905</a></td><td>C4B</td><td>C4B2</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379906' method='get'>AY379906</a></td><td>C4B</td><td>C4B2</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379907' method='get'>AY379907</a></td><td>C4B</td><td>C4B2</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379908' method='get'>AY379908</a></td><td>C4B</td><td>C4B2</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379909' method='get'>AY379909</a></td><td>C4B</td><td>C4B2</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379910' method='get'>AY379910</a></td><td>C4B</td><td>C4B1</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379911' method='get'>AY379911</a></td><td>C4B</td><td>C4B1</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379912' method='get'>AY379912</a></td><td>C4A</td><td>C4A4</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379913' method='get'>AY379913</a></td><td>C4A</td><td>C4A4</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379914' method='get'>AY379914</a></td><td>C4A</td><td>C4A4</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379915' method='get'>AY379915</a></td><td>C4A</td><td>C4A4</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379916' method='get'>AY379916</a></td><td>C4A</td><td>C4A4</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379917' method='get'>AY379917</a></td><td>C4A</td><td>C4A4</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379918' method='get'>AY379918</a></td><td>C4A</td><td>C4A4</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379919' method='get'>AY379919</a></td><td>C4A</td><td>C4A4</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379920' method='get'>AY379920</a></td><td>C4A</td><td>C4A4</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379921' method='get'>AY379921</a></td><td>C4A</td><td>C4A4</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379922' method='get'>AY379922</a></td><td>C4A</td><td>C4A6</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379923' method='get'>AY379923</a></td><td>C4A</td><td>C4A6</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379924' method='get'>AY379924</a></td><td>C4B</td><td>C4B1</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379925' method='get'>AY379925</a></td><td>C4A</td><td>C4A</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379926' method='get'>AY379926</a></td><td>C4A</td><td>C4A</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379927' method='get'>AY379927</a></td><td>C4A</td><td>C4A91</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379928' method='get'>AY379928</a></td><td>C4A</td><td>C4A3</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379929' method='get'>AY379929</a></td><td>C4A</td><td>C4A3</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379934' method='get'>AY379934</a></td><td>C4A</td><td>C4A3</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379935' method='get'>AY379935</a></td><td>C4A</td><td>C4A2</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379960' method='get'>AY379960</a></td><td>C4A</td><td>C4A6</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379961' method='get'>AY379961</a></td><td>C4B</td><td>C4B1</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379962' method='get'>AY379962</a></td><td>C4A</td><td>C4A4</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379963' method='get'>AY379963</a></td><td>C4A</td><td>C4A4</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379964' method='get'>AY379964</a></td><td>C4A</td><td>C4A4</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379965' method='get'>AY379965</a></td><td>C4A</td><td>C4A4</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379966' method='get'>AY379966</a></td><td>C4A</td><td>C4A4</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379967' method='get'>AY379967</a></td><td>C4B</td><td>C4B5</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379968' method='get'>AY379968</a></td><td>C4B</td><td>C4B2</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379969' method='get'>AY379969</a></td><td>C4B</td><td>C4B2</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379970' method='get'>AY379970</a></td><td>C4B</td><td>C4B2</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY379971' method='get'>AY379971</a></td><td>C4B</td><td>C4B2</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY463003' method='get'>AY463003</a></td><td>PARK2</td><td>Parkin</td><td>6q25.2-q27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY465114' method='get'>AY465114</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY465115' method='get'>AY465115</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY536008' method='get'>AY536008</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY582141' method='get'>AY582141</a></td><td>HLA-DPB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY603356' method='get'>AY603356</a></td><td>HLA-C</td><td>MHC class I antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY603357' method='get'>AY603357</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY604572' method='get'>AY604572</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY604575' method='get'>AY604575</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY604578' method='get'>AY604578</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY604590' method='get'>AY604590</a></td><td>HLA-DRB4</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY604595' method='get'>AY604595</a></td><td>HLA-DRB5</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY650051' method='get'>AY650051</a></td><td>HLA-DPA1</td><td>MHC class II antigen</td><td>6p23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY702306' method='get'>AY702306</a></td><td>TAAR5</td><td>trace amine associated receptor 5</td><td>6q23.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY745246' method='get'>AY745246</a></td><td>PARK2</td><td>parkin</td><td>6q25.2-q27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY745247' method='get'>AY745247</a></td><td>PARK2</td><td>parkin</td><td>6q25.2-q27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY799806' method='get'>AY799806</a></td><td>TNFA</td><td>tumor necrosis factor</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY855160' method='get'>AY855160</a></td><td>HLA-DPB1</td><td>MHC class II antigen</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY855161' method='get'>AY855161</a></td><td>HLA-DPB1</td><td>MHC class II antigen</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY899913' method='get'>AY899913</a></td><td>HLA-DRB5</td><td>MHC class II antigen</td><td>6p23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY904343' method='get'>AY904343</a></td><td>HLA-A</td><td>MHC class I antigen</td><td>6p23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AY947537' method='get'>AY947537</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=BA000025' method='get'>BA000025</a></td><td>C2</td><td>lysosomal sialidase</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=D13174' method='get'>D13174</a></td><td>HLA-DPB1</td><td>HLA-DP antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=D28769' method='get'>D28769</a></td><td>HOX12</td><td>HOX12 protein</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=D83956' method='get'>D83956</a></td><td>HLA-B</td><td>HLA class I antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=D83957' method='get'>D83957</a></td><td>HLA-C</td><td>HLA class I antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=D86566' method='get'>D86566</a></td><td>NOTCH4</td><td>notch related protein</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=D89333' method='get'>D89333</a></td><td>HLA-B</td><td>MHC class I cell surface glycoprotein</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=D89334' method='get'>D89334</a></td><td>HLA-B</td><td>MHC class I cell surface glycoprotein</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=DQ011880' method='get'>DQ011880</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=DQ089022' method='get'>DQ089022</a></td><td>HLA-DPB1</td><td>MHC class II antigen</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=DQ097843' method='get'>DQ097843</a></td><td>CTGF</td><td>connective tissue growth factor</td><td>6q23.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=DQ148298' method='get'>DQ148298</a></td><td>HLA-DPB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=DQ148299' method='get'>DQ148299</a></td><td>HLA-DPB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=DQ148300' method='get'>DQ148300</a></td><td>HLA-DPB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=DQ148301' method='get'>DQ148301</a></td><td>HLA-DPB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=DQ206450' method='get'>DQ206450</a></td><td>DPB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=EF012158' method='get'>EF012158</a></td><td>F13A1</td><td>coagulation factor XIII</td><td>6p25.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=EF059809' method='get'>EF059809</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=EF059810' method='get'>EF059810</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=EF408257' method='get'>EF408257</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=EF541487' method='get'>EF541487</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=EF661662' method='get'>EF661662</a></td><td>CYP21A2</td><td>steroid 21 hydroxylase</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=AC005587' method='get'>AC005587</a></td><td>WUGSC:H_DJ0988G15.1</td><td>phosphodiesterase I beta</td><td>6</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=EU051380' method='get'>EU051380</a></td><td>LCA5</td><td>lebercilin</td><td>6q12-q16.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=EU081886' method='get'>EU081886</a></td><td>FSHA</td><td>follicle-stimulating hormone alpha subunit</td><td>6q12-q21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=EU113296' method='get'>EU113296</a></td><td>LCA5</td><td>lebercilin</td><td>6q12-q16.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=EU113297' method='get'>EU113297</a></td><td>LCA5</td><td>lebercilin</td><td>6q12-q16.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=EU113298' method='get'>EU113298</a></td><td>LCA5</td><td>lebercilin</td><td>6q12-q16.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=EU167536' method='get'>EU167536</a></td><td>HLA-Cw</td><td>MHC class I antigen</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=EU189054' method='get'>EU189054</a></td><td>CYP21A2</td><td>steroid 21 hydroxylase</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=EU236681' method='get'>EU236681</a></td><td>CYP21A2</td><td>steroid 21-hydroxylase</td><td>6p21.3; near HLA class 3 region</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=EU236682' method='get'>EU236682</a></td><td>CYP21A2</td><td>steroid 21-hydroxylase</td><td>6p21.3; near HLA class 3 region</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=EU556740' method='get'>EU556740</a></td><td>CYP21A2</td><td>truncated cytochrome P-450 c21 hydroxylase</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=EU556741' method='get'>EU556741</a></td><td>CYP21A2</td><td>cytochrome P-450 c21 hydroxylase enzyme</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=EU563938' method='get'>EU563938</a></td><td>CYP21A2</td><td>cytochrome P-450 c21 hydroxylase enzyme</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=EU862819' method='get'>EU862819</a></td><td>HLA-A</td><td>MHC class I antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=FJ167389' method='get'>FJ167389</a></td><td>HLA-DRB</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=FJ226006' method='get'>FJ226006</a></td><td>CD24</td><td>CD24</td><td>6q21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=FJ376815' method='get'>FJ376815</a></td><td>CYP21A2</td><td>adrenal enzyme 21 hydroxylase</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=FJ449755' method='get'>FJ449755</a></td><td>HLA-G</td><td>MHC class I antigen</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=FJ538293' method='get'>FJ538293</a></td><td>CYP21A2</td><td>steroid 21-hydroxylase</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=FM211032' method='get'>FM211032</a></td><td>HLA-DPB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=FM211033' method='get'>FM211033</a></td><td>HLA-DPB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=FM211034' method='get'>FM211034</a></td><td>HLA-DPB1</td><td>truncated MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=GQ166779' method='get'>GQ166779</a></td><td>CYP21A2</td><td>cytochrome P450 family 21 subfamily A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=GQ166783' method='get'>GQ166783</a></td><td>CYP21A2</td><td>cytochrome P450 family 21 subfamily A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=GQ166784' method='get'>GQ166784</a></td><td>CYP21A2</td><td>cytochrome P450 family 21 subfamily A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=GQ166785' method='get'>GQ166785</a></td><td>CYP21A2</td><td>cytochrome P450 family 21 subfamily A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=GQ166786' method='get'>GQ166786</a></td><td>CYP21A2</td><td>cytochrome P450 family 21 subfamily A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=GQ166787' method='get'>GQ166787</a></td><td>CYP21A2</td><td>cytochrome P450 family 21 subfamily A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=GQ166788' method='get'>GQ166788</a></td><td>CYP21A2</td><td>cytochrome P450 family 21 subfamily A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=GQ202274' method='get'>GQ202274</a></td><td>HLA</td><td>MHC class I antigen</td><td>6q21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=GQ202275' method='get'>GQ202275</a></td><td>HLA</td><td>MHC class I antigen</td><td>6q21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=GQ202277' method='get'>GQ202277</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6q21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=HM231277' method='get'>HM231277</a></td><td>HLA-E</td><td>MHC class I antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=HM347430' method='get'>HM347430</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=HM347431' method='get'>HM347431</a></td><td>HLA-B</td><td>MHC class I antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=HQ202739' method='get'>HQ202739</a></td><td>CD109</td><td>CD109 antigen</td><td>6q13</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=JQ013008' method='get'>JQ013008</a></td><td>HLA-G</td><td>MHC class I antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=JQ744563' method='get'>JQ744563</a></td><td>HLA-E</td><td>MHC class Ib antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=L17310' method='get'>L17310</a></td><td>HLA-DPB1</td><td>MHC class II HLA-DP-beta-1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=L17311' method='get'>L17311</a></td><td>HLA-DPB1</td><td>MHC class II HLA-DP-beta-1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=L17313' method='get'>L17313</a></td><td>HLA-DPB1</td><td>MHC class II HLA-DP-beta-1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=L17314' method='get'>L17314</a></td><td>HLA-DPB1</td><td>MHC class II HLA-DP-beta-1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=L22076' method='get'>L22076</a></td><td>HLA-DPB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=L22077' method='get'>L22077</a></td><td>HLA-DPB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=L23399' method='get'>L23399</a></td><td>HLA-DPB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=L29082' method='get'>L29082</a></td><td>HLA-DRB1-0811</td><td>MHC class II HLA antigen</td><td>short arm of chromosome 6</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=L42280' method='get'>L42280</a></td><td>HLA-B*3908</td><td>lymphocyte antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=L42282' method='get'>L42282</a></td><td>HLA-B*44032</td><td>lymphocyte antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=L42283' method='get'>L42283</a></td><td>HLA-B*44031</td><td>lymphocyte antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=L76640' method='get'>L76640</a></td><td>HLA-B39061</td><td>MHC class I antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=M12792' method='get'>M12792</a></td><td>CYP21</td><td>steroid 21-hydroxylase</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=M30580' method='get'>M30580</a></td><td>HLA-A</td><td>HLA-Aw33.1 precursor</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=M32137' method='get'>M32137</a></td><td>COL9A1</td><td>alpha-1 type IX collagen</td><td>6q12-q14</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=M34534' method='get'>M34534</a></td><td>COL9A1</td><td>alpha-1 type IX collagen</td><td>6q12-q14</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=M95529' method='get'>M95529</a></td><td>CLPS</td><td>colipase</td><td>6pter-p21.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U04877' method='get'>U04877</a></td><td>HLA-DMA</td><td>HLA DMA</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U04878' method='get'>U04878</a></td><td>HLA-DMA</td><td>HLA DMA</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U19247' method='get'>U19247</a></td><td>interferon-gamma receptor alpha chain gene</td><td>interferon-gamma receptor alpha chain</td><td>6q23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U22311' method='get'>U22311</a></td><td>HLA-DPB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U22312' method='get'>U22312</a></td><td>HLA-DPB1-Cam2</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U22313' method='get'>U22313</a></td><td>HLA-DPB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U25442' method='get'>U25442</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U25638' method='get'>U25638</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U25639' method='get'>U25639</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U25826' method='get'>U25826</a></td><td>SC1</td><td>transcription factor SC1</td><td>6p23.1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U29534' method='get'>U29534</a></td><td>HLA-DPB1</td><td>MHC class II antigen HLA-DP-beta</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U30518' method='get'>U30518</a></td><td>TPMT</td><td>thiopurine methyltransferase</td><td>6p22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U37116' method='get'>U37116</a></td><td>DDX13</td><td>helicase-like protein</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U37117' method='get'>U37117</a></td><td>RD</td><td>nuclear protein</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U38520' method='get'>U38520</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U39086' method='get'>U39086</a></td><td>HLA-DQB1</td><td>MHC class II antigen HLA-DQB</td><td>6p23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U39809' method='get'>U39809</a></td><td>HLA-DQB1</td><td>MHC class II HLA-DQ-beta-1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U39821' method='get'>U39821</a></td><td>HLA-DQB1</td><td>MHC class antigen II HLA-DQ-beta-1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U39822' method='get'>U39822</a></td><td>HLA-DQB1</td><td>MHC class II antigen HLA-DQ-beta-1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U39825' method='get'>U39825</a></td><td>HLA-DQB1</td><td>MHC class II HLA-DQ-beta-1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U41634' method='get'>U41634</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U42625' method='get'>U42625</a></td><td>TNFA</td><td>tumor necrosis factor alpha</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U45984' method='get'>U45984</a></td><td>CMKBR6</td><td>CCR6 chemokine receptor</td><td>6q27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U50061' method='get'>U50061</a></td><td>HLA-DRB4</td><td>MHC class II antigen HLA-DRB4*0201N</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U52693' method='get'>U52693</a></td><td>Creb-rp</td><td>adrenal Creb-rp</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U53588' method='get'>U53588</a></td><td>HCG V</td><td>HCG V</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U56602' method='get'>U56602</a></td><td>PXAAA1</td><td>Pxaaa1p</td><td>6p11-6p22</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U56940' method='get'>U56940</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U56941' method='get'>U56941</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U56942' method='get'>U56942</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U56943' method='get'>U56943</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U56944' method='get'>U56944</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U56945' method='get'>U56945</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U56946' method='get'>U56946</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U56947' method='get'>U56947</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U56948' method='get'>U56948</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U56949' method='get'>U56949</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U56950' method='get'>U56950</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U56951' method='get'>U56951</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U56952' method='get'>U56952</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U56953' method='get'>U56953</a></td><td>MICA</td><td>MHC CLASS I CHAIN RELATED-GENE A 014</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U56954' method='get'>U56954</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U56955' method='get'>U56955</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U60215' method='get'>U60215</a></td><td>HLA-C</td><td>MHC class I HLA-C heavy chain</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U60216' method='get'>U60216</a></td><td>HLA-C</td><td>MHC class I HLA-C heavy chain</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U60217' method='get'>U60217</a></td><td>HLA-C</td><td>MHC class I protein HLA-C heavy chain</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U60218' method='get'>U60218</a></td><td>HLA-C</td><td>MHC class I protein HLA-C heavy chain</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U60321' method='get'>U60321</a></td><td>HLA-C</td><td>MHC class I protein HLA-C heavy chain</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U60322' method='get'>U60322</a></td><td>HLA-C</td><td>MHC class I protein HLA-C heavy chain</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U60323' method='get'>U60323</a></td><td>HLA-C</td><td>MHC class I protein HLA-C heavy chain</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U60324' method='get'>U60324</a></td><td>HLA-C</td><td>MHC class I protein HLA-C heavy chain</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U60422' method='get'>U60422</a></td><td>HLA-C</td><td>MHC class I protein HLA-C heavy chain</td><td>6p21-3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U60423' method='get'>U60423</a></td><td>HLA-C</td><td>MHC class I protein HLA-C heavy chain</td><td>6p21-3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U61273' method='get'>U61273</a></td><td>HLA-C</td><td>MHC class I protein HLA-C heavy chain</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U61274' method='get'>U61274</a></td><td>HLA-C</td><td>MHC class I protein HLA-C heavy chain</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U65402' method='get'>U65402</a></td><td>GPR31</td><td>seven transmembrane G-coupled receptor</td><td>6q27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U65416' method='get'>U65416</a></td><td>MICB</td><td>MHC class I molecule</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U66796' method='get'>U66796</a></td><td>LAMA2</td><td>laminin alpha 2 chain</td><td>6q2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U68032' method='get'>U68032</a></td><td>STRL22</td><td>G protein-coupled receptor</td><td>6q27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U68391' method='get'>U68391</a></td><td>HLA-DRB1</td><td>MHC class II</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U69623' method='get'>U69623</a></td><td>PERB11.1</td><td>PERB11.1 protein</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U69628' method='get'>U69628</a></td><td>PERB11.1</td><td>PERB11.1 protein</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U69630' method='get'>U69630</a></td><td>PERB11.1</td><td>PERB11.1 protein</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U69631' method='get'>U69631</a></td><td>PERB11.1</td><td>PERB11.1 protein</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U69964' method='get'>U69964</a></td><td>PERB11.1</td><td>MHC class I-like molecule PERB11.1-13.1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U69965' method='get'>U69965</a></td><td>PERB11.1</td><td>MHC class I-like molecule PERB11.1-18.2</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U69966' method='get'>U69966</a></td><td>PERB11.1</td><td>MHC class I-like molecule PERB11.1-35.1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U69968' method='get'>U69968</a></td><td>PERB11.1</td><td>MHC class I-like molecule PERB11.1-44.3</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U69969' method='get'>U69969</a></td><td>PERB11.1</td><td>MHC class I-like molecule PERB11.1-46.1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U69970' method='get'>U69970</a></td><td>PERB11.1</td><td>MHC class I-like molecule PERB11.1-47.1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U69971' method='get'>U69971</a></td><td>PERB11.1</td><td>MHC class I-like molecule PERB11.1-52.1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U69972' method='get'>U69972</a></td><td>PERB11.1</td><td>MHC class I-like molecule PERB11.1-54.1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U69973' method='get'>U69973</a></td><td>PERB11.1</td><td>MHC class I-like molecule PERB11.1-57.1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U69974' method='get'>U69974</a></td><td>PERB11.1</td><td>MHC class I-like molecule PERB11.1-62.1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U69975' method='get'>U69975</a></td><td>PERB11.1</td><td>MHC class I-like molecule PERB11.1-65.1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U69976' method='get'>U69976</a></td><td>PERB11.1</td><td>MHC class I-like molecule PERB11.1-7.1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U69977' method='get'>U69977</a></td><td>PERB11.1</td><td>MHC class I-like molecule PERB11.1-8.1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U69978' method='get'>U69978</a></td><td>PERB11.2</td><td>MHC class I-like molecule PERB11.2-IMX</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U70545' method='get'>U70545</a></td><td>HLA DRB4</td><td>HLA class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U70863' method='get'>U70863</a></td><td>HLA-A2</td><td>MHC class I antigen</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U72064' method='get'>U72064</a></td><td>DRB1</td><td>HLA class II DRB1 antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U72264' method='get'>U72264</a></td><td>HLA-DRB1</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U73113' method='get'>U73113</a></td><td>HLA-B*5603</td><td>MHC cell surface glycoprotein</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U73304' method='get'>U73304</a></td><td>CNR1</td><td>CB1 cannabinoid receptor</td><td>6q14-15</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U77344' method='get'>U77344</a></td><td>HLA-DQB1</td><td>MHC class II antigen DQB1</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U80914' method='get'>U80914</a></td><td>HLA-H</td><td>hereditary haemochromatosis protein</td><td>6p22</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U81568' method='get'>U81568</a></td><td>TPMT</td><td>thiopurine methyltransferase</td><td>6p22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U81569' method='get'>U81569</a></td><td>TPMT</td><td>thiopurine methyltransferase</td><td>6p22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U81570' method='get'>U81570</a></td><td>TPMT</td><td>thiopurine methyltransferase</td><td>6p22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U81571' method='get'>U81571</a></td><td>TPMT</td><td>thiopurine methyltransferase</td><td>6p22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U81572' method='get'>U81572</a></td><td>TPMT</td><td>thiopurine methyltransferase</td><td>6p22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U81573' method='get'>U81573</a></td><td>TPMT</td><td>thiopurine methyltransferase</td><td>6p22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U82403' method='get'>U82403</a></td><td>HLA-DR beta</td><td>MHC class II HLA-DR-beta</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U83580' method='get'>U83580</a></td><td>HLA-B</td><td>MHC class I HLA-B</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U83581' method='get'>U83581</a></td><td>HLA-B</td><td>MHC class I HLA-B</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U85035' method='get'>U85035</a></td><td>HLA-DQ</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U89335' method='get'>U89335</a></td><td>NOTCH4</td><td>notch4</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U89336' method='get'>U89336</a></td><td>NOTCH4</td><td>G18</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U89337' method='get'>U89337</a></td><td>CREB-RP</td><td>NG7</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U90563' method='get'>U90563</a></td><td>HLA-B</td><td>MHC class I antigen HLA-B heavy chain</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U90564' method='get'>U90564</a></td><td>HLA-B</td><td>MHC class I antigen HLA-B heavy chain</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U90565' method='get'>U90565</a></td><td>HLA-B</td><td>MHC class I antigen HLA-B heavy chain</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U90566' method='get'>U90566</a></td><td>HLA-B</td><td>MHC class I antigen HLA-B heavy chain</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=U92032' method='get'>U92032</a></td><td>HLA-DQB</td><td>MHC class II DQ-beta</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X12662' method='get'>X12662</a></td><td>arg</td><td>arginase</td><td>q23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X58898' method='get'>X58898</a></td><td>CYP21</td><td>P450c21</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X58899' method='get'>X58899</a></td><td>CYP21</td><td>steroid 21-monooxygenase</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X58900' method='get'>X58900</a></td><td>CYP21</td><td>steroid 21-monooxygenase</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X58902' method='get'>X58902</a></td><td>CYP21</td><td>steroid 21-monooxygenase</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X58904' method='get'>X58904</a></td><td>CYP21</td><td>steroid 21-monooxygenase</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X58906' method='get'>X58906</a></td><td>CYP21</td><td>steroid 21-monooxygenase</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X58907' method='get'>X58907</a></td><td>CYP21</td><td>steroid 21-monooxygenase</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X58908' method='get'>X58908</a></td><td>CYP21A/CYP21B fusion gene</td><td>steroid 21-monooxygenase</td><td>6p</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X60382' method='get'>X60382</a></td><td>COL10A1</td><td>collagen subunit (alpha-1 (X)) 3</td><td>6q 21-22-3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X64545' method='get'>X64545</a></td><td>HLA-DRB2</td><td>MHC class II antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X65120' method='get'>X65120</a></td><td>COL10A1</td><td>alpha1(X)collagen</td><td>q21-q22</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X65585' method='get'>X65585</a></td><td>HLA-DRB</td><td>MHC class II antigen</td><td>6p21.3; HGML_LOCUS_UID=LV0063D</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X65586' method='get'>X65586</a></td><td>HLA-DRB</td><td>MHC class II antigen</td><td>6p21.3; HGML_LOCUS_UID=LV0063D</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X65727' method='get'>X65727</a></td><td>GSTalpha locus</td><td>glutathione S-transferase</td><td>p12</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X68272' method='get'>X68272</a></td><td>HLA-DBR1</td><td>HLA-DRbeta-chain</td><td>locus HLA-DBR1</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X77331' method='get'>X77331</a></td><td>C2</td><td>complement component C2</td><td>p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X80700' method='get'>X80700</a></td><td>G17</td><td>PBX2</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X83699' method='get'>X83699</a></td><td>IGF2R</td><td>insulin-like growth factor type II receptor</td><td>6q25-27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X83700' method='get'>X83700</a></td><td>IGF2R</td><td>insulin-like growth factor type II receptor</td><td>6q25-27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X83701' method='get'>X83701</a></td><td>IGF2R</td><td>insulin-like growth factor II receptor</td><td>6q25-27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X83702' method='get'>X83702</a></td><td>IGF2R</td><td>insulin-like growth factor type II receptor</td><td>6q25-27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X87200' method='get'>X87200</a></td><td>DRB1*1116</td><td>Beta 1 domain of MHC Class II HLA DRB1 molecule</td><td>p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X89902' method='get'>X89902</a></td><td>PPP1R11</td><td>protein phosphatase 1 regulatory (inhibitor)</td><td>p21.3 mu</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X91875' method='get'>X91875</a></td><td>igf2R</td><td>insulin-like growth factor type 2 receptor</td><td>q26</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X92841' method='get'>X92841</a></td><td>MICA</td><td>MHC class I chain-related protein A</td><td>p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X94480' method='get'>X94480</a></td><td>HLA-B*18 variant</td><td>MHC type I antigen</td><td>short arm</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X94481' method='get'>X94481</a></td><td>HLA-B*5101 variant</td><td>MHC type I antigen</td><td>short arm</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X94482' method='get'>X94482</a></td><td>HLA-B*5501 variant</td><td>MHC type I antigen</td><td>short arm</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X95235' method='get'>X95235</a></td><td>TFAP2</td><td>transcription factor AP2</td><td>p23-24</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X95760' method='get'>X95760</a></td><td>HLA-DRB3</td><td>MHC Class II HLA-DRB3</td><td>p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X96670' method='get'>X96670</a></td><td>RING3</td><td>kinase</td><td>p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X98378' method='get'>X98378</a></td><td>SKI2W</td><td>SKI2W protein</td><td>p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=X99771' method='get'>X99771</a></td><td>HLA-DRB3</td><td>HLA-DRB3 major histocompatibility complex class</td><td>codon 10 to 88 of HLA-DRB3 gene</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Y08063' method='get'>Y08063</a></td><td>HLA-DRB3</td><td>HLA-DRB3 major histocompatability complex class</td><td>codon 7 to 88</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Y08862' method='get'>Y08862</a></td><td>MHC-DPB1*6001</td><td>major histocompatability complex</td><td>q21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Y09342' method='get'>Y09342</a></td><td>HLA-DRB5</td><td>human leucocyte antigen</td><td>6p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Y13566' method='get'>Y13566</a></td><td>HLA-B</td><td>alpha 1 domain</td><td>6p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Y14240' method='get'>Y14240</a></td><td>LAMA4</td><td>laminin alpha 4</td><td>q21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Y14768' method='get'>Y14768</a></td><td>AIF1</td><td>allograft inflamatory factor-1</td><td>p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Y16736' method='get'>Y16736</a></td><td>dif-2</td><td>DIF-2 protein</td><td>p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Y17847' method='get'>Y17847</a></td><td>EYA4</td><td>EYA4 protein</td><td>q23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z84474' method='get'>Z84474</a></td><td>HCG14</td><td>ribosomal protein L13 pseudogene</td><td>p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z84476' method='get'>Z84476</a></td><td>TRIM27</td><td>ret finger protein</td><td>p21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z84480' method='get'>Z84480</a></td><td>CDC2L6</td><td>cell division cycle 2-like 6 (CDK8-like)</td><td>q21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z84484' method='get'>Z84484</a></td><td>PNPLA1</td><td>patatin-like phospholipase domain containing 1</td><td>p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z84485' method='get'>Z84485</a></td><td>PNPLA1</td><td>patatin-like phospholipase domain containing 1</td><td>p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z84486' method='get'>Z84486</a></td><td>SGK1</td><td>serum/glucocorticoid regulated kinase 1</td><td>q23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z84488' method='get'>Z84488</a></td><td>SART2</td><td>novel transcript</td><td>q21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z84489' method='get'>Z84489</a></td><td>HLA-DQA1</td><td>major histocompatibility complex class II DQ</td><td>p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z84814' method='get'>Z84814</a></td><td>HLA-DRB3</td><td>major histocompatibility complex class II DR</td><td>p21.1-21.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z85986' method='get'>Z85986</a></td><td>SFRS3</td><td>splicing factor arginine/serine-rich 3</td><td>p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z85996' method='get'>Z85996</a></td><td>CDKN1A</td><td>cyclin-dependent kinase inhibitor 1A (p21</td><td>p21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z85999' method='get'>Z85999</a></td><td>DCBLD1</td><td>discoidin CUB and LCCL domain containing 1</td><td>q21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z86062' method='get'>Z86062</a></td><td>SIM1</td><td>single-minded homolog 1 (Drosophila)</td><td>q16</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z93017' method='get'>Z93017</a></td><td>BAK1</td><td>BCL2-antagonist/killer 1</td><td>p21.2-21.33</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z93020' method='get'>Z93020</a></td><td>RANBP9</td><td>RAN binding protein 9</td><td>p23</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z93021' method='get'>Z93021</a></td><td>KHDRBS2</td><td>KH domain containing RNA binding signal</td><td>q12</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z94721' method='get'>Z94721</a></td><td>FGFR1OP</td><td>FGFR1 oncogene partner</td><td>q27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z95152' method='get'>Z95152</a></td><td>MAPK13</td><td>mitogen-activated protein kinase 13</td><td>p21.1-21.33</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z95326' method='get'>Z95326</a></td><td>SLC35F1</td><td>solute carrier family 35 member F1</td><td>q22.1-22.33</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z95329' method='get'>Z95329</a></td><td>BVES</td><td>blood vessel epicardial substance</td><td>q21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z97832' method='get'>Z97832</a></td><td>ZNF76</td><td>novel EGF-like and CUB domain protein similar to</td><td>p21.1-21.33</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z97989' method='get'>Z97989</a></td><td>TRAF3IP2</td><td>TRAF3 interacting protein 2</td><td>q21-22</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z98036' method='get'>Z98036</a></td><td>NUDT3</td><td>novel transcript</td><td>p21.2-21.33</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z98049' method='get'>Z98049</a></td><td>RPS6KA2</td><td>ribosomal protein S6 kinase 90kDa polypeptide</td><td>q26-27</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z98050' method='get'>Z98050</a></td><td>HIVEP1</td><td>human immunodeficiency virus type I enhancer</td><td>p24</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z98172' method='get'>Z98172</a></td><td>NUS1</td><td>nuclear undecaprenyl pyrophosphate synthase 1</td><td>q21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z98200' method='get'>Z98200</a></td><td>OSTM1</td><td>putative novel transcript</td><td>q16-21</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z98742' method='get'>Z98742</a></td><td>LACE1</td><td>lactation elevated 1</td><td>q21-22</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z98744' method='get'>Z98744</a></td><td>HIST1H2AK</td><td>histone 1 H2ak</td><td>p21.3-22.3</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z98745' method='get'>Z98745</a></td><td>dJ29K1.2</td><td>dJ29K1.2 (KIAA0426 (C2H2 type zinc finger</td><td>p21.3-22.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z98880' method='get'>Z98880</a></td><td>ROS1</td><td>v-ros UR2 sarcoma virus oncogene homolog 1</td><td>q22</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z99128' method='get'>Z99128</a></td><td>SRPK1</td><td>SFRS protein kinase 1</td><td>p21.1-22.2</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z99129' method='get'>Z99129</a></td><td>HSF2</td><td>heat shock transcription factor 2</td><td>q22</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z99495' method='get'>Z99495</a></td><td>RPEL</td><td>RPEL repeat containing 1</td><td>p24</td></tr>
<tr>
<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession=Z99496' method='get'>Z99496</a></td><td>C6orf204</td><td>synovial sarcoma X breakpoint (SSX) pseudogene</td><td>q22.1-22.33</td></tr>
</table>
</body>
</html>
    </div> <!-- content -->
  </body>
</html>

    """

This CGI script  displays a summary table when Genbank Accession, Gene Identifier, Protein product
or chromosomal location is searched on search html page. This CGI script also displays summary table of all 
the genes in chromosome 6, when on the gene summary html page, with Genbank Accession, Gene Identifier,
Protein product and chromosomal location being the column headers. 

As Genbank Accession is unique, one entry in a table will be returned whereas for Gene Identifier,Protein
product or chromosomal location one or more entries in a table can be returned. This CGI script also allows
users to select any Genbank Accession cell which will take user to detail page of that gene; detail page
will display Genbank Accession, Gene Identifier, Protein Product, Amino Acid sequence, Chromosomal Location,
Coding region-CDS,DNA sequences-with coding regions highlighted and star indicating restriction enzyme and 
codon frequency.
============
Program: List all CGI script
Author: Maham Ahmad
Date Created: 19 April 2020

'''


import cgi
#print ("Content-Type: text/html\n")

# Add the bl sub-directory to the module path
# and the directory above to import the config file

import sys
sys.path.insert(0, "/d/user6/az001/bl/")
sys.path.insert(0, "/d/user6/az001/db/") 

import blapi      # Import the Business Logic API
import htmlutils  # Import HTML utilities
import config     # Import configuration information (e.g. URLs)

# Useful debugging output
#import cgitb
#cgitb.enable()

# Grab the content of the form
form = cgi.FieldStorage()

accession = form.getvalue("accession")
gene_id = form.getvalue("gene_id")
product = form.getvalue("product")
location = form.getvalue("location")
entries = blapi.getAllEntries(accession = accession, gene_id = gene_id, product = product,location = location)
html    = htmlutils.header()


#Table Design

html += "<html>\n"
html += "<head>\n"
html += "<title>Gene Summary Table</title>\n"
html += "</head>"
html += "<body>\n"
html += "<h1>Gene Summary Table:</h1>\n"
html += "<style>"
html += "table{"
html += "width:100%;"
html += "}"
html += "table, {"
html += "border: 1px solid black;"
html += "border-collapse: collapse;"
html += "}"
html += "th, td {"
html += "border: 1px white;"
html += "padding: 15px;"
html += "text-align: left;"
html += "}"
html += "table#t01 tr:nth-child(even){"
html += "background-color: #eee;"
html += "}"
html += "table#t01 tr:nth-child(odd){"
html += "background-color: #fff;"
html += "}"
html += "table#t01 th {"
html += "background-color: black;"
html += "color: white;"
html += "}"
html += "</style>"


#Gene summary table page: Genbank Accession, Gene Identifier, Protein product and chromosomal location with Genbank Accession linking to detail page of gene

html += "<table id =\"t01\">"
html += "<tr><th>Genbank Accession</th>"
html += "<th>Gene Identifier</th>"
html += "<th>Protein Product</th>"
html += "<th>Chromosomal Location</th>"
html += "</tr>\n"
for _ in entries:	
	html += "<tr>\n"
	html += "<td><a href='http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/az001/search.py?accession={}' method='get'>".format(_['accession'])+ _['accession']+ "</a></td>" 
	html += "<td>"+_['gene_id'] + "</td>"	
	html += "<td>"+_['product'] + "</td>"
	html += "<td>"+_['location'] + "</td>"
	html += "</tr>\n"

	
html += "</table>\n"

html += "</body>\n"
html += "</html>\n"
html += htmlutils.footer()

#print(html)   


    print(MSG, file=file)
    
if __name__ == "__main__":
   import doctest
   doctest.testmod()    