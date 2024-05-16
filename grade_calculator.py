#Student Average Grade Calculator by James Giraldo

def calculate_average_grade():
    # This section prompts the user for their name and scores
    student_name = input("Hi! Welcome to the grade average calculator! May I have your name, please? ")
    math_score = float(input("Thank you! What is your math score? "))
    science_score = float(input("Great! What is your science score? "))
    english_score = float(input("Finally, what is your english score? "))

    # This calculates the student's average test scores
    average_grade = ((math_score+science_score+english_score)/3)

    # Return the student's name and their average grade
    return student_name, average_grade

if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # This will output the student's name and average grade rounded to 2 decimal places
    print(f'{student_name } your average grade is {average_grade:.2f}!')