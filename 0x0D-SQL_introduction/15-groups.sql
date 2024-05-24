-- count number of recore with the same score
SELECT `score`,
    COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY SCORE DESC;