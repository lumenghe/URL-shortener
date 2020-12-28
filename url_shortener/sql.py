""" SQL statement """

GET_SHORTENER = """
SELECT * FROM URL WHERE original_url = %s;
"""

GET_ORIGINAL_URL = """
SELECT * FROM URL WHERE shortener = %s;
"""

INSERT = """
INSERT INTO URL (shortener, original_url, created, updated)
VALUES (%s, %s, %s, %s);
"""

UPDATE = """
UPDATE URL 
SET updated = %s 
WHERE original_url = %s;
"""

DEPRECATION = """
DELETE FROM URL 
WHERE updated < %s;
"""

DELETE_SHORTENER = """
DELETE FROM URL 
WHERE shortener = %s;
"""

