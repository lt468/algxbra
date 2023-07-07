CREATE TABLE highscores (
    ID INTEGER NOT NULL PRIMARY KEY,
    Name CHAR(255) NOT NULL DEFAULT 'anon',
    Easy INTEGER NOT NULL DEFAULT 0, 
    Medium INTEGER NOT NULL DEFAULT 0,
    Hard INTEGER NOT NULL DEFAULT 0
);