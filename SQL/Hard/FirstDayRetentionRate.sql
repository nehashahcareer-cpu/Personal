/*
Problem: First Day Retention Rate
Problem ID: 2090
Dialect: SQL Server (T-SQL)

Objective:
Calculate the proportion of distinct players who logged in exactly
one calendar day after their first-ever login.

Formula:
Retention Rate =
    Players who logged in one day after their first login
    ------------------------------------------------------
                    Total distinct players

Approach:
1. Use a CTE (first_days) to find each player's earliest login date
   using MIN(login_date), grouped by player_id.
2. Join the CTE with players_logins to find subsequent login records.
3. Filter records where DATEDIFF(DAY, first_day, login_date) = 1.
4. Count distinct retained players to avoid counting a player multiple
   times if multiple login records exist on the qualifying date.
5. Divide by the total number of distinct players in the original table.
6. Cast the numerator to FLOAT to avoid integer division.

Key Concepts:
- MIN(): Finds each player's first-ever login date.
- GROUP BY: Produces one first-login record per player.
- DATEDIFF(DAY, ...): Identifies logins one calendar-day boundary
  after the first login.
- COUNT(DISTINCT ...): Prevents duplicate player counts.
- FLOAT: Ensures fractional division instead of integer division.

Complexity:
- Time: Depends on the execution plan and available indexes; typically
  dominated by scanning, grouping, and joining the login records.
- Space: Depends on the intermediate grouping and join operations.

Important:
- The denominator must include ALL distinct players, including players
  who never logged in again.
- A player who logs in multiple times on the next day counts only once.
- Players with only one login remain in the denominator but not the
  numerator.
*/

WITH first_days AS (
    SELECT
        player_id,
        MIN(login_date) AS first_day
    FROM players_logins
    GROUP BY player_id
)
SELECT
    CAST(COUNT(DISTINCT first_days.player_id) AS FLOAT)
    /
    (
        SELECT COUNT(DISTINCT player_id)
        FROM players_logins
    ) AS retention_rate
FROM first_days
JOIN players_logins
    ON first_days.player_id = players_logins.player_id
WHERE DATEDIFF(DAY, first_days.first_day, players_logins.login_date) = 1;
