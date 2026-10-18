/*
Problem: Find Users Active for 3 Consecutive Days or More
Table: sf_events
Dialect: SQL Server (T-SQL)

Objective:
Find all users who were active on 3 or more consecutive calendar days.

Approach:
1. Deduplicate user_id and record_date to ensure each user contributes
   at most one record per calendar day.
2. Use ROW_NUMBER() partitioned by user_id and ordered by record_date.
3. Calculate a grouping key by subtracting the row number, in days,
   from record_date using DATEDIFF().
4. Consecutive dates produce the same grouping key.
5. Group by user_id and the calculated grouping key.
6. Use HAVING COUNT(*) >= 3 to identify streaks of at least 3 days.
7. Use DISTINCT in the final SELECT to return each qualifying user once.

Key Concepts:
- ROW_NUMBER(): Assigns a sequential number to each user's activity dates.
- DATEDIFF(): Calculates the difference in days between two dates.
- Gaps-and-islands technique: Groups consecutive dates using a common key.
- GROUP BY: Identifies each user's consecutive-day streaks.
- HAVING: Filters groups to retain streaks of at least 3 days.
- DISTINCT: Prevents a user from appearing more than once in the output.

Important:
- Deduplication is necessary if multiple events can occur for the same
  user on the same day.
- DENSE_RANK() assigns the same rank to duplicate dates, but does not
  by itself prevent duplicate rows from inflating COUNT(*).
- If the table guarantees one row per user per date, the initial
  deduplication step is unnecessary.

Complexity:
- Time: Depends on the execution plan; typically dominated by sorting
  and processing records for each user.
- Space: Depends on sorting and intermediate grouping requirements.
*/

WITH distinct_activity AS (
    SELECT DISTINCT
        user_id,
        record_date
    FROM sf_events
),
activity_groups AS (
    SELECT
        user_id,
        record_date,
        DATEDIFF(
            DAY,
            ROW_NUMBER() OVER (
                PARTITION BY user_id
                ORDER BY record_date
            ),
            record_date
        ) AS group_key
    FROM distinct_activity
)
SELECT DISTINCT
    user_id
FROM activity_groups
GROUP BY
    user_id,
    group_key
HAVING COUNT(*) >= 3;
