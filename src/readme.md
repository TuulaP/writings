# pick-textfromxml

The purpose of the script is to extract just the raw text from the custom XML of the National Library of Finland.

At the end the extracted text is written to the stdout.

Input parameter: filename  (should be in the custom export XML format of #NatLibfi .

One example version of the expected data can be found from ../data directory.

##Example of use:

python pick_textfromxml.py -i ..\data\1457-4721_1871-07-03_77_001.xml 
