from db.run_sql import run_sql

from models.topic import Topic
import repositories.topic_repository as topic_repository

from models.difficulty import Difficulty
import repositories.difficulty_repository as difficulty_repository

from models.question import Question
import repositories.question_repository as question_repository

from models.quiz import Quiz
import repositories.quiz_repository as quiz_repository

#save
def save(quiz):
    sql = "INSERT INTO quizzes (date, number_of_questions, difficulty_id, topic_id, question_list) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [quiz.date, quiz.number_of_questions, quiz.difficulty.id, quiz.topic.id, quiz.question_list]
    results = run_sql(sql, values)
    id = results[0]['id']
    quiz.id = id

#select
def select(id):
    sql = "SELECT * FROM quizzes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    difficulty = difficulty_repository.select(result["difficulty_id"])
    topic = topic_repository.select(result["topic_id"])

    if result is not None:
        quiz = Quiz(result["date"], result["number_of_questions"], difficulty, topic, result["question_list"])
    return quiz

#select-all
def select_all():
    quizzes = []
    sql = "SELECT * FROM quizzes"
    results = run_sql(sql)
    for result in results:
        difficulty = difficulty_repository.select(result["difficulty_id"])
        topic = topic_repository.select(result["topic_id"])
        quiz = Quiz(result["date"], result["number_of_questions"], difficulty, topic, result["question_list"], result["id"])
        quizzes.append(quiz)
    return quizzes

#delete
def delete(id):
    sql = "DELETE FROM quizzes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#delete-all
def delete_all():
    sql = "DELETE FROM quizzes"
    run_sql(sql)

#update
def update(quiz):
    sql = "UPDATE quizzes SET (date, number_of_questions, difficulty, topic, question_list) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [quiz.date, quiz.number_of_questions, quiz.difficulty.id, quiz.topic.id, quiz.question_list, quiz.id]
    run_sql(sql, values)