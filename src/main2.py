import textwrap

item = {}

class Person:
    def __init__(self, name, points):
        self._name = name
        self._points = points

        # the same person can be in different project (but points assigned to one project)
        # call functions from module; restructure once we have elements

        # setter (given me the rules(that B+c=100))
    #  to return the number of points


# getter is a return command - it returns what comes out of the setter function; may print or might

class Project:
    def __init__(self, project, listppl):
        self._projectname = project
        self._list_of_persons = listppl

        # create epmty list
        # depending on vhoice of project use append option, it appends the names into the list

        # dict: {p1: name1,nae2, name3, 3}
        # extract first 3 postions from a dictionary into a list (asking for info from the same columns)
        # panda library to read data from files and organize it

    # use pandas to store:
    #    1) what person A gave to B and C (B+C=100)
    #   2) what peron A received from B and C (total doesn't = 100)


# create a dictionary from opt. C input
def itemmaker(project_name, students):
    project_name = project_name.upper()
    item[project_name] = students


# Welcomes the user into our application.
def print_welcome_message():
    print('Welcome to Split-it\n')


# Lists all the menu options for the user

def print_menu_options():
    menu_dict = {'About\t\t': '(A)', 'CreateProject\t': '(C)',
                 'Enter Votes\t': '(V)', 'Show Project\t': '(S)',
                 'Quit\t\t': '(Q)'}
    for k, v in menu_dict.items():
        print('{} {}'.format(k, v))
    print("\nPlease choose an option and press <ENTER>:")


# validation of number of team members
def is_int(text):
    count = 0
    max_attempt = 5
    try:
        a = int(text)
        if a == 3:
            return True
        else:
            raise ValueError()
    except ValueError:
        count += 1
        if count > max_attempt:
            exit(0)  # exit does not work
        print('\033[92m' + 'Invalid Input. Please try again.' + '\033[0m')
        return False


# validation of any string input
def valid_text(self):
    counting = 0
    max_attempts = 3
    while len(self) < 3 or len(self) > 20 or any(i.isdigit() for i in self):
        if counting > max_attempts:
            print('\033[92m' + 'You have been exited from the program. \n' + '\033[0m')
            exit()  # exit does not work
        counting += 1
        self = input('\033[92m' + 'Invalid Input. Please try again. \n' + '\033[0m')


# assure, that names of team members are not repeated
def nonrep(self, liste):
    self = self.upper()
    counter = 0
    kicker = 3
    while self in liste:
        counter += 1
        if counter > kicker:
            print('BYE')
            get_menu_option_from_user(0)  # this does not yet work
        print('\033[92m' + 'You already have a team member with that name. \n' + '\033[0m')
        self = input("\t Try again: ")
        self = self.upper()
    else:
        liste.append(self)


# Opt A: description of program
def option_a():
    print('\033[1m' + '\n\nOption A: About Spliddit\n' + '\033[0m')
    instruction = """Hello. This is Spliddit. I am an app that can help you share 
    and distribute things with your friends and colleagues, from grades to bills, 
    to notes and good memories. What would you like to split today? 
    You can decide that by personalizing me in option C."""
    list = textwrap.wrap(instruction, width=50)
    for element in list:
        print(element)
    input("\nPress <Enter> to return to the main menu: ")


# Opt C: create a project
def option_c():
    print('\033[1m' + '\n\nOption C: Creating a Project' + '\033[0m')
    project_name = input("Enter the project name: ")
    valid_text(project_name)
    students = []
    validinput = False
    while not validinput:
        number = input("Enter the number of team members: ")
        if is_int(number):
            validinput = True
            number = int(number)
    for i in range(number):
        student = input("\t Enter the name of team member " + str(i + 1) + ": ")
        valid_text(student)
        nonrep(student, students)
        itemmaker(project_name, students)
    input("\nPress <Enter> to return to the main menu:\n ")

def choose_project():
    text = input("Enter the project name: ")
    text = text.upper()

    while text not in item:
        print("Error:")
        text = input("Enter the project name: ")
        text = text.upper()

    print('\033[92m' + 'Try again. Enter an existing project name: ' + '\033[0m')
    choose_project()

    # later on inorporate validation to try 3 times
    # capital letter validation by input.upper()



# choice of a menu option
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
        print('\033[92m' + '\nPlease choose only options from the menu above: ' + '\033[0m')

        get_menu_option_from_user(1)


# Return to start of the application,
def main():
    print_welcome_message()
    get_menu_option_from_user()


if __name__ == '__main__':
    main()


# DELIVERABLE 2 Parts and Notes



def input_point():
    students = []

    for i in range(1, 4):
        memberNumber = input('Team member number' + str(i) + ':')
        students.append(memberName)

    print(students)

    for i in students:
        if i == students[0]:
            print('Enter' + (students[0]) + "'s votes. Points must add up to 100")
            voteSecond = input('Enter vote for' + (students[1] + ':'))
            voteThird = input('Enter vote for' + (students[2] + ':'))
        elif i == students[1]:
            print('Enter' + (students[1]) + "'s votes. Points must add up to 100")
            voteFirst = input('Enter vote for' + (students[0] + ':'))
            voteThird = input('Enter vote for' + (students[2] + ':'))
        elif i == students[2]:
            print('Enter' + (students[1]) + "'s votes. Points must add up to 100")
            voteFirst = input('Enter vote for' + (students[0] + ':'))
            voteSecond = input('Enter vote for' + (students[1] + ':'))

        input_point():


# validation of points adding up to 100\n",
def valid_100(self):
    counting = 0
    max_attempts = 3
    if voteSecond and voteThird == 100
        return True
    else:
        print(ValueError()
        print('Enter' + (students[0]) + "'s votes. Points must add up to 100")


