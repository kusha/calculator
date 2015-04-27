#!/usr/bin/env python3

"""
Basic calculator with GUI.
"""

__author__ = "Mark Birger, Daniil Khudiakov, Martin Knotek"
__date__ = "26 Apr 2015"
__credits__ = ["Mark Birger", "Daniil Khudiakov", "Martin Knotek"]

__license__ = "GNU General Public License v3.0"
__version__ = "1.0"
__maintainer__ = "Mark Birger"
__status__ = "Production"

import mathlib
from tkinter import *

class Calculator:

    def __init__(self):
        self.story = [["", None, False]]
        self.selected = 0
        self.input_string = ""
        self.result = None
        self.valid = False
        self.update_locked = False
        self.root = None
        self.input_widget = None
        self.result_widget = None
        self.index_widget = None
        self.button_up = None
        self.button_down = None
        self.init_gui()

    def init_gui(self):

        self.root = Tk()
        self.root.wm_title("RedHead Calculator")
        self.root.resizable(width=FALSE, height=FALSE)

        labelfont = ('Helvetica', 50, 'normal')

        self.root.bind('z', self.story_up)
        self.root.bind('x', self.story_down)

        frame_left = Frame(self.root, width=100, heigh=100, bd=10)
        frame_right = Frame(self.root, width=150, heigh=75, bd=10)

        input_string = StringVar()
        input_string.trace(
            "w", 
            lambda name, index, mode, input_string=input_string: \
            self.callback(input_string))

        self.input_widget = Entry(frame_right, textvariable=input_string)
        self.input_widget.config(bg='white', fg='black')
        self.input_widget.config(font=labelfont)
        self.input_widget.config(justify=RIGHT)

        self.result_widget = Entry(
            frame_right, text='Type your expression', state='readonly')
        self.result_widget.config(bg='white', fg='grey')
        self.result_widget.config(font=labelfont)
        self.result_widget.config(justify=RIGHT)

        self.index_widget = Label(frame_left, text='#'+str(self.selected+1))
        self.index_widget.config(bg='white', fg='black')
        self.index_widget.config(font=labelfont)
        self.index_widget.config(justify=RIGHT)
        self.index_widget.config(height=1, width=3)

        self.button_up = Button(
            frame_left, 
            text="Previous", 
            command=self.story_up, 
            state=DISABLED)
        self.button_down = Button(
            frame_left, 
            text="New", 
            command=self.story_down)

        frame_left.pack(side='left')
        frame_right.pack(side='right')

        self.input_widget.pack(expand=YES, fill=BOTH)
        self.result_widget.pack(expand=YES, fill=BOTH)

        self.button_up.pack(expand=YES, fill=BOTH)
        self.index_widget.pack(expand=YES, fill=BOTH)
        self.button_down.pack(expand=YES, fill=BOTH)

        self.root.mainloop()

    def story_save(self):
        self.story[self.selected][0] = self.input_string
        self.story[self.selected][1] = self.result
        self.story[self.selected][2] = self.valid

    def story_up(self, event=None):
        self.root.focus()
        self.selected -= 1
        self.story_update()

    def story_down(self, event=None):
        self.root.focus()
        self.selected += 1
        self.story_update()

    def story_update(self):
        if self.selected < 0:
            self.selected = 0
        if self.selected > 98:
            self.selected = 98
        if self.selected >= len(self.story):
            # self.story.append([self.input_string, self.result, self.valid])
            self.story.append(["", None, False])
        if self.selected == 0:
            self.button_up['state'] = DISABLED
        else:
            self.button_up['state'] = 'normal'
        if self.selected == len(self.story)-1:
            self.button_down['text'] = "New"
        else:
            self.button_down['text'] = 'Next'
        if self.selected == 98:
            self.button_down['state'] = DISABLED
        else:
            self.button_down['state'] = 'normal'
        print(self.story[self.selected])
        self.input_string = self.story[self.selected][0]
        print(self.story[self.selected])
        self.result = self.story[self.selected][1]
        print(self.story[self.selected])
        self.valid = self.story[self.selected][2]
        print(self.story[self.selected])
        self.update_locked = True
        self.input_widget.delete(0, END)
        self.input_widget.insert(0, self.input_string)
        self.update_locked = False
        self.count()

    def callback(self, input_string):
        if not self.update_locked:
            self.input_string = input_string.get()
            print(self.input_string)
            self.count()

    def count(self):
        result = mathlib.evaluate(self.input_string, self.story)
        if result:
            self.result = result
            self.valid = True
        else:
            # self.result = None
            self.valid = False
        print("count", self.story[self.selected])
        self.story_save()
        print("count", self.story[self.selected])
        self.draw()

    def draw(self):
        self.index_widget['text'] = '#'+str(self.selected+1)
        if self.result is None:
            # self.result_widget['text'] = 'Type your expression'
            return
        if self.valid:
            self.input_widget.config(fg='black')
            self.result_widget.config(state='normal')
            self.result_widget.delete(0, END)
            self.result_widget.insert(0, self.result)
            self.result_widget.config(bg='white', fg='black', state='readonly')
        else:
            self.input_widget.config(fg='red')
            self.result_widget.config(state='normal')
            self.result_widget.delete(0, END)
            self.result_widget.insert(0, self.result)
            self.result_widget.config(bg='white', fg='grey', state='readonly')

if __name__ == "__main__":
    CALCULATOR = Calculator()
