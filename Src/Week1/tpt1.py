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


