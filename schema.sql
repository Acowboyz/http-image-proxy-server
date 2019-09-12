-- Initialize the database.

DROP TABLE IF EXISTS apicounter;
--
--
CREATE TABLE apicounter (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  api_name TEXT UNIQUE NOT NULL,
  count INTEGER NOT NULL DEFAULT 0
);

INSERT INTO apicounter (api_name)
VALUES ('proxy')