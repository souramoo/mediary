import pyodbc
import pandas as pd


server = 'mediary.database.windows.net'
database = 'MeDiary'
username = 'mediary'
password = 'hackcambridge-1'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

# cursor.execute("SELECT @@version;")
# row = cursor.fetchone()
# while row:
#     print(row[0])
#     row = cursor.fetchone()

# View database
query = "SELECT * FROM Conditions"
df = pd.read_sql(query, cnxn)
print(df)

# Write to database
cursor.execute("INSERT INTO Conditions(nhs_number, condition,img1, img2) values ('01234', 'condition', 'img1', 'img2')")
cnxn.commit()

# cursor.execute("DELETE FROM Conditions")
# cnxn.commit()

cursor.close()
cnxn.close()