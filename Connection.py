import psycopg2

def connect():
    try:
        # try to establish connection to database
        connection = psycopg2.connect(user="postgres",
                                      password="hyt43bdf",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")
        cursor = connection.cursor()
        print("Connected to database ")
    except (Exception, psycopg2.Error) as error:
        print("Error in db operation", error)
    finally:
    # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
connect()
