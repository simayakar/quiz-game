
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0


    def still_has_questions(self):
        if len(self.question_list) == self.question_number:
            return False
        else:
            return True


    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        u_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(u_answer, question.answer)

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's' wrong.")
        print(f"The correct answer was: {c_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")