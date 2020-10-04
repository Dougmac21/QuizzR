DROP TABLE IF EXISTS topics;
DROP TABLE IF EXISTS difficulties;
DROP TABLE IF EXISTS quizzes;
DROP TABLE IF EXISTS questions;

CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE difficulties (
    id SERIAL PRIMARY KEY,
    level VARCHAR(10)
);

CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    the_question VARCHAR(255),
    correct_answer VARCHAR(255),
    alt_ans_1 VARCHAR(255),
    alt_ans_2 VARCHAR(255),
    alt_ans_3 VARCHAR(255),
    difficulty VARCHAR(255),
    topic VARCHAR(255),
    used BOOLEAN
);

CREATE TABLE quizzes (
    id SERIAL PRIMARY KEY,
    date VARCHAR(255),
    number_of_questions INT,
    difficulty VARCHAR(255),
    topic VARCHAR(255),
    question_list TEXT
);