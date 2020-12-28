""" SQL statement """

GET_SHORTENER = """
SELECT * FROM URL WHERE original_url = %s;
"""
