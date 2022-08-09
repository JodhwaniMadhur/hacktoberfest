import psycopg2
from sql_class import PostGresDB
import pandas as pd

data = pd.read_csv("../client/SDE_Assignment.csv")
data = data.to_string(index=False,index_names=False,header=False).split('\n')
vals = ['-'.join(ele.split()) for ele in data]
print(vals)
db_obj = PostGresDB()
db_obj.printTable("farmer_data")
del db_obj