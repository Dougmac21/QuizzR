from db.run_sql import run_sql

from models.topic import Topic
import repositories.topic_repository as topic_repository

from models.question import Question
import repositories.question_repository as question_repository

from models.quiz import Quiz
import repositories.quiz_repository as quiz_repository


#save
def save(question):
    sql = "INSERT INTO questions (question, correct_answer, alt_ans_1, alt_ans_2, alt_ans_3, difficulty, topic, used) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [question.the_question, question.correct_answer, question.alt_ans_1, question.alt_ans_2, question.alt_ans_3, question.difficulty, question.topic, question.used]
    results = run_sql(sql, values)
    id = results[0]['id']
    question.id = id


#select
def select(id):
    sql = "SELECT * FROM questions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    question = Question(result["the_question"], result["correct_answer"], result["alt_ans_1"], result["alt_ans_2"], result["alt_ans_3"], result["difficulty"], result["topic"], result["used"], result["id"])
    return question


#select-all
def select_all():
    questions = []
    sql = "SELECT * FROM questions"
    results = run_sql(sql)
    for result in results:
        question = Question(result["the_question"], result["correct_answer"], result["alt_ans_1"], result["alt_ans_2"], result["alt_ans_3"], result["difficulty"], result["topic"], result["used"], result["id"])
        questions.append(question)
    return questions


#delete
def delete(id):
    sql = "DELETE FROM questions HERE is = %s"
    values = [id]
    run_sql(sql, values)


#delete-all
def delete_all():
    sql = "DELETE FROM questions"
    run_sql(sql)


#update
def update(question):
    sql = "UPDATE questions SET (the_question, correct_answer, alt_ans_1, alt_ans_2, alt_ans_3, difficulty, topic) = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [question.the_question, question.correct_answer, question.alt_ans_1, question.alt_ans_2, question.alt_ans_3, question.difficulty, question.topic, question.used, question.id]
    run_sql(sql, values)

