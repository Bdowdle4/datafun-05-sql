-- 8. query_group_by.sql - use GROUP BY clause (and optionally with aggregation)

-- group books by the length of their titles
SELECT 
    CASE 
        WHEN LENGTH(title) < 10 THEN 'Short'
        WHEN LENGTH(title) >= 10 AND LENGTH(title) < 20 THEN 'Medium'
        ELSE 'Long'
    END AS length_of_title,
    COUNT(*) AS number_of_books
FROM 
    books
GROUP BY 
    length_of_title;