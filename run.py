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

houses = SHEET.worksheet('Houses')
data = houses.get_all_values()

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

name = input("Please enter your Name:\n")
age = input(f"Hi {name}, please tell us your age:\n")
country = input("Thank you, finally please tell us what Country you are from:\n")

print("Confirming non-Muggle status........\n")
print("Non-muggle status validated\n")

print(f"Welcome to Howgwarts School of Witchcraft and Wizardry {name}. \nWe are delighted to have you join us for the XXXX school term.\n")

print("In order to place you in the correct house for your time with us, the Sorting Hat needs to know a little more about you...")

print(f"So, {name} are you ready to get started?")
