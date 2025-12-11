-- # Write your MySQL query statement below
-- select distinct player_id, min(event_date) as first_login from Activity group by player_id;
SELECT player_id, MIN(event_date) first_login
FROM Activity
GROUP BY 1;
