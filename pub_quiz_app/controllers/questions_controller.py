from flask import Blueprint, Flask, redirect, render_template, request

from models.topic import Topic
import repositories.topic_repository as topic_repository

from models.difficulty import Difficulty
import repositories.difficulty_repository as difficulty_repository

from models.question import Question
import repositories.question_repository as question_repository

questions_blueprint = Blueprint("questions", __name__)

#index
@questions_blueprint.route("/questions")
def all_questions():
    questions = question_repository.select_all()
    return render_template("/questions/index.html", all_questions=questions)

#new
@questions_blueprint.route("/questions/new")
def new_question():
    questions = question_repository.select_all()
    topics = topic_repository.select_all()
    difficulties = difficulty_repository.select_all()
    return render_template("/questions/new.html", all_questions=questions, all_topics=topics, all_difficulties=difficulties)

#create
@questions_blueprint.route("/questions", methods=["POST"])
def create_question():
    the_question = request.form["the_question"]
    correct_answer = request.form["correct_answer"]
    alt_ans_1 = request.form["alt_ans_1"]
    alt_ans_2 = request.form["alt_ans_2"]
    alt_ans_3 = request.form["alt_ans_3"]

    difficulty_id = request.form["difficulty"]
    difficulty = difficulty_repository.select(difficulty_id)

    topic_id = request.form["topic"]
    topic = topic_repository.select(topic_id)

    used = False

    new_question = Question(the_question, correct_answer, alt_ans_1, alt_ans_2, alt_ans_3, difficulty, topic, used)
    question_repository.save(new_question)
    return redirect("/questions")

#edit
@questions_blueprint.route("/questions/<id>/edit")
def edit_question(id):
    question = question_repository.select(id)
    topics = topic_repository.select_all()
    difficulties = difficulty_repository.select_all()
    return render_template('/questions/edit.html', question=question, all_topics=topics, all_difficulties=difficulties)


#update
@questions_blueprint.route("/questions/<id>", methods=["PUT"])
def update_question(id):
    the_question = request.form["the_question"]
    correct_answer = request.form["correct_answer"]
    alt_ans_1 = request.form["alt_ans_1"]
    alt_ans_2 = request.form["alt_ans_2"]
    alt_ans_3 = request.form["alt_ans_3"]

    difficulty_id = request.form["difficulty"]
    difficulty = difficulty_repository.select(difficulty_id)

    topic_id = request.form["topic"]
    topic = topic_repository.select(topic_id)

    question = Question(the_question, correct_answer, alt_ans_1, alt_ans_2, alt_ans_3, difficulty, topic, id)
    question_repository.update(question)
    return redirect("/questions")

#show
# show goes here


#delete
@questions_blueprint.route("/questions/<id>/delete", methods=["POST"])
def delete_question(id):
    question_repository.delete(id)
    return redirect("/questions")
