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


# select_statement = 'select first_name, last_name from customers'
# cursor.execute(select_statement)
# result = cursor.fetchall()
# cust_df = pd.DataFrame(result, columns=['first_name' ,'last_name'])
# cursor_multdim = conn_multdim.cursor()
# for i, f in cust_df.iterrows():
#     insert_statement = f"insert into dim_cliente values({i+1}, '{f['first_name']}  {f['last_name']}')"
#     cursor_multdim.execute(insert_statement)
#     conn_multdim.commit()


# select_statement = 'select first_name, last_name from employees'
# cursor.execute(select_statement)
# result = cursor.fetchall()
# cust_df = pd.DataFrame(result, columns=['first_name' ,'last_name'])
# cursor_multdim = conn_multdim.cursor()
# for i, f in cust_df.iterrows():
#     insert_statement = f"insert into dim_vendedor values({i+1}, '{f['first_name']}  {f['last_name']}')"
#     cursor_multdim.execute(insert_statement)
#     conn_multdim.commit()


# select_statement = 'select distinct country_region from customers'
# cursor.execute(select_statement)
# result = cursor.fetchall()
# prod_df = pd.DataFrame(result, columns=['country_region'])
# for i,r in prod_df.iterrows():
#     insert_statement = f"insert into dim_regiao values({i+1}, '{r['country_region']}')"
#     cursor_multdim.execute(insert_statement)
#     conn_multdim.commit()

# select_statement = 'select distinct city from customers'
# cursor.execute(select_statement)
# result = cursor.fetchall()
# prod_df = pd.DataFrame(result, columns=['city'])
# for i,r in prod_df.iterrows():
#     insert_statement = f"insert into dim_municipio values({i+1}, '{r['city']}')"
#     cursor_multdim.execute(insert_statement)
#     conn_multdim.commit()

select_statement = 'select distinct category from products'
cursor.execute(select_statement)
result = cursor.fetchall()
prod_df = pd.DataFrame(result, columns=['category'])
for i,r in prod_df.iterrows():
    insert_statement = f"insert into dim_catproduto values({i+1}, '{r['category']}')"
    cursor_multdim.execute(insert_statement)
    conn_multdim.commit()

# select_statement = 'select distinct state_province from customers'
# cursor.execute(select_statement)
# result = cursor.fetchall()
# prod_df = pd.DataFrame(result, columns=['state_province'])
# for i,r in prod_df.iterrows():
#     insert_statement = f"insert into dim_uf values({i+1}, '{r['state_province']}')"
#     cursor_multdim.execute(insert_statement)
#     conn_multdim.commit()

