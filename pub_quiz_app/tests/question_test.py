import unittest

from models.question import Question
from models.quiz import Quiz
from models.topic import Topic

class QuestionTest(unittest.TestCase):

    def setUp(self):
        self.question = Question("What is 2 plus 2?", "4", "3", "2", "1", "EASY", "Science")

    