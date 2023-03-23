import tkinter as tk
from tkinter import ttk
import pyttsx3

tts_engine = pyttsx3.init()


def text_to_speech():
    tts_engine.say(text_var.get())
    tts_engine.runAndWait()
    tts_engine.stop()


root = tk.Tk()
text_var = tk.StringVar()

frame = ttk.LabelFrame(root, text="Text to speech")
frame.pack(fill="both", expand=True, padx=10, pady=10)

label = ttk.Label(frame, text="Text :", font=("calibri", 20))
label.pack(side=tk.LEFT, padx=5)

text = ttk.Entry(frame, textvariable=text_var, font=("Times New Roman", 20), width=27)
text.pack(side=tk.LEFT, padx=10)

button = ttk.Button(frame, text="OK", command=text_to_speech)
button.pack(side=tk.LEFT, padx=10)

root.title("PyVoice")
root.geometry("600x200")
root.resizable(False, False)
root.mainloop()
