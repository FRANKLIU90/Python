import sqlite3 as sql
from testEmployee import Employee


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employee VALUES (:first ,:last,:pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


conn = sql.connect(':memory:')
c = conn.cursor()

c.execute("""CREATE TABLE employee (
    first_name TEXT,
    last_name TEXT,
    pay INTEGER
    )""")

conn.commit()


emp_1 = Employee('frank', 'young', 50000)
# with conn:
#     c.execute("INSERT INTO employee VALUES(:first,:last,:pay) ", {'first': emp_1.first, 'last': emp_1.last, 'pay': emp_1.pay})

insert_emp(emp_1)

c.execute("SELECT * FROM employee")
results = c.fetchall()
print(results)
