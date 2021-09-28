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

department_values = [(2, 'MARKETING'), (2, 'SALES'), (1, 'IT'), (1, 'SALES'), (3, 'IT')]
c.executemany("INSERT INTO Departments VALUES (?, ?)", department_values)
print('**DEPARTMENTS TABLE ROWS INSERTED SUCCESSFULLY**')

choice = 1
while choice:
    dept_id = input("Enter the department id of your choice: ")
    c.execute("SELECT DEPARTMENT_NAME FROM DEPARTMENTS WHERE DEPARTMENTS_ID = :DEPT_ID", {'DEPT_ID': dept_id})
    row = c.fetchone()
    print(f"\nEmployees working in the department {row[0]} are: ")
    c.execute("SELECT EMP.NAME, EMP.ID, EMP.SALARY, EMP.DEPARTMENT_ID, EMP.CITY, DEPT.DEPARTMENT_NAME "
              "FROM EMPLOYEE EMP, DEPARTMENTS DEPT where EMP.DEPARTMENT_ID = :DEPT_ID AND DEPT.DEPARTMENTS_ID = :DEPT_ID"
              , {'DEPT_ID': dept_id})
    result = c.fetchall()
    for i in result:
        print("\nNAME           :", i[0])
        print("ID             :", i[1])
        print("SALARY         :", i[2])
        print("DEPARTMENT_ID  :", i[3])
        print("CITY           :", i[4])
        print("DEPARTMENT_NAME:", row[1])
    choice = int(input("Do you wish to continue or not (0/1)"))

conn.commit()
conn.close()