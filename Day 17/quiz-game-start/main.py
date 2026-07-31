#2.creating question bank on question objects
#7. create a new method which is going to be called still_has_question, return a boolean depending on the value of question_number.
#use the while loop to show the next question until the end

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[0].answer).2

# QuizBrain(question_bank) .3

# quiz = QuizBrain(question_bank)
# quiz.next_question() .4

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quizz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")