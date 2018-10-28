def main():
    menu1 = {'About\t\t': '(A)', 'CreateProject\t': '(C)',
             'Enter Votes\t': '(V)', 'Show Project\t': '(S)',
             'Quit\t\t': '(Q)'}

    print('Welcome to Split-it\n')

    for k, v in menu1.items():
        print(f'{k} {v}')


if __name__ == '__main__': main()

choice = input("\n Please choose an option and press <ENTER>: ")
status = False
count = 0
max_attempt = 3
items = ['A', 'C', 'V', 'S', 'Q']

while choice not in items:
    count += 1
    if count > max_attempt:
        from sys import exit

        exit()
    choice = input("\n Please choose only options from the menu above: ")
    if choice in items: break

if choice == 'A':
    print("\n\n\n ")
    print('\033[1m' + 'Option A: About Spliddit\n' + '\033[0m')
    import textwrap

    instruction = """Hello. This is Spliddit. I am an app that can help you share and distribute things 
    with your friends and colleagues, from grades to bills, 
    to notes and good memories. What would you like to split today? 
    You can decide that by personalizing me in option C."""
    list = textwrap.wrap(instruction, width=50)
    for element in list:
        print(element)
    input("\nPress <Enter> to return to the main menu: ")
    main()

if choice == 'Q':
    from sys import exit

    exit()  # is there a posher way of leaving?

if choice == 'V':
    print('\n')
    main()  # Other option needed to get back to Menu (goto?)

if choice == 'S':
    print('\n')
    main()  # Other option needed to get back to Menu (goto?)


def is_int(text):
    try:
        int(text)
        return True
    except:
        return False


# input
print("\n\n\n ")
print('\033[1m' + 'Option C: Creating a Project\n' + '\033[0m')

name = []
n = input('\nEnter the project name: ')

students = []
x = input("Enter the number of team members: ")  # what if you put in a negative number
count = 0
max_attempt = 3
while not is_int(x):
    count += 1
    if count > max_attempt:
        from sys import exit

        exit()
    x = input('Please enter a proper number: ')
x = int(x)
while x < 0:
    x = x * (-1)
    print(
        '\033[92m' + 'Presumably you meant to type in {}, since minus people are not a thing Mr wannabe Aristotle\n'.format(
            x) + '\033[0m')
    if x >= 1: break
for i in range(x):
    y = input("\t Enter the name of team member {}: ".format(str(i + 1)))  # what if you don't put in anything?
    students.append(y)
input("\nPress <Enter> to return to the main menu:\n ")
main()