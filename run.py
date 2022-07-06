from datetime import datetime 
import gspread
from google.oauth2.service_account import Credentials

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
    print(r"""
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
    print(r"""
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
    """
    name = input("Please enter your Name:\n")
    validate_name(name)
    age = input(f"Hi {name}, please tell us your age:\n")
    validate_age(int(age))
    country = input("Thank you, finally, please tell us what Country you are from:\n")

    print("Confirming non-Muggle status........\n")
    print("Non-muggle status validated\n")
    print(f"Welcome to Howgwarts School of Witchcraft and Wizardry {name}. \nWe are delighted to have you join us for the {year} school term.\n")
    print("In order to place you in the correct house for your time with us, the Sorting Hat needs to know a little more about you...")
    print(f"So, {name} are you ready to get started?")

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

def validate_age(number):
    """
    Raises error if age entered is over 18.
    """
    try: 
      if number > 18:
        raise ValueError(
          f"{number}! Those over 18 are above the age of acceptance for Hogwarts"
        )
    except ValueError as e:
      print(f"{e}, please re-count your years and try again.\n")

def main():
    intro_logo_2()
    welcome()

main()