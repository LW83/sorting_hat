import os
from datetime import datetime 
from time import sleep
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Style
from questions import questions

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
data = houses.get_all_values()

def intro_logo_1():
    print(Fore.YELLOW + r"""
       =                             
       =:                            
       :+                            
       .#:                           
        *+                           
        =#-                          
        -##.                         
        :##=                         
         ###.                        
         *##=                :.      
         =###.            .=*#+      
         -###+          :+#####.     
         .####-      :=*#######-     
          ####*   .=*##########+     
          +####--*##############.    
          -##############**#####-    
          .###########*=. .#####+    
           *#######+-.     .#####.   
           +####+:          -####=   
           -*=:              +####.  
                             .*###:  
                              .*##+  
                               :###  
                                =##: 
                                 +#= 
                                  ** 
                                  :#:
                                   ==
                                    +
                                    """.center(70))

def intro_logo_2():
    print(Fore.BLUE +r"""
                                        =++++=====.             
                                        +@@@@@@@@@: .-+*:       
                          :---------=   :@@@@@@@@@%@@%%@@#.     
          .........::     =@@@@@@@@-    @@@@@@@@@=   .@@@@+    
          -%@@@@@@@@=     .@@@@@@@*     #@@@@@@@@:    %@@@@%:  
            :@@@@@@@@       @@@@@@@+     +@@@@@@@@:    *@@@@@@* 
            :@@@@@@@@       %@@@@@@=     :@@@@@@@@:    =@@@@@@@:
            .@@@@@@@@       #@@@@@@=      @@@@@@@@:    -@@@@@@@.
            .@@@@@@@@       #@@@@@@=      #@@@@@@@:    :@@@@@@@ 
            @@@@@@@@       *@@@@@@=      =@@@@@@@-    .@@@@@@# 
            @@@@@@@@       *@@@@@@+      .@@@@@@@-    .@@@@@@+ 
            %@@@@@@@       *@@@@@@+:--=-. @@@@@@@-    .@@@@@@- 
      .:-   %@@@@@@@       *@@@@@@@%*+=%@%@@@@@@@=*-  .@@@@@@- 
    #@+:    #@@@@@@@.    :*@@@@@@@*    =@@@@@@@@@=.%#=@@@@@%=  
    .##=.   #@@@@@@@:.-*@@@@@@@@@@*    .@@@@@@@@@+  *@%#+-.    
      =%@%+-#@@@@@@@@@@@@%+#@@@@@@*     %@@@@@@@@*             
        .-+%@@@@@@@@#+=:   =@@@@@@*     +@@@@@@@@%             
            +@@@@@@@-      =@@@@@@*     :@@@@@@%@@             
            +@@@@@@@-      -@@@@@@*      @@@@@@==@.            
            +@@@@@@@-      -@@@@@@*    +-#@@@@@= =.            
            +@@@@@@@-      -@@@@@@*    -@@@@@@@=               
            *@@@@@@@-      -@@@@@@*     @@@@@@@=               
            #@@@@@@@=      =@@@@@@*     #@@@@@@=               
            -@@@@@@@@=      *@@@@@@*     -@@@@@@=               
          =#%@@@@@@@@%:     %@@@@@@#      @@@%+@=               
                      ..  .#@@@@@@@@:     #@@# ==               
                        -*******##%%+.   -@@*                  
                                          @@+                  
                                          #@-                  
                                          -@:                  
                                            @                   
                                            *     """)

def welcome():
    """
    Welcome function to request name, age and 
    country inputs from user. 
    """
    print('THE SORTING HAT\n'.center(70))

    sleep(2)
    
    while True: 
        name = input("Please tell me your name:".center(70))
        if validate_name(name):
            print(f"\nNice to meet you {name}!".center(70))
            break
    
    sleep(1)

    while True:
        age = input(f"\nPlease tell me your age:".center(70))  
        if validate_age(int(age)):
            print(f"\nThank you!".center(70))
            break
    
    sleep(1)

    while True: 
        country = input("\nFinally, please tell us what Country you are from:".center(70))
        if validate_country(country):
            print(f"\nThank you {name}!".center(70))
            break
    
    sleep(2)
    clear_display()

    print("Confirming non-Muggle status........\n".center(70))
    sleep(3)
    print("Non-Muggle status VALIDATED\n".center(70))
    sleep(2)
    clear_display()
    
    intro_logo_1()
    print(Style.RESET_ALL)
    print(f"Welcome to Hogwarts School of Witchcraft and Wizardry {name}.\n".center(70))
    sleep(2)
    print(f"We are delighted to have you join us for the {year} school term.\n".center(70))
    sleep(3)
    print("In order to place you in the correct house for your time with us, ".center(70))
    print("the Sorting Hat needs to know a little more about you...\n".center(70))
    sleep(3)
    print(f"So, {name}, are you ready to get started?\n".center(70))

def start_sorting():
    sort = input("\nPlease enter y for 'Let's get sorted!' or n if you wish to remove the sorting hat.".center(70))
    if sort == 'n':
        print(f"\n\nYou have removed the sorting hat. Goodbye NAME maybe we will see you next term instead.".center(70))
        sleep (3)
        clear_display()
        main()
    elif sort == 'y':
        generate_questions()
    elif sort == '':
        print("\nPlease enter either 'y' or 'n' in order to proceed.\n".center(70))
    else:
        print("\nPlease enter either 'y' or 'n' in order to proceed.\n".center(70))

def generate_questions():
    """
    Runs through sorting hat questions
    """
    clear_display()
    for q in questions:  #https://stackoverflow.com/questions/33069253/looping-through-multiple-choice-questions
        print(q['question'])
        sleep(1)
        for i, c in enumerate(q['options']):
            print(chr(97 + i)+ ':', c)
            
        while True: 
            answer = input("Enter your answer:\n>>> ".center(70))
    
            if validate_answer(answer):
                print('\nThank you'.center(70))
                break

        sleep(1)
        clear_display()

def clear_display(): #dnlBowers
    """"
    Clears the console
    """
    command = 'clear'
    if os.name in (
            'nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
  
def validate_name(name):
    """
    Raises error if name entered has numerical entries.
    """
    try: 
      if name.isnumeric():
        raise ValueError(
          f"\nPlease enter your name as text, you entered {name}"
        )
      elif len(name.strip()) == 0: #rockymiss
        raise ValueError(
          "\nPlease enter your name, we need this to ensure you can be accepted to Hogwarts"
        )
    except ValueError as e:
      print(f"{e}, please try again.\n")
      return False
    
    return True

def validate_age(number):
    """
    Raises error if age entered is over 18.
    """
    try: 
      if number > 18:
        raise ValueError(
          f"\n{number}! Hogwarts cannot accept students over the age of 18."
          "\n Please re-count your years and try again."
        )
      elif number < 4:
        raise ValueError(
          f"\nHogwarts can only accept students over the age of 4." 
          "\nAs you are only {number} you will need to wait a few years and come back."
          "Please re-counr your years and try again."
        )
      elif len(str(number.strip)) == 0
        raise ValueError(
          "\nPlease tell us your age so we are sure you can be accepted to Hogwarts."
        )
      else:
        return True

    except ValueError as e:
      print(f"\n{e}\n")
      return False

def validate_country(country):
    """
    Raises error if name entered has numerical entries.
    """
    try: 
      if name.isnumeric():
        raise ValueError(
          f"\nPlease enter your country as text, you entered {name}"
        )
      elif len(name.strip() == 0:
        raise ValueError(
          "\nPlease enter your country, we need this to ensure you can be accepted to Hogwarts"
        )
    except ValueError as e:
      print(f"{e}, please try again.\n")
      return False
    
    return True

def validate_answer(answer):
    """
    Raises error if answer entered is not a, b, c, or d.
    """
    try: 
      if answer not in {'a','b','c','d'}:
        raise ValueError(
          f"\nYou answered {answer},"
        )
      elif answer == '':
        raise ValueError(
          "\nYou did not provide an answer,"
        )
      else:
        return True

    except ValueError as e:
      print(f"{e} please select a, b, c or d as your answer to proceed.\n")
      return False
    
def main():
    intro_logo_2()
    print(Style.RESET_ALL)
    welcome()
    start_sorting()
    generate_questions()

main()