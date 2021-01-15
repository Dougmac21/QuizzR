import unittest

from models.question import Question
from models.quiz import Quiz
from models.topic import Topic
from models.user_topic import UserTopic
from models.difficulty import Difficulty


class QuestionTest(unittest.TestCase):

    def setUp(self):
        self.question = Question("What is 2 plus 2?", "4", "3", "2", "1", "EASY", "Science", False)

    def test_question_has_parameters(self):
        self.assertEqual("What is 2 plus 2?", self.question.the_question)
        self.assertEqual("4", self.question.correct_answer)
        self.assertEqual("3", self.question.alt_ans_1)
        self.assertEqual("2", self.question.alt_ans_2)
        self.assertEqual("1", self.question.alt_ans_3)
        self.assertEqual("EASY", self.question.difficulty)    
        self.assertEqual("Science", self.question.topic)
        self.assertEqual(False, self.question.used)

    def test_questions_can_be_added(self):
        self.question2 = Question("What is 3 plus 3?", "6", "5", "4", "3", "MEDIUM", "Maths", False)
        self.assertEqual("What is 3 plus 3?", self.question2.the_question)
        self.assertEqual("6", self.question2.correct_answer)
        self.assertEqual("5", self.question2.alt_ans_1)
        self.assertEqual("4", self.question2.alt_ans_2)
        self.assertEqual("3", self.question2.alt_ans_3)
        self.assertEqual("MEDIUM", self.question2.difficulty)    
        self.assertEqual("Maths", self.question2.topic)
        self.assertEqual(False, self.question2.used)