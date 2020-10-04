import pdb

from models.topic import Topic
import repositories.topic_repository as topic_repository

from models.question import Question
import repositories.question_repository as question_repository

from models.quiz import Quiz
import repositories.quiz_repository as quiz_repository


topic_repository.delete_all()

topic_00 = Topic("General Knowledge")
topic_repository.save(topic_00)

topic_01 = Topic("Geography")
topic_repository.save(topic_01)

topic_02 = Topic("History")
topic_repository.save(topic_02)

topic_03 = Topic("Sport")
topic_repository.save(topic_03)

topic_04 = Topic("Science")
topic_repository.save(topic_04)

topic_05 = Topic("Literature")
topic_repository.save(topic_05)

topic_06 = Topic("Entertainment")
topic_repository.save(topic_06)

topic_repository.select_all()


question_repository.delete_all()

question_001 = Question("What is the capital of Scotland?", "Edinburgh", "Glasgow", "Dundee", "Stirling", "EASY", "Geography", False)
question_repository.save(question_001)

question_002 = Question("Who shot JFK?", "Lee Harey Oswald", "Eminem", "Dr Dre", "Easy-E", "EASY", "History", False)
question_repository.save(question_002)

question_003 = Question("Which team won the world cup in 1966?", "England", "Germany", "Australia", "Nigeria", "EASY", "Sport", False)
question_repository.save(question_003)

question_004 = Question("Who invented gravity?", "Isaac Newton", "Albert Einstein", "Jimmy Carter", "Meryl Streep", "EASY", "Science", False)
question_repository.save(question_004)

question_005 = Question("Who wrote Catch-22?", "Joseph Heller", "John Steinbeck", "Ernest Hemmingway", "Jane Austin", "MEDIUM", "Literature", False)
question_repository.save(question_005)

question_006 = Question("Who shot Mr Burns?", "Maggie Simpson", "Homer Simpson", "Marge Simpson", "Smithers", "EASY", "Entertainment", False)
question_repository.save(question_006)

question_repository.select_all()


quiz_repository.delete_all()

quiz_01 = Quiz("2020-01-01", 5, "EASY", "General Knowledge", [])
quiz_repository.save(quiz_01)

quiz_repository.select_all()


pdb.set_trace()
