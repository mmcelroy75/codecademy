--To see what survey table looks like:

SELECT *
FROM survey
LIMIT 10;


--To count responses to the individual survey questions:

SELECT response, 
  COUNT(DISTINCT user_id)
FROM survey 
WHERE question = '1. What are you looking for?'
GROUP BY response
ORDER BY 2 DESC;

SELECT response, 
  COUNT(DISTINCT user_id)
FROM survey 
WHERE question = '2. What''s your fit?'
GROUP BY response
ORDER BY 2 DESC;

SELECT response, 
  COUNT(DISTINCT user_id)
FROM survey 
WHERE question = '3. Which shapes do you like?'
GROUP BY response
ORDER BY 2 DESC;

SELECT response, 
  COUNT(DISTINCT user_id)
FROM survey 
WHERE question = '4. Which colors do you like?'
GROUP BY response
ORDER BY 2 DESC;

SELECT response, 
  COUNT(DISTINCT user_id)
FROM survey 
WHERE question = '5. When was your last eye exam?'
GROUP BY response
ORDER BY 2 DESC;

--Home Try-on Purchase funnel query:

WITH funnel AS (
  SELECT DISTINCT q.user_id AS 'ids',
    h.user_id IS NOT NULL AS 'is_home_try_on',
    h.number_of_pairs AS 'pairs',
    p.user_id IS NOT NULL AS 'is_purchase'
  FROM quiz AS q
  LEFT JOIN home_try_on AS h
    ON q.user_id = h.user_id
  LEFT JOIN purchase AS p
    ON p.user_id = q.user_id
)

--To analyze the funnel data:

SELECT COUNT(*),
  SUM(is_home_try_on), 
  SUM(is_purchase)
FROM funnel;

SELECT SUM(is_home_try_on),
  pairs,
  SUM(is_purchase)
FROM funnel
WHERE pairs = '3 pairs';

SELECT SUM(is_home_try_on),
  pairs,
  SUM(is_purchase)
FROM funnel
WHERE pairs = '5 pairs';
