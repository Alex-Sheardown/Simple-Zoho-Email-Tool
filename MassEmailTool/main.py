import emailfunctions
import csv
import pandas as pd


myCSV = 'emailspreadsheet.csv'

subject = "Email test via csv"
from_addr = "YourZohoEmailAddressHere"
passw = "YourAppSpecificPasswordHere"
emailMessage = 'emailbody.txt'

emailfunctions.bulkEmail(subject,emailMessage,from_addr,passw,myCSV)



 
 
