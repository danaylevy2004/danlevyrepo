# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders

# module imports
import os

# file imports
import Src.Week0.matrix as matrix
import Src.Week0.swap as swap
import Src.Week0.boat as boat
import Src.Week0.christmastree as christmastree
import Src.Week1.fibonacci as fibonacci
import Src.Week1.tpt1 as tpt1
import Src.Week2.tpt2 as tpt2
import Src.Week3.binarysearch as binarysearch

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
]

white = "\033[37m"

daniel = """ 
    ___       ___       ___       ___       ___       ___   
   /\  \     /\  \     /\__\     /\  \     /\  \     /\__\  
  /::\  \   /::\  \   /:| _|_   _\:\  \   /::\  \   /:/  /  
 /:/\:\__\ /::\:\__\ /::|/\__\ /\/::\__\ /::\:\__\ /:/__/   
 \:\/:/  / \/\::/  / \/|::/  / \::/\/__/ \:\:\/  / \:\  \   
  \::/  /    /:/  /    |:/  /   \:\__\    \:\/  /   \:\__\  
   \/__/     \/__/     \/__/     \/__/     \/__/     \/__/           
                                                        
"""


# Submenu list of [Prompt, Action]
# Works similarly to main_menu

pattern_sub_menu = [
    ["Christmas Tree", christmastree.options],
    ["Boat", boat.run]
]

math_sub_menu = [
    ["Matrix", matrix.matrix],
    ["Fibonacci", tpt1.tester2],
    ["Factorial", tpt2.factorial],
    ["Find Factors", tpt2.factorfinder]
]

data_sub_menu = [
    ["Swap", swap.swap],
    ["InfoDB", tpt1.tester]
]

random_sub_menu = [
    ["Fibonacci", fibonacci.fibonacci],
    ["Binary Search", binarysearch.binarysearchnumberguessing]
]


# Menu banner is typically defined by menu owner
border = "=" * 34
banner = white + f"\n{border}\nSelect An Option\n{border}"

def menu():
    print(white + daniel)
    title = banner
    menu_list = main_menu.copy()
    menu_list.append(["Pattern", pattern_submenu])
    menu_list.append(["Math", math_submenu])
    menu_list.append(["Data", data_submenu])
    menu_list.append(["Random", random_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()

def pattern_submenu():
    title = "Pattern submenu" + banner + white
    buildMenu(title, pattern_sub_menu)

def math_submenu():
    title = "Math submenu" + banner + white
    buildMenu(title, math_sub_menu)

def data_submenu():
    title = "Data submenu" + banner + white
    buildMenu(title, data_sub_menu)

def random_submenu():
    title = "Random Function Submenu" + banner + white
    buildMenu(title, random_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '-', value[0])

    # get user choice
    choice = input("Type your choice: ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            try:
                os.system('clear')
            except:
                os.system('cls')
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    except TypeError:
        print(f"Not callable {action}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again

if __name__ == "__main__":
    menu()