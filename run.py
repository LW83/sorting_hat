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
                                """)

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
    clear_display()

    while True:
        age = input(f"\nPlease tell me your age:".center(70))
        
        if validate_age(int(age)):
            print(f"\nThank you!".center(70))
            break
    
    sleep(1)
    clear_display()

    country = input("\nFinally, please tell us what Country you are from:\n".center(70))
  
    sleep(2)
    clear_display()

    print("\nConfirming non-Muggle status........\n".center(70))
    sleep(3)
    print("Non-Muggle status VALIDATED\n".center(70))
    sleep(2)
    print(f"Welcome to Hogwarts School of Witchcraft and Wizardry {name}.\n".center(70))
    sleep(2)
    print(f"We are delighted to have you join us for the {year} school term.\n".center(70))
    sleep(3)
    print("In order to place you in the correct house for your time with us, ".center(70))
    print("the Sorting Hat needs to know a little more about you...\n".center(70))
    sleep(2)
    print(f"So, {name}, are you ready to get started?\n".center(70))

def start_sorting():
    sort = input("Please enter y for 'Let's get sorted!' or n if you wish to remove the sorting hat.".center(70))
    if sort == 'n':
        print(f"You have removed the sorting hat. Goodbye {name} maybe we will see you next term instead.".center(70))
        welcome()
    elif sort == 'y':
        generate_questions()
    else:
        print("\nPlease enter either 'y' or 'n' in order to proceed.".center(70))

#def generate_questions():#

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
          f"Please enter your name as text, you entered {name}"
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
          f"{number}! Those over 18 are above the age of acceptance for Hogwarts"
        )
      elif number < 4:
        raise ValueError(
          f"Unfortunately Hogwarts can only accept students over the age of 4. As you are only {number} you will need to wait a few years and come back."
        )
      else:
        return True

    except ValueError as e:
      print(f"{e} Please re-count your years and try again.\n")
      return False
    
def main():
    intro_logo_2()
    print(Style.RESET_ALL)
    welcome()
    start_sorting()

main()