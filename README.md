# URL shortener

## Summary

The purpose of this project is to develop a url shortener which could do:
 1. return shorter url from long url
 2. access long url from its shorter url
 3. mapping is stocked in Postgres DB
 4. users could have information by REST API
 5. automatically deprecate useless urls from url table
 6. Remove shorter url manually from database by REST API GET

It contains the following files and folders:
* url_shortener: core python code
* requirements.txt: all python library need
* CHANGELOG.md
* .docker: including init.sql which create table URL when postgres database initializes
* Dockerfile
* docker-compose.yml
* Makefile
* pylintrc
* README.md


## How to build and run code

* `make run`: to run the project.

* `make format`: to run black lib on all the code (code formatter)

* `make style`: pylint all the codes folders

* `make down: docker-compose down --volumes`: to remove declared named volumes

## Examples

1. Get shorter url from long url.
"""bash
curl -i -X POST -H "Content-Type: application/json" http://127.0.0.1:5000/shorten_url -d '{
    "url": "www.google.fr"
}' 
"""

2. Get long url from shorter url.
"""bash
curl -i -X POST -H "Content-Type: application/json" http://127.0.0.1:5000/original_url -d '{
    "shortened": "tJ~xVGlibms="
}' 
"""

3. open http://127.0.0.1:5000/tJ~xVGlibms=, you could get http://www.google.fr page.

 OR you could do 
"""bash
curl -i -X GET -H "Content-Type: application/json" http://127.0.0.1:5000/tJ~xVGlibms=
"""

4. You could access to database shortener by
"""bash
docker exec -ti url_shortener_postgres_1 psql -U shortener -W
"""
then password should be
"""bash
shortener
"""

Here is database and table information: 
"""bash
POSTGRES_USER=shortener
POSTGRES_PASSWORD=shortener
POSTGRES_DB=shortener
POSTGRES_HOST=localhost
"""
URL table is created by .docker/init.sql
"""bash
CREATE TABLE IF NOT EXISTS URL (
    shortener VARCHAR(255) NOT NULL,
    original_url VARCHAR(255) NOT NULL,
    created TIMESTAMP,
    updated TIMESTAMP,
   PRIMARY KEY (shortener, original_url)
);
"""

shortener=# \d+
                          List of relations
 Schema | Name | Type  |  Owner   | Persistence | Size  | Description 
--------+------+-------+----------+-------------+-------+-------------
 public | url  | table | shortener | permanent   | 16 kB | 
(1 row)

shortener=# select * from url;
  shortener   |     original_url     |          created           |          updated          
--------------+----------------------+----------------------------+---------------------------
 tJ~xVGlibms= | http://www.google.fr | 2020-09-27 18:39:54.649368 | 2020-09-27 18:41:54.64938
(1 row)

5. automatically deprecate useless urls from url table, useless urls means those are not searched more than DELTA time before now
by default, I give DELTA 60 seconds. it could be changed as we want.

6. remove shorter url manually from database
"""bash
127.0.0.1:5000/remove/tJ~xVGlibms=
"""

## Potential improvements

* Add unit test, integration test, functional test with test report by using py.test wutg --junitxml --cov

* Think about scaling apps, may need replace psycopg2 by asyncpg and asyncio python library

* Security and Authentification

* Think about more use cases: 

i.e. Store all user searching history per url for analytics
     Could do custom batch url, for example, we could give a company a batch of shorter urls which begin at same characters
     Remove original url manually from database by REST API

* may need expiration time in table as different urls may have different exiration time, use could definie expiration time

* try different cryptographic hash function such as MD5, Base 62

