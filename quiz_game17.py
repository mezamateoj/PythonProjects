from quiz_gdata import question_data
class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class QuizBrain:

    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        self.current_question = self.q_list[self.q_number]
        self.q_number += 1
        self.user = input(f'Q.{self.q_number}: {self.current_question.text} (True / False): ')
        self.check_answer()

    def still_has_q(self):
        return self.q_number < len(self.q_list)

    def check_answer(self):
        if self.user.lower() == self.current_question.answer.lower():
            self.score += 1
            print('Thats right!')
        else:
            print('Thats wrong')
        print(f'The correct answer was: {self.current_question.answer}')
        print(f'Your current score is: {self.score}/{self.q_number}')
        print()


question_bank = []
for i in question_data:
    new_question = Question(i['text'], i['answer'])
    question_bank.append(new_question)  
    
quiz = QuizBrain(question_bank)
while quiz.still_has_q():
    quiz.next_question()

print('You have completed the quiz')
print(f'Your final score was: {quiz.score}/{quiz.q_number}')
