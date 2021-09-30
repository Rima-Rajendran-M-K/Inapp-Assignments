import sqlite3

conn = sqlite3.connect("database.sqlite")
c = conn.cursor()

# Counts all the rows in the Teams table
print("\nCount of all the rows in Teams table: "+str(c.execute("SELECT COUNT(*) FROM Teams").fetchone()[0]))

# All the unique values that are included in the Season column in the Teams table
result = c.execute("SELECT DISTINCT Season FROM Teams").fetchall()
print("\nUnique Seasons: ")
for row in result:
    print(row[0])

# The largest and smallest stadium capacity that is included in the Teams table
result = c.execute("SELECT MAX(StadiumCapacity), MIN(StadiumCapacity) FROM Teams").fetchall()[0]
print(f"\nLargest Stadium Capacity is : {result[0]}\nSmallest Stadium Capacity is: {result[1]}")

# The sum of squad players for all teams during the 2014 season from the Teams table
print("\nSum of squad players(2014): "+str(c.execute("SELECT SUM(KaderHome) FROM Teams WHERE Season = '2014'").fetchone()[0]))

# Matches table to know how many goals did Man United score during home games on average? [Answer - 2.16]
print("\nAverage goals scored by Man United during home games is: "+str(c.execute("SELECT ROUND(AVG(FTHG), 2) FROM Matches WHERE HomeTeam = 'Man United'").fetchone()[0]))
