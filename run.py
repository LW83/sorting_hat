import os
import statistics
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
student = {"Name" : "", "Age" : "", "Country" : "", "House" : ""}

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
        name = input("Please tell me your name:\n>>>".center(70))
        
        if validate_name(name):
            print(f"\nNice to meet you {name}!".center(70))
            student.update({"Name" : name}) #rockymiss
            break
    
    sleep(1)

    while True:
        age = input(f"\nPlease tell me your age:\n>>>".center(70))  
        
        if validate_age(age):
            print(f"\nThank you!".center(70))
            student.update({"Age" : age}) 
            break
    
    sleep(1)

    while True: 
        country = input("\nFinally, please tell us what Country you are from:".center(70))
        if validate_country(country):
            print(f"\nThank you {name}!".center(70))
            student.update({"Country" : country})
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

    return student

def start_sorting():
    sort = input("\nPlease enter y for 'Let's get sorted!' or n if you wish to remove the sorting hat.".center(70))
    if sort == 'n':
        print(f"\n\nYou have removed the sorting hat. Goodbye {student['Name']} maybe we will see you next term instead.".center(70))
        sleep (3)
        clear_display()
        main()
    elif sort == 'y':
        generate_questions()
    else:
        print("\nPlease enter either 'y' or 'n' in order to proceed.\n".center(70))

def generate_questions():
    """
    Runs through sorting hat questions
    """
    clear_display()
    
    answers = []
    
    for q in questions:
        print(q['question']) #https://stackoverflow.com/questions/33069253/looping-through-multiple-choice-questions
        sleep(1)
        for i, c in enumerate(q['options']):
            print(chr(97 + i) + ':', c)

        while True: 
            answer = input("Enter your answer:\n>>> ".center(70))
    
            if validate_answer(answer):
                print('\n\nThank you'.center(70))
                answers.append(answer)
                break

        sleep(1)
        clear_display()
    
    house = statistics.mode(answers)
    
    if house == 'a':
        student.update({"House" : "Gryffindor"})
    elif house == 'b':
        student.update({"House" : "Slytherin"})
    elif house == 'c':
        student.update({"House" : "Hufflepuff"})
    elif house == 'd':
        student.update({"House" : "Ravenclaw"})
    else:
        print("Hmmmmm...I am having some trouble sorting you.")
        print("Perhaps we should run through the questions again..")
    
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
      #elif number.isnumeric() = False
      #  raise ValueError(
      #    "\nPlease tell us your age so we are sure you can be accepted to Hogwarts."
      #  )
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

def update_house_spreadsheet():#rockymiss
    """
    Populates Houses tab of Google spreadsheet
    with name, age and country input data.
    """
    new_student = list(student.values())
    houses.append_row(new_student)

def determine_house():
    if (student['House'] == "Gryffindor"):
        print(Fore.RED + r"""
                                        
                    :=*%%#:              
                -*%@@@@@@@@*             
            :+%@@@@@@@@@@@@@@-           
         -*@@@@@@@@%+-.@@@@@@@#.         
      -#@@@@@@@@+:     :@@@@@@@@=        
   .*@@@@@@@@@+         +@@@@@@@@%      .
   +@@@@@@@@@#           %@@@@@@@@+      
   +@@@@@@@@@#           +@@@@@%=        
   +@@@@@@@@@#           =@@@+:          
   #@@@@@@@@@#           %#-             
   #@@@@@@@@@*          -.               
   #@@@@@@@@@+                           
   @@@@@@@@@@+                           
   @@@@@@@@@@+                           
   @@@@@@@@@@+              :=+*#%%##    
   @@@@@@@@@@+         .=*%@@@@@@@@@@    
   @@@@@@@@@@+    .-+#@@@@@@@@@@@@@@@    
   @@@@@@@@@@+   :+*%@@@@@%@@@@@@@@@%    
   @@@@@@@@@@+         .   @@@@@@@@@#    
   @@@@@@@@@@+             @@@@@@@@@#    
   #@@@@@@@@@+             @@@@@@@@@@    
   #@@@@@@@@@+             @@@@@@@@@@    
   :@@@@@@@@@+             @@@@@@@@@@    
    .#@@@@@@@+             @@@@@@@@@%    
      -@@@@@@%:            @@@@@@@@*.    
        -%@@@@@*.        -%@@@@@@*:      
          -*@@@@@#=..-+%@@@@@@@+.        
            .+@@@@@@@@@@@@@%*:           
               =%@@@@@@%*=.              
                 .:-:.      """)
        print("")
        print(f"Welcome to Gryffindor {student['Name']}!".center(80))
        print(Style.RESET_ALL)
        sleep(1)
        print("")
        print("Gryffindor students are couragous and daring.".center(80))
        print("\n")
        print("Gryffindor House values nerve, leadership and chivalry.".center(80))
    elif (student['House'] == "Slytherin"):
        print(Fore.GREEN + r"""
                      .-*#%-              
                  .=%@@@@@@%:            
                -#@@@@@@@@@@@+           
             .+@@@@@@@@@@@@@@@@-         
           -#@@@@@@@@@@@@@@@@@@@%:       
        :*@@@@@@*. .-*@@@@@@@@@@@@+      
      =%@@@@@@@:       -#@@@@@@@@@@@:    
    *@@@@@@@@@*          :*@@@@@@@@@@.   
   %@@@@@@@@@@@:           .*@@@@@@@@%   
    *@@@@@@@@@@@*            :%@@@@@@@.  
     -@@@@@@@@@@@@-           =@@@@@%=   
       +@@@@@@@@@@@%:       =##+=-:      
        .#@@@@@@@@@@@*.                  
          -%@@@@@@@@@@@+                 
            =@@@@@@@@@@@@=               
             .*@@@@@@@@@@@%-             
               :%@@@@@@@@@@@#:           
                 =@@@@@@@@@@@@*.         
                   +@@@@@@@@@@@@+        
         .:=++:     .#@@@@@@@@@@@@=      
      -*@@@@=         =@@@@@@@@@@@@%:    
    -@@@@@@#           .#@@@@@@@@@@@@+   
    *@@@@@@@+            =@@@@@@@@@@@@#  
    .@@@@@@@@#            =@@@@@@@@@@@@. 
     -@@@@@@@@@-         .#@@@@@@@@@%-
      -@@@@@@@@@#.      +@@@@@@@@@*- 
        +@@@@@@@@@+   :%@@@@@@@@+.  
         .#@@@@@@@@@*+@@@@@@@#-       
           -@@@@@@@@@@@@@@%=.            
             *@@@@@@@@@@*:               
              :%@@@@@*-                  
                ===:           """)
        print("")
        print(f"Welcome to Slytherin {student['Name']}!".center(80))
        print(Style.RESET_ALL)
        sleep(1)
        print("")
        print("Slytherin students are ambitious and shrewd".center(80))
        print("with a tendency to look after themselves instead of others.".center(80))
        print("\n")
        print("Slytherins are always striving to be the best and will do".center(80))
        print("almost anything to achieve honor and glory.".center(80))
    elif (student['House'] == "Hufflepuff"):
        print(Fore.YELLOW + r"""
                                            
                                  ..     
                       .=%@@@@@@@@@=     
       :*@@@@@@@@@@=      @@@@@@@@.      
         *@@@@@@@@*       @@@@@@@#       
         =@@@@@@@@*       @@@@@@@%       
         =@@@@@@@@*       @@@@@@@%       
         =@@@@@@@@*       @@@@@@@%       
         -@@@@@@@@*       @@@@@@@@       
         -@@@@@@@@*       @@@@@@@@      
         -@@@@@@@@*       @@@@@@@@     
         -@@@@@@@@#       @@@@@@@@:=*%@@@
     :-: -@@@@@@@@#       @@@@@@@@@@@@@@@
   *@=   :@@@@@@@@#       @@@@@@@@-   .*@
   =@#   :@@@@@@@@#     -*@@@@@@@@.    .@
    =@@*--@@@@@@@@#.-+%@@@@@@@@@@@.    
      -*%@@@@@@@@@@@@@%+-.@@@@@@@@:    
         :@@@@@@@@@-.     @@@@@@@@:    
         :@@@@@@@@%       @@@@@@@@:    
         .@@@@@@@@%       @@@@@@@@-    
         .@@@@@@@@%       @@@@@@@@-     
         .@@@@@@@@%       @@@@@@@@-      
         .@@@@@@@@@       @@@@@@@@=      
         .@@@@@@@@@       @@@@@@@@=      
         :@@@@@@@@@       @@@@@@@@=      
       :+@@@@@@@@@@%-     @@@@@@@@+      
       .........::::::   *@@@@@@@@#      
                       :*##########*-  
                       """)
        print("")
        print (f"Welcome to Hufflepuff {student['Name']}!".center(80))
        print(Style.RESET_ALL)
        sleep(1)
        print("")
        print("Hufflepuff students are hard-working,".center(80))
        print("friendly, loyal and honest.".center(80)) 
        print("\n")
        print("Hufflepuff House values dedication,".center(80))
        print("patience, loyalty, and fair play.".center(80))
    elif (student['House'] == "Ravenclaw"):
        print(Fore.BLUE + r"""
    -@@@@@@@@@@   :+-          
    @@@@@@@@@@+#@@@@#.        
    %@@@@@@@@@@#+-+@@@=       
    +@@@@@@@@@    =@@@@%:     
    -@@@@@@@@@    -@@@@@@*.   
    .@@@@@@@@@    :@@@@@@@@.  
     %@@@@@@@@    .@@@@@@@@   
     *@@@@@@@@     @@@@@@@%  
     -@@@@@@@@     @@@@@@@* 
     .@@@@@@@@     @@@@@@@=  
      @@@@@@@@     %@@@@@@:   
   ##+%@@@@@@@.    #@@@@@@    
   +@@@@@@@@@@@%+-%@@@@@@%    
   :@@@@@@@@@@@@@@@@@%*=:     
    %@@@@@@@@*:@@@@@+       
    +@@@@@@@@# .@@@@%       
    :@@@@@@@@%  =@@@@-       
     @@@@@@*@@   %@@@%       
   : *@@@@@::%   :@@@@-       
   +@@@@@@@-      +@@@@       
   .@@@@@@@-       %@@@*      
    %@@@@@@-       :@@@@-     
    =@@@@@@=        +@@@@.    
    .@@@@@@=         @@@@#    
     #@@@*@+         =@@@@#   
     =@@@:.=          @@@@@#  
      @@@             #@@@@@@*
      #@%             ###%%@@@
      -@*                    :
       @=                     
       *-                     
       -.                     
                        """)
        print("")
        print (f"Welcome to Ravenclaw {student['Name']}!".center(80))
        print(Style.RESET_ALL)
        sleep(1)
        print ("")
        print("Ravenclaw House values wisdom, wit, intellectual".center(80))
        print("ability and creativity.".center(80))
        print("\n")
        print("Students in Ravenclaw are noted for".center(80)) 
        print("their individuality and acceptance of people and things".center(80))
        print("that others would consider weird, as well as their".center(80))
        print("outstanding intelligence.".center(80)) 
    else:
        print("Hmmm there seems to be something amiss...")

def conclusion():
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
  input("""
        Please enter h if you are happy with your house and wish to
        see who your fellow housemates will be or r if you wish to be 
        re-sorted.
        """.center(80))

def quit():

def re-sort():

def see_housemates():

def main():
    #intro_logo_2()
    #print(Style.RESET_ALL)
    welcome()
    start_sorting()
    update_house_spreadsheet()
    determine_house()

main()