-- 7. query_sorting.sql - use ORDER BY to sort data.

-- Sort authors based on first name
SELECT first_name, last_name
FROM authors
ORDER BY first_name ASC;