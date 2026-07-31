#1.create a question class with an __init()__ method with two attributes: text and answer attribute

class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

# new_q = Question("sdfsdf", "False")
# print(new_q.text)

#2.creating question bank on question objects