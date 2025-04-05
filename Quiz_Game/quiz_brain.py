class QuizBrain:
    def __init__(self, qlist):
        self.question_number = 0
        self.question_list = qlist
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        currentques = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {currentques.text} (True/False): ").lower()
        self.check_answer(ans, currentques.answer)

    def check_answer(self, ans, correctans):

        if ans == correctans.lower():
            print("You got it right!")
            self.score += 1
            print("Your score is " f"{self.score}""/"f"{self.question_number}\n\n")

        else:
            print(f"It is wrong.\nThe correct answer was {correctans}")
            print("Your score is " f"{self.score}""/"f"{self.question_number}\n\n")

