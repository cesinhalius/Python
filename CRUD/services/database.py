import pyodbc 


server = 'LAPTOP-5AUDMN70\SQLEXPRESS' 
database = 'CRUD_Python' 
username = 'LAPTOP-5AUDMN70\Cesar Roberto' 
password = '' 

cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
cursor = cnxn.cursor()