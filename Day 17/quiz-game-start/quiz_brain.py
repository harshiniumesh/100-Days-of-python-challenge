# 3.asking the question
# 4.checking if the answer was correct at end if the quiz
#8. check if user has answerd correctly or no- starts at line 25
class QuizBrain:

    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
#7starts from nxt line
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

        # if self.question_number < len(self.question_list): ...in a easy method can use simply return
        #     return True
        # else:
        #     return False


#5.create a method called next_question inside QuizBrain
#6.Retrieve the item at the current question_number from the question_list.use the input()function to show the user the Question text and ask for the user's answer.
#9. add a new attribute called score to the QuizBrain class and increment it by 1 when it gets correct
#10 add space to see clearly the each question and answer to see output- line 30

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect!")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is; {self.score}/{self.question_number}.")
        print('\n')


#11. create to tell the user have completed the challenge and final score number to scored number result--in main file