import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='Anumoy_1234',
        database='javadb'
    )

    if connection.is_connected() :
        print("Connection gets established ...")
        cursor = connection.cursor()

        # SQL query to create a table
        # create_table_query = '''
        # CREATE TABLE IF NOT EXISTS course (
        #     course_id INT AUTO_INCREMENT PRIMARY KEY,
        #     course_name VARCHAR(50) NOT NULL
        # )
        # '''
        # cursor.execute(create_table_query)
        # print('Course table created successfully')

        # courses = [
        #     ('Java',),
        #     ('Python',),
        #     ('C++',),
        #     ('Javascript',)
        # ] 

        # insert_table_query = '''
        #    insert into course(course_name) values(%s)
        # '''

        # cursor.executemany(insert_table_query, courses)
        # connection.commit()
        # print('Details inside Course table inserted successfully')
except Exception as e:
    print("Error while connecting to MySQL DB", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")    