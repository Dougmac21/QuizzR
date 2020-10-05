import unittest

from models.question import Question
from models.quiz import Quiz
from models.topic import Topic
from models.difficulty import Difficulty


class QuizTest(unittest.TestCase):
    def setUp(self):
        self.test_quiz = Quiz("2020-01-01", 5, "EASY", "General Knowledge", [])

    
    def test_quiz_has_parameters(self):
        self.assertEqual("2020-01-01", self.test_quiz.date)
        self.assertEqual(5, self.test_quiz.number_of_questions)
        self.assertEqual("EASY", self.test_quiz.difficulty)
        self.assertEqual("General Knowledge", self.test_quiz.topic)
        self.assertEqual([], self.test_quiz.question_list)

    