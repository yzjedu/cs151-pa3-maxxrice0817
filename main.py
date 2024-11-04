# Code goes here and DO NOT FORGET INTRO COMMENTS
from logging import DEBUG


#prints however many lines user wants
def lines():
        blank = ''
        count = 0
        num_lines = int(input('How many lines do you want?: '))
        num_chars = int(input('How many characters do you want?: '))
        characters = input('what characters do you want?: ')
        while count < num_lines:
                print(characters * num_chars)
                count += 1
#prints a design of a circle
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

one = ('  0    0\n'
     '     -   \n'
     '\________/\n')

two = ('  ^   0\n'
     '    -   \n'
     '_________\n'
     '          ')
bear = ''

#Chooses between 3 designs of my choice
#Art from website https://www.asciiart.eu/animals/bears
def custom_designs():
    def bear():
        print(' __         __')
        print('/  \.-"""-./  \ ')
        print('\    -   -    /')
        print(' |   o   o   |')
        print(' \  .-''-.   / ')
        print('' '   -\__Y__/-' '')
        print('     `---`')

    user_choice = input('What shape would you like to pick? wink, smile, or bear? ').lower()
    while user_choice != 'wink' and user_choice != 'smile' and user_choice != 'bear':
        user_choice = input('INVALID INPUT: What shape would you like to pick? wink, smile, or bear?')
    if user_choice == 'wink':
        print(two)
    elif user_choice == 'smile':
        print(one)
    elif user_choice == 'bear':
        bear()

def main():
    lines()
    circle()
    custom_designs()

main()