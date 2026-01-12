# Your python solution will go here. Use the console to test your output
# Uncomment this line to test you file
print("hello console!")

# 1. 

def greet(name):
    return print(f"Hello, {name}!")

greet("Amy")

# 2.

def is_positive(num):
    return num > 0

print(is_positive(2))

#3 . 
def double(number):
    return number * 2

print(double(4))

#4. 
def get_length(str):
    return len(str)

print(get_length("Hello how are you"))

#5. 
def say_yes_or_no(is_cool):
    if is_cool:
        return "Yes!"
    else:
        return "NO :("
    

print(say_yes_or_no(True))

#6 

def add(a, b):
    return a + b

print(add(5, 6))

def is_adult(age):
    return age >= 18

print(is_adult(17))

#8.

def shout(text):
    return text.upper()

print(shout("watch out!"))

#9. 

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
print(get_grade(2))

# 10.

def is_even(num):
    return num % 2 == 0

print(is_even(18))

# 11.

def max_num(a, b):
    if a > b:
        return a
    return b
print(max_num(9,5))

#12.

def describe_temperature(temp):
    if temp >= 30:
        return "Hot!"
    elif temp >= 20:
        return "Warm"
    elif temp >= 10:
        return "Cool"
    else:
        return "Cold!"
    
print(describe_temperature(25))

#13. 

def can_vote(age, is_citizen):
    return age>= 18 and is_citizen == True

print(can_vote(27, False))

#14. 

def get_message(hour):
    if hour < 12:
        return "Good morning!"
    elif hour < 17:
        return "Good Afternoon"
    else:
        return "Good evening!"
    
print(get_message(16))