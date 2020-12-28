""" SQL statement """

GET_SHORTENER = """
SELECT * FROM URL WHERE original_url = %s;
"""

GET_ORIGINAL_URL = """
SELECT * FROM URL WHERE shortener = %s;
"""

