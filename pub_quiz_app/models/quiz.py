class Quiz():
    def __init__(self, date, number_of_questions, difficulty, topic, the_question_list, correct_answer_list, alt_ans_1_list, alt_ans_2_list, alt_ans_3_list, id=None):
        self.date = date
        self.number_of_questions = number_of_questions
        self.difficulty = difficulty
        self.topic = topic
        self.the_question_list = []
        self.correct_answer_list = []
        self.alt_ans_1_list = []
        self.alt_ans_2_list = []
        self.alt_ans_3_list = []
        self.id = id

