class Quiz():
    def __init__(self, date, number_of_questions, difficulty, topic, question_list, id=None):
        self.date = date
        self.number_of_questions = number_of_questions
        self.difficulty = difficulty
        self.topic = topic
        self.question_list = []
        self.id = id