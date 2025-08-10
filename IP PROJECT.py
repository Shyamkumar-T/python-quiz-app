import tkinter as tk
from tkinter import messagebox

# Define the quiz questions and answers
questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "What is the largest mammal on Earth?",
       "In which year did Christopher Columbus reach the America?",
    "what is the capital of india?",
    "how many alphabets are there?",
    "how many states are there in india",
    "how many union territories are there in india",
    "how many consonants are there in alphabets?",
    "what is the national bird of india?",
    
]

answers = [
    ["Paris", "London", "Berlin", "Rome"],
    ["Mars", "Venus", "Jupiter", "Saturn"],
    ["Blue Whale", "Elephant", "Giraffe", "Hippopotamus"],
    ["1492", "1607", "1776", "1812"],
    ["delhi","vishakapatnam","tamil nadu","rajasthan"],
    ["26","25","45","37"],
    ["27","28","30","32"],
    ["7","8","9","10"],
    ["20","21","22","19"],
    ["tiger","duck","peacock","ostrich"]
]

correct_answers = [0, 0, 0, 0,0,0,1,1,1,2]  # Index of the correct answer for each question

# Initialize variables
current_question = 0
score = 0

# Function to check the selected answer
def check_answer():
    global current_question, score
    selected_option = option_var.get()
    if selected_option == correct_answers[current_question]:
        score += 1

    current_question += 1

    if current_question < len(questions):
        update_question()
    else:
        messagebox.showinfo("Quiz Over", f"You scored {score}/{len(questions)}")

# Function to update the question and options
def update_question():
    question_label.config(text=questions[current_question])
    for i, option in enumerate(option_labels):
        option.config(text=answers[current_question][i])
    option_var.set(-1)

# Create the main window
window = tk.Tk()
window.title("Quiz App")

# Create widgets

question_label = tk.Label(window, text="", font=("Helvetica", ))
option_var = tk.IntVar()
option_labels = []

for i in range(4):
    option = tk.Radiobutton(
        window, text="", variable=option_var, value=i, font=("Helvetica", 10)
    )
    option_labels.append(option)

next_button = tk.Button(
    window, text="Next", command=check_answer, font=("Helvetica", 12)
)

# Arrange widgets using grid layout
question_label.grid(row=0, column=0, columnspan=2, pady=10)
for i, option in enumerate(option_labels):
    option.grid(row=i + 1, column=0, columnspan=2, padx=10, pady=5)
next_button.grid(row=5, column=0, columnspan=2, pady=10)

# Start the quiz
update_question()

window.mainloop()