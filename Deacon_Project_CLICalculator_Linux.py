import os
import time

clear = lambda: os.system('clear')
clear()

history = []

print(r"""

   ____ _     ___    ____    _    _     ____ _   _ _        _  _____ ___  ____  
  / ___| |   |_ _|  / ___|  / \  | |   / ___| | | | |      / \|_   _/ _ \|  _ \ 
 | |   | |    | |  | |     / _ \ | |  | |   | | | | |     / _ \ | || | | | |_) |
 | |___| |___ | |  | |___ / ___ \| |__| |___| |_| | |___ / ___ \| || |_| |  _ < 
  \____|_____|___|  \____/_/   \_\_____\____|\___/|_____/_/   \_\_| \___/|_| \_\
                                                                                

""")
time.sleep(1)
clear()

def calculate():
    clear()
    print(r"""CLI Calculator
=======================================================
Enter 'help' for assistance.
Enter 'clear' to clear the screen.
Enter 'history' to continue from previous calculations.
=======================================================
    """)
    try:
        expression = input("Calculate: ")
        if expression == "help":
            clear()
            print(r"""CLI Calculator Help Menu
=======================================================
Enter 'help' for assistance.
Enter 'clear' to clear the screen.
Enter 'history' to view calculation history.
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
            input("Press enter to continue. ")
            clear()
            calculate()
        elif expression == "clear":
            clear()
            calculate()
        elif expression == "history":
            clear()
            print(r"""CLI Calculator
=======================================================
Enter 'help' for assistance.
Enter 'clear' to clear the screen.
Enter 'history' to continue from previous calculations.
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
        else:
            result = eval(expression)
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

def continue_calculation(last_result):
    clear()
    print(r"""CLI Calculator
=======================================================
Enter 'help' for assistance.
Enter 'clear' to clear the screen.
Enter 'history' to continue from previous calculations.
=======================================================
    """)
    new_expression = input(f"{last_result}")
    combined_expression = f"{last_result}{new_expression}"
    try:
        if new_expression == "help":
            clear()
            print(r"""CLI Calculator Help Menu
=======================================================
Enter 'help' for assistance.
Enter 'clear' to clear the screen.
Enter 'history' to view calculation history.
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
calculate()