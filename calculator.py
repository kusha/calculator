#!/usr/bin/env python3

"""@package docstring
@brief Basic calculator with GUI.
@mainpage Calculator module. After installation avialable
with rhcalc command.
"""

__author__ = "Mark Birger, Daniil Khudiakov, Martin Knotek"
__date__ = "26 Apr 2015"
__credits__ = ["Mark Birger", "Daniil Khudiakov", "Martin Knotek"]

__license__ = "GNU General Public License v3.0"
__version__ = "1.0"
__maintainer__ = "Mark Birger"
__status__ = "Production"

import mathlib
import sys
try:
    from tkinter import *                    
except ImportError:
    print("Tk is not available in PyPi.")
    print("You need to manually install it:")
    print("sudo apt-get install python3-tk")
    sys.exit(1)

class Calculator:
    """
    Class implements calculator with GUI.
    Uses evaluation form mathlib.
    """

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
        """
        This method creates windows, widgets and other things.
        GUI is implemented with Tk. It's mainloop at the end
        of this method.
        """

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
            frame_right, text='Type your expression', state='normal')
        self.result_widget.config(bg='white', fg='grey', state='readonly')
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

        self.draw()

        self.root.mainloop()

    def story_save(self):
        """
        Saves actual exression and result at each change.
        """
        self.story[self.selected][0] = self.input_string
        self.story[self.selected][1] = self.result
        self.story[self.selected][2] = self.valid

    def story_up(self):
        """
        Moves up in results story. It's button callback.
        """
        self.root.focus()
        self.selected -= 1
        self.story_update()

    def story_down(self):
        """
        Moves down in results story. It's button callback.
        """
        self.root.focus()
        self.selected += 1
        self.story_update()

    def story_update(self):
        """
        This method locks button if necessary and creates new
        cell if they are not created.
        """
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
        """
        Method called at each input expression form change.
        @param input_string tkinter string object with Entry content
        """
        if not self.update_locked:
            self.input_string = input_string.get()
            print(self.input_string)
            self.count()

    def count(self):
        """
        This method uses mathlib to evaluate current expression.
        """
        story = [None] + \
            [float(i[1]) if i[1] is not None else i[1] for i in self.story]
        result = mathlib.evaluate(self.input_string, story)
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
        """
        Method updates GUI (forms, labels) after each
        model change.
        """
        self.index_widget['text'] = '#'+str(self.selected+1)
        if self.result is None:
            self.result_widget.config(state='normal')
            self.result_widget.delete(0, END)
            self.result_widget.insert(0, 'Type your expression')
            self.result_widget.config(bg='white', fg='grey', state='readonly')
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

def main():
    """
    Main function needed for rhcalc call.
    """
    Calculator()

if __name__ == "__main__":
    main()
