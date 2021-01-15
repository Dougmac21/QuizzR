from db.run_sql import run_sql

from models.user_topic import UserTopic
import repositories.user_topic_repository as user_topic_repository


#save
def save(user_topic):
    sql = "INSERT INTO user_topics (name) VALUES (%s) RETURNING id"
    values = [user_topic.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user_topic.id = id
    return user_topic


#select
def select(id):
    sql = "SELECT * FROM user_topics WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    user_topic = UserTopic(result["name"], result["id"])
    return user_topic


#select-all
def select_all():
    user_topics = []

    sql = "SELECT * FROM user_topics"
    results = run_sql(sql)

    for result in results:
        user_topic = UserTopic(result["name"], result["id"])
        user_topics.append(user_topic)
    return user_topics


#delete
def delete(id):
    sql = "DELETE FROM user_topics WHERE id = %s"
    values = [id]
    run_sql(sql, values)


#delete-all
def delete_all():
    sql = "DELETE FROM user_topics"
    run_sql(sql)


#update
def update(user_topic):
    sql = "UPDATE user_topics SET (name) = (%s) WHERE id = %s"
    values = [user_topic.name, user_topic.id]
    run_sql(sql, values)