#import os and time module
import os
import time

#set the command for clearing the console
clear = lambda: os.system('clear')
clear()

#create a list called "history" to store calculation histories
history = []

#print calculator startup screen
print(r"""

   ____ _     ___    ____    _    _     ____ _   _ _        _  _____ ___  ____  
  / ___| |   |_ _|  / ___|  / \  | |   / ___| | | | |      / \|_   _/ _ \|  _ \ 
 | |   | |    | |  | |     / _ \ | |  | |   | | | | |     / _ \ | || | | | |_) |
 | |___| |___ | |  | |___ / ___ \| |__| |___| |_| | |___ / ___ \| || |_| |  _ < 
  \____|_____|___|  \____/_/   \_\_____\____|\___/|_____/_/   \_\_| \___/|_| \_\
                                                                                

""")
#wait for 1 second
time.sleep(1)
#clear console
clear()

#create a function for the calculating function
def calculate():
    clear()
    #print calculator default menu
    print(r"""CLI Calculator
=======================================================
Enter 'help' for assistance.
Enter 'clear' to clear the screen.
Enter 'history' to continue from previous calculations.
Enter 'game' to play the calculator mini game.
=======================================================
    """)
    #use try and except to show an error message instead of terminating the process when user provides unsupported input
    try:
        #ask for an expression and save the expression to a variable called "expression"
        expression = input("Calculate: ")
        #if the user input is "help"
        if expression == "help":
            clear()
            #print a help menu
            print(r"""CLI Calculator Help Menu
=======================================================
Enter 'help' for assistance.
Enter 'clear' to clear the screen.
Enter 'history' to view calculation history.
Enter 'game' to play the calculator mini game.
=======================================================
Supported Operations:
1. Basic Arithmetic:
- Addition: 1+1
- Subtraction: 1-1
- Multiplication: 1*1
- Division: 1/1
        
2. Exponentiation
- 1^1 oor 1**1
        
Note: Percentages are not directly supported 
      using the "%" symbol. Calculate
      percentages by dividing by 100.
=======================================================
            """)
            #ask for an input and go back to the calculator when user presses enter
            input("Press enter to continue. ")
            clear()
            calculate()
        #else, if user input is "clear", clear the console
        elif expression == "clear":
            clear()
            calculate()
        #else, if user input is "history"
        elif expression == "history":
            clear()
            print(r"""CLI Calculator
=======================================================
Enter 'help' for assistance.
Enter 'clear' to clear the screen.
Enter 'history' to continue from previous calculations.
Enter 'game' to play the calculator mini game.
=======================================================
            """)
            #print the title "Calculations History"
            print("Calculations History")
            #print the list "history" in a numbered format 
            for number, letter in enumerate(history):
                print(f"{number+1}. {letter}")
            print(r"""
=======================================================
            """)
            formatted_output = '/'.join(map(str, range(1, len(history) + 1)))
            #ask user to choose a number from the history the continue calculation
            history_actual_input = int(input(f"Enter the number corresponding to your choice ({formatted_output}): ")) - 1
            #call function with the number from the choice of user
            continue_calculation(history[history_actual_input])
        #else, if expression is "game"
        elif expression == "game":
            #call function "game" to start playing a game
            game(expression)
        #else, if expression is none of the above
        else:
            #evaluate the user input as a mathematics expression and save the answer to the variable "result"
            result = eval(expression)
            #add the answer to the calculation histories by adding it to the list "history"
            history.append(result)
            #print the answer
            print("=", result)
            print(r"""
=======================================================
                  
1. New Calculation.
2. Continue calculation with current result.
            """)
            #let the user decide whether they want to start a new calculation or continue the calculation with the current number
            calculation_choice = input("(1/2): ")
            #if user input equals to "1", clear the console and start a new calculation
            if calculation_choice == "1":
                clear()
                calculate()
            #else, if user input equals to "2", call the function "continue_calculation" with the variable "result"
            elif calculation_choice == "2":
                continue_calculation(result)
            #else, if the input equals to none of the above
            else:
                #print an error message
                print(r"""
=======================================================    
Error. Press enter to continue.
=======================================================
                """)
                #after user presses enter, clear the console and start with a new calculation
                input()
                clear()
                calculate()
    except:
        #if user input is invalid, print an error message
        print(r"""
=======================================================    
Error. Press enter to continue.
=======================================================
""")
        #when user presses enter, clear the console and start with a new calculation
        input()
        clear()
        calculate()

#function to let calculation continue with the current result
def continue_calculation(last_result):
    clear()
    print(r"""CLI Calculator
=======================================================
Enter 'help' for assistance.
Enter 'clear' to clear the screen.
Enter 'history' to continue from previous calculations.
Enter 'game' to play the calculator mini game.
=======================================================
    """)
    #ask for an input with the current result printed on the console
    new_expression = input(f"{last_result}")
    #calculate the combination of the current result and the new operators and numbers
    combined_expression = f"{last_result}{new_expression}"
    try:
        if new_expression == "help":
            clear()
            print(r"""CLI Calculator Help Menu
=======================================================
Enter 'help' for assistance.
Enter 'clear' to clear the screen.
Enter 'history' to view calculation history.
Enter 'game' to play the calculator mini game.
=======================================================
Supported Operations:
1. Basic Arithmetic:
- Addition: 1+1
- Subtraction: 1-1
- Multiplication: 1*1
- Division: 1/1
        
2. Exponentiation
- 1^1 oor 1**1
        
Note: Percentages are not directly supported 
      using the "%" symbol. Calculate
      percentages by dividing by 100.
=======================================================
Press enter to continue.
            """)
            input()
            clear()
            calculate()
        elif new_expression == "clear":
            clear()
            calculate()
        elif new_expression == "history":
            clear()
            print(r"""CLI Calculator
=======================================================
Enter 'help' for assistance.
Enter 'clear' to clear the screen.
Enter 'history' to continue from previous calculations.
Enter 'game' to play the calculator mini game.
=======================================================
            """)
            print("Calculations History")
            for number, letter in enumerate(history):
                print(f"{number+1}. {letter}")
            print(r"""
=======================================================
            """)
            formatted_output = '/'.join(map(str, range(1, len(history) + 1)))
            history_actual_input = int(input(f"Enter the number corresponding to your choice ({formatted_output}): ")) - 1
            continue_calculation(history[history_actual_input])
        elif new_expression == "game":
            game(new_expression)
        else:
            result = eval(combined_expression)
            history.append(result)
            print("=", result)
            print(r"""
=======================================================   
1. New Calculation.
2. Continue calculation with current result.
            """)
            calculation_choice = input("(1/2): ")
            if calculation_choice == "1":
                clear()
                calculate()
            elif calculation_choice == "2":
                continue_calculation(result)
            else:
                print(r"""
=======================================================
Error. Press enter to continue.
=======================================================
                """)
                input()
                clear()
                calculate()
    except:
        print(r"""
=======================================================
Error. Press enter to continue.
=======================================================
""")
        input()
        clear()
        calculate()

#game
#the code is not efficient, but if it works, don't touch it
def game(last_result):
    # clear the console after every interaction to keep the interface clean
    clear = lambda: os.system('clear')
    clear()

    # title screen
    print(r"""
   ____      _            _       _                                          
  / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __    __ _  __ _ _ __ ___   ___ 
 | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|  / _` |/ _` | '_ ` _ \ / _ \
 | |__| (_| | | (__| |_| | | (_| | || (_) | |    | (_| | (_| | | | | | |  __/
  \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|     \__, |\__,_|_| |_| |_|\___|
                                                  |___/   

    To return to the calculator, finish the game or restart the application.
    """)
    #wait for 3 seconds
    time.sleep(3)
    clear()
    print(r"""
        Interactive Game

  ___  ___  ___  __ _ _ __   ___
 / _ \/ __|/ __|/ _` | '_ \ / _ \
|  __/\__ \ (__| (_| | |_) |  __/
 \___||___/\___|\__,_| .__/ \___|
                     |_|          
    """)
    input("Press enter to start ")

    # outcomes
    def one():
        # clear the console
        clear = lambda: os.system('clear')
        clear()
        # print text description
        print("You wake up and see that you are in an empty room.")
        print("There is a phone and a key on the floor. What will you do?")
        # print ascii art
        print(r"""
        ||
  ______||       
 / ____ o|       
| / ;; \ |       
| ______ |       
||______||       ____     
||      ||      , =, ( _________
||______||      | ='  (VvvVvV--'
|'\[--]/'|      |____(
|  ¨''¨  |
|  ''''  |
|        |
|        |
|        |
|________| 
        """)
        # print choices
        print("A. Pick up the phone")
        print("B. Pick up the key")
        # using while loop for the input
        while True:
            # request input
            one_input = input()
            # if user chooses A, jump to a different outcome and break loop
            if one_input == "a" or one_input == "A":
                two()
                break
            # if user chooses B, jump to a different outcome and break loop
            elif one_input == "b" or one_input == "B":
                three()
                break
            # else, tell the user to try again
            else:
                print("Invalid input, please try again.")
    def one_a():
        clear = lambda: os.system('clear')
        clear()
        print("There is a phone and a key on the floor. What will you do?")
        print(r"""
        ||
  ______||       
 / ____ o|       
| / ;; \ |       
| ______ |       
||______||       ____     
||      ||      , =, ( _________
||______||      | ='  (VvvVvV--'
|'\[--]/'|      |____(
|  ¨''¨  |
|  ''''  |
|        |
|        |
|        |
|________| 
        """)
        print("A. Pick up the phone")
        print("B. Pick up the key")
        while True:
            one_a_input = input()
            if one_a_input == "a" or one_a_input == "A":
                two()
                break
            elif one_a_input == "b" or one_a_input == "B":
                three()
                break
            else:
                print("Invalid input, please try again.")
    def two():
        clear = lambda: os.system('clear')
        clear()
        print("You picked up the phone. You received a text message.")
        print(r"""
        ||
  ______||
 / ____ o|
| / ;; \ |
| ______ |
||______|| 
||1 MSG || 
||______|| 
|'\[--]/'|
|  ¨''¨  |
|  ''''  |
|        |
|        |
|        |
|________|
    """)
        print("A. Open the text message")
        print("B. Ignore and call 911")
        while True:
            two_input = input()
            if two_input == "a" or two_input == "A":
                four()
                break
            elif two_input == "b" or two_input == "B":
                five()
                break
            else:
                print("Invalid input, please try again.")

    def three():
        clear = lambda: os.system('clear')
        clear()
        print("You picked up the key and looked around, you saw two doors.")
        print(r"""
 _______________         _______________
|\ ___________ /|       |\ ___________ /|
| |  _ _ _ _  | |       | |  _ _ _ _  | |
| | | | | | | | |       | | | | | | | | |
| | |-+-+-+-| | |       | | |-+-+-+-| | |
| | |-+-+=+%| | |       | | |-+-+=+%| | |
| | |_|_|_|_| | |       | | |_|_|_|_| | |
| |    ___    | |       | |    ___    | |
| |   [___] ()| |       | |   [___] ()| |
| |         ||| |       | |         ||| |
| |         ()| |       | |         ()| |
| |           | |       | |           | |
| |           | |       | |           | |
| |           | |       | |           | |
|_|___________|_|       |_|___________|_|
        """)
        print("A. Try to unlock the first door")
        print("B. Try to unlock the second door")
        while True:
            three_input = input()
            if three_input == "a" or three_input == "A":
                six_a()
                break
            elif three_input == "b" or three_input == "B":
                seven_a()
                break
            else:
                print("Invalid input, please try again.")

    def four():
        clear = lambda: os.system('clear')
        clear()
        print("You opened the text message. An anonymous number said, “ARE YOU READY TO PLAY A GAME?")
        print(r"""
        ||
  ______||  
 / ____ o| 
| / ;; \ | 
| ______ | 
||______|| 
||OPENED|| 
||______|| 
|'\[--]/'| 
|  ¨''¨  | 
|  ''''  | 
|        | 
|        | 
|        | 
|________| 
        """)
        print("A. Ask him 'Who is he?'")
        print("B. Ignore it, put down the phone")
        print("C. Ignore it, call 911")
        while True:
            four_input = input()
            if four_input == "a" or four_input == "A":
                eight()
                break
            elif four_input == "b" or four_input == "B":
                one_a()
            elif four_input == "c" or four_input == "C":
                five()
                break
            else:
                print("Invalid input, please try again.")

    def five():
        clear = lambda: os.system('clear')
        clear()
        print(r"""
        ||
  ______||  
 / ____ o| 
| / ;; \ | 
| ______ | 
||______|| 
|| 911  || 
||______|| 
|'\[--]/'| 
|  ¨''¨  | 
|  ''''  | 
|        | 
|        | 
|        | 
|________| 
        """)
        print("You ignored the message and called 911. The man with a weird voice picked up the call. 'NO ONE CAN HELP YOU. YOU WILL NOT ESCAPE.'")
        print("A. Try to unlock the first door")
        print("B. Try to unlock the second door")
        while True:
            five_input = input()
            if five_input == "a" or five_input == "A":
                eight()
                break
            elif five_input == "b" or five_input == "B":
                one_a()
                break
            else:
                print("Invalid input, please try again.")

    def six():
        clear = lambda: os.system('clear')
        clear()
        print("You tried to unlock the first door. It opened. You see a green forest.")
        print(r"""
 _______________
|\ ___________ /|
| |  /|,| |   | |
| | |,x,| |   | |
| | |,x,' |   | |
| | |,x   ,   | |
| | |/    |%==| |
| |    /] ,   | |
| |   [/ ()   | |
| |       |   | |
| |       |   | |
| |       |   | |
| |      ,'   | |
| |   ,'      | |
|_|,'_________|_|    
        """)
        print("A. Walk into the forest")
        print("B. Walk into the second door")
        while True:
            six_input = input()
            if six_input == "a" or six_input == "A":
                nine()
                break
            elif six_input == "b" or six_input == "B":
                seven()
                break
            else:
                print("Invalid input, please try again.")

    def six_a():
        clear = lambda: os.system('clear')
        clear()
        print("You tried to unlock the first door. It opened. You see a green forest.")
        print(r"""
 _______________
|\ ___________ /|
| |  /|,| |   | |
| | |,x,| |   | |
| | |,x,' |   | |
| | |,x   ,   | |
| | |/    |%==| |
| |    /] ,   | |
| |   [/ ()   | |
| |       |   | |
| |       |   | |
| |       |   | |
| |      ,'   | |
| |   ,'      | |
|_|,'_________|_|    
        """)
        print("A. Walk into the forest")
        print("B. Try to unlock the second door")
        while True:
            six_a_input = input()
            if six_a_input == "a" or six_a_input == "A":
                nine()
                break
            elif six_a_input == "b" or six_a_input == "B":
                seven()
                break
            else:
                print("Invalid input, please try again.")

    def seven():
        clear = lambda: os.system('clear')
        clear()
        print("You tried to unlock the second door. It opened. You see another room.")
        print(r"""
 _______________
|\ ___________ /|
| |  /|,| |   | |
| | |,x,| |   | |
| | |,x,' |   | |
| | |,x   ,   | |
| | |/    |%==| |
| |    /] ,   | |
| |   [/ ()   | |
| |       |   | |
| |       |   | |
| |       |   | |
| |      ,'   | |
| |   ,'      | |
|_|,'_________|_|    
        """)
        print("A. Walk into the first door")
        print("B. Walk into the room")
        while True:
            seven_input = input()
            if seven_input == "a" or seven_input == "A":
                nine()
                break
            elif seven_input == "b" or seven_input == "B":
                ten()
                break
            else:
                print("Invalid input, please try again.")

    def seven_a():
        clear = lambda: os.system('clear')
        clear()
        print("You tried to unlock the second door. It opened. You see another room.")
        print(r"""
 _______________
|\ ___________ /|
| |  /|,| |   | |
| | |,x,| |   | |
| | |,x,' |   | |
| | |,x   ,   | |
| | |/    |%==| |
| |    /] ,   | |
| |   [/ ()   | |
| |       |   | |
| |       |   | |
| |       |   | |
| |      ,'   | |
| |   ,'      | |
|_|,'_________|_|    
        """)
        print("A. Try to unlock the first door")
        print("B. Walk into the room")
        while True:
            seven_a_input = input()
            if seven_a_input == "a" or seven_a_input == "A":
                six()
                break
            elif seven_a_input == "b" or seven_a_input == "B":
                ten()
                break
            else:
                print("Invalid input, please try again.")
    def eight():
        clear = lambda: os.system('clear')
        clear()
        print("You asked him for his identity. Suddenly, your phone shut off by itself.")
        print(r"""
        ||
  ______||
 / ____ o|
| / ;; \ |
| ______ |
||______|| 
|| OFF  ||
||______|| 
|'\[--]/'|
|  ¨''¨  |
|  ''''  |
|        |
|        |
|        |
|________|
        """)
        print("A. Try to restart the phone")
        print("B. Put down the phone and pick up the key")
        while True:
            eight_input = input()
            if eight_input == "a" or eight_input == "A":
                eleven()
                break
            elif eight_input == "b" or eight_input == "B":
                three()
                break
            else:
                print("Invalid input, please try again.")
    def nine():
        clear = lambda: os.system('clear')
        clear()
        print("You walked into the forest. There are a lot of trees but no animals. Suddenly you heard arobotic sound: 'If you want to survive, you need to finish this maze. HAHAHAHAHAHA.'")
        print("""
                  * *    
           *    *  *
      *  *    *     *  *
     *     *    *  *    *
 * *   *    *    *    *   *
 *     *  *    * * .#  *   *
 *   *     * #.  .# *   *
  *     "#.  #: #" * *    *
 *   * * "#. ##"       *
   *       "###
             "##
              ##.
              .##:
              :###
              ;###
            ,####.
/\/\/\/\/\/.######.\/\/\/\/\
        """)
        print("A. Scream")
        print("B. Say “Nah I don’t want to survive.")
        while True:
            nine_input = input()
            if nine_input == "a" or nine_input == "A":
                twelve()
                break
            elif nine_input == "b" or nine_input == "B":
                thirteen()
                break
            else:
                print("Invalid input, please try again.")
    def ten():
        clear = lambda: os.system('clear')
        clear()
        print("You walked into the room. Suddenly, you heard a robotic voice: 'THERE IS NO EXIT'")
        print("A. Scream")
        print("B. Find hints in the room to escape")
        while True:
            ten_input = input()
            if ten_input == "a" or ten_input == "A":
                fourteen()
                break
            elif ten_input == "b" or ten_input == "B":
                fifteen()
                break
            else:
                print("Invalid input, please try again.")
    def eleven():
        clear = lambda: os.system('clear')
        clear()
        print("You tried to restart the phone. It did not work.")
        print(r"""
        ||
  ______||
 / ____ o|
| / ;; \ |
| ______ |
||______|| 
||      ||
||______|| 
|'\[--]/'|
|  ¨''¨  |
|  ''''  |
|        |
|        |
|        |
|________|
        """)
        print("A. Put down the phone and pick up the key")
        while True:
            eleven_input = input()
            if eleven_input == "a" or eleven_input == "A":
                three()
                break
            else:
                print("Invalid input, please try again.")
    def twelve():
        clear = lambda: os.system('clear')
        clear()
        print("'AHHHHH!' You scremed. 'AHHHHH! YOU SCARED ME! WHAT'S YOUR PROBLEM! NOW FINISH THE MAZE OR YOU DIE!' The robotic voice said.")
        print("A. Continue")
        print("B. Say 'Nah I don't want to survive.'")
        while True:
            twelve_input = input()
            if twelve_input == "a" or twelve_input == "A":
                sixteen()
                break
            elif twelve_input == "b" or twelve_input == "B":
                thirteen()
                break
            else:
                print("Invalid input, please try again.")
    def thirteen():
        clear = lambda: os.system('clear')
        clear()
        print("'Nah I don't want to survive.' You said. 'Oh, wait, what?' The robotic voice said. 'I don't care. Finish the maze or you die!")
        print("A. Continue")
        while True:
            thirteen_input = input()
            if thirteen_input == "a" or thirteen_input == "A":
                sixteen()
                break
            else:
                print("Invalid input, please try again.")
    def fourteen():
        clear = lambda: os.system('clear')
        clear()
        print("'AHHHHH!' You screamed. 'AHHHHH! YOU SCARED ME! WHAT'S YOUR PROBLEM!' The robotic voice said.")
        print("A. Find hints in the room to escape")
        while True:
            fourteen_input = input()
            if fourteen_input == "a" or fourteen_input == "A":
                fifteen()
                break
            else:
                print("Invalid input, please try again.")
    def fifteen():
        clear = lambda: os.system('clear')
        clear()
        print("'You started to find hints in the room. You find a locked door requiring 4 digits numeric password.")
        print("A. Continue finding hints")
        while True:
            fifteen_input = input()
            if fifteen_input == "a" or fifteen_input == "A":
                seventeen()
                break
            else:
                print("Invalid input, please try again.")
    def sixteen():
        clear = lambda: os.system('clear')
        clear()
        print("Escape the maze!")
        print(r"""
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              | X       |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    |              |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |    
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'    `-------------------'
        """)
        sixteen_input = input("(Up/Down/Left/Right): ")
        #when the user answered correctly, print another maze with a new position
        if sixteen_input == ("right") or sixteen_input == ("Right"):
            clear = lambda: os.system('clear')
            clear()
            print("Escape the maze!")
            print(r""" 
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              |       X |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    |              |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |    
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'    `-------------------'
            """)
            sixteen_input = input("(Up/Down/Left/Right): ")
            if sixteen_input == ("up") or sixteen_input == ("Up"):
                clear = lambda: os.system('clear')
                clear()
                print("Escape the maze!")
                print(r""" 
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                 X |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    |              |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |    
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'    `-------------------'
                """)
                sixteen_input = input("(Up/Down/Left/Right): ")
                if sixteen_input == ("left") or sixteen_input == ("Left"):
                    clear = lambda: os.system('clear')
                    clear()
                    print("Escape the maze!")
                    print(r""" 
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |      X            |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    |              |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |    
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'    `-------------------'
                    """)
                    sixteen_input = input("(Up/Down/Left/Right): ")
                    if sixteen_input == ("down") or sixteen_input == ("Down"):
                        clear = lambda: os.system('clear')
                        clear()
                        print("Escape the maze!")
                        print(r""" 
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |           X  |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    |              |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |    
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'    `-------------------'
                        """)
                        sixteen_input = input("(Up/Down/Left/Right): ")
                        if sixteen_input == ("left") or sixteen_input == ("Left"):
                            clear = lambda: os.system('clear')
                            clear()
                            print("Escape the maze!")
                            print(r"""
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    | X            |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    |              |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |    
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'    `-------------------'
                            """)
                            sixteen_input = input("(Up/Down/Left/Right): ")
                            if sixteen_input == ("up") or sixteen_input == ("Up"):
                                clear = lambda: os.system('clear')
                                clear()
                                print("Escape the maze!")
                                print(r""" 
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |  X                          |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    |              |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |    
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'    `-------------------'
                                """)
                                sixteen_input = input("(Up/Down/Left/Right): ")
                                if sixteen_input == ("right") or sixteen_input == ("Right"):
                                    clear = lambda: os.system('clear')
                                    clear()
                                    print("Escape the maze!")
                                    print(r""" 
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |                           X |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    |              |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |   
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'    `-------------------'
                                    """)
                                    sixteen_input = input("(Up/Down/Left/Right): ")
                                    if sixteen_input == ("down") or sixteen_input == ("Down"):
                                        clear = lambda: os.system('clear')
                                        clear()
                                        print("Escape the maze!")
                                        print(r""" 
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    |              |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |  X                |    
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'    `-------------------'
                                        """)
                                        sixteen_input = input("(Up/Down/Left/Right): ")
                                        if sixteen_input == ("right") or sixteen_input == ("Right"):
                                            clear = lambda: os.system('clear')
                                            clear()
                                            print("Escape the maze!")
                                            print(r""" 
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    |              |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                 X |    
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'    `-------------------'
                                            """)
                                            sixteen_input = input("(Up/Down/Left/Right): ")
                                            if sixteen_input == ("up") or sixteen_input == ("Up"):
                                                clear = lambda: os.system('clear')
                                                clear()
                                                print("Escape the maze!")
                                                print(r""" 
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    |            X |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |    
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'    `-------------------'
                                                """)
                                                sixteen_input = input("(Up/Down/Left/Right): ")
                                                if sixteen_input == ("left") or sixteen_input == ("Left"):
                                                    clear = lambda: os.system('clear')
                                                    clear()
                                                    print("Escape the maze!")
                                                    print(r""" 
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    | X            |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |    
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'    `-------------------'
                                                    """)
                                                    sixteen_input = input("(Up/Down/Left/Right): ")
                                                    if sixteen_input == ("up") or sixteen_input == ("Up"):
                                                        clear = lambda: os.system('clear')
                                                        clear()
                                                        print("Escape the maze!")
                                                        print(r""" 
,---------------------------------------.---------.    
|                                    X  |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    |              |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |    
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'    `-------------------'
                                                        """)
                                                        sixteen_input = input("(Up/Down/Left/Right): ")
                                                        if sixteen_input == ("left") or sixteen_input == ("Left"):
                                                            clear = lambda: os.system('clear')
                                                            clear()
                                                            print("Escape the maze!")
                                                            print(r"""
,---------------------------------------.---------.    
| X                                     |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    |              |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |    
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'    `-------------------'
                                                            """)
                                                            sixteen_input = input("(Up/Down/Left/Right): ")
                                                            if sixteen_input == ("down") or sixteen_input == ("Down"):
                                                                clear = lambda: os.system('clear')
                                                                clear()
                                                                print("Escape the maze!")
                                                                print(r""" 
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    |              |    
|    `----:    ,---------.    |    `---------.    |    
| X       |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |    
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'    `-------------------'
                                                                """)
                                                                sixteen_input = input("(Up/Down/Left/Right): ")
                                                                if sixteen_input == ("right") or sixteen_input == ("Right"):
                                                                    clear = lambda: os.system('clear')
                                                                    clear()
                                                                    print("Escape the maze!")
                                                                    print(r""" 
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    |              |    
|    `----:    ,---------.    |    `---------.    |    
|       X |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |    
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'    `-------------------'
                                                                    """)
                                                                    sixteen_input = input("(Up/Down/Left/Right): ")
                                                                    if sixteen_input == ("down") or sixteen_input == ("Down"):
                                                                        clear = lambda: os.system('clear')
                                                                        clear()
                                                                        print("Escape the maze!")
                                                                        print(r""" 
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    |              |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |    
:----'    |    |    |    |    |    ,--------------:    
|       X |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'    `-------------------'
                                                                        """)
                                                                        sixteen_input = input("(Up/Down/Left/Right): ")
                                                                        if sixteen_input == ("left") or sixteen_input == ("Left"):
                                                                            clear = lambda: os.system('clear')
                                                                            clear()
                                                                            print("Escape the maze!")
                                                                            print(r""" 
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    |              |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |    
:----'    |    |    |    |    |    ,--------------:    
| X       |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'    `-------------------'
                                                                            """)
                                                                            sixteen_input = input("(Up/Down/Left/Right): ")
                                                                            if sixteen_input == ("down") or sixteen_input == ("Down"):
                                                                                clear = lambda: os.system('clear')
                                                                                clear()
                                                                                print("Escape the maze!")
                                                                                print(r""" 
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    |              |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |    
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
| X                      |    |                   |    
`------------------------'    `-------------------'
                                                                                """)
                                                                                sixteen_input = input("(Up/Down/Left/Right): ")
                                                                                if sixteen_input == ("right") or sixteen_input == ("Right"):
                                                                                    clear = lambda: os.system('clear')
                                                                                    clear()
                                                                                    print("Escape the maze!")
                                                                                    print(r""" 
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    |              |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |    
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                      X |    |                   |    
`------------------------'    `-------------------'
                                                                                    """)
                                                                                    sixteen_input = input("(Up/Down/Left/Right): ")
                                                                                    if sixteen_input == ("up") or sixteen_input == ("Up"):
                                                                                        clear = lambda: os.system('clear')
                                                                                        clear()
                                                                                        print("Escape the maze!")
                                                                                        print(r""" 
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    |              |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |    
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |            X |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'    `-------------------'
                                                                                        """)
                                                                                        sixteen_input = input("(Up/Down/Left/Right): ")
                                                                                        if sixteen_input == ("left") or sixteen_input == ("Left"):
                                                                                            clear = lambda: os.system('clear')
                                                                                            clear()
                                                                                            print("Escape the maze!")
                                                                                            print(r""" 
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    |              |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |    
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    | X            |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'    `-------------------'
                                                                                            """)
                                                                                            sixteen_input = input("(Up/Down/Left/Right): ")
                                                                                            if sixteen_input == ("up") or sixteen_input == ("Up"):
                                                                                                clear = lambda: os.system('clear')
                                                                                                clear()
                                                                                                print("Escape the maze!")
                                                                                                print(r""" 
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    | X                 |    |              |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |    
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'    `-------------------'
                                                                                                """)
                                                                                                sixteen_input = input("(Up/Down/Left/Right): ")
                                                                                                if sixteen_input == ("right") or sixteen_input == ("Right"):
                                                                                                    clear = lambda: os.system('clear')
                                                                                                    clear()
                                                                                                    print("Escape the maze!")
                                                                                                    print(r""" 
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                 X |    |              |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |    
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'    `-------------------'
                                                                                                    """)
                                                                                                    sixteen_input = input("(Up/Down/Left/Right): ")
                                                                                                    #when the user passed the maze, jump to a different outcome
                                                                                                    if sixteen_input == ("down") or sixteen_input == ("Down"):
                                                                                                        clear = lambda: os.system('clear')
                                                                                                        clear()
                                                                                                        print("Escape the maze!")
                                                                                                        print(r""" 
,---------------------------------------.---------.    
|                                       |         |    
|    ,-----------------------------.    |    .    |    
|    |                             |    |    |    |    
|    |    ,-------------------.    |    |    |    |    
|    |    |                   |    |    |    |    |    
|    |    `----     ,----     |    |    |    |    |    
|    |              |         |    |    |    |    |    
|    |    ,---------"---------:    |    `----'    |    
|    |    |                   |    |              |    
|    `----:    ,---------.    |    `---------.    |    
|         |    |         |    |              |    |    
|    .    |    |    .    |    |     ---------'    |    
|    |    |    |    |    |    |                   |    
:----'    |    |    |    |    |    ,--------------:    
|         |    |    |    |    |    |              |    
|    .    |    `----'    |    |    |     ----.    |    
|    |    |              |    |    |         |    |    
|    `----"---------     |    |    `---------'    |    
|                        |    |                   |    
`------------------------'  X `-------------------'
                                                                                                        """)
                                                                                                        eighteen()
                                                                                                    #if the player lost, jump to the game over screen
                                                                                                    else:
                                                                                                        sixteen_gameover()
                                                                                                else:
                                                                                                    sixteen_gameover()
                                                                                            else:
                                                                                                sixteen_gameover()
                                                                                        else:
                                                                                            sixteen_gameover()
                                                                                    else:
                                                                                        sixteen_gameover()
                                                                                else:
                                                                                    sixteen_gameover()
                                                                            else:
                                                                                sixteen_gameover()
                                                                        else:
                                                                            sixteen_gameover()
                                                                    else:
                                                                        sixteen_gameover()
                                                                else:
                                                                    sixteen_gameover()
                                                            else:
                                                                sixteen_gameover()
                                                        else:
                                                            sixteen_gameover()
                                                    else:
                                                        sixteen_gameover()
                                                else:
                                                    sixteen_gameover()
                                            else:
                                                sixteen_gameover()
                                        else:
                                            sixteen_gameover()
                                    else:
                                        sixteen_gameover()
                                else:
                                    sixteen_gameover()
                            else:
                                sixteen_gameover()
                        else:
                            sixteen_gameover()
                    else:
                        sixteen_gameover()
                else:
                    sixteen_gameover()
            else:
                sixteen_gameover()
        else:
            sixteen_gameover()
    def sixteen_gameover():
        clear = lambda: os.system('clear')
        clear()
        print("The robotic sound can’t hold his happiness. “HAHAHAHAHA! LOOKS LIKE SOMEONE CAN’T EVEN PASS A MAZE OR SPELT THE ANSWER WRONG! EVEN A KID PLAYS BETTER THAN YOU! TODAY IS THE DAY YOU DIE!” You rubbed your eyes. Suddenly you are seeing things in third person view, and you are staring at your body being hanged.")
        print(r"""
   __ _  __ _ _ __ ___   ___    _____   _____ _ __ 
  / _` |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
 | (_| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
  \__, |\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
  |___/                                            
        """)
        input("Press enter to return to the calculator ")
        calculate()
    def seventeen():
        clear = lambda: os.system('clear')
        clear()
        print("You continued searching for hints. You saw a piece of paper and apiece of scrambled note.")
        print("A. Read the piece of paper")
        print("B. Read the piece of scrambled note")
        while True:
            seventeen_input = input()
            if seventeen_input == "a" or seventeen_input == "A":
                nineteen()
                break
            elif seventeen_input == "b" or seventeen_input == "B":
                twenty()
                break
            else:
                print("Invalid input, please try again.")
    def eighteen():
        clear = lambda: os.system('clear')
        clear()
        print("It is surprising that you made it, but it is not gonna be that easy from now on!” The robotic sound said. Suddenly, thick smokes isspreading,and you passed out.")
        print("A. Continue")
        while True:
            eighteen_input = input()
            if eighteen_input == "a" or eighteen_input == "A":
                twenty_one()
                break
            else:
                print("Invalid input, please try again.")
    def nineteen():
        clear = lambda: os.system('clear')
        clear()
        print("You see a poem written on a piece of paper.")
        print(r"""
“Browsing worlds within pages,
Opening doors to unknown lands,
Opening minds with endless knowledge,
Keeping stories close at hand,
Shelves filled with tales, old and new,
Holding memories, dreams, and more,
Encouraging imaginations to soar,
Lifelong companions, forever true,
Fragments of worlds, to me, they're due.”
        """)
        print("Did you notice anything? (7 letters, enter 'hint' for hints)")
        while True:
            nineteen_input = input()
            if nineteen_input == "bookshelf" or nineteen_input == "Bookshelf" or nineteen_input == "BOOKSHELF":
                twenty_two()
                break
            elif nineteen_input == "hint" or nineteen_input == "Hint":
                print("Hint: Acrostic")
            else:
                print("Invalid input, please try again.")
    def twenty():
        clear = lambda: os.system('clear')
        clear()
        print("You see a message on the piece of scrambled note.")
        print("DON'T GET TRICKED BY HIM! LEAVE NOW!")
        print("You remembered that the door did not close when you come in.")
        print("A. Run to the door and try to leave.")
        print("B. Ignore it.")
        while True:
            twenty_input = input()
            if twenty_input == "a" or twenty_input == "A":
                twenty_three()
                break
            elif twenty_input == "b" or twenty_input == "B":
                nineteen()
                break
            else:
                print("Invalid input, please try again.")
    def twenty_two():
        clear = lambda: os.system('clear')
        clear()
        print("'B...O...O...K...S...H...E...L...F... bookshelf?' You start looking around and see a bookshelf. You approach it.")
        print("There are four books ordered neatly. Their names fromleft to right are “Whispers of the Forgotten Realm6”, “Shadows in the Moonlight9”, “The Enigma of Eternity4”, “Journey tothe “Stellar Nexus2”.")
        print(r"""
 _________________________________________________________
||-------------------------------------------------------||
||.--.    .-._                        .----.             ||
|||==|____| |H|___            .---.___|''''|_____.--.___ ||
|||  |====| | |xxx|_          |+++|=-=|_  _|-=+=-|==|---|||
|||==|    | | |   | \         |   |   |_\/_|     |  | ^ |||
|||  |    | | |   |\ \   .--. |   |=-=|_/\_|-=+=-|  | ^ |||
|||  |    | | |   |_\ \_( oo )|   |   |    |     |  | ^ |||
|||==|====| |H|xxx|  \ \ |''| |+++|=-=|''''|-=+=-|==|---|||
||`--^----'-^-^---'   `-' ""  '---^---^----^-----^--^---^||
||-------------------------------------------------------||
||-------------------------------------------------------||
||               ___                   .-.__.-----. .---.||
||              |===| .---.   __   .---| |XX|<(*)>|_|^^^|||
||         ,  /(|   |_|   |__|''|__|:x:|=|  |     |=|   |||
||      _a'{ / (|===|+|   |++|  |==|   | |  |     | |   |||
||      '/\\/ _(|===|-|   |  |''|  |:x:|=|  |     | |   |||
||_____  -\{___(|   |-|   |  |  |  |   | |  |     | |   |||
||       _(____)|===|+|   |  |''|==|:x:|=|XX|<(*)>|=|^^^|||
||              `---^-^---^--^--'--^---^-^--^-----^-^---^||
||-------------------------------------------------------||
||_______________________________________________________||
        """)
        print("Did you notice anything? (4 digits number, enter 'hint' for hints)")
        while True:
            twenty_two_input = input()
            if twenty_two_input == "6942" or twenty_two_input == "6942":
                twenty_four()
                break
            elif twenty_two_input == "hint" or twenty_two_input == "Hint":
                print("Hint: Read the description again, look at the numbers in the books' name.")
            else:
                print("Invalid input, please try again.")
    def twenty_three():
        clear = lambda: os.system('clear')
        clear()
        print("You run all the way back to the beginning room. Everything is empty. But there is a door half opened.")
        print(r"""
 _______________
|\ ___________ /|
| |  /|,| |   | |
| | |,x,| |   | |
| | |,x,' |   | |
| | |,x   ,   | |
| | |/    |%==| |
| |    /] ,   | |
| |   [/ ()   | |
| |       |   | |
| |       |   | |
| |       |   | |
| |      ,'   | |
| |   ,'      | |
|_|,'_________|_|    
        """)
        print("A. Escape")
        print("B. Go back to the second room and continue looking for hints.")
        while True:
            twenty_input = input()
            if twenty_input == "a" or twenty_input == "A":
                twenty_five()
                break
            elif twenty_input == "b" or twenty_input == "B":
                nineteen()
                break
            else:
                print("Invalid input, please try again.")
    def twenty_four():
        clear = lambda: os.system('clear')
        clear()
        print("6...9...4...2...? WAIT, the password for the locked door is also a 4 digits number!")
        print("You approached to the locked door, enter the password, and the door opened. Suddenly, thick smoke is spreading, and you passed out.")
        print(r"""
     .--------.
    / .------. \
   / /        \ \
   | |        | |
  _| |________| |_
.' |_|        |_| '.
'._____ ____ _____.'
|     .'____'.     |
'.__.'.'    '.'.__.'
'.__  |      |  __.'
|   '.'.____.'.'   |
'.____'.____.'____.'
'.________________.'    
        """)
        print("A. Continue")
        while True:
            twenty_four_input = input()
            if twenty_four_input == "a" or twenty_four_input == "A":
                twenty_one()
                break
            else:
                print("Invalid input, please try again.")
    def twenty_five():
        clear = lambda: os.system('clear')
        clear()
        print("You opened the door and see a room that looks black and suffocating. The robotic sound seemed to be notice that he is trying to escape. It said, “HAHAHAHAHA! SEE WHO IS TRYINGTO ESCAPE! I TOLD YOU, THERE IS NO EXIT. TODAY IS THE DAY YOU DIE! HAHAHAHAHA!” You rubbed your eyes. Suddenly you are seeing things in third person view, and you are staring atyour body being hanged.")
        print(r"""
   __ _  __ _ _ __ ___   ___    _____   _____ _ __ 
  / _` |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
 | (_| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
  \__, |\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
  |___/                                            
        """)
    def twenty_one():
        clear = lambda: os.system('clear')
        clear()
        print("You woke up and find yourself sitting in a chair. There is a desk in front of you. On the desk there is a piece of paper with tons of math equations written on it. “Do you know what is something everyone is afraid of? MATH! (except Asians) If you can finish all the math questions, I will free you. But if you don’t, you are mine's! HAHAHAHAHA!”")
        print("""
    _.--"""""""--._
  .'               '.
 /         o         \
 |    o         o    |
 |      o     o      |
 |         o         |
 |    o         o    |
 |.-.      o      .-.|
 /   |  o     o  |   \
 /--. |___________| .--\
/    \/           \/    \
|    /_____________\    |
|    |             |    |
|    '-------------'    |
|    :             :    |
|____:_____________:____|
|                       |
|_______________________|
 (__)               (__)
        """)
        print("A. Continue")
        while True:
            twenty_input = input()
            if twenty_input == "a" or twenty_input == "A":
                twenty_six()
                break
            else:
                print("Invalid input, please try again.")
    def twenty_six():
        clear = lambda: os.system('clear')
        clear()
        twenty_six_input = input("Question 1: 12^2= ")
        if twenty_six_input == "144":
            twenty_six_input = input("Question 2: 470247+137053= ")
            if twenty_six_input == "607300":
                twenty_six_input = input("Question 3: Which number is equivalent to 3^(4)÷3^(2)? ")
                if twenty_six_input == "9":
                    twenty_six_input = input ("Question 4: 8.563+4.8292 ")
                    if twenty_six_input == "13.3922":
                        twenty_six_input = input ("Question 5: Sally is 54 years old and her mother is 80, how many years ago was Sally’s mother times her age?")
                        if twenty_six_input == "41":
                            twenty_six_input = input("Question 6: There is a three-digit number. The second digit is four times as big as the third digit, while the first digit is three less than the second digit. What is the number?")
                            if twenty_six_input == "141":
                                twenty_six_input = input("Question 7: -15+(-5x)=0; x= ")
                                if twenty_six_input == "-3":
                                    twenty_six_input = input("Question 8: 1.92/3= ")
                                    if twenty_six_input == "0.64":
                                        twenty_six_input = input("Question 9: If 72*96=6927, 58*87=7885, then 79*86= ")
                                        if twenty_six_input == "6897":
                                            twenty_six_input = input("Question 10: Look at this series: 36, 34, 30, 28, 24, … What number should come next? ")
                                            if twenty_six_input == "22":
                                                print("'Not bad. I keep my promise. We can play again next time...” You passed out again. When you wake up, you find yourself in your bed.")
                                                print(r"""
  _   _                           _ 
 | |_| |__   ___    ___ _ __   __| |
 | __| '_ \ / _ \  / _ \ '_ \ / _` |
 | |_| | | |  __/ |  __/ | | | (_| |
  \__|_| |_|\___|  \___|_| |_|\__,_|
                                                """)
                                                input("Press enter to return to the calculator ")
                                                calculate()
                                            else:
                                                print("An random Asian dad appears in front of you. 'You can't even do simple Maths. Timmy can do all these when he was 1. Failure.' Your ass got beaten and you died.")
                                                print(r"""
   __ _  __ _ _ __ ___   ___    _____   _____ _ __ 
  / _` |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
 | (_| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
  \__, |\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
  |___/                                            
                                                """)
                                                input("Press enter to return to the calculator ")
                                                calculate()
                                        else:
                                            print("An random Asian dad appears in front of you. 'You can't even do simple Maths. Timmy can do all these when he was 1. Failure.' Your ass got beaten and you died.")
                                            print(r"""
   __ _  __ _ _ __ ___   ___    _____   _____ _ __ 
  / _` |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
 | (_| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
  \__, |\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
  |___/                                            
                                            """)
                                            input("Press enter to return to the calculator ")
                                            calculate()
                                    else:
                                        print("An random Asian dad appears in front of you. 'You can't even do simple Maths. Timmy can do all these when he was 1. Failure.' Your ass got beaten and you died.")
                                        print(r"""
   __ _  __ _ _ __ ___   ___    _____   _____ _ __ 
  / _` |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
 | (_| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
  \__, |\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
  |___/                                            
                                        """)
                                        input("Press enter to return to the calculator ")
                                        calculate()
                                else:
                                    print("An random Asian dad appears in front of you. 'You can't even do simple Maths. Timmy can do all these when he was 1. Failure.' Your ass got beaten and you died.")
                                    print(r"""
   __ _  __ _ _ __ ___   ___    _____   _____ _ __ 
  / _` |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
 | (_| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
  \__, |\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
  |___/                                            
                                    """)
                                    input("Press enter to return to the calculator ")
                                    calculate()
                            else:
                                print("An random Asian dad appears in front of you. 'You can't even do simple Maths. Timmy can do all these when he was 1. Failure.' Your ass got beaten and you died.")
                                print(r"""
   __ _  __ _ _ __ ___   ___    _____   _____ _ __ 
  / _` |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
 | (_| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
  \__, |\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
  |___/                                            
                                """)
                                input("Press enter to return to the calculator ")
                                calculate()
                        else:
                            print("An random Asian dad appears in front of you. 'You can't even do simple Maths. Timmy can do all these when he was 1. Failure.' Your ass got beaten and you died.")
                            print(r"""
   __ _  __ _ _ __ ___   ___    _____   _____ _ __ 
  / _` |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
 | (_| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
  \__, |\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
  |___/                                            
                            """)
                            input("Press enter to return to the calculator ")
                            calculate()
                    else:
                        print("An random Asian dad appears in front of you. 'You can't even do simple Maths. Timmy can do all these when he was 1. Failure.' Your ass got beaten and you died.")
                        print(r"""
   __ _  __ _ _ __ ___   ___    _____   _____ _ __ 
  / _` |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
 | (_| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
  \__, |\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
  |___/                                            
                        """)
                        input("Press enter to return to the calculator ")
                        calculate()
                else:
                    print("An random Asian dad appears in front of you. 'You can't even do simple Maths. Timmy can do all these when he was 1. Failure.' Your ass got beaten and you died.")
                    print(r"""
   __ _  __ _ _ __ ___   ___    _____   _____ _ __ 
  / _` |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
 | (_| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
  \__, |\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
  |___/                                            
                    """)
                    input("Press enter to return to the calculator ")
                    calculate()
            else:
                print("An random Asian dad appears in front of you. 'You can't even do simple Maths. Timmy can do all these when he was 1. Failure.' Your ass got beaten and you died.")
                print(r"""
   __ _  __ _ _ __ ___   ___    _____   _____ _ __ 
  / _` |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
 | (_| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
  \__, |\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
  |___/                                            
                """)
                input("Press enter to return to the calculator ")
                calculate()
        else:
            print("An random Asian dad appears in front of you. 'You can't even do simple Maths. Timmy can do all these when he was 1. Failure.' Your ass got beaten and you died.")
            print(r"""
   __ _  __ _ _ __ ___   ___    _____   _____ _ __ 
  / _` |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
 | (_| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
  \__, |\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
  |___/                                            
            """)
            input("Press enter to return to the calculator ")
            calculate()
    one()
calculate()