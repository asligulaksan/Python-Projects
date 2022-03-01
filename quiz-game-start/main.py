from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# creating the question bank
question_bank=[]
for item in question_data:
    text = item["question"]
    answer = item["correct_answer"]
    Q = Question(text,answer)
    question_bank.append(Q)

quiz = QuizBrain(question_bank)

# loop through all the questions in the question bank
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")

