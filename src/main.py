def print_welcome_message():
    print('Welcome to Split-it')


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


def safe_int_input():
    text = input()
    if is_int(text):
        return int(text)
    print("Try again. Enter an integer number:")
    safe_int_input()

def option_a():
    print('\033[1m' + 'Option A: About Spliddit\n' + '\033[0m')
    print("Hello. This is Spliddit. "
          "I am an app that can help you share and distribute things with your friends and colleagues, "
          "from grades to bills, to notes and good memories. "
          "What would you like to split today? "
          "You can decide that by personalizing me in option C.")
    input("\nPress <Enter> to return to the main menu: ")

def option_c():
    print('\033[1m' + 'Option C: Creating a Project' + '\033[0m')
    print("Enter the project name: ")

    project_name = input()  # value never used
    students = [] # value never used

    print("Enter the number of team members:")
    number = safe_int_input()

    while number <= 0:
        print("The number must be positive:")
        number = safe_int_input()

    for i in range(number):
        print("\t Enter the name of team member " + str(i+1) + ": ")
        student = input()
        students.append(student)
    input("\nPress <Enter> to return to the main menu:\n ")


def get_menu_option_from_user(attempt=0):
    if attempt == 0:
        print_menu_options()

    choice = input()
    choice = choice.upper()
    if choice == "A":
        option_a()
        get_menu_option_from_user(0)
    elif choice == "Q":
        exit(0)
    elif choice == "V":
        get_menu_option_from_user(0)
    elif choice == "S":
        get_menu_option_from_user(0)
    elif choice == "C":
        option_c()
        get_menu_option_from_user(0)
    else:
        print("\n Please choose only options from the menu above: ")
        get_menu_option_from_user(1)


def main():
    print_welcome_message()
    get_menu_option_from_user()


if __name__ == '__main__':
    main()
