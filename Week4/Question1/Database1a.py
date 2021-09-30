import sqlite3

conn = sqlite3.connect('cars.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS CAR")

c.execute("""CREATE TABLE CAR(
        NAME_OF_CAR CHAR(30) PRIMARY KEY NOT NULL,
        NAME CHAR(20) NOT NULL)""")
print('*****CAR TABLE CREATED*****')

values = [('HYUNDAI', 'AMAL'),
          ('MARUTI SWIFT', 'ANJANA'),
          ('TOYOTA FORTUNER', 'SNEHA'),
          ('HYUNDAI I20', 'AFAF'),
          ('VOLKSWAGEN TAIGUN', 'NANDANA'),
          ('MARUTI', 'ARJUN'),
          ('KIA SELTOS', 'RITHUN'),
          ('TATA HARRIER', 'SREESHA'),
          ('HYUNDAI I10', 'AMANYU'),
          ('MARUTI VITARA', 'NANDANA')]
c.executemany("INSERT INTO CAR (NAME_OF_CAR, NAME) VALUES (?, ?)", values)
print('**TABLE ROWS INSERTED SUCCESSFULLY**')
conn.commit()

print('CAR NAME', '  NAME')
c.execute("SELECT * FROM CAR")
rows = c.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()
