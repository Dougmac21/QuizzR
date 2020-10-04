import unittest

from models.question import Question
from models.quiz import Quiz
from models.topic import Topic

class QuestionTest(unittest.TestCase):

    def setUp(self):
        self.question = Question("What is 2 plus 2?", "4", "3", "2", "1", "EASY", "Science")

    def test_question_has_parameters(self):
        self.assertEqual("What is 2 plus 2?", self.question.the_question)
        self.assertEqual("4", self.question.correct_answer)
        self.assertEqual("3", self.question.alt_ans_1)
        self.assertEqual("2", self.question.alt_ans_2)
        self.assertEqual("1", self.question.alt_ans_3)
        self.assertEqual("EASY", self.question.difficulty)    
        self.assertEqual("Science", self.question.topic)