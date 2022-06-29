# NAICS-Filter
This tool filters excel files on a massive scale. Specifically, I used it for filtering government spreadsheets for contract opportunities that match my company's NAICS codes.
However, the template I uploaded can be modified to search and filter for anything. 

INSTRUCTIONS: 
EXECUTION: 
The program must be run in the same folder as the excel docs. 

EDITS: 
LINE 10 & 13: add path to folder that contains all of the excel docs you want to filter
LINE 45: edit to desired substring- the program will search each spreadsheet for a column with a name that includes the substring
LINE 54: add any search criteria as a list. The program batches by substring, so criteria can be anything contained in the column you're searching

All processed data will be exported to a new file under the current working directory titled "processed data"
