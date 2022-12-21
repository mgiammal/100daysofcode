from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q_data in question_data:
    question_bank.append(Question(q_data.get("text"), q_data.get("answer")))

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()
