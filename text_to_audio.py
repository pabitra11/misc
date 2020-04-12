from gtts import gTTS
import os
from tkinter import *
from tkinter.ttk import *
from pygame import mixer

# importing askopenfile function
# from class filedialog
from tkinter.filedialog import askopenfile

root = Tk()
root.geometry('800x800')


# This function will be used to open
# file in read mode and only Python files
# will be opened
def open_file():
    file = askopenfile(mode='r', filetypes=[('Python Files', '*.txt')])
    if file is not None:
        content = file.read()
        Label(root, text=content).pack()
        language = 'en'
        myobj = gTTS(text=content, lang=language, slow=False)
        myobj.save("welcome.mp3")
        mixer.init()
        mixer.music.load('welcome.mp3')
        mixer.music.play()


btn = Button(root, text='Open', command=lambda: open_file())
btn.pack(side=TOP, pady=10)

mainloop()