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

smile = ('  0    0\n'
     '     -   \n'
     '\________/\n')

wink = ('  ^   0\n'
     '    -   \n'
     '_________\n'
     '          ')
bear = ''
choice = input('What do you want? wink, smile, or bear: ').lower()
while choice == smile and choice == wink and choice == bear:
    if choice == smile:
        print(smile)
    elif choice == wink:
        print(wink)
    #Art from website https://www.asciiart.eu/animals/bears
    elif choice == bear:
        print(' __         __')
        print('/  \.-"""-./  \ ')
        print('\    -   -    /')
        print(' |   o   o   |')
        print(' \  .-''-.   / ')
        print('' '   -\__Y__/-' '')
        print('     `---`')