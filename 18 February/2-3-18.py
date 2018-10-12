import sqlite3 as sql
# from testEmployee import Employee
conn = sql.connect('employee.db')
cursor = conn.cursor()
# cursor.execute("""CREATE TABLE employee(
#     first_name text,
#     last_name text,
#     pay integer
#     ) """)
# conn.commit()
cursor.execute("INSERT INTO employee values('frank','young',50000)")
# cursor.execute('SELECT * FROM employee WHERE first_name=1')
# result = cursor.fetchall()
# print(result)

conn.commit()

conn.close()
