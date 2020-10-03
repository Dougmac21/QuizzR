from flask import Flask, render_template

from controllers.topics_controller import topic_blueprint
from controllers.questions_controller import question_blueprint
from controllers.quiz_controller import quiz_blueprint

app = Flask(__name__)

app.register_blueprint(question_blueprint)
app.register_blueprint(quiz_blueprint)
app.register_blueprint(topic_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__== '__main__':
    app.run()

