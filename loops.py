# **Python Loops Practice – Combined Concepts**  

# Do these one at a time.  
# Attempt each exercise → paste your code/output in chat when done.  
# Use `input()`, `int()`, `try/except` where needed, and combine loops + conditionals.

# 1. **Validated Countdown Timer**  
#    Ask the user for a positive integer (starting number).  
# If invalid (not a number, or ≤ 0), ask again until valid.  
# Then count down from that number to 1 (one number per line).  
# End with "Liftoff!"  

def countdown_timer():
    while True:
        user_input = input("Enter a positive integer to count down from: ").strip()
        try:
            start = int(user_input)
            if start > 0:
                break
            else:
                print("Please enter a positive integer")
        except ValueError:
            print("Please enter a valid positive integer")
    for i in range(start,0,-1):
        print(i)
    print("Liftoff!")
    
# countdown_timer()

#    Example run:  
#    Enter a number: abc  
#    Please enter a positive integer.  
#    Enter a number: -3  
#    Please enter a positive integer.  
#    Enter a number: 5  
#    5  
#    4  
#    3  
#    2  
#    1  
#    Liftoff!

# 2. **Sum of Evens Only (with user limit)**  
#    Ask for a number N (validate: positive integer > 0).  
#    Loop from 1 to N, add up **only the even numbers**.  
#    Print the sum and how many evens you found.  

def sum_even():
    while True:
        user_input = input("Enter a positive integer N: ").strip()
        try:
            n = int(user_input)
            if n > 0:
                break
            else:
                print("Please enter a positive integer")
        except ValueError:
            print("Please enter a valid positive integer")
    total = 0
    even_count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
            even_count += 1
    print(f"Sum of evens: {total} (found {even_count} evens)")
    

#    Example:  
#    Enter N: 10  
#    Sum of evens: 30 (found 5 evens)

# 3. **Password Retry with Limit**  
#    Hardcode password = "bootcamp2025"  
#    Give the user **3 attempts** max.  
# Each try: ask for input  
# Correct → "Access granted!" and stop  
# Wrong → "Wrong! X attempts left."  
# After 3 fails → "Locked out. Try again later."

def password_retry():
    secret = "bootcamp2025"
    attempts_left = 3
    
    while attempts_left > 0:
        guess = input(f"Enter password({attempts_left} attempts left): ").strip()
        if guess == secret:
            print("Access granted!")
            return
        else:
            attempts_left -= 1
            print(f"Wrong! {attempts_left} attempts left.")
            
    print("Locked out. Try again later.")
    
# password_retry()

# 4. **Number Guessing with Hints & Attempt Counter**  
#    Hardcode secret number = 7 (or any between 1–20)  
#    Let user guess repeatedly until correct.  
#    After each guess:  
# "Too high", "Too low", or "Correct!"  
# Show current attempt number ("Guess #3")  
# On win: "You got it in X guesses!"

def number_guess():
    secret = 9
    attempt = 0
    print("Guess a number between 1 and 20!")
    
    while True:
        attempt += 1
        guess_input = input(f"Guess #{attempt}: ").strip()
        try:
            guess = int(guess_input)
        except ValueError:
            print("Please enter a number!")
            attempt -= 1
            continue
        if guess == secret:
            print(f"Correct! You got it in {attempt} guesses!")
            break
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")

# number_guess()
# 5. **Multiplication Table Builder**  
#    Ask for a number between 1 and 12 (validate it).  
#    Print the full ×1 to ×10 table, nicely formatted.  

#    Example output for 7:  
#    7 × 1 = 7  
#    7 × 2 = 14  
#    ...  
#    7 × 10 = 70

def multiple_table():
    while True:
        user_input = input("Enter a number between 1 and 12: ").strip()
        try:
            num = int(user_input)
            if 1 <= num <= 12:
                break
            else:
                print("Please enter a number between 1 and 12")
        except ValueError:
            print("Please enter a valid number.")
    print(f"\nMultiplication table for {num}:")
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")
        
# multiple_table()

# 6. **Star Pyramid Builder**  
#    Ask for height (1–10, validate).  
#    Print a centered pyramid of stars.  

def star_pyramid():
    while True:
        user_input = input("Enter a pyramid height (1-10).").strip()
        try:
            height = int(user_input)
            if 1<= height <= 10:
                break
            else:
                print("Please enter a number between 1 and 10")
        except ValueError:
            print("Please enter a valid number.")
            
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))
star_pyramid()
                

#    Example for height 5:  
 
#       ***  
#      *****  
#     *******  
#    *********

# Tips & reminders:  
# Use `while True` + `try/except ValueError` for safe `int(input())`  
# Watch indentation when putting `if` inside loops  
# `range(1, n+1)` includes n  
# `break` to exit loops early  
# f-strings are your friend: `f"Guess #{attempt}"`