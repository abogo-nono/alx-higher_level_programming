-- list only the best user base on thier score
SELECT `score`,
    `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;