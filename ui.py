from tkinter import *
from quiz_brain import QuizBrain
class ui:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Modified Quiz app")
        self.window.minsize(width=400, height=600)
        self.window.config(padx=20, pady=20, bg="#375362")
        # creating a label
        self.score_label = Label(text="Score:0",fg="white",padx=10, pady=10, bg="#375362",font=("Arial",20,"bold"))
        
        self.score_label.grid(row=0, column=1)

        # creating the canvas
        self.canvas = Canvas(width=400, height=300, bg="white")
        self.text =self.canvas.create_text(180, 100, width=370, text="Some question text", fill = "#375362",font = ("Arial", 20 ,"italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        # creating True buttons
        self.correct_photo = PhotoImage(file="true.png")
        self.correct_button = Button(image = self.correct_photo, bg="#375362",command=self.true_clicked)
        self.correct_button.grid(row=2, column=0)
       
        # creating false buttons
        self.wrong_photo = PhotoImage(file="false.png")
        self.wrong_button = Button( image = self.wrong_photo, bg="#375362",command=self.false_clicked)
        self.wrong_button.grid(row=2, column=1)
        
        self.get_next_question()
        self.window.mainloop()  
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score:{self.quiz.score}")
        if self.quiz.still_has_question():
            question_tex = self.quiz.Next_question()
            self.canvas.itemconfig(self.text, text= question_tex)
        else:
            self.canvas.itemconfig(self.text, text=f"You have finished the quiz,your total socore is {self.quiz.score}")
            self.wrong_button.config(state="disabled")
            self.correct_button.config(state="disabled")
    def true_clicked(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)


    def false_clicked(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            
        self.window.after(1000, self.get_next_question)