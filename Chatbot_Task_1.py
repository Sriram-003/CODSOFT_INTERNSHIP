import tkinter as tk
from PIL import Image,ImageTk
from tkinter import scrolledtext
from datetime import datetime
from nltk import punkt
import re
import random

class RuleBasedChatbot:
    def __init__(self):
        self.rules = [
            (r'hi|hello',['Hello Sir,','Greetings','Hey!']),
            (r'what is your name',["I'm a rule based chatbot"]),
            (r'bye|exit',['Goodbye!','See you later!']),
            (r'help|what is your role',['I can tell some basic definition \nof technical words and basic arithmetical operations']),
            (r'what is photosynthesis', ["Photosynthesis is the process by which green plants and \nsome other organisms use sunlight to synthesize foods with the help of chlorophyll."]),
            (r'what is gravity',["Gravity is a force that attracts two bodies towards each other, the \nforce that causes apples to fall towards the ground."]),
            (r'what is an atom', ["An atom is the smallest unit of ordinary matter that forms a chemical \nelement. Each atom consists of a nucleus and one or more electrons."]),
            (r'what is the speed of light',["The speed of light in a vacuum is approximately \n299,792 kilometers per second (186,282 miles per second)."]),
            (r'what is a noun(.+?)',  ["A noun is a word that functions as the name of a specific object \nor set of objects, such as living creatures, places, actions, qualities, states of existence, or ideas."]),
            (r'what is verb', ["A verb is a word that describes an action, state, or occurrence, \nand forms the main part of the predicate of a sentence."]),
            (r'How do I improve my study habits(.+?)', ["To improve your study habits, try setting a regular \nstudy schedule, taking breaks, using study aids, and reviewing your notes regularly."]),
            (r'How can I manage my time better\?', ["To manage your time better, you can use a planner, \nprioritize tasks, set goals, and avoid procrastination."]),
            (r'sum of (\d+) and (\d+)', self.addition),
            (r'add (\d+) and (\d+)', self.addition),
            (r'what is (\d+) - (\d+)', self.subtraction),
            (r'subtract (\d+) and (\d+)', self.subtraction),
            (r'multiply (\d+) and (\d+)', self.multiplication),
            (r'what is (\d+) / (\d+)', self.division),
            (r'what is a prime number', ["A prime number is a natural number greater than 1 that has \nno positive divisors other than 1 and itself."]),
            (r'what is a quadratic equation', ["A quadratic equation is a second-order polynomial equation\n in a single variable x with the form ax^2 + bx + c = 0."]),
            (r'(.*)',['I am sorry, I don\'t understand that. Could you please rephrase?']),
    ]

    def addition(self, groups):
        return f"The sum of {groups[1]} and {groups[2]} is {int(groups[1]) + int(groups[2])}."
    
    def subtraction(self, groups):
        return f"The difference between {groups[1]} and {groups[2]} is {int(groups[1]) - int(groups[2])}."
    
    def multiplication(self, groups):
        return f"The product of {groups[1]} and {groups[2]} is {int(groups[1]) * int(groups[2])}."
    
    def division(self, groups):
        try:
            result = int(groups[1]) / int(groups[2])
            return f"The quotient of {groups[1]} divided by {groups[2]} is {result}."
        except ZeroDivisionError:
            return "Division by zero is not allowed."
    def chatbot_respond(self,message):
        for pattern, response in self.rules:
            match = re.match(pattern, message, re.IGNORECASE)
            if match:
                if callable(response):
                    return response(match)
                else:
                    return random.choice(response)
        return "I'm sorry, I don't understand that"
# Function to handle sending messages
def send_message(event=None):
    user_input = entry.get()
    if user_input:
        display_message("You: " + user_input, "user")
        response = chatbot.chatbot_respond(user_input)
        display_message("Bot: " + response, "bot")
        entry.delete(0, tk.END)

# Function to display messages in the chat window
def display_message(message, sender):
    chat_window.config(state=tk.NORMAL)
    if sender == "user":
        frame1 = tk.Frame(chat_window, bg="#d0ffff")
        tk.Label(frame1,text=message,font=("Arial",11),bg="#d0ffff").grid(row=0,column=0,sticky="w",padx=5,pady=5)
        tk.Label(frame1, text=datetime.now().strftime("%H:%M"),
          font=("Arial",7),bg="#d0ffff").grid(row=1,column=0,sticky="e")
        chat_window.window_create('end', window=frame1)
        chat_window.tag_add("user_tag", "end-1c linestart", "end-1c lineend")
        chat_window.insert(tk.END, "\n")
    else:
        frame2 = tk.Frame(chat_window, bg="#ffffd0")
        tk.Label(frame2,text=message,font=("Arial",11),bg="#ffffd0").grid(row=0,column=0,sticky="w",padx=5,pady=5)
        tk.Label(frame2, text=datetime.now().strftime("%H:%M"),
          font=("Arial",7),bg="#ffffd0").grid(row=1,column=0,sticky="e")
        chat_window.insert(tk.END, "\n")
        chat_window.window_create('end', window=frame2)
        chat_window.insert(tk.END, "\n")
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)

chatbot=RuleBasedChatbot()
# Set up the main application window
root = tk.Tk()
root.title("Rule-Based Chatbot")
root.geometry("600x500")

icon=ImageTk.PhotoImage(file="chatbot1.png")
root.iconphoto(False,icon)
# Create a frame for the chat window
frame = tk.Frame(root,bg="#ABB2B9")
frame.pack(pady=60)

# Create a scrolled text widget for the chat window
chat_window = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=90, height=20, state=tk.DISABLED)
chat_window.pack()

# Configure tag styles for user and bot messages
chat_window.tag_configure("user_tag", justify="right")
chat_window.tag_configure("bot_tag", justify="left")

bottom_label = tk.Label(root, bg="#ABB2B9", height=80)
bottom_label.place(relwidth=1, rely=0.825)

# message entry box
entry = tk.Entry(bottom_label, bg="#2C3E50", fg="#EAECEE", font="arial")
entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
entry.focus()
entry.bind("<Return>", send_message)


# send button
send_button = tk.Button(bottom_label, text="Send", font="Helvetica 13 bold", width=20, bg="#ABB2B9",
                             command=send_message)
send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

# Run the application
root.mainloop()
