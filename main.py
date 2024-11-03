# Code goes here and DO NOT FORGET INTRO COMMENTS
from logging import DEBUG


#prints however many lines user wants
def lines():
        blank = ''
        count = 0
        num_lines = int(input('How many lines do you want?: '))
        if num_lines.isdigit:

        num_chars = int(input('How many characters do you want?: '))
        characters = input('what characters do you want?: ')
        while count < num_lines:
            print(characters * num_chars)
            count += 1

def circle():
        print('Below is a print of the circle:')
        print(
              '     ___----___\n'
              '   /            \   \n'
              ' /               \ \n'
              ' |               |\n'
              ' |               | \n'
              '  \             / \n'
              '    \          / \n'
              '     ---___---\n')

A = ('  0    0\n'
     '     -   \n'
     '\________/\n')
lines()