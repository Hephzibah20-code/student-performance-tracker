# A program for a teacher who wants to record a student's performance in three subjects
student_name = input("Enter student name: ") # collects student name

while student_name .replace(" ", "").isalpha( ) == False:
    print("Invalid name. Use letters only.")
    student_name = input("Enter student name: ") # collects student name
student_name = student_name.title( )    

math_score = float(input("Enter Math score: ")) # collects Math score

while math_score < 0 or math_score > 100:
    print("Invalid score. Score must be between 0 and 100.")
    math_score = float(input("Enter Math score: "))

eng_score = float(input("Enter English score: ")) # collects English score

while eng_score < 0 or eng_score > 100:
    print("Invalid score. Score must be between 0 and 100.")
    eng_score = float(input("Enter English score: "))
    
pyt_score = float(input("Enter Python score: ")) # collects Python score

while pyt_score < 0 or pyt_score > 100:
    print("Invalid score. Score must be between 0 and 100.")
    pyt_score = float(input("Enter Python score: "))

# Displays all three scores
print(f"math score: {math_score}")
print(f"eng_score: {eng_score}")
print(f"pyt_score: {pyt_score}" )

# Calculates total score
total_score = math_score + eng_score + pyt_score
print(total_score) #displays the total score

# Calculates average score
avg_score = total_score / 3
print(round(avg_score, 2)) # displays the average score

if avg_score >= 70: # Determines student grade based on the average score
    grade = "A"
elif avg_score >= 60:
    grade = "B"
elif avg_score >= 50:
    grade = "C" 
elif avg_score >= 45:
    grade = "D"
elif avg_score >= 40:
    grade = "E"
else:
    grade = "F" 

# Display message to say student final grade
message = f"{student_name}, your final grade is {grade}." 
print(message)

# Display message to check Pass / Fail
if avg_score >= 40:
    print("You Passed!")
else:
    print("You Failed!")

        

 
    
 


 