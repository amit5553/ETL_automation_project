#import pandas as pd
#import sqlalchemy

#df=pd.read_csv('C:/Users/amitk/PycharmProjects/ETL_Automation_Project/emp.csv')
#print(df)
#print(type(df))

import pandas as pd
from sqlalchemy import create_engine, false
#import cx_Oracle
#oracle_con_cx_oracle = create_engine("oracle+cx_oracle://system:amit123@localhost:1521/xe")
#query='''select * from employees'''

#df=pd.read_sql(query,oracle_con_cx_oracle)

import pandas as pd
from sqlalchemy import create_engine
import oracledb
dsn = oracledb.makedsn("localhost", 1521, sid="orcl")
conn = oracledb.connect(
    user="system",
    password="amit123",
    dsn=dsn
)

df2 = pd.read_sql("select * from employees",conn)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(df2.to_string(index=False))