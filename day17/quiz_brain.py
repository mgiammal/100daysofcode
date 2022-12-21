class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        """
        Checks if there are questions left in the question list
        :return:
        """
        return self.question_number < len(self.questions_list)

    def next_question(self):
        """
        Pull up question from list depending on current question number
        :return:
        """
        current_question = self.questions_list[self.question_number]
        question = current_question.text
        answer = current_question.answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question} (True/False)?: ")
        self.check_answer(user_answer, answer)

    def check_answer(self, user_answer, correct_answer):
        """
        Checks user answer vs correct answer
        :param user_answer:
        :param correct_answer:
        :return:
        """
        if user_answer.lower() is correct_answer.lower():
            print("You got the answer right!")
        else:
            print("The answer was incorrect")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")

