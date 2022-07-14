import os
import statistics
from datetime import datetime
from time import sleep
import gspread
from google.oauth2.service_account import Credentials
from colorama import Style
from tabulate import tabulate
from questions import questions
import logos

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hogwarts_houses')

year = datetime.now().year
houses = SHEET.worksheet('Houses')
student = {"Name": "", "Age": "", "Country": "", "House": ""}


def welcome():
    """
    Welcome function to request name, age and
    country inputs from user.
    """
    print('THE SORTING HAT\n'.center(80))
    sleep(3)
    clear_display()

    while True:
        print("")
        print("")
        print("")
        name = input("Please tell me your name:\n>>> ")
        if validate_name(name):
            print("")
            print(f"Nice to meet you {name}!")
            student.update({"Name": name})  # rockymiss
            break
    sleep(1)

    while True:
        print("")
        age = input("Please tell me your age:\n>>> ")
        if validate_age(age):
            print("")
            print("Thank you!")
            student.update({"Age": age})
            break
    sleep(1)

    while True:
        print("")
        country = input("""Finally, please tell us what Country you are from:\n
        >>> """)
        if validate_country(country):
            print("")
            print(f"Thank you {name}!".center(80))
            student.update({"Country": country})
            break
    sleep(2)

    print("")
    print("Confirming non-Muggle status........\n".center(80))
    sleep(3)
    print("Non-Muggle status VALIDATED\n".center(80))
    sleep(2)
    clear_display()
    logos.intro_logo_1()
    print(Style.RESET_ALL)
    print(f"""Welcome to Hogwarts School of Witchcraft and Wizardry {name}.\n""".center(80))
    print(f"We are delighted to have you join us for the {year} school term.\n".center(80))
    sleep(3)
    clear_display()
    print("")
    print("")
    print("In order to place you in the correct House for your time with us, ".center(80))
    print("the Sorting Hat needs to know a little more about you...\n".center(80))
    sleep(3)
    print(f"So, {name}, are you ready to get started?".center(80))
    sleep(1)

    return student


def start_sorting():
    """
    Function to verify with user that they wish to proceed.
    Option to quit at this stage.
    """
    sort = input("""\n      Please enter y to start or n if you wish to remove the Sorting Hat.\n>>> """)
    if sort == 'n':  # Add if sort not in lowercase...
        print("")
        print("You have decided to remove the sorting hat.".center(80))
        print("")
        print(f"""Goodbye {student['Name']} maybe we will see you next term instead.""".center(80))
        sleep(3)
        clear_display()
        main()
    elif sort == 'y':
        print("")
        print("Let's get sorting!!!".center(80))
        sleep(1)
        generate_questions()
    else:
        print("\nPlease enter either 'y' or 'n' in order to proceed.\n".center(70))


def generate_questions():
    """
    Function to run through sorting hat questions and
    calculate mode of answers in order to determine
    House.
    """
    clear_display()
    answers = []
    for q in questions:
        print(q['question'])  # from Stackoverflow see Readme
        sleep(1)
        for i, c in enumerate(q['options']):
            print(chr(97 + i) + ':', c)

        while True:
            answer = input("""Enter your answer or press q to remove the Sorting Hat:\n>>> """.center(70))
            if validate_answer(answer):
                print('\n\nThank you'.center(70))
                answers.append(answer)
                break

        sleep(1)
        clear_display()
    house = statistics.mode(answers)
    if house == 'a':
        student.update({"House": "Gryffindor"})
    elif house == 'b':
        student.update({"House": "Slytherin"})
    elif house == 'c':
        student.update({"House": "Hufflepuff"})
    elif house == 'd':
        student.update({"House": "Ravenclaw"})
    else:
        print("Hmmmmm...I am having some trouble sorting you.")
        print("Perhaps we should run through the questions again..")


def clear_display():  # dnlBowers
    """"
    Clears the console
    """
    command = 'clear'
    if os.name in (
            'nt', 'dos'):
        command = 'cls'
    os.system(command)


def validate_name(name):
    """
    Raises error if name entered is numerical
    or is blank.
    """
    try:
        if name.isnumeric():
            raise ValueError(
              f"\nPlease enter your name as text, you entered {name}"
            )
        elif len(name.strip()) == 0:  # rockymiss
            raise ValueError(
              """\nPlease enter your name, we need this to ensure you can be accepted to Hogwarts"""
            )
    except ValueError as e:
        print(f"{e}, please try again.\n")
        return False
    return True


def validate_age(number):
    """
    Raises error if age entered is under 4,
    over 18, a number is not entered or the
    entry is not a number.
    """
    try:
        if int(number) > 18:
            raise ValueError(
              f"\n{number}! Hogwarts cannot accept students over the age of 18."
              "\nPlease re-count your years and try again."
            )
        elif int(number) < 4:
            raise ValueError(
              "\nHogwarts can only accept students over the age of 4."
              f"\nAs you are only {number} you will need to wait a few years and come back."
              "Please re-count your years and try again."
            )
    except ValueError as e:
        print(f"\n{e}\n")
        return False


def validate_country(country):
    """
    Raises error if name entered is numerical
    or is blank.
    """
    try:
        if country.isnumeric():
            raise ValueError(
              f"\nPlease enter your country as text, you entered {country}"
            )
        elif len(country.strip()) == 0:
            raise ValueError(
              "\nPlease enter your country, we need this to ensure you can be accepted to Hogwarts"
            )
    except ValueError as e:
        print(f"{e}, please try again.\n")
        return False
    return True


def validate_answer(answer):
    """
    Raises error if answer entered is not
    a, b, c, or d or option to quit (q).
    """
    try:
        if answer not in {'a', 'b', 'c', 'd', 'q'}:
            raise ValueError(
              f"\nYou answered {answer},"
            )
        elif answer == 'q':
            quit_game()
            return True

    except ValueError as e:
        print(f"{e} please select a, b, c or as your answer to proceed or q to \n remove the Sorting Hat.\n")
        return False


def update_house_spreadsheet():  # rockymiss
    """
    Populates Houses tab of Google spreadsheet
    with name, age and country input data and
    final determined house.
    """
    new_student = list(student.values())
    houses.append_row(new_student)


def determine_house():
    """
    Function to display determined House,
    information about House and students.
    """
    if student['House'] == "Gryffindor":
        logos.gryffindor_logo()
        print("")
        print(f"Welcome to Gryffindor {student['Name']}!".center(80))
        print(Style.RESET_ALL)
        sleep(3)
        print("")
        clear_display()
        print("")
        print("")
        print("Gryffindor students are couragous and daring.".center(80))
        print("\n")
        print("Gryffindor House values nerve, leadership and chivalry.".center(80))
        sleep(3)
    elif student['House'] == "Slytherin":
        logos.slytherin_logo()
        print("")
        print(f"Welcome to Slytherin {student['Name']}!".center(80))
        print(Style.RESET_ALL)
        sleep(3)
        print("")
        clear_display()
        print("")
        print("")
        print("Slytherin students are ambitious and shrewd".center(80))
        print("with a tendency to look after themselves instead of others.".center(80))
        print("\n")
        print("Slytherins are always striving to be the best and will do".center(80))
        print("almost anything to achieve honor and glory.".center(80))
        sleep(3)
    elif student['House'] == "Hufflepuff":
        logos.hufflepuff_logo()
        print("")
        print(f"Welcome to Hufflepuff {student['Name']}!".center(80))
        print(Style.RESET_ALL)
        sleep(3)
        print("")
        clear_display()
        print("")
        print("")
        print("Hufflepuff students are hard-working,".center(80))
        print("friendly, loyal and honest.".center(80))
        print("\n")
        print("Hufflepuff House values dedication,".center(80))
        print("patience, loyalty, and fair play.".center(80))
        sleep(3)
    elif student['House'] == "Ravenclaw":
        logos.ravenclaw_logo()
        print("")
        print(f"Welcome to Ravenclaw {student['Name']}!".center(80))
        print(Style.RESET_ALL)
        sleep(3)
        print("")
        clear_display()
        print("")
        print("")
        print("Ravenclaw House values wisdom, wit, intellectual".center(80))
        print("ability and creativity.".center(80))
        print("\n")
        print("Students in Ravenclaw are noted for".center(80))
        print("their individuality and acceptance of people and things".center(80))
        print("that others would consider weird, as well as their".center(80))
        print("outstanding intelligence.".center(80))
        sleep(3)
    else:
        print("Hmmm there seems to be something amiss...".center(80))
        print(" ")
        print("Let's go back and try again".center(80))
        re_sort()


def conclusion():
    """
    Function to give student option to accept
    determined House or ask to be re-sorted.
    """
    print("")
    print("")
    print(f"Congratulations {student['Name']} on being accepted".center(80))
    print(f"into {student['House']} House. We wish you all the best".center(80))
    print("and hope you enjoy your time with us here at Hogwarts for".center(80))
    print(f"the {year} school year.".center(80))
    sleep(2)
    print("")
    print("Alternatively, if you are not happy with the House".center(80))
    print(f"you have been put into {student['Name']}, we can run".center(80))
    print("through the questions again to find you a better fit!".center(80))
    print("")
    while True:
        print("")
        print("Please enter h if you are happy with your house and wish to meet".center(80))
        print("your new housemates".center(80))
        print("or".center(80))
        next_step = input("enter r if you wish to be re-sorted.\n>>>".center(80))
        if validate_conclusion(next_step):
            print("")
            print('Thank you'.center(70))
            print("")
            break
    if next_step == "r":
        re_sort()
    elif next_step == "h":
        update_house_spreadsheet()
        see_housemates()


def validate_conclusion(next_step):
    """
    Raises error if answer entered is not h or r.
    """
    try:
        if next_step not in {'h', 'r'}:
            raise ValueError(
              f"\nYou answered {next_step},"
            )
        elif next_step == '':
            raise ValueError(
              "\nYou did not provide an answer,"
            )
        else:
            return True

    except ValueError as e:
        print(f"{e} please select h or r as your answer to proceed.\n")
        return False


def quit_game():
    """
    Function to quit current status and return
    to start.
    """
    print("")
    print("You have decided to remove the Sorting Hat.".center(80))
    print("")
    print("Maybe we will see you back in Hogwarts next year.".center(80))
    print("")
    print(f"Goodbye {student['Name']}".center(80))
    sleep(3)
    clear_display()
    main()


def re_sort():
    """
    Function to return to questions if student
    wishes to be re-sorted.
    """
    generate_questions()
    determine_house()
    conclusion()


def see_housemates():
    """
    Function to generate a table with housemates
    of student based on determined house for student.
    """
    clear_display()
    print("Meet some of your fellow housemates for the coming term:".center(80))
    print("")
    print("")
    student_data = houses.get_all_values()
    dict_keys = ['Name', 'Age', 'Country', 'House']
    list_of_dict = [dict(zip(dict_keys, student)) for student in student_data]

    if student['House'] == "Gryffindor":
        classmates = [i for i in list_of_dict if i['House'] == 'Gryffindor']
    elif student['House'] == "Slytherin":
        classmates = [i for i in list_of_dict if i['House'] == 'Slytherin']
    elif student['House'] == "Hufflepuff":
        classmates = [i for i in list_of_dict if i['House'] == 'Hufflepuff']
    elif student['House'] == "Ravenclaw":
        classmates = [i for i in list_of_dict if i['House'] == 'Ravenclaw']
    print(tabulate(classmates, headers="keys", tablefmt="simple",))
    sleep(3)
    print("")
    print("Thank you for trying on the Sorting Hat.".center(80))
    print("")
    print("We wish you the very best for your time in Hogwarts.".center(80))
    print("")
    print("We must now move on to the next student.".center(80))
    print("")
    print("Goodbye!".center(80))
    sleep(7)
    main()


def main():
    """
    Function to call main functions of game
    to run.
    """
    clear_display()
    logos.intro_logo_2()
    print(Style.RESET_ALL)
    welcome()
    start_sorting()
    determine_house()
    conclusion()


main()
