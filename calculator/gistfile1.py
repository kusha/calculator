#!/usr/bin/env python3

# math section
import math
import re

math_namespace = vars(math).copy()
math_namespace['__builtins__'] = None

regex_function = r'(\d+!|\d+(\.\d+)?\^\d+|\|[+,-]?\d+(\.\d+)?\|)'
regex_value = r'(\d+|\d+\.\d+|'+regex_function+')'
regex_operation = r'(\+|\-|\*|\/)'
regex_all = '^[+,-]?('+regex_value+regex_operation+')*'+regex_value+"$"
valid_pattern = re.compile(regex_all)

def evaluate(expression):
    if valid_pattern.match(expression):
        expression=re.sub(r'(\d+)!',"factorial("+r'\1'+")",expression)
        expression=re.sub(r'(\d+(\.\d+)?)\^(\d+)',"pow("+r'\1'+","+r'\3'+")",expression)
        expression=re.sub(r'\|[+,-]?(\d+(\.\d+)?)\|',r'\1',expression)
        result = eval(expression, math_namespace)
        return str(result)
    else:
        return None

# gui section
from tkinter import *

root = Tk()
labelfont = ('Bebas Neue', 50, 'normal')

def callback(input_string):
    result = evaluate(input_string.get())
    if result:
        input_widget.config(fg='black')
        result_widget['text'] = result
    else:
        input_widget.config(fg='red')

input_string = StringVar()
input_string.trace("w", lambda name, index, mode, input_string=input_string: callback(input_string))

input_widget = Entry(root, textvariable=input_string)
input_widget.config(bg='white', fg='black')
input_widget.config(font=labelfont)
input_widget.config(justify=RIGHT)
input_widget.pack(expand=YES, fill=BOTH)

result_widget = Label(root, text='Hello config world')
result_widget.config(bg='white', fg='black')
result_widget.config(font=labelfont)
result_widget.config(justify=RIGHT)
result_widget.config(height=1, width=20)
result_widget.pack(expand=YES, fill=BOTH)

root.mainloop()
