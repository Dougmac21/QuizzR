import unittest

from models.question import Question
from models.quiz import Quiz
from models.topic import Topic
from models.user_topic import UserTopic
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

    def test_quiz_can_be_added(self):
        self.test_quiz_2 = Quiz("2020-02-02", 10, "MEDIUM", "Geography", [])
        self.assertEqual("2020-02-02", self.test_quiz_2.date)
        self.assertEqual(10, self.test_quiz_2.number_of_questions)
        self.assertEqual("MEDIUM", self.test_quiz_2.difficulty)
        self.assertEqual("Geography", self.test_quiz_2.topic)
        self.assertEqual([], self.test_quiz_2.question_list)