import unittest

from models.question import Question
from models.quiz import Quiz
from models.topic import Topic
from models.difficulty import Difficulty

class DifficultyTest(unittest.TestCase):

    def setUp(self):
        self.difficulty = Difficulty("Difficult")


    def test_difficulty_level_exists(self):
        self.assertEqual("Difficult", self.difficulty.level)

    def test_new_difficulty_level_added(self):
        self.difficulty_2 = Difficulty("Very Difficult")
        self.assertEqual("Very Difficult", self.difficulty_2.level)