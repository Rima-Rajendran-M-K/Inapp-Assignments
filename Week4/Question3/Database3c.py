import sqlite3

conn = sqlite3.connect("database.sqlite")
c = conn.cursor()

print("\nHOME TEAM - FTHG - FTAG")
result = c.execute("SELECT HomeTeam, FTHG, FTAG FROM Matches WHERE Season = '2010' AND HomeTeam = 'Aachen' ORDER BY FTHG DESC ").fetchall()
for row in result:
    print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}")

print("\nHOME TEAM --- COUNT(FTR)")
result = c.execute("SELECT HOmeTeam, COUNT(FTR) FROM Matches WHERE FTR = 'H' AND Season = '2016' GROUP BY HomeTeam ORDER BY COUNT(FTR) DESC").fetchall()
for row in result:
    print(f"{row[0]} --- {row[1]}")

print("\nFirst ten rows from the Unique_Teams table: ")
result = c.execute("SELECT * FROM Unique_Teams LIMIT 10").fetchall()
for row in result:
    print(row)

print("\nMATCH ID--UNIQUE TEAM ID--TEAM NAME (Using WHERE statement): ")
result = c.execute("SELECT Teams_in_Matches.Match_id, Teams_in_Matches.Unique_Team_ID, Unique_Teams.TeamName FROM Unique_Teams, Teams_in_Matches WHERE Teams_in_Matches.Unique_Team_ID = Unique_Teams.Unique_Team_ID LIMIT 10").fetchall()
for row in result:
    print(row)

print("\nMATCH ID--UNIQUE TEAM ID--TEAM NAME (Using JOIN statement): ")
result = c.execute("SELECT Teams_in_Matches.Match_id, Teams_in_Matches.Unique_Team_ID, Unique_Teams.TeamName FROM Teams_in_Matches JOIN Unique_Teams ON Teams_in_Matches.Unique_Team_ID = Unique_Teams.Unique_Team_ID LIMIT 10").fetchall()
for row in result:
    print(row)

print("\nJoining together the Unique_Teams data table and the Teams table!!")
result = c.execute("SELECT * FROM Unique_Teams JOIN Teams LIMIT 10").fetchall()
for row in result:
    print(row)

print("\nU_T_ID--TEAM NAME--AVG_AGE--SEASON--FOREIGN_PLAYERS")
result = c.execute("SELECT Unique_Teams.Unique_Team_ID, Unique_Teams.TeamName, Teams.AvgAgeHome, Teams.Season, Teams.ForeignPlayersHome FROM Unique_Teams JOIN Teams ON Unique_Teams.TeamName = Teams.TeamName LIMIT 5").fetchall()
for row in result:
    print(row)

print("\nM_ID--U_T_ID--TEAM NAME")
result = c.execute("SELECT MAX(Match_id), Teams_in_Matches.Unique_Team_ID, Unique_Teams.TeamName FROM Teams_in_Matches JOIN Unique_Teams ON Teams_in_Matches.Unique_Team_ID = Unique_Teams.Unique_Team_ID WHERE TeamName LIKE '%y' OR TeamName LIKE '%r' GROUP BY Teams_in_Matches.Unique_Team_ID, TeamName").fetchall()
for row in result:
    print(row)
