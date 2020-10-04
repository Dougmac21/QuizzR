import unittest

from models.question import Question
from models.quiz import Quiz
from models.topic import Topic

class TopicTest(unittest.TestCase):

    def setUp(self):
        self.topic = Topic("Test Topic")

    