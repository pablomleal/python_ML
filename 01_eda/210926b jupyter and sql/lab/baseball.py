# Imports
import sqlite3 as sq3
import pandas.io.sql as pds
import pandas as pd

filepath = 'baseball.db'
con = sq3.Connection(filepath)

queryStar = 'SELECT * FROM allstarfull'
observations = pds.read_sql_query(queryStar, con)

queryMaster = 'SELECT * FROM sqlite_master'
tables = pds.read_sql_query(queryMaster, con)

optional = 'SELECT * FROM batting';REsult = pds.read_sql_query(optional, con)


print(observations)
print(tables)
