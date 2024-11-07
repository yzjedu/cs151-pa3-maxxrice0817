# Code goes here and DO NOT FORGET INTRO COMMENTS
from logging import DEBUG


#prints however many lines user wants
#purpose: print lines by length, which character line is made of, how many characters in each line
#name: lines
#parameter: none

def lines():
            blank = ''
            count = 0
            num_lines = input('How many lines do you want?: ')
            while not num_lines.isdigit():
                num_lines = input('ERROR: How many lines do you want?: ')
            num_chars = int(input('How many characters do you want?: '))
            characters = input('what characters do you want?: ')
            num_lines = int(num_lines)
            while count < num_lines:
                    print(characters * num_chars)
                    count += 1
    #prints a design of a circle
    #purpose: print a circle
    #name: circle
    #parameters: none
def circle():
            play = input('Would you like to play a circle? (y/n): ')
            if play == 'yes':
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
            else:
                print('Program ended: have a nice day')
def custom_designs():
        one = (f'{"^":>3}{"^":>3}\n {"-":^7}\n{"":-<8}')

        two= (f'{"^":>3}{"0":>3}\n {"-":^7}\n{"":-<8}')


    #Chooses between 3 designs of my choice
    #Art from website https://www.asciiart.eu/animals/bears
    #
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