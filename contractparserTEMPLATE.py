import pandas as pd
import numpy as np
import os
from pathlib import Path
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 


#Modify this line with path where all your excel docs are
path = r'PATH TO EXCEL DOCS'
filesList = []
#make new directory to store processed files, need to check if folder exists or not
Path("PATH FROM LINE 10/processed data").mkdir(parents=True, exist_ok=True)

for root, dirs, files in os.walk(path):
    for file in files: 
        filesList.append(os.path.join(root,file))
 

#for each file in folder: 
for filePath in filesList:
    try: 
        #isolate filename for later
        fileName = os.path.basename(filePath)
        file = os.path.splitext(fileName)
        newName = file[0]
        extension = file[1]
        print(extension)
        print(newName)
    
        #read in excel doc
        #df = pd.read_excel(filePath)
        if extension == '.xlsx':
            df = pd.read_excel(filePath)
        elif extension == '.csv':
            df = pd.read_csv(filePath)

        #get names of columns: 
        columnNames = df.columns.values.tolist()
        naicsColumn = ""
        
        #SEARCH FOR SPECIFIC COLUMN 
        #check if DESIRED substring exists in column name list: 
        for name in columnNames: 
            if ('ENTER SUBSTRING HERE' in name):
                naicsColumn = name
        print("selectd column: ", naicsColumn)
        
        #ensure that the selected column is converted to str data type: 
        df[naicsColumn] = df[naicsColumn].astype(str)
    

        #MODIFY WITH DESIRED FILTERS- I used NAICS codes, but can be anything. They must be strings
        options = ['541512', '541511']
        #iterate thru each option in data, then the str.contains argument adds more rows. 
        newDf = pd.DataFrame()
        for code in options:
            subSet = df[df[naicsColumn].str.contains(code)]
            newDf = newDf.append(subSet)
        

        #next- export result to excel/csv file using isolated filename 
        newDf.to_csv( cwd + '/' + newName + 'processed.csv', index=False)
    except:
        pass
    