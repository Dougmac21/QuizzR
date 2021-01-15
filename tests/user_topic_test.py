import unittest

from models.question import Question
from models.quiz import Quiz
from models.topic import Topic
from models.user_topic import UserTopic
from models.difficulty import Difficulty


class UserTopicTest(unittest.TestCase):

    def setUp(self):
        self.user_topic = UserTopic("Test User_Topic")


    def test_user_topic_exists(self):
        self.assertEqual("Test User_Topic", self.user_topic.name)

    def test_new_user_topic_added(self):
        self.user_topic_1 = UserTopic("Everton Football Club")
        self.assertEqual("Everton Football Club", self.user_topic_1.name)
