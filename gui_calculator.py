# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 08:52:22 2025

@author: HP
"""

import tkinter as tk
from tkinter import PhotoImage

# Initial theme colors
is_dark = False
light_theme = {
    "bg": "#f5f5f5", "fg": "#000", "entry_bg": "#fff", "btn_bg": "#e0e0e0"
}
dark_theme = {
    "bg": "#222", "fg": "#fff", "entry_bg": "#333", "btn_bg": "#444"
}

# Apply theme
def apply_theme():
    theme = dark_theme if is_dark else light_theme
    root.config(bg=theme["bg"])
    entry.config(bg=theme["entry_bg"], fg=theme["fg"])
    for btn in buttons_list:
        btn.config(bg=theme["btn_bg"], fg=theme["fg"])
    label.config(bg=theme["bg"], fg=theme["fg"])

# Window setup
root = tk.Tk()
root.title("Bindu's Unique Calculator 💖")
root.geometry("360x520")

# Entry
entry = tk.Entry(root, font=("Comic Sans MS", 24), bd=5, relief="ridge", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipadx=5, ipady=10)

# Handle button click
def on_click(button_text):
    current = entry.get()
    if button_text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "←":
        entry.delete(len(current)-1, tk.END)
    elif button_text == "🌗":
        toggle_theme()
    else:
        entry.insert(tk.END, button_text)

# Button layout
layout = [
    ['7', '8', '9', '÷'],
    ['4', '5', '6', '×'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+'],
    ['←', '🌗']  # Backspace and Dark mode
]

buttons_list = []
# Create buttons
for i, row in enumerate(layout):
    for j, btn_text in enumerate(row):
        if btn_text == '÷': display_text = '/'
        elif btn_text == '×': display_text = '*'
        else: display_text = btn_text

        btn = tk.Button(
            root, text=btn_text, width=5, height=2,
            font=('Comic Sans MS', 16, 'bold'),
            relief="raised", bd=3,
            command=lambda text=display_text: on_click(text)
        )
        btn.grid(row=i+1, column=j, padx=8, pady=8)
        buttons_list.append(btn)

# Toggle dark/light mode
def toggle_theme():
    global is_dark
    is_dark = not is_dark
    apply_theme()

# Footer label
label = tk.Label(root, text="Created by Bindu 💫", font=('Arial', 10))
label.place(x=110, y=490)

# Optional: Add a photo (PNG only, small size)
try:
    photo = PhotoImage(file="bindu.png")  # make sure image is in same folder
    image_label = tk.Label(root, image=photo, bg="#f5f5f5")
    image_label.place(x=10, y=460)
except:
    pass  # Ignore if photo not found

apply_theme()  # Apply theme on startup

# Run
root.mainloop()