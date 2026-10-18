/*
Problem: Actor Rating Difference Analysis
Dialect: SQL Server (T-SQL)

Objective:
For each actor, calculate:
1. Average rating of all films except the most recent film.
2. Rating of the most recent film.
3. Difference between the latest rating and the average previous rating,
   rounded to two decimal places.

Special Case:
If an actor has only one film, use that film's rating for both the
average rating and latest rating. The rating difference should be 0.

Approach:
1. Use ROW_NUMBER() partitioned by actor_name and ordered by release_date
   descending to rank each actor's films from newest to oldest.
2. Use the latest CTE to retrieve the rating of the most recent film
   (row_num = 1).
3. Use the previous CTE to calculate the average rating of earlier films
   (row_num > 1).
4. LEFT JOIN the two CTEs so actors with only one film are retained.
5. Use ISNULL() to substitute the latest rating when no previous-film
   average exists.
6. Use ROUND() to calculate the rating difference to two decimal places.

Key Concepts:
- ROW_NUMBER(): Ranks rows within each actor's partition.
- PARTITION BY: Restarts ranking for each actor.
- AVG(): Calculates the average of previous film ratings.
- LEFT JOIN: Preserves actors without previous films.
- ISNULL(): Handles NULL averages for actors with one film.
- ROUND(): Rounds the rating difference to two decimal places.

Complexity:
- Time: Approximately O(n log n), depending on the execution plan,
  primarily due to ranking and sorting.
- Space: Depends on the execution plan and intermediate sorting needs.

Assumption:
Release dates determine film recency. If an actor has multiple films
with the same release date, ROW_NUMBER() may select either film as
the latest unless a tie-breaker is specified.
*/

WITH ranked_films AS (
    SELECT
        actor_name,
        film_rating,
        release_date,
        ROW_NUMBER() OVER (
            PARTITION BY actor_name
            ORDER BY release_date DESC
        ) AS row_num
    FROM actor_rating_shift
),
latest AS (
    SELECT
        actor_name,
        film_rating AS latest_rating
    FROM ranked_films
    WHERE row_num = 1
),
previous AS (
    SELECT
        actor_name,
        AVG(film_rating) AS avg_rating
    FROM ranked_films
    WHERE row_num > 1
    GROUP BY actor_name
)
SELECT
    l.actor_name,
    ISNULL(p.avg_rating, l.latest_rating) AS avg_rating,
    l.latest_rating,
    ROUND(
        l.latest_rating - ISNULL(p.avg_rating, l.latest_rating),
        2
    ) AS rating_difference
FROM latest AS l
LEFT JOIN previous AS p
    ON l.actor_name = p.actor_name
ORDER BY actor_name;
