from db.run_sql import run_sql

from models.difficulty import Difficulty
import repositories.difficulty_repository as difficulty_repository


#save
def save(difficulty):
    sql = "INSERT INTO difficulties (level) VALUES (%s) RETURNING id"
    values = [difficulty.level]
    results = run_sql(sql, values)
    id = results[0]['id']
    difficulty.id = id
    return difficulty

#select
def select(id):
    sql = "SELECT * FROM difficulties WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    difficulty = Difficulty(result["level"], result["id"])
    return difficulty

#select-all
def select_all():
    all_difficulties = []
    sql = "SELECT * FROM difficulties"
    results = run_sql(sql)
    for result in results:
        difficulty = Difficulty(result["level"], result["id"])
        all_difficulties.append(difficulty)
    return all_difficulties

#delete
def delete(id):
    sql = "DELETE FROM difficulties WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#delete-all
def delete_all():
    sql = "DELETE FROM difficulties"
    run_sql(sql)

#update
def update(topic):
    sql = "UPDATE difficulties SET (level) = (%s) WHERE id = %s"
    values = [difficulty.level, difficulty.id]
    run_sql(sql, values)
