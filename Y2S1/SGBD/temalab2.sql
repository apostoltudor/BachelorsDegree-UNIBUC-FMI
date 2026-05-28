--ex 8
SELECT 
    t.title_id,
    t.title,
    CASE 
        WHEN EXISTS (
            SELECT 1
            FROM reservation r
            LEFT JOIN rental rn ON r.res_date = rn.book_date 
                               AND r.member_id = rn.member_id 
                               AND r.title_id = rn.title_id
            WHERE r.title_id = t.title_id AND rn.book_date IS NULL
        ) THEN 'Nu'
        ELSE 'Da'
    END AS imprumutat_la_rezervare
FROM 
    title t
ORDER BY 
    t.title_id;

--ex 9
SELECT 
    m.last_name || ' ' || m.first_name AS nume_membru,
    t.title AS titlu_film,
    COUNT(*) AS numar_imprumuturi
FROM 
    member m
JOIN rental r ON m.member_id = r.member_id
JOIN title t ON r.title_id = t.title_id
GROUP BY 
    m.member_id, m.last_name, m.first_name, t.title_id, t.title
HAVING 
    COUNT(*) > 0
ORDER BY 
    m.last_name, m.first_name, t.title;