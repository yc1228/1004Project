CREATE TABLE crime( 
	borough VARCHAR(50), 
	Year INT, 
	Count INT
);

LOAD DATA LOCAL INFILE "/Users/Christine/Desktop/borough_year.csv" INTO TABLE crime
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;

CREATE TABLE graduation(
	Year INT,
	borough VARCHAR(50), 
	Graduation DECIMAL
);

LOAD DATA LOCAL INFILE "/Users/Christine/Desktop/graduation_rate.csv" INTO TABLE graduation
    -> FIELDS TERMINATED BY ','
    -> ENCLOSED BY '"'
    -> LINES TERMINATED BY '\n'
    -> IGNORE 1 ROWS;

SELECT c.borough, c.Year, c.Count, g.Graduation
FROM crime c, graduation g
WHERE c.borough=g.borough and c.Year=g.Year;
