DROP TABLE IF EXISTS topics
DROP TABLE IF EXISTS quizzes
DROP TABLE IF EXISTS questions

CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    topic VARCHAR(255)
);

CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    question VARCHAR(255),
    correct_answer VARCHAR(255),
    alt_ans_1 VARCHAR(255),
    alt_ans_2 VARCHAR(255),
    alt_ans_3 VARCHAR(255),
    difficulty VARCHAR(255),
    topic_id SERIAL REFERENCES topics(id)
);

CREATE TABLE quiz (
    id SERIAL PRIMARY KEY,
    date VARCHAR(255),
    number_of_questions INT,
    difficulty VARCHAR(255),
    topic_id SERIAL REFERENCES topics(id)
);