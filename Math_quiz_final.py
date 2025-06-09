import random

def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list: {valid_ans}"
    # makes sure the user input is in valid_ans
    while True:
        user_response = input(question).lower()
        for item in valid_ans:
            if user_response == item or user_response == item[0]:
                return item
        print(error)
        print()

def instructions():
    # prints instructions
    print('''
 *** Instructions ***   
You can choose how many questions you want to be tested on.
Answers are rounded to the nearest whole number.
The quiz includes:
  - Addition
  - Subtraction
  - Multiplication
  - Division
    ''')

def int_check(question):
    while True:
        error = "Please enter an integer greater than 0."
        to_check = input(question)
        if to_check == "":
            return "infinite" # if user presses <enter> they choose infinite mode
        try:
            response = int(to_check)
            if response < 1:
                print(error) # if user chooses an int under 1 gives an error
            else:
                return response
        except ValueError:
            print(error)

def get_operations():
    print("Choose operations you'd like to be tested on.")
    print("Enter + for Addition, - for Subtraction, * for Multiplication, / for Division, <enter> for all")
    # valid operations
    valid_ops = ["+", "-", "*", "/"]
    while True:
        response = input("Your choice: ").replace(" ", "") # replaces spaces with no space
        if response == "":
            return valid_ops # if user presses <enter> they get choose all ops
        selected = response.split(",")
        if all(op in valid_ops for op in selected):
            return selected
        else:
            print("Invalid input. Please enter valid operations like +,-,*,/ or <enter>")

def generate_question(ops):
    operation = random.choice(ops)
    # chooses a random num between 1-10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    # makes num1 always bigger than num2
    if operation == '-':
        num1 = num1 + num2
    if operation == '/':
        num1 = num1 * num2
        # prints question and rounds answers to a whole number
    question = f"{num1} {operation} {num2}"
    answer = round(eval(question))
    return question, answer

# main routine
print("Welcome to MATH MANIACS \n")

# ask user if they want to see instructions
if string_checker("Do you want to see the instructions? ") == "yes":
    instructions()

while True:
    # stored variables
    mode = "regular"
    correct_count = 0
    wrong_count = 0
    questions_asked = 0

    # Get number of rounds
    rounds_input = int_check("How many rounds would you like? Press <enter> for infinite mode: ")
    # gives amounts of rounds to user
    if rounds_input == "infinite":
        num_rounds = 999999
        rounds_display = "infinite mode"
    else:
        num_rounds = rounds_input
        rounds_display = f"{num_rounds} rounds"
    # prints how many rounds user chose
    print(f"\n✅ You chose: {rounds_display}")
    # prints what ops the user chose
    selected_ops = get_operations()
    print(f"✅ You chose the following operations: {' '.join(selected_ops)}")

    #quiz loop
    while questions_asked < num_rounds:
        if rounds_display == "infinite mode":
            print(f"\nRound {questions_asked + 1} (infinite mode)")
        else:
            print(f"\nRound {questions_asked + 1} of {num_rounds}")

        question, correct_answer = generate_question(selected_ops)
        print(f"What is {question}? (Type 'xxx' to quit)")
        user_input = input("Your answer: ")
        # if user inputs xxx the game ends
        if user_input.lower() == "xxx":
            break
        try:
            user_answer = int(round(float(user_input))) # if the user inputs a string it gives an invalid input
        except ValueError:
            print("Invalid input. That counts as incorrect.")
            user_answer = None
        # if user ans is correct is adds +1 to the total count otherwise it adds to the wrong count
        if user_answer == correct_answer:
            print("Correct!\n")
            correct_count += 1
        else:
            print(f"Incorrect. The correct answer was {correct_answer}\n") # prints correct ans
            wrong_count += 1

        questions_asked += 1

    #quiz summary
    # asks user if they want quiz summary and prints it for them
    if string_checker("Do you want to see your quiz summary? (yes/no): ") == "yes":
        print("Quiz Summary")
        print(f"Total Questions Answered: {questions_asked}")
        print(f"Correct: {correct_count} | Incorrect: {wrong_count}")

        # gives percent of ans correct
        if questions_asked > 0:
            percentage = (correct_count / questions_asked) * 100
            print(f"Percentage Correct: {percentage:.2f}%")
        else:
            print("No questions were answered.")
    else:
        print("Quiz summary skipped.")

    #play again
    #asks user if they want to play again
    play_again = string_checker("\nDo you want to play again? (yes/no): ")
    if play_again == "no":
        print("Thanks for playing the MATH MANIACS. Goodbye!")
        break
