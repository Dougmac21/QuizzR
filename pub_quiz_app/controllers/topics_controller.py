from flask import Blueprint, Flask, redirect, render_template, request

from models.topic import Topic
import repositories.topic_repository as topic_repository

topics_blueprint = Blueprint("topics", __name__)


#index
@topics_blueprint.route("/topics")
def all_topics():
    topics = topic_repository.select_all()
    return render_template("/topics/index.html", all_topics=topics)


#new
@topics_blueprint.route("/topics/new")
def new_topic():
    topics = topic_repository.select_all()
    return render_template("/topics/new.html", all_topics=topics)


#create
@topics_blueprint.route("/topics", methods=["POST"])
def create_topic():
    name = request.form["name"]
    new_topic = Topic(name)
    topic_repository.save(new_topic)
    return redirect("/topics")


#edit
@topics_blueprint.route("/topics/<id>/edit")
def edit_topic(id):
    topic = topic_repository.select(id)
    return render_template("/topics/edit.html", topic=topic)


#update
@topics_blueprint.route("/topics/<id>", methods = ["POST"])
def update_topic(id):
    name = request.form["name"]
    topic = Topic(name, id)
    topic_repository.update(topic)
    return redirect("/topics")


#show
@topics_blueprint.route("/topics/<id>" methods=["GET"])
def show_topic(id):
    topic = topic_repository.select(id)
    return render_template('/topics/show.html', topic=topic)


#delete
@topics_blueprint.route("/topics/<id>/delete", methods=["POST"])
def delete_topic(id):
    topic_repository.delete(id)
    return redirect("/topics")