class Question():

    def __init__(self, the_question, correct_answer, alt_ans_1, alt_ans_2, alt_ans_3, difficulty_id, topic_id, used = False, id=None):
        self.the_question = the_question
        self.correct_answer = correct_answer
        self.alt_ans_1 = alt_ans_1
        self.alt_ans_2 = alt_ans_2
        self.alt_ans_3 = alt_ans_3
        self.difficulty_id = difficulty_id
        self.topic_id = topic_id
        self.used = used
        self.id = id
