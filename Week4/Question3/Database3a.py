import sqlite3

conn = sqlite3.connect("database.sqlite")
c = conn.cursor()

# The names of both the Home Teams and Away Teams in each match played in 2015 and Full time Home Goals (FTHG) = 5
print("\nHOME TEAM----||----AWAY TEAM")
result = (c.execute("SELECT HomeTeam, AwayTeam FROM matches WHERE Season = '2015' AND FTHG = '5'")).fetchall()
for row in result:
    print(f"{row[0]}---||---{row[1]}")

# The details of the matches where Arsenal is the Home Team and  Full Time Result (FTR) is “A” (Away Win)
result = (c.execute("SELECT * FROM Matches WHERE HOmeTeam ='Arsenal' AND FTR = 'A'").fetchall())
print('\n')
for row in result:
    print(row)

# All the matches from the 2012 season till the 2015 season where Away Team is Bayern Munich and Full time Away Goals (FTHG) > 2
result = (c.execute("SELECT HomeTeam, FTR FROM Matches WHERE Season BETWEEN 2012 AND 2015 AND AwayTeam = 'Bayern Munich' AND FTAG > 2").fetchall())
print("\nHOME TEAM ---||--- RESULT")
for row in result:
    print(f"{row[0]}----||----{row[1]}")

# All the matches where the Home Team name begins with “A” and Away Team name begins with “M”
result = (c.execute("SELECT HomeTeam, AwayTeam, FTR FROM Matches WHERE HomeTeam LIKE 'A%' AND AwayTeam LIKE 'M%'")).fetchall()
print("\nHOME TEAM ---||---- AWAY TEAM ---||--- RESULT")
for row in result:
    print(f"{row[0]}----||----{row[1]}----||----{row[2]}")
