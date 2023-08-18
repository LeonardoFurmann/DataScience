#DATA SCIENCE
##ENGENHARIA DE DADOS
#LEONARDO FURMANN
#17/08/2023

import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    password = 'positivo',
    database = 'northwind'
)

conn_multdim = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    password = 'positivo',
    database = 'muldim_1'
)

cursor = connection.cursor()
cursor_multdim = conn_multdim.cursor()

# carregamento de dados na multidimensional produtos
# select_statement = 'select product_name from products'
# cursor.execute(select_statement)
# result = cursor.fetchall()
# prod_df = pd.DataFrame(result, columns=['product_name'])
# for i,r in prod_df.iterrows():
#     insert_statement = f"insert into dim_produto values({i+1}, '{r['product_name']}')"
#     cursor_multdim.execute(insert_statement)
#     conn_multdim.commit()

# prod_df = prod_df['product_name'].unique()

select_statement = 'select first_name, last_name from customers'
cursor.execute(select_statement)
result = cursor.fetchall()
cust_df = pd.DataFrame(result, columns=['first_name' ,'last_name'])
cursor_multdim = conn_multdim.cursor()

for i, f in cust_df.iterrows():
    insert_statement = f"insert into dim_cliente values({i+1}, '{f['first_name']}  {f['last_name']}')"
    cursor_multdim.execute(insert_statement)
    conn_multdim.commit()


