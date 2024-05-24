-- list all records (score, name) and skip those who don't have a value for name
SELECT `score`,
    `name`
FROM `second_table`
WHERE `name` != ''
ORDER BY `score` DESC;