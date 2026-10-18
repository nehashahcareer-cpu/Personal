
/*
============================================================
Question: Free-to-Paid Conversion Within 14 Days
Platform: SQL Server (T-SQL)
Topic: Conditional Aggregation, LEFT JOIN, Date Functions
Difficulty: Medium
============================================================

PROBLEM:
--------
The Consumer Monetization team measures how many free users
upgrade to a paid plan within 14 days of signing up.

A user converts if they upgrade from their signup date through
the 14th day after signup, inclusive, at any time of day.

Some users upgrade multiple times; others never upgrade.

For each signup month, return:
1. First day of the signup month
2. Number of signups
3. Number of users who converted within 14 days
4. Conversion rate as a percentage

TABLES:
-------
ai_free_signups:
    signup_date DATE
    user_id     VARCHAR

ai_paid_upgrades:
    upgrade_id  VARCHAR
    upgraded_at DATETIME2
    user_id     VARCHAR


SOLUTION:
---------
*/

SELECT
    DATEFROMPARTS(
        YEAR(s.signup_date),
        MONTH(s.signup_date),
        1
    ) AS signup_month,

    COUNT(DISTINCT s.user_id) AS total_signups,

    COUNT(DISTINCT
        CASE
            WHEN u.upgraded_at >= s.signup_date
             AND u.upgraded_at < DATEADD(
                    DAY, 15, s.signup_date
                 )
            THEN s.user_id
        END
    ) AS converted_users,

    CAST(
        100.0 * COUNT(DISTINCT
            CASE
                WHEN u.upgraded_at >= s.signup_date
                 AND u.upgraded_at < DATEADD(
                        DAY, 15, s.signup_date
                     )
                THEN s.user_id
            END
        )
        / NULLIF(COUNT(DISTINCT s.user_id), 0)
        AS DECIMAL(5, 2)
    ) AS conversion_rate_pct

FROM ai_free_signups AS s

LEFT JOIN ai_paid_upgrades AS u
    ON u.user_id = s.user_id

GROUP BY
    DATEFROMPARTS(
        YEAR(s.signup_date),
        MONTH(s.signup_date),
        1
    )

ORDER BY signup_month;


/*
============================================================
REVISION SUMMARY
============================================================

1. DATEFROMPARTS(YEAR(date), MONTH(date), 1)
   Returns the first day of the signup month.

2. COUNT(DISTINCT user_id)
   Counts each user only once, even if they have multiple
   upgrade records.

3. Conditional aggregation
   CASE returns user_id only when the upgrade qualifies.
   COUNT(DISTINCT ...) ignores NULL values.

4. Inclusive 14-day window
   upgraded_at >= signup_date
   AND upgraded_at < DATEADD(DAY, 15, signup_date)

   The exclusive upper bound includes the entire 14th day,
   including all times and fractional seconds.

5. LEFT JOIN
   Retains users who never upgraded.

6. Conversion rate
   converted_users / total_signups * 100.0

   100.0 ensures decimal arithmetic.
   NULLIF prevents division by zero.

COMMON MISTAKES:
- Using OR instead of AND between date boundaries.
- Using <= DATEADD(DAY, 14, signup_date) with DATETIME2,
  which may exclude part of the 14th day.
- Using SUM(CASE ...) after a one-to-many join, which can
  count a user multiple times.
- Forgetting DISTINCT when counting unique users.
- Using INNER JOIN, which excludes users who never upgraded.
- Integer division when calculating percentages.

ASSUMPTION:
user_id identifies a unique signup user. If multiple signup
events per user are possible, clarify the intended metric.

============================================================
*/
