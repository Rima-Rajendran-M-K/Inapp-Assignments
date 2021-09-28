import sqlite3

conn = sqlite3.connect('Employee.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS EMPLOYEE")

c.execute("""CREATE TABLE EMPLOYEE (
        NAME CHAR(20) NOT NULL,
        ID INT PRIMARY KEY NOT NULL,
        SALARY INT NOT NULL,
        DEPARTMENT_ID INT NOT NULL)""")
print('*****EMPLOYEE TABLE CREATED*****')
conn.commit()

c.execute("ALTER TABLE EMPLOYEE ADD COLUMN CITY CHAR(30)")
print('**NEW COLUMN ADDED SUCCESSFULLY**')

emp_values = [('AMAL', 101, 34000, 4, 'TVM'),
              ('ANJANA', 102, 30000, 2, 'EKM'),
              ('SNEHA', 103, 32000, 5, 'CAN'),
              ('NANDANA', 104, 28000, 3, 'CLT'),
              ('BHARATH', 105, 35000, 1, 'CLT')]
c.executemany("INSERT INTO EMPLOYEE (NAME, ID, SALARY, DEPARTMENT_ID, CITY) VALUES (?, ?, ?, ?, ?)", emp_values)
print('**EMPLOYEE TABLE ROWS INSERTED SUCCESSFULLY**')
conn.commit()

def emp_details():
    c.execute("SELECT NAME,ID, SALARY FROM EMPLOYEE")
    results = c.fetchall()
    for i in results:
        print("\nNAME  :", i[0])
        print("ID    :", i[1])
        print("SALARY:", i[2])

def list_employees(alpha):
    c.execute("SELECT * FROM EMPLOYEE WHERE NAME LIKE '"+alpha+"%'")
    record = c.fetchall()
    if len(record) == 0:
        print(f"No employee with name starting with {alpha.title()}")
    else:
        print(f"Employees whose name starts with {alpha.capitalize()}:  ")
        for i in record:
            print("\nNAME         :", i[0])
            print("ID           :", i[1])
            print("SALARY       :", i[2])
            print("DEPARTMENT_ID:", i[3])
            print("CITY         :", i[4])

def details_emp(emp_id):
    c.execute("SELECT * FROM EMPLOYEE WHERE ID = :EMP_ID", {'EMP_ID': emp_id})
    result = c.fetchall()
    if len(result) == 0:
        print(f"No employee with the employee id {emp_id}!!")
    else:
        print(f"Employee with employee id {emp_id}:  ")
        for i in result:
            print("\nNAME         :", i[0])
            print("ID           :", i[1])
            print("SALARY       :", i[2])
            print("DEPARTMENT_ID:", i[3])
            print("CITY         :", i[4])

def change_name(emp_id, n_name):
    c.execute("SELECT NAME FROM EMPLOYEE WHERE ID = :EMP_ID", {'EMP_ID': emp_id})
    result = c.fetchone()
    print("Name of Employee :", result[0])
    c.execute("UPDATE EMPLOYEE SET NAME = :N_NAME WHERE ID = :EMP_ID", {'N_NAME': n_name, 'EMP_ID': emp_id})
    c.execute("SELECT NAME FROM EMPLOYEE WHERE ID = :EMP_ID", {'EMP_ID': emp_id})
    result = c.fetchone()
    print("Name of Employee after Update:", result[0].upper())

while 1:
    print("\n-----MENU-----")
    print("\n1. Employ details\n2. List of employee names starting with a particular letter"
          "\n3. Details of employee whose ID is given""\n4. Change the name of employee whose ID is given by user"
          "\n5. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        emp_details()
    elif ch == 2:
        letter = (input("Enter an alphabet of your choice: "))
        list_employees(letter.capitalize())
    elif ch == 3:
        id = int(input("Enter an employee id: "))
        details_emp(id)
    elif ch == 4:
        id = int(input("Enter an employees id: "))
        new_name = input("Enter the new name: ")
        change_name(id, new_name.capitalize())
        print(f"The changed name of {id} is {new_name.upper()}")
    elif ch == 5:
        exit()
    else:
        print("Invalid choice!!")
conn.commit()
conn.close()
