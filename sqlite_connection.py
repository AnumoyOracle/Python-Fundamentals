import sqlite3

conn = sqlite3.connect("student.db")

# Create a table

# conn.execute(''' 
#     create table fee(
#        fee_id INTEGER PRIMARY KEY AUTOINCREMENT,
#        student_id INTEGER,
#        fee_amount INTEGER                        
#     )
# ''')


# insert a record in the table

# query = '''
# insert into fee(student_id, fee_amount) values(?,?) 
# '''

# feesCollection = [
#     (3, 20000),
#     (6, 15000),
#     (8, 18000),
#     (9, 25000)
# ]

# conn.executemany(query, feesCollection)
# conn.commit()

# query = '''
# insert into student(student_name, student_dept) values(?, ?)
# '''

# conn.execute(query,('Anumoy Nandy','IT'))
# conn.commit()

# students = [
#     ('Anonyo Dey','CSE'),
#     ('Anirban Ghosh','EE'),
#     ('Priyangshu Sadhu','IT')
# ]

# query = '''
# insert into student(student_name, student_dept) values(?, ?)
# '''

# conn.executemany(query, students)
# conn.commit()

# conn.execute(query)
# conn.commit()


# select a record from the table

# query = "select * from student limit ?,? "
# records = conn.execute(query,(2,2))
# for record in records:
#     print(record)


# delete a record from the table

# query = "delete from student where student_dept = ? "
# conn.execute(query,('ECE',))
# conn.commit()


# update a record inside the table

# query = '''
# update student set student_dept = ? where student_name = ?
# '''

# conn.execute(query,('CE','Priyangshu Sadhu'))
# conn.commit()


# select records using user inputs

# dept1 = input('Enter first department : ')
# dept2 = input('Enter second department : ')

# query = "select * from student where student_dept = ? or student_dept = ?"
# records = conn.execute(query, (dept1, dept2))
# for record in records:
#     print(record[1], record[2])


# join operation between two tables

# query = "select * from student s join fee f on s.student_id = f.student_id"
# records = conn.execute(query)

# for record in records:
#     print(record)




conn.close()