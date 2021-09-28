import sqlite3

conn = sqlite3.connect("Employee.db")
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS DEPARTMENTS")
c.execute("""CREATE TABLE DEPARTMENTS (
            DEPARTMENTS_ID INT NOT NULL ,
            DEPARTMENT_NAME CHAR(30) NOT NULL,
            FOREIGN KEY (DEPARTMENTS_ID) REFERENCES EMPLOYEE (DEPARTMENT_ID))""")
print('*****DEPARTMENTS TABLE CREATED*****')
conn.commit()

department_values = [(5, 'MARKETING'),
                     (4, 'PURCHASING'),
                     (1, 'IT'),
                     (2, 'CLERK'),
                     (3, 'SALES')]
c.executemany("INSERT INTO Departments VALUES (?, ?)", department_values)
print('**DEPARTMENTS TABLE ROWS INSERTED SUCCESSFULLY**')

choice = 1
while choice:
    dept_id = input("Enter the department id of your choice(1/2/3/4/5): ")
    c.execute("SELECT DEPARTMENT_NAME FROM DEPARTMENTS WHERE DEPARTMENTS_ID = :DEPT_ID", {'DEPT_ID': dept_id})
    c.execute("SELECT NAME, ID, SALARY, DEPARTMENT_ID, CITY, DEPARTMENT_NAME FROM EMPLOYEE, DEPARTMENTS WHERE "
              "EMPLOYEE.DEPARTMENT_ID = :DEPT_ID AND DEPARTMENTS.DEPARTMENTS_ID = :DEPT_ID", {'DEPT_ID': dept_id})
    result = c.fetchall()
    print(f"\nEmployees working in the department {result[0][5]} are: ")
    for i in result:
        print("\nNAME           :", i[0])
        print("ID             :", i[1])
        print("SALARY         :", i[2])
        print("DEPARTMENT_ID  :", i[3])
        print("CITY           :", i[4])
        print("DEPARTMENT_NAME:", i[5])
    choice = int(input("Do you wish to continue or not (0/1): "))

conn.commit()
conn.close()
