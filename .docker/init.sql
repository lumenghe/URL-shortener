CREATE TABLE IF NOT EXISTS URL (
    shortener VARCHAR(255) NOT NULL,
    original_url VARCHAR(255) NOT NULL,
    created TIMESTAMP,
    updated TIMESTAMP,
   PRIMARY KEY (shortener, original_url)
);
