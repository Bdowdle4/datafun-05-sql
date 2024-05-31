-- 6. query_filter.sql - use WHERE to filter data based on conditions.

-- filter book data based on year published
SELECT 
    *
FROM 
    books
WHERE 
    year_published > 1900;