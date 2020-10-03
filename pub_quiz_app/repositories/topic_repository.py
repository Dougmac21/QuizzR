from db.run_sql import run_sql
from models.topic import Topic

#save
def save(topic)
    sql = "INSERT INTO topics (topic) VALUES (%s) RETURNING id"
    values = [topic.topic]
    results = run_sql(sql, values)
    id = results[0]['id']
    zombie.id = id


#select
def select(id):
    sql = "SELECT * FROM topics WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    topic = Topic(result["topic"])
    return topic

#select-all
def select_all():
    topics = []
    sql = "SELECT * FROM topics"
    results = run_sql(sql)
    for result in results:
        topic = Topic(result["topic"], result["id"])
        topics.append(topic)
    return topics

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
    sql = "UPDATE topics SET (topic) = (%s) WHERE id = %s"
    values = [topic.topic, topic.id]
    run_sql(sql, values)


## select quizzes of topic
# extension