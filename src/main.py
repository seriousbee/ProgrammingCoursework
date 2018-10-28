def print_welcome_message():
    print('Welcome to Split-it\n')
    print_menu_options()


def print_menu_options():
    menu_dict = {'About\t\t': '(A)', 'CreateProject\t': '(C)',
             'Enter Votes\t': '(V)', 'Show Project\t': '(S)',
             'Quit\t\t': '(Q)'}
    for k, v in menu_dict.items():
        print(f'{k} {v}') # not 100% what this f is but it doesn't work without it
    print("Please choose an option and press <ENTER>:")


def is_int(text):
    try:
        int(text)
        return True
    except ValueError:
        return False


def option_A():
    print("\n")
    print("------------")
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
    main()  # woow, this is dangerous

def option_C():
    print('\033[1m' + 'Option C: Creating a Project\n' + '\033[0m')

    name = []  # value never used?
    n = input('\nEnter the project name: ')  # value nevver used?

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


def get_menu_option_from_user(attempt=0):
    if attempt > 3:
        exit(0)
    choice = input()
    if choice == "A":
        pass
    elif choice == "Q":
        pass
    elif choice == "V":
        pass
    elif choice == "S":
        pass
    elif choice == "C":
        pass
    else:
        print("\n Please choose only options from the menu above: ")
        get_menu_option_from_user(attempt+1)


def main():
    print_welcome_message()
    get_menu_option_from_user()


if __name__ == '__main__':
    main()
