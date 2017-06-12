import os
import pandas as pd
import sys

MIN_NUM_ARGS = 2

def printUsage():
    print "Usage: xlsx2csv.py <xlsx-files-folderpath>" 

def xlsx2csv(input_file_path):
	print "Processing file:" , input_file_path
	output_file_path = input_file_path.replace('.xlsx','.csv')
	data = pd.read_excel(input_file_path,encoding='utf-8')
	if ('Unnamed: 0' in data.columns):
		data = data.drop('Unnamed: 0',1)
	data.to_csv(output_file_path,encoding='utf-8',index=False)

if len(sys.argv) < MIN_NUM_ARGS: 
    print "Wrong Usage!"
    printUsage()
    exit(1)


directory = sys.argv[1]
for file in os.listdir(directory):
	if file.endswith('.xlsx'):
		xlsx2csv(os.path.join(directory,file))	
