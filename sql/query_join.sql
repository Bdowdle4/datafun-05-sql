-- 9. query_join.sql - use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.

SELECT authors.first, authors.last, books.title, books.year_published
FROM authors
INNER JOIN books ON authors.author_id = books.author_id;