import sqlite3

conn = sqlite3.connect('hospital.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS HOSPITAL")
c.execute("DROP TABLE IF EXISTS DOCTOR")

# Table creation
c.execute("""CREATE TABLE HOSPITAL(
        HOSPITAL_ID INT PRIMARY KEY NOT NULL,
        HOSPITAL_NAME CHAR(30) NOT NULL,
        BED_COUNT INT NOT NULL)""")
print('*****HOSPITAL TABLE CREATED*****')

c.execute("""CREATE TABLE DOCTOR(
        DOCTOR_ID INT PRIMARY KEY NOT NULL,
        DOCTOR_NAME CHAR(20) NOT NULL,
        HOSPITAL_ID INT NOT NULL,
        JOINING_DATE DATE NOT NULL,
        SPECIALITY CHAR(30) NOT NULL,
        SALARY INT NOT NULL,
        EXPERIENCE INT NULL,
        FOREIGN KEY (HOSPITAL_ID) REFERENCES HOSPITAL(HOSPITAL_ID))""")
print('*****DOCTOR TABLE CREATED*****')
conn.commit()

# Inserting values into table
values_hospital = [(1, 'MAYO CLINIC', 200),
                   (2, 'CLEVELAND CLINIC', 400),
                   (3, 'JOHNS HOPKINS', 1000),
                   (4, 'UCLA MEDICAL CENTER', 1500)]
c.executemany("INSERT INTO HOSPITAL (HOSPITAL_ID, HOSPITAL_NAME, BED_COUNT) VALUES (?, ?, ?)", values_hospital)
print('**HOSPITAL TABLE ROWS INSERTED SUCCESSFULLY**')

values_doctor = [(101, 'DAVID', 1, '2005-02-10', 'PEDIATRIC', 40000, 'NULL'),
                 (102, 'MICHAEL', 1, '2018-07-23', 'ONCOLOGIST', 20000, 'NULL'),
                 (103, 'SUSAN', 2, '2016-05-19', 'GARNACOLOGIST', 25000, 'NULL'),
                 (104, 'ROBERT', 2, '2017-12-28', 'PEDIATRIC', 28000, 'NULL'),
                 (105, 'LINDA', 3, '2004-06-04', 'GARNACOLOGIST', 42000, 'NULL'),
                 (106, 'WILLIAM', 3, '2012-09-11', 'DERMATOLOGIST', 30000, 'NULL'),
                 (107, 'RICHARD', 4, '2014-08-21', 'GARNACOLOGIST', 32000, 'NULL'),
                 (108, 'KAREN', 4, '2011-10-17', 'RADIOLOGIST', 30000, 'NULL')]
c.executemany("INSERT INTO DOCTOR (DOCTOR_ID, DOCTOR_NAME, HOSPITAL_ID, JOINING_DATE, SPECIALITY, SALARY, EXPERIENCE) "
              "VALUES (?, ?, ?, ?, ?, ?, ?)", values_doctor)
print('**DOCTOR TABLE ROWS INSERTED SUCCESSFULLY**')
conn.commit()


def get_doctors_list(hospital_id):
    c.execute("SELECT DOCTOR_NAME FROM DOCTOR WHERE HOSPITAL_ID = :H_ID", {"H_ID": hospital_id})
    doctor = c.fetchall()
    for doc in doctor:
        print(doc[0])

def doctors(spec, sal):
    c.execute("SELECT DOCTOR_NAME FROM DOCTOR WHERE SPECIALITY = :SPEC AND SALARY >= :SAL", {"SPEC": spec, "SAL": sal})
    doctor = c.fetchall()
    for doc in doctor:
        print(doc[0])

def hospital_name(doc_name):
    c.execute("SELECT * FROM DOCTOR WHERE DOCTOR_NAME = :DOC", {"DOC": doc_name})
    id = c.fetchone()
    hos_id = id[2]
    c.execute("SELECT HOSPITAL_NAME FROM HOSPITAL WHERE HOSPITAL_ID = :ID", {"ID": hos_id})
    name = c.fetchone()
    return(name[0])

while 1:
    print("\n-----MENU-----")
    print("\n1. List of all doctors as per thr given Hospital id\n2. Doctors according to speciality and salary"
          "\n3. Hospital name of doctor\n4. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        hospital_id = int(input("Enter hospital id (1/2/3/4): "))
        print("Doctors working in the given hospital id are: ")
        get_doctors_list(hospital_id)
    elif ch == 2:
        speciality = input("Enter the preferred speciality: ")
        salary = int(input("Enter the salary: "))
        print(f"{speciality.title()} doctors with salary above {salary} are: ")
        doctors(speciality, salary)
    elif ch == 3:
        name = input("Enter the doctors name: ")
        print(f"The hospital name where {name} workS is: {hospital_name(name)}")
    elif ch == 4:
        exit()
    else:
        print("Invalid choice!!")

conn.close()
