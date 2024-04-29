# Modules
import mysql.connector
import pandas as pd

# Creating the path
path = 'G:\My Drive\Programming\Learning_Python\PYE\data_analysis_project\institutions_list_cleaned.csv'

# Defining the project
project = 'br_edu'
dataset = 'brasil_superior_education'
table = 'institutions_list'


# Establishing data connection with MySQL
conn = mysql.connector.connect(option_files='C:/Users/MAYSA/.my.cnf')

# Importing the cvs file to MySQL
# The 'utf-8-sig' was used to keep the accents from the original file
df = pd.read_csv(path,  encoding='utf-8-sig')

# Creating a cursor 
mycursor = conn.cursor()

# Creating the table and inserting data
mycursor.execute(
    '''CREATE TABLE if NOT EXISTS institutions_list (
        institution_code INT, 
        name VARCHAR(255), 
        category VARCHAR(255), 
        city VARCHAR(255), 
        state VARCHAR(255), 
        situation VARCHAR(255))'''
)

for index, row in df.iterrows(): 
    sql = "INSERT IGNORE INTO institutions_list (institution_code, name, category, city, state, situation) VALUES (%s, %s, %s, %s, %s, %s)" 
    val = (row['CODIGO_DA_IES'], row['NOME_DA_IES'], row['CATEGORIA_DA_IES'], row['MUNICIPIO'], row['UF'], row['SITUACAO_IES']) 
    mycursor.execute(sql, val) 

conn.commit() 
conn.close() 

