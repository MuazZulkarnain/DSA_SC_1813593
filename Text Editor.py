from tkinter import *

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

window = Tk()
window.title("Text Editor")
file = None

# Size application
window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

# Font application
font_name = StringVar(window)
font_name.set("Arial")
font_size = StringVar(window)
font_size.set("25")

# Text and scroll application
text_area = Text(window, font=(font_name.get(), font_size.get()))
scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

# Menu
menu_bar = Menu(window)
window.config(menu=menu_bar)
menu_bar.add_cascade(label="Cut", command=cut)
menu_bar.add_cascade(label="Copy", command=copy)
menu_bar.add_cascade(label="Paste", command=paste)

window.mainloop()