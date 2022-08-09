class PostGresDB:
    import psycopg2,os,pandas
    connection = 0
    DATABASE_URL=os.environ['DATABASE_URL']
    def __init__(self):
        try:
            self.connection = self.psycopg2.connect(self.DATABASE_URL, sslmode='require')
            print("Database connection established successfully")
        except (Exception, self.psycopg2.DatabaseError) as error:
            print(error)

    def __del__(self):
        if self.connection is not None:
            self.connection.close()
            print("MySQL connection is closed")

    def createTable(self, table_name):
        cursor = self.connection.cursor()
        create_table_query = f"CREATE TABLE {table_name}(phone_number Varchar NOT NULL,farmer_name Varchar NOT NULL,state_name Varchar NOT NULL,district_name Varchar NOT NULL,village_name varchar NOT NULL);"
        print(create_table_query)
        cursor.execute(create_table_query)
        self.connection.commit()
        cursor.close()

    def csvToDatabase(self, table_name, csv_data):
        cursor = self.connection.cursor()
        for i in range(0,len(csv_data)):
            row_data_list = csv_data[i].split("-")
            print(row_data_list)
            sql = f"INSERT INTO {table_name}(phone_number,farmer_name,state_name,district_name,village_name) VALUES (\'{row_data_list[0]}\',\'{row_data_list[1]}\',\'{row_data_list[2]}\',\'{row_data_list[3]}\',\'{row_data_list[4]}\')"
            print(sql)
            cursor.execute(sql)
            print("Record inserted")
        self.connection.commit()
        cursor.close()

    def printTable(self,table_name):
        cursor = self.connection.cursor()
        data = self.pandas.read_sql_query(f"SELECT * FROM {table_name};",self.connection)
        df = self.pandas.DataFrame(data)
        df.to_csv('./exported_data.csv', index = False)
        cursor.close()
    
    def deleteTable(self, table_name):
        cursor = self.connection.cursor()
        cursor.execute(f"DROP TABLE {table_name}")
        self.connection.commit()
        cursor.close()