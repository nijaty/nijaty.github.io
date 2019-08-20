CREATE TABLE students(
id SERIAL PRIMARY KEY,
name VARCHAR(200),
surname VARCHAR(200),
email VARCHAR(200) UNIQUE,
birthday DATE,
point VARCHAR(200),
join_date DATE DEFAULT NOW()
);

