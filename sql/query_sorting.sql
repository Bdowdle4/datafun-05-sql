-- 7. query_sorting.sql - use ORDER BY to sort data.

-- Sort authors based on first name
SELECT first, last
FROM authors
ORDER BY first ASC;