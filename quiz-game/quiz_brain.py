# TODO 1: asking the questions
# TODO 2: checking if the answer correct
# TODO 3: checking if we're the end of quiz

class QuizBrain:

    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # Getting answer from the user, calling function to check answer
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer,current_question.answer)

    # Returns boolean if whether there is question remaining or not
    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    # Checking the answer, printing the score
    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("")










