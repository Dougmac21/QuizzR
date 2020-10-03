class Question():
    def __init__(self, question, correct_answer, alt_ans_1, alt_ans_2, alt_ans_3,, difficulty, topic, id=None):
        self.question = question
        self.correct_answer = correct_answer
        self.alt_ans_1 = alt_ans_1
        self.alt_ans_2 = alt_ans_2
        self.alt_ans_3 = alt_ans_3
        self.difficulty = difficulty
        self.topic = topic
        self.id = id
