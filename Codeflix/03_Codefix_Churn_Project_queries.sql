{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf610
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \'971. \
\
SELECT *\
FROM subscriptions\
LIMIT 100;\
\
\'972.\
 \
SELECT MIN(subscription_start),\
  MAX(subscription_start)\
FROM subscriptions;\
\
\'973. \
\
WITH months AS\
(SELECT\
  '2017-01-01' AS first_day,\
  '2017-01-31' AS last_day\
UNION\
SELECT\
  '2017-02-01' AS first_day,\
  '2017-02-28' AS last_day\
UNION\
SELECT\
  '2017-03-01' AS first_day,\
  '2017-03-31' AS last_day\
),\
\
\'974.\
\
cross_join AS\
(SELECT *\
FROM subscriptions\
CROSS JOIN months),\
\
\'975. and 6. \
\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 status AS\
(SELECT id, \
  first_day AS month,\
  CASE\
    WHEN (subscription_start < first_day)\
      AND (subscription_end > first_day OR subscription_end IS NULL) AND (segment = 87) THEN 1\
    ELSE 0\
  END AS is_active_87,\
  CASE\
    WHEN (subscription_start < first_day)\
      AND (subscription_end > first_day OR subscription_end IS NULL) AND (segment = 30) THEN 1\
    ELSE 0\
  END AS is_active_30,\
  CASE\
    WHEN (subscription_end BETWEEN first_day AND last_day)\
      AND (segment = 87) THEN 1\
    ELSE 0\
  END AS is_canceled_87,\
  CASE\
    WHEN (subscription_end BETWEEN first_day AND last_day)\
      AND (segment = 30) THEN 1\
    ELSE 0\
  END AS is_canceled_30\
FROM cross_join\
), \
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 \
\'977. \
\
status_aggregate AS\
(SELECT month,\
  SUM(is_active_87) AS sum_active_87,\
  SUM(is_active_30) AS sum_active_30,\
  SUM(is_canceled_87) AS sum_canceled_87,\
  SUM(is_canceled_30) AS sum_canceled_30\
FROM status\
GROUP BY month)\
\
\'978. \
\
SELECT month,\
  1.0 * sum_canceled_87 / sum_active_87 AS churn_rate_87,\
  1.0 * sum_canceled_30 / sum_active_87 AS churn_rate_30\
FROM status_aggregate;\
\
\'979.\
\
status AS\
(SELECT id, \
  first_day AS month,\
  segment,\
  CASE\
    WHEN (subscription_start < first_day)\
      AND (subscription_end > first_day OR subscription_end IS NULL) THEN 1\
    ELSE 0\
  END AS is_active,\
  CASE\
    WHEN (subscription_end BETWEEN first_day AND last_day) THEN 1\
    ELSE 0\
  END AS is_canceled\
FROM cross_join\
), \
status_aggregate AS\
(SELECT month,\
  segment,\
  SUM(is_active) AS sum_active,\
  SUM(is_canceled) AS sum_canceled\
FROM status\
GROUP BY month, segment)\
\
SELECT\
  month,\
  segment,\
  AVG(1.0 * sum_canceled / sum_active) AS churn_rate\
FROM status_aggregate\
GROUP BY month, segment;\
\
\
}