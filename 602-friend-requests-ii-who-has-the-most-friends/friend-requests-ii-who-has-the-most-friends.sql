# Write your MySQL query statement below
WITH all_friends AS (
    SELECT requester_id AS user_id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS user_id FROM RequestAccepted
),
friend_count AS (
    SELECT user_id, COUNT(*) AS num_friends
    FROM all_friends
    GROUP BY user_id
)
SELECT user_id AS id, num_friends as num
FROM friend_count
ORDER BY num_friends DESC
LIMIT 1;
