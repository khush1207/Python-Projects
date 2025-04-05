from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    ques = Question(i["question"], i["correct_answer"])
    question_bank.append(ques)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz!\nYou final score is " f"{quiz.score}""/"f"{quiz.question_number}")

