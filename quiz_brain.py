import html
class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)
    
    def Next_question(self):
        self.current_question = self.question_list[self.question_number]
        q_tex = html.unescape(self.current_question.text)
        self.question_number += 1 
        return f"Q.{self.question_number}:-{q_tex}"
        # c_ans=input(f"Q.{self.question_number}:-{current_question.text}(True/False):")
    


        
    def check_answer(self,user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            print("!!You got it correct!!")
            self.score +=1
            return True
        else:
            print("!!You got it wrong!!")
            print(f"({self.score}/{self.question_number})")
            return False

