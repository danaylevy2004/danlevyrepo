## Code Display
### Week 0
```import os

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
                os.system()
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
 ```
### Week 1
```
# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars
InfoDb = []
# List with dictionary records placed in a list
InfoDb.append({
    "FirstName": "Dutch",
    "LastName": " Van Der Linde",
    "DOB": "Sometime 1855",
    "Residence": "Tahiti, French Polynesia",
    "Email": "ihaveaplan@gmail.com",
    "Owns_Cars":["Albino Arabian"]
})

InfoDb.append({
    "FirstName": "Arthur",
    "LastName": "Morgan",
    "DOB": "Sometime 1863",
    "Residence": "Saint Denis, New Hanover",
    "Email": "tbornottb@gmail.com",
    "Owns_Cars":["Arabian", "Turkoman", "Fox Trotter"]
})

InfoDb.append({
    "FirstName": "John",
    "LastName": "Marston",
    "DOB": "Sometime 1863",
    "Residence": "MacFarlane Ranch, West Elizabeth",
    "Email": "iloveabagail@gmail.com",
    "Owns_Cars":["Albino Arabian", "American Paint"]
})


# given an index this will print InfoDb content
def print_data(n):
    print("First Name:", InfoDb[n]["FirstName"], "Last Name:", InfoDb[n]["LastName"], "Date of Birth:", InfoDb[n]["DOB"], "Residence:", InfoDb[n]["Residence"], "Email:", InfoDb[n]["Email"] )  # using comma puts space between values
    print("\t", "Horses: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Owns_Cars"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

def for_loop():
    for x in range(len(InfoDb)):
        # print(InfoDb[x])
        print_data(x)

def while_loop(x):
    while x < len(InfoDb):
        # print(InfoDb[x])
        print_data(x)
        x += 1


def recursive_loop(x):
    if x < len(InfoDb):
        # print(InfoDb[x])
        print_data(x)
        recursive_loop(x + 1)

# hack 3: fibonnaci

def fibonacci(n):
    if n == 0:
        return 0 # for 0
    elif n == 1:
        return 1 # for 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) # recursion

def tester2():
    try:
        num = int(input("Term of Fibonacci Sequence: ")) # user input
        # check if the number is negative
        if num < 0:
            print("Negative Input") # negative input
        else:
            print(num, "terms of the Fibonacci Sequence:")
            for i in range(num):
                print(fibonacci(i), end="Sigma male notation")# list 0-n
            print()
    except:
        print("Non Integer Input") # non-integer input

# tester2()

def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion
    # tester2()
    exit()
    # hack3()

# tester()
```
### Week 2
```
# Function to find the Factors of a Number

class FindFactors:
    def __init__(self):
        print("1", end=" ")
    def __call__(self, n):
        for val in range(2,n + 1):
            if n % val == 0:
                print(val, end=" ")
        print()

def factorfinder():
    print("Factor Finder")
    num = int(input("Enter any Number to Find its Factors: "))
    factors = FindFactors()
    factors(num)

class Factorial:
    def __init__(self):
        pass
    def __call__(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self(n - 1)

def factorial():
    fac = Factorial()
    print("Factorial")
    num = int(input("Enter Number to Find its Factorial: "))
    print(fac(num))
```
