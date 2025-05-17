import tkinter as tk
from PIL import Image, ImageTk # type: ignore
import random

# Initialize scores
user_score = 0
computer_score = 0

# Choices and images
choices = ["rock", "paper", "scissors"]
images = {}

def load_images():
    for choice in choices:
        img = Image.open(f"{choice}.png").resize((100, 100))
        images[choice] = ImageTk.PhotoImage(img)

def play(user_choice):
    result_label.config(text="Rock... Paper... Scissors...")
    window.after(1000, lambda: show_result(user_choice))

def show_result(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    # Set images
    user_image_label.config(image=images[user_choice])
    comp_image_label.config(image=images[computer_choice])

    # Determine winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text="Score - You: 0 | Computer: 0")
    user_image_label.config(image="")
    comp_image_label.config(image="")

# GUI Setup
window = tk.Tk()
window.title("Rock-Paper-Scissors")
window.geometry("400x500")
window.resizable(False, False)

# Load images
load_images()

# Labels
title = tk.Label(window, text="Rock-Paper-Scissors", font=("Arial", 18, "bold"))
title.pack(pady=10)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=12, command=lambda: play("rock"))
paper_btn = tk.Button(button_frame, text="Paper", width=12, command=lambda: play("paper"))
scissors_btn = tk.Button(button_frame, text="Scissors", width=12, command=lambda: play("scissors"))

rock_btn.grid(row=0, column=0, padx=5)
paper_btn.grid(row=0, column=1, padx=5)
scissors_btn.grid(row=0, column=2, padx=5)

# Image Displays
img_frame = tk.Frame(window)
img_frame.pack(pady=10)

user_image_label = tk.Label(img_frame)
user_image_label.grid(row=0, column=0, padx=20)

comp_image_label = tk.Label(img_frame)
comp_image_label.grid(row=0, column=1, padx=20)

# Result and Score
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

score_label = tk.Label(window, text="Score - You: 0 | Computer: 0", font=("Arial", 12, "bold"))
score_label.pack(pady=5)

# Reset Button
reset_btn = tk.Button(window, text="Reset Game", command=reset_game, bg="red", fg="white")
reset_btn.pack(pady=10)

window.mainloop()
