from flask import Blueprint, Flask, redirect, render_template, request

from models.user_topic import UserTopic
import repositories.user_topic_repository as user_topic_repository

user_topics_blueprint = Blueprint("user_topics", __name__)


#index
@user_topics_blueprint.route("/user_topics")
def all_user_topics():
    user_topics = user_topic_repository.select_all()
    return render_template("/user_topics/index.html", all_user_topics=user_topics)


#new
@user_topics_blueprint.route("/user_topics/new")
def new_user_topic():
    user_topics = user_topic_repository.select_all()
    return render_template("/user_topics/new.html", all_user_topics=user_topics)


#create
@user_topics_blueprint.route("/user_topics", methods=["POST"])
def create_user_topic():
    name = request.form["name"]
    new_user_topic = UserTopic(name)
    user_topic_repository.save(new_user_topic)
    return redirect("/user_topics")


#edit
@user_topics_blueprint.route("/user_topics/<id>/edit")
def edit_user_topic(id):
    user_topic = user_topic_repository.select(id)
    return render_template("/user_topics/edit.html", user_topic=user_topic)


#update
@user_topics_blueprint.route("/user_topics/<id>", methods = ["POST"])
def update_user_topic(id):
    name = request.form["name"]
    user_topic = UserTopic(name, id)
    user_topic_repository.update(user_topic)
    return redirect("/user_topics")


#show
@user_topics_blueprint.route("/user_topics/<id>", methods=["GET"])
def show_user_topic(id):
    user_topic = user_topic_repository.select(id)
    return render_template('/user_topics/show.html', user_topic=user_topic)


#delete
@user_topics_blueprint.route("/user_topics/<id>/delete", methods=["POST"])
def delete_user_topic(id):
    user_topic_repository.delete(id)
    return redirect("/user_topics")