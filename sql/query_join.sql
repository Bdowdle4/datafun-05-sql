-- 9. query_join.sql - use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.

SELECT authors.first, authors.last, books.year_published, books.title,
FROM authors
INNER JOIN books ON authors.author_id = books.author_id;