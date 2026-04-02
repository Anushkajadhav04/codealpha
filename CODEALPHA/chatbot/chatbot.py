import tkinter as tk
from tkinter import scrolledtext
import datetime

# Chatbot logic
def get_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hello", "hi", "hey"]:
        return "Hello! How can I help you?"

    elif "time" in user_input:
        return "Time: " + datetime.datetime.now().strftime("%H:%M:%S")

    elif "date" in user_input:
        return "Date: " + datetime.datetime.now().strftime("%Y-%m-%d")

    elif "capital of india" in user_input:
        return "Capital of India is New Delhi"

    elif "largest planet" in user_input:
        return "Jupiter is the largest planet"

    elif "calculate" in user_input:
        try:
            expr = user_input.replace("calculate", "")
            return "Result: " + str(eval(expr))
        except:
            return "Invalid calculation"

    elif user_input in ["bye", "exit"]:
        return "Goodbye!"

    else:
        return "I don't understand that."


# Send message
def send_message(event=None):  # event added for Enter key
    user_text = entry_box.get().strip()
    if user_text == "":
        return

    # User bubble
    chat_area.insert(tk.END, "You: " + user_text + "\n", "user")

    response = get_response(user_text)

    # Bot bubble
    chat_area.insert(tk.END, "Bot: " + response + "\n\n", "bot")

    entry_box.delete(0, tk.END)
    chat_area.yview(tk.END)


# GUI setup
window = tk.Tk()
window.title("Smart Chatbot 🤖")
window.geometry("450x550")
window.configure(bg="#1e1e1e")

# Chat area
chat_area = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    font=("Arial", 12),
    bg="#2b2b2b",
    fg="white",
    insertbackground="white"
)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Styling tags (chat bubbles)
chat_area.tag_config("user", foreground="#00ffcc", font=("Arial", 12, "bold"))
chat_area.tag_config("bot", foreground="#ffcc00", font=("Arial", 12))

# Input box
entry_box = tk.Entry(
    window,
    font=("Arial", 12),
    bg="#3c3f41",
    fg="white",
    insertbackground="white"
)
entry_box.pack(padx=10, pady=5, fill=tk.X)

# Bind Enter key
entry_box.bind("<Return>", send_message)

# Send button
send_button = tk.Button(
    window,
    text="Send",
    command=send_message,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold")
)
send_button.pack(pady=5)

# Run app
window.mainloop()