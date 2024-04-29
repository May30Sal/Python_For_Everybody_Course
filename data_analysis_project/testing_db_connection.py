# modules
import mysql.connector
from mysql.connector import errorcode

# conn = mysql.connector.connect(host='localhost',
#     port=3306,
#     user='root',
#     database='br_edu')
# print("connection successful!")

# #!This path below is to avoid showing my DB credentials!
try:                           
  cnx = mysql.connector.connect(option_files='C:/Users/MAYSA/.my.cnf') 
  print("connection successful!")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()