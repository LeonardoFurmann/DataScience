#DATA SCIENCE
##ENGENHARIA DE DADOS
#LEONARDO FURMANN
#10/10/2023

import mysql.connector
import pandas as pd


conn_northwind = mysql.connector.connect(
    host= '127.0.0.1',
    user = 'root',
    password = '123456',
    database = 'northwind'
)

conn_multdim = mysql.connector.connect(
    host= '127.0.0.1',
    user = 'root',
    password = '123456',
    database = 'multdim_2'
)

cursor = conn_northwind.cursor()
cursor_multdim = conn_multdim.cursor()

# select_statement = 'select distinct product_name from products'
# cursor.execute(select_statement)
# result = cursor.fetchall()
# prod_df = pd.DataFrame(result, columns=['product_name'])
# for i,r in prod_df.iterrows():
#     insert_statement = f"insert into dim_produto values({i+1}, '{r['product_name']}')"
#     cursor_multdim.execute(insert_statement)
#     conn_multdim.commit()


# select_statement = 'select first_name, last_name from customers'
# cursor.execute(select_statement)
# result = cursor.fetchall()
# cust_df = pd.DataFrame(result, columns=['first_name' ,'last_name'])
# cursor_multdim = conn_multdim.cursor()
# for i, f in cust_df.iterrows():
#     insert_statement = f"insert into dim_cliente values({i+1}, '{f['first_name']}  {f['last_name']}')"
#     cursor_multdim.execute(insert_statement)
#     conn_multdim.commit()


# select_statement = 'select distinct first_name, last_name from employees'
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

# select_statement = 'select distinct category from products'
# cursor.execute(select_statement)
# result = cursor.fetchall()
# prod_df = pd.DataFrame(result, columns=['category'])
# for i,r in prod_df.iterrows():
#     insert_statement = f"insert into dim_catproduto values({i+1}, '{r['category']}')"
#     cursor_multdim.execute(insert_statement)
#     conn_multdim.commit()

# select_statement = 'select distinct state_province from customers'
# cursor.execute(select_statement)
# result = cursor.fetchall()
# prod_df = pd.DataFrame(result, columns=['state_province'])
# for i,r in prod_df.iterrows():
#     insert_statement = f"insert into dim_uf values({i+1}, '{r['state_province']}')"
#     cursor_multdim.execute(insert_statement)
#     conn_multdim.commit()

# select_statement = 'select distinct payment_type from orders'
# cursor.execute(select_statement)
# result = cursor.fetchall()
# prod_df = pd.DataFrame(result, columns=['payment_type'])
# for i,r in prod_df.iterrows():
#     insert_statement = f"insert into dim_meiopagamento values({i+1}, '{r['payment_type']}')"
#     cursor_multdim.execute(insert_statement)
#     conn_multdim.commit()

