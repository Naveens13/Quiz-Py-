from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import ui

# Question bank to give to the user
question_bank=[]
for question in question_data:
    question_text=question["question"]
    question_answer=question["correct_answer"]
    qn=Question(question_text,question_answer)
    question_bank.append(qn)


quiz = QuizBrain(question_bank)
quiz_look = ui(quiz)
# giving the question to the user and checking the answer
while quiz.still_has_question():
    quiz.Next_question()

print(f"{quiz.score}/{quiz.question_number} is your score")