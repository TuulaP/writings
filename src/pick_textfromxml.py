#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" ##The purpose of the script is to extract just the raw text from the custom XML of the National Library of Finland.
At the end the extracted text is written to the stdout.

Input parameter: filename  (should be in the custom export XML format of #NatLibfi .
One example version of the expected data can be found from ../data directory.

##Example of use:

python pick_textfromxml.py -i ..\\data\\1457-4721_1871-07-03_77_001.xml 

"""

import xml.etree.ElementTree as ET


def getALTOContent (filename,myxpath=".//{kk-ocr}text"):
	""" 
	Function to return the text of ALTO file 
	2nd parameter can be used to define own XPATH location.
	"""
		
    #without this namespace changes to ns0.
    #TODO: preferably should read these from the file and do registration dynamicallly

	namespaces= {'mods':"http://www.loc.gov/mods/v3",
                 'mets':"http://www.loc.gov/METS/",
                 'lc':"http://www.loc.gov/mets/profiles",
                 'pm':"http://www.loc.gov/mets/profiles/printMaterial",
                 'xsi':"http://www.w3.org/2001/XMLSchema-instance",
                 'rights':"http://www.loc.gov/rights/" ,
                 'xlink':"http://www.w3.org/TR/xlink",
                 'mix':"http://www.loc.gov/mix/",
				 }

	for prefix, uri in namespaces.items():
		ET.register_namespace(prefix, uri)

    #reads in the file
	et = ET.parse(filename)
	item = et.findall(myxpath)  # gets the desired element

	return item[0].text




if __name__ == "__main__":


    from optparse import OptionParser
    parser = OptionParser()

    parser.add_option("-i", "--input", type="string", dest="input",
                  help="Input file name", metavar="input")


    (options, args) = parser.parse_args()
    inputfile = options.input

    if (not inputfile or len(inputfile)==0 ):
        print("Please give the input file with -i parameter")
        sys.exit()


    infiletext = getALTOContent(inputfile)

    #print "From file %s, got \n%s" % (inputfile, infiletext)
    print infiletext

	