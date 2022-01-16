STATUS_QUERY = """
SELECT
    p.address,
    p.city,
    p.price,
    p.description,
    s.name,
    p.year
FROM status_history sh
LEFT JOIN status s ON s.id = sh.status_id
LEFT JOIN property p ON p.id = sh.property_id
WHERE s.name='{}'
AND (p.address IS NOT NULL OR p.address <> "")
AND (p.year IS NOT NULL OR p.year <> "")
AND (p.description IS NOT NULL OR p.description <> "")
AND (p.price IS NOT NULL OR p.price <> "0" or p.price <> 0)
ORDER BY sh.update_date DESC;
"""

CITY_QUERY = """
SELECT
    p.address,
    p.city,
    p.price,
    p.description,
    s.name,
    p.year
FROM status_history sh
LEFT JOIN status s ON s.id = sh.status_id
LEFT JOIN property p ON p.id = sh.property_id
WHERE p.city='{}'
AND (p.address IS NOT NULL OR p.address <> "")
AND (p.year IS NOT NULL OR p.year <> "")
AND (p.description IS NOT NULL OR p.description <> "")
AND (p.price IS NOT NULL OR p.price <> "0" or p.price <> 0)
ORDER BY sh.update_date DESC;
"""

CITY_YEAR_QUERY = """
SELECT
    p.address,
    p.city,
    p.price,
    p.description,
    s.name,
    p.year
FROM status_history sh
LEFT JOIN status s ON s.id = sh.status_id
LEFT JOIN property p ON p.id = sh.property_id
WHERE p.city='{}' AND p.year='{}'
AND (p.address IS NOT NULL OR p.address <> "")
AND (p.year IS NOT NULL OR p.year <> "")
AND (p.description IS NOT NULL OR p.description <> "")
AND (p.price IS NOT NULL OR p.price <> "0" or p.price <> 0)
ORDER BY sh.update_date DESC;
"""

CITY_YEAR_STATE_QUERY = """
SELECT
    p.address,
    p.city,
    p.price,
    p.description,
    s.name,
    p.year
FROM status_history sh
LEFT JOIN status s ON s.id = sh.status_id
LEFT JOIN property p ON p.id = sh.property_id
WHERE p.city='{}' AND p.year='{}' AND p.state='{}'
AND (p.address IS NOT NULL OR p.address <> "")
AND (p.year IS NOT NULL OR p.year <> "")
AND (p.description IS NOT NULL OR p.description <> "")
AND (p.price IS NOT NULL OR p.price <> "0" or p.price <> 0)
ORDER BY sh.update_date DESC;
"""

CITY_STATE_QUERY = """
SELECT
    p.address,
    p.city,
    p.price,
    p.description,
    s.name,
    p.year
FROM status_history sh
LEFT JOIN status s ON s.id = sh.status_id
LEFT JOIN property p ON p.id = sh.property_id
WHERE p.city='{}' AND p.state='{}'
AND (p.address IS NOT NULL OR p.address <> "")
AND (p.year IS NOT NULL OR p.year <> "")
AND (p.description IS NOT NULL OR p.description <> "")
AND (p.price IS NOT NULL OR p.price <> "0" or p.price <> 0)
ORDER BY sh.update_date DESC;
"""

YEAR_QUERY = """
SELECT
    p.address,
    p.city,
    p.price,
    p.description,
    s.name,
    p.year
FROM status_history sh
LEFT JOIN status s ON s.id = sh.status_id
LEFT JOIN property p ON p.id = sh.property_id
WHERE p.year='{}'
AND (p.address IS NOT NULL OR p.address <> "")
AND (p.year IS NOT NULL OR p.year <> "")
AND (p.description IS NOT NULL OR p.description <> "")
AND (p.price IS NOT NULL OR p.price <> "0" or p.price <> 0)
ORDER BY sh.update_date DESC;
"""

YEAR_STATE_QUERY = """
SELECT
    p.address,
    p.city,
    p.price,
    p.description,
    s.name,
    p.year
FROM status_history sh
LEFT JOIN status s ON s.id = sh.status_id
LEFT JOIN property p ON p.id = sh.property_id
WHERE p.year='{}' AND p.state='{}'
AND (p.address IS NOT NULL OR p.address <> "")
AND (p.year IS NOT NULL OR p.year <> "")
AND (p.description IS NOT NULL OR p.description <> "")
AND (p.price IS NOT NULL OR p.price <> "0" or p.price <> 0)
ORDER BY sh.update_date DESC;
"""

STATE_QUERY = """
SELECT
    p.address,
    p.city,
    p.price,
    p.description,
    s.name,
    p.year
FROM status_history sh
LEFT JOIN status s ON s.id = sh.status_id
LEFT JOIN property p ON p.id = sh.property_id
WHERE p.state='{}'
AND (p.address IS NOT NULL OR p.address <> "")
AND (p.year IS NOT NULL OR p.year <> "")
AND (p.description IS NOT NULL OR p.description <> "")
AND (p.price IS NOT NULL OR p.price <> "0" or p.price <> 0)
ORDER BY sh.update_date DESC;

"""

