#1. Traffic Light Response

def traffic_light(color):
    if color == "green":
        return "Go!"
    elif color == "yellow":
        return "Slow down"
    elif color == "red":
        return "Stop"
    else:
        return "Invalid color"
    
print(traffic_light("green"))
print(traffic_light("blue"))

# 2. Weather Outfit Suggester

#Write a function suggest_outfit(temperature) that returns a suggestion:
	#  ≥ 25 → “Wear shorts and t-shirt”
	#  15 to 24 → “Light jacket is enough”
	#  < 15 → “Bring a coat!”
 
def suggest_outfit(temperature):
    if temperature >= 25:
        return "Wear shorts and a t-shirt!"
    elif 15 <= temperature < 25: #chained comparison
        return "Light jacket is enough"
    else:
        return "Bring a coat!"
    

print(suggest_outfit(28))
print(suggest_outfit(18))
print(suggest_outfit(10))


# 3. Login Attempt Checker

# Write check_login_attempts(attempts) that returns:
# 	•  0–2 attempts → “Welcome back!”
# 	•  3–4 attempts → “Be careful, too many tries”
# 	•  5+ attempts → “Account locked – try again later”
# (Goal: Simple numeric ranges with >=, multiple elif)

def check_login_attempts(attempts):
    if attempts <= 2:
        return "Welcome back!"
    elif 3 <= attempts <= 4:
        return "Be careful, too many tries"
    else:
        return "Account locked -- try again later"
    
print(check_login_attempts(1))
print(check_login_attempts(6))
print(check_login_attempts(3))

# 4. Can They Ride the Roller Coaster?

# Write can_ride(height, has_ticket) that returns True or False:
# 	•  Must be at least 140 cm tall and have a ticket
# (Goal: Logical and, return boolean directly, True/False capitalization)

def can_ride(height, has_ticket):
    return height >= 140 and has_ticket == True

print(can_ride(150, True), "should print True")
print(can_ride(140, False), "should print False")
print(can_ride(120, True), "should print False")
print(can_ride(100, False), "should print False")

# 5. Grade Comment Generator

# Write grade_comment(score) that returns:
# 	•  90–100 → “Excellent!”
# 	•  80–89 → “Great job”
# 	•  70–79 → “Good effort”
# 	•  60–69 → “Needs improvement”
# 	•  Below 60 → “Let’s study more together”
# (Goal: Multiple conditions, inclusive ranges, final else)

def grade_comment(score):
    if 90 <= score <= 100:
        return "Excellent!"
    elif 80 <= score <= 89:
        return "Great job"
    elif 70 <= score <= 79:
        return "Good effort"
    elif 60 <= score <= 69:
        return "Needs Improvement"
    else:
        return "Let's study more together"
    
print(grade_comment(92))
print(grade_comment(2))
print(grade_comment(66))
print(grade_comment(82))
print(grade_comment(72))