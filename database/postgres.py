import os,psycopg2

DATABASE_URL = os.environ['DATABASE_URL']


create_table_query = """CREATE TABLE farmers

 (
  phone_number Varchar NOT NULL,
  farmer_name Varchar NOT NULL,
  state_name Varchar NOT NULL,
  district_name Varchar NOT NULL,
  village_name Integer NOT NULL
);"""
try:
        connection = psycopg2.connect(DATABASE_URL, sslmode='require')
        cursor = connection.cursor()
        # create table one by one
        cursor.execute(create_table_query)
        print("Table created successfully in PostgreSQL ")
        # close communication with the PostgreSQL database server
        cursor.close()
        # commit the changes
        connection.commit()
except (Exception, psycopg2.DatabaseError) as error:
        print(error)
finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')