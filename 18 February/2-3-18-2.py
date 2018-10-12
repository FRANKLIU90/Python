import sqlite3 as sql
from testEmployee import Employee


def add_value(emp):
    with conn:
        c.execute("INSERT INTO testEmployee VALUES (:first,:last,:pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_by_name(emp):
    c.execute("SELECT * FROM testEmployee WHERE last=:last AND first=:first ", {'last': emp.last, 'first': emp.first})
    return c.fetchall()


def remove_by_name(emp):
    with conn:
        c.execute(""" DELETE FROM testEmployee
            WHERE last=:last AND first=:first """, {'last': emp.last, 'first': emp.first})


conn = sql.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE testEmployee (
first TEXT,
last TEXT,
pay INTEGER

)
    """)

emp_1 = Employee('eric', 'clapton', 80000)
emp_2 = Employee('neil', 'young', 90000)
emp_3 = Employee('bob', 'young', 70000)
emp_4 = Employee('joe', 'cocker', 85000)

c.execute("INSERT INTO testEmployee VALUES ('frank','young',50000),('lou','reed',60000)")

c.execute("INSERT INTO testEmployee VALUES (:first,:last,:pay)", {'first': emp_1.first, 'last': emp_1.last, 'pay': emp_1.pay})
c.execute("INSERT INTO testEmployee VALUES (:first,:last,:pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
c.execute("INSERT INTO testEmployee VALUES (:first,:last,:pay)", {'first': emp_3.first, 'last': emp_3.last, 'pay': emp_3.pay})


conn.commit()


add_value(emp_4)

remove_by_name(emp_2)


c.execute("SELECT * FROM testEmployee")
results = c.fetchall()
for result in results:
    print(result)


conn.close()
