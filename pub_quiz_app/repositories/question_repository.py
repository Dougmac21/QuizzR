from db.run_sql import run_sql
from models.question import Question


#save
def save(question):
    sql = "INSEERT INTO questions (question, correct_answer, alt_ans_1, alt_ans_2, alt_ans_3, difficulty, topic) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [question.question, question.correct_answer, question.alt_ans_1, question.alt_ans_2, question.alt_ans_3, question.difficulty, question.topic]
    results = run_sql(sql, values)
    id = results[0]['id']
    question.id = id


#select
def select(id):
    sql = "SELECT * FROM questions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    question = Question(result["question"], result["correct_answer"], result["alt_ans_1"], result["alt_ans_2"], result["alt_ans_3"], result["difficulty"], result["topic"], result["id"])
    return question


#select-all
def select_all():
    questions = []
    sql = "SELECT * FROM questions"
    results = run_sql(sql)
    for result in results:
        question = Question(result["question"], result["correct_answer"], result["alt_ans_1"], result["alt_ans_2"], result["alt_ans_3"], result["difficulty"], result["topic"], result["id"])
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
    sql = "UPDATE questions SET (question, correct_answer, alt_ans_1, alt_ans_2, alt_ans_3, difficulty, topic) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [question.question, question.correct_answer, question.alt_ans_1, question.alt_ans_2, question.alt_ans_3, question.difficulty, question.topic, question.id]
    run_sql(sql, values)

