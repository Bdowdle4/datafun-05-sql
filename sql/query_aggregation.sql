-- 5. query_aggregation.sql - use aggregation functions including COUNT, AVG, SUM.

SELECT
Count(*) as total_books,
AVG(year_published) as average_year_published,
MIN(year_published) as oldest_book_published,
MAX(year_published) as newest_book_published
FROM books;