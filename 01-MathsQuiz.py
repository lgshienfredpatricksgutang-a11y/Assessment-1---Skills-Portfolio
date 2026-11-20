import tkinter as tk
import random
from tkinter import messagebox

class MathsQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Maths Quiz")
        self.root.geometry("400x300")

        self.score = 0
        self.question_count = 0
        self.current_answer = 0
        self.attemps = 0
        self.difficulty = 1


        self.menu_frame = tk.Frame(root)
        self.quiz_frame = tk.Frame(root)
        self.result_frame = tk.Frame(root)

        for frame in (self.menu_frame, self.quiz_frame, self.result_frame):
            frame.grid(row=0, column=0, sticky='nsew')

        self.displayMenu()
        self.setup_quiz()
        self.setup_result()

    def displayMenu(self):
        for widget in self.menu_frame.winfo_children():
            widget.destroy()

        tk.Label(self.menu_frame, text='DIFFICULTY LEVEL', font=('Arial', 14, 'bold')).pack (pady=20)

        tk.Button(self.menu_frame, text='1. Easy (1 digit)', width=20,
                  command=lambda: self.start_quiz(1)).pack(pady=5)

        tk.Button(self.menu_frame, text='2. Moderate (2 digits)', width=20,
                  command= lambda: self.start_quiz(2)).pack(pady=5)

        tk.Button(self.menu_frame, text='3. Advance (4 digits)', width=20,
                  command=lambda: self.start_quiz(3)).pack(pady=5)

        self.menu_frame.tkraise()

    def start_quiz(self, difficulty):
        self.difficulty = difficulty
        self.score = 0
        self.question_count = 0
        self.next_question()

    def randomInt(self):
        if self.difficulty == 1:
            return random.randint(1, 9)
        elif self.difficulty == 2:
            return random.randint(10, 99)
        else:
            return random.randint(1000, 9999)

    def decideOperation(self):
        return random.choice(['+', '-'])

    def setup_quiz(self):
        self.q_label = tk.Label(self.quiz_frame, text='', font=('Arial', 18))
        self.q_label.pack(pady=20)

        self.ans_entry = tk.Entry(self.quiz_frame, font=('Arial', 14))
        self.ans_entry.pack(pady=10)

        self.submit_btn = tk.Button(self.quiz_frame, text='Submit', command=self.isCorrect)

        self.submit_btn.pack(pady=10)

        self.feedback_label = tk.Label(self.quiz_frame, text='', fg= 'red')
        self.feedback_label.pack(pady=10)

    def displayProblem(self):
        num1 = self.randomInt()
        num2 = self.randomInt()
        operation = self.decideOperation()

        self.current_answer = num1 + num2 if operation == '+' else num1 - num2
        self.q_label.config(text=f'{num1} {operation} {num2} =')
        self.ans_entry.delete(0, tk.END)
        self.attemps = 1

    def next_question(self):
        if self.question_count >= 10:
            self.displayResults()
        else:
            self.question_count += 1
            self.quiz_frame.tkraise()
            self.feedback_label.config(text='')
            self.displayProblem()

    def isCorrect(self):

        try:
            user_ans = int(self.ans_entry.get())
        except ValueError:
            self.feedback_label.config(text='Please enter a valid number!')
            return

        if user_ans == self.current_answer:
            if self.attemps == 1:
                self.score += 10
                self.feedback_label.config(text='Correct! 10 points.', fg='green')
            else:
                self.score += 5
                self.feedback_label.config(text='Correct on 2nd try! 5 points.', fg='green')

            self.root.after(1000, self.next_question)

        else:
            if self.attemps == 1:
                self.attemps = 2
                self.feedback_label.config(text='Wrong! Trytt again.', fg='red')
                self.ans_entry.delete(0, tk.END)
            else:
                self.feedback_label.config(text=f'Wrong! The Answer was {self.current_answer}.', fg='red')
                self.root.after(1500, self.next_question)

    def setup_result(self):
        self.result_label = tk.Label(self.result_frame, text='', font=('Arial', 16))
        self.result_label.pack(pady=20)

        self.rank_label = tk.Label(self.result_frame, text='', font=('Arial', 14, 'bold'))
        self.rank_label.pack(pady=10)

        tk.Button(self.result_frame, text='Play Again', command=self.displayMenu).pack(pady=20)

    def displayResults(self):
        self.result_frame.tkraise()
        self.result_label.config(text=f"Quiz is Over!\nYour Score: {self.score}/100")

        if self.score >= 90:
            rank = 'A+'
        elif self.score >= 80:
            rank = 'A'
        elif self.score >= 70:
            rank = 'B'
        elif self.score >= 60:
            rank = 'C'
        elif self.score >= 50:
            rank = 'D'
        else :
            rank = 'F'

        self.rank_label.config(text=f'Rank: {rank}')

if __name__ == '__main__':
    root = tk.Tk()
    app = MathsQuiz(root)
    root.mainloop()
        
        








