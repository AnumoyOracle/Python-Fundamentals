import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Anumoy_1234",
        database="javadb",
    )

    if connection.is_connected():

        print("Connection gets established ...")

        cursor = connection.cursor()

        # Create a table ------------>>>

        # create_table_query = '''
        # create table student(
        #     student_id INT PRIMARY KEY AUTO_INCREMENT,
        #     student_name VARCHAR(50) NOT NULL,
        #     student_dept VARCHAR(50) NOT NULL,
        #     student_email VARCHAR(50) NOT NULL
        # )
        # '''
        # cursor.execute(create_table_query)

        # Insert details inside table ------------>>>

        # students = [
        #     ('Anumoy Nandy', 'IT', 'anumoy@gmail.com'),
        #     ('Kunal Pramanick', 'IT', 'kunal@gmail.com'),
        #     ('Manas Pratim Biswas', 'IT', 'manas@gmail.com'),
        #     ('Anirban Ghosh', 'EE', 'anirban@gmail.com'),
        #     ('Kabir Raj Singh', 'CSE', 'kabir@gmail.com'),
        #     ('Suvankar Das', 'CSE', 'suvankar@gmail.com'),
        #     ('Anannyo Dey', 'CSE', 'anannyo@gmail.com'),
        #     ('Sabarno Biswas', 'EE', 'sabarno@gmail.com')
        # ]
        # insert_into_table_query = '''
        #    insert into student(student_name, student_dept, student_email) values(%s,%s,%s)
        # '''
        # cursor.executemany(insert_into_table_query,students)
        # connection.commit()
        # print('Details inserted into the table succcessfully ...')

    # Select query

    # select_query = '''
    #     select student_name, student_dept
    #     from student
    #     where student_name = %s or student_dept = %s
    # '''

    # cursor.execute(select_query, ('Anirban Ghosh', 'IT'))
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)

    # Delete a record from the table

    # delete_query = '''
    #    delete from student where student_dept = %s
    # '''

    # cursor.execute(delete_query, ('EE',))
    # connection.commit()

    # Update record inside a table

    # update_data_in_table = '''
    #    update student set student_dept = %s where student_dept = %s
    # '''

    # cursor.execute(update_data_in_table, ('InfoTech','IT'))
    # connection.commit()

    
    # group by -> order by -> limit a,b

    # limit_order_by_query = '''
    #    select * from student order by student_name limit 2,2
    # '''

    # cursor.execute(limit_order_by_query)
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)

    # search_query = "select * from student where student_name like %s or student_dept = %s"
    # cursor.execute(search_query,("%an%", 'CSE'))
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)


    # join_query = '''
    #                 select * from 
    #                 student left join course on student.course_id = course.course_id
    #                 union
    #                 select * from
    #                 student right join course on student.course_id = course.course_id
    #             '''
    # cursor.execute(join_query)
    # rows = cursor.fetchall()

    # for row in rows:
    #     print(row)


    # misc_query = '''
    #   select * from student where course_id between %s and %s
    # '''

    # cursor.execute(misc_query, (2, 3))
    # rows = cursor.fetchall()

    # for row in rows:
    #     print(row)


    # query = '''
    #    select count(*), student_dept from student group by student_dept
    # '''

    # cursor.execute(query)
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)


    # query = '''
    #     select distinct(student_dept) from student
    # '''

    # cursor.execute(query)
    # rows = cursor.fetchall()

    # for row in rows:
    #     print(row[0])


    # query = '''
    #    select sum(course_id), avg(course_id), student_dept from student group by student_dept
    # '''

    # cursor.execute(query)
    # rows = cursor.fetchall()

    # for row in rows:
    #     print(row[2], row[0], row[1])


    # query = '''
    #    select * from student where course_id not in (2,3)
    # '''

    # cursor.execute(query)
    # rows = cursor.fetchall()

    # for row in rows:
    #     print(row)
    

except Exception as e:
    print("MySQL connection can not be established ...", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed now ...")
