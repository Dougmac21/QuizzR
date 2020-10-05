from flask import Blueprint, Flask, redirect, render_template, request

from models.topic import Topic
import repositories.topic_repository as topic_repository

from models.difficulty import Difficulty
import repositories.difficulty_repository as difficulty_repository

from models.question import Question
import repositories.question_repository as question_repository

from models.quiz import Quiz
import repositories.quiz_repository as quiz_repository



quizzes_blueprint = Blueprint("quizzes", __name__)

#index
@quizzes_blueprint.route("/quizzes")
def all_quizzes():
    quizzes = quiz_repository.select_all()
    return render_template("/quizzes/index.html", all_quizzes=quizzes)

#new
@quizzes_blueprint.route("/quizzes/new")
def new_quiz():
    quizzes = quiz_repository.select_all()
    topics = topic_repository.select_all()
    difficulties = difficulty_repository.select_all()
    return render_template("/quizzes/new.html", all_quizzes=quizzes, all_topics=topics, all_difficulties=difficulties)

#create
@quizzes_blueprint.route("/quizzes", methods=["POST"])
def create_quiz():
    date = request.form["date"]
    number_of_questions = request.form["number_of_questions"]
    difficulty = request.form["difficulty"]
    topic = request.form["topic"]
    question_list = request.form["question_list"]
    new_quiz = Quiz(date, number_of_questions, difficulty, topic, question_list)
    quiz_repository.save(new_quiz)
    return redirect("/quizzes")

#edit
@quizzes_blueprint.route("/quizzes/<id>/edit")
def edit_quiz(id):
    quiz = quiz_repository.select(id)
    return render_template("/quizzes/edit.html", this_quiz=quiz)

#update
@quizzes_blueprint.route("/quizzes/<id>", methods = ["POST"])
def update_quiz(id):
    date = request.form["date"]
    number_of_questions = request.form["number_of_questions"]
    difficulty = request.form["difficulty"]
    topic = request.form["topic"]
    question_list = request.form["question_list"]
    quiz = Quiz(date, number_of_questions, difficulty, topic, question_list, id)
    quiz_repository.update(quiz)
    return redirect("/quizzes")

#delete
@quizzes_blueprint.route("/quizzes/<id>/delete", methods=["POST"])
def delete_quiz(id):
    quiz_repository.delete(id)
    return redirect("/quizzes")



