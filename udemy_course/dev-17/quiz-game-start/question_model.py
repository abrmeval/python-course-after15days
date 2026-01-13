class Question:
    # Constructor method
    # self represents the instance of the class
    # It binds the attributes with the given arguments
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

# new_q = Question("Is sky blue?", "True")
# print(new_q.text)
# print(new_q.answer)