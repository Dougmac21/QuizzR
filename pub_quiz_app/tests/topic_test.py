import unittest

from models.question import Question
from models.quiz import Quiz
from models.topic import Topic
from models.difficulty import Difficulty


class TopicTest(unittest.TestCase):

    def setUp(self):
        self.topic = Topic("Test Topic")


    def test_topic_exists(self):
        self.assertEqual("Test Topic", self.topic.name)

    def test_new_topic_added(self):
        self.topic_1 = Topic("Anthropology")
        self.assertEqual("Anthropology", self.topic_1.name)
