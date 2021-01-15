DROP TABLE IF EXISTS quizzes;
DROP TABLE IF EXISTS questions;
DROP TABLE IF EXISTS user_topics;
DROP TABLE IF EXISTS topics;
DROP TABLE IF EXISTS difficulties;


CREATE TABLE difficulties (
    id SERIAL PRIMARY KEY,
    level VARCHAR(10)
);

CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE user_topics (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    the_question VARCHAR(255),
    correct_answer VARCHAR(255),
    alt_ans_1 VARCHAR(255),
    alt_ans_2 VARCHAR(255),
    alt_ans_3 VARCHAR(255),
    difficulty_id INT REFERENCES difficulties(id),
    topic_id INT REFERENCES topics(id),
    user_topic_id INT REFERENCES user_topics(id),
    used BOOLEAN
);

CREATE TABLE quizzes (
    id SERIAL PRIMARY KEY,
    date DATE,
    number_of_questions INT,
    difficulty_id INT REFERENCES difficulties(id),
    topic_id INT REFERENCES topics(id),
    user_topic_id INT REFERENCES user_topics(id),
    question_list TEXT
    -- ALTER TABLE ADD COLUMN FOR EACH QUESTION/ANS1/2/3/4
);