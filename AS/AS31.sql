SELECT matchid, player
  FROM goal
  WHERE teamid = 'GER'
  
SELECT id,stadium,team1,team2
  FROM game
  WHERE id=1012
  
SELECT player, teamid, stadium, mdate
  FROM game JOIN goal ON (game.id=goal.matchid)
  WHERE teamid='GER'
  
SELECT team1, team2, player
  FROM goal JOIN game ON (game.id=goal.matchid)
  WHERE player LIKE 'Mario%'
  
SELECT player, teamid, coach, gtime
  FROM goal JOIN eteam ON (goal.teamid=eteam.id)
  WHERE gtime<=10

SELECT mdate, teamname
  FROM game JOIN eteam ON (team1=eteam.id)
  WHERE coach='Fernando Santos'
  
SELECT player
  FROM goal JOIN game ON (goal.matchid=game.id)
  WHERE stadium='National Stadium, Warsaw'
  
SELECT DISTINCT player
  FROM game JOIN goal ON matchid = id 
  WHERE teamid<>'GER' AND( team1='GER' OR team2='GER')

SELECT teamname, COUNT(matchid)
  FROM eteam JOIN goal ON (eteam.id=goal.teamid)
  GROUP BY teamname

SELECT stadium, COUNT(matchid)
  FROM game JOIN goal ON (game.id=goal.matchid)
  GROUP BY stadium

SELECT matchid,mdate, COUNT(matchid)
  FROM game JOIN goal ON matchid = id 
  WHERE (team1 = 'POL' OR team2 = 'POL')
  GROUP BY matchid, mdate

SELECT matchid, mdate, COUNT(matchid)
  FROM goal JOIN game ON (goal.matchid=game.id)
  WHERE teamid='GER'
  GROUP BY matchid, mdate
