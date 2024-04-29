import mysql.connector
import pandas as pd
#from sqlalchemy import create_engine

# Creating the path
path = 'G:\My Drive\Programming\Learning_Python\PYE\data_analysis_project\institutions_list_cleaned.csv'

# Establishing data connection with MySQL
conn = mysql.connector.connect(option_files='C:/Users/MAYSA/.my.cnf')

# Creating a cursor 
mycursor = conn.cursor()

# Extracting and transforming data from MySQL

# Counting the rows and checking if the entire cvs file was uploaded to the database
# rowstotal = mycursor.execute("SELECT COUNT(*) FROM institutions_list;")
# for (rowstotal) in mycursor:
#     print(rowstotal[0])

# Visualizing the data
# query = mycursor.execute(
#     ''' 
#         SELECT * 
#         FROM institutions_list
#         LIMIT 10
#     ''')
# for (query) in mycursor:
#     print(query)

# Creating a new dataframe with some data that we need to analyze
dataframe = pd.read_sql("SELECT name, category, city, state, situation FROM institutions_list", conn)
# print(dataframe.columns)

#! Counting the amount of institutions per state
# institution_per_state = dataframe['state'].value_counts()
# print(institution_per_state)

# # Creating a bar plot
# color = ['lightblue', 'blue', 'purple', 'red', 'black']
# ax = dataframe['state'].value_counts().plot(kind='bar', figsize=(14,8), title="Number of institutions per state", color=color)
# ax.set_xlabel("state")
# ax.set_ylabel("number of institutions")
# ax.bar_label(ax.containers[0], label_type='edge')
# plt.show()

#! Counting the amount of active and inactive institutions
# situation = dataframe['situation'].value_counts()
# print(situation)

# # Creating a pie plot
# labels = ['Active', 'Inactive']
# ax = dataframe['situation'].value_counts().plot(kind='pie', figsize=(5, 5), title="Institutions Situation - Year Base 2022", labels=labels,  autopct='%.2f')
# plt.show()

#! Counting the amount of active/inactive institutions per state
# dataframe.value_counts(["state", "situation"])
# state_x_situation = pd.crosstab(dataframe.state,dataframe.situation)
# print(state_x_situation)

#! Counting the amount of institutions per city
# institution_per_city = dataframe['city'].value_counts()

#! Creating a new .csv file with the numbers of intitutions per city called "inst_city.csv"
# institution_per_city.to_csv('G:\My Drive\Programming\Learning_Python\PYE\data_analysis_project\inst_city.csv', encoding='utf-8')

#! Counting the amount of private and public institutions
# category = dataframe['category'].value_counts()
# print(category)

#! Counting the amount of public/private institutions per state
# dataframe.value_counts(["state", "category"])
# state_x_category = pd.crosstab(dataframe.state,dataframe.category)
# print(state_x_category)

#! Identifying the situation per state
dataframe.value_counts(["situation", "category"])
situation_x_category = pd.crosstab(dataframe.situation,dataframe.category)
print(situation_x_category)
#situation_x_category.to_csv('G:\My Drive\Programming\Learning_Python\PYE\data_analysis_project\data.csv')

conn.close()


