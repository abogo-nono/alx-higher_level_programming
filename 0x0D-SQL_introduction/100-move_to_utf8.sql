-- A  script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
-- Step 1: Convert the database to UTF-8
ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Step 2: Convert the table to UTF-8
ALTER TABLE `hbtn_0c_0`.`first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Step 3: Convert the field to UTF-8
ALTER TABLE `hbtn_0c_0`.`first_table`
MODIFY COLUMN `name` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;