from db.run_sql import run_sql

from models.topic import Topic
import repositories.topic_repository as topic_repository


#save
def save(topic):
    sql = "INSERT INTO topics (name) VALUES (%s) RETURNING id"
    values = [topic.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    topic.id = id
    return topic


#select
def select(id):
    sql = "SELECT * FROM topics WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    topic = Topic(result["name"], result["id"])
    return topic


#select-all
def select_all():
    all_topics = []

    sql = "SELECT * FROM topics"
    results = run_sql(sql)

    for result in results:
        topic = Topic(result["name"], result["id"])
        all_topics.append(topic)
    return all_topics


#delete
def delete(id):
    sql = "DELETE FROM topics WHERE id = %s"
    values = [id]
    run_sql(sql, values)


#delete-all
def delete_all():
    sql = "DELETE FROM topics"
    run_sql(sql)


#update
def update(topic):
    sql = "UPDATE topics SET (name) = (%s) WHERE id = %s"
    values = [topic.name, topic.id]
    run_sql(sql, values)