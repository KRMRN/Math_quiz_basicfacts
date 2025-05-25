import random

def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list: {valid_ans}"
    while True:
        user_response = input(question).lower()
        for item in valid_ans:
            if item == user_response or user_response == item[0]:
                return item
        print(error)
        print()


def instructions():
    print('''
 *** Instructions ***   
You can choose how many questions you want to be tested on

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
            return "infinite"  # infinite mode
        try:
            response = int(to_check)
            if response < 1:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


def get_operations():
    print("Choose operations you'd like to be tested on.")
    print("Enter + for Addition, - for Subtraction, * for Multiplication, / for Division")

    valid_ops = ["+", "-", "*", "/"]
    while True:
        response = input("Your choice: ").replace(" ", "")
        if response == "":
            return valid_ops
        selected = response.split(",")
        if all(op in valid_ops for op in selected):
            return selected
        else:
            print("Invalid input. Please enter valid operations like +,-,*,/")


def generate_question(ops):
    operation = random.choice(ops)
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    # the divison would be clean
    if operation == '/':
        num1 = num1 * num2
    question = f"{num1} {operation} {num2}"
    answer = round(eval(question))
    return question, answer


# Main routine starts here
print("Welcome to the Math Quiz\n")

# Ask user if they want instructions
if string_checker("Do you want to see the instructions? ") == "yes":
    instructions()

mode = "regular"
score = 0
correct_count = 0
wrong_count = 0
rounds_played = 0
quiz_history = []

# Ask how many rounds the user wants
num_rounds = int_check("How many rounds would you like? Press <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 999999

selected_ops = get_operations()

# quiz loop
while rounds_played < num_rounds:
    if mode == "infinite":
        print(f"\nRound {rounds_played + 1} (infinite mode)")
    else:
        print(f"\nRound {rounds_played + 1} of {num_rounds}")

    question, correct_answer = generate_question(selected_ops)
    print(f"What is {question}? (Type 'xxx' to quit)")
    user_input = input("Your answer: ")

    if user_input.lower() == "xxx":
        break

    # Try to convert input to a number
    try:
        user_answer = int(round(float(user_input)))
    except ValueError:
        print("Invalid input. That counts as incorrect.")
        user_answer = None

    # Check if the answer is correct
    if user_answer == correct_answer:
        print("Correct!\n")
        correct_count += 1
        result = "Correct"
    else:
        print(f"Incorrect. The correct answer was {correct_answer}\n")
        wrong_count += 1
        result = "Incorrect"

    rounds_played += 1
    quiz_history.append({
        "question": question,
        "your_answer": user_answer,
        "correct_answer": correct_answer,
        "result": result
    })

# quiz summary
print("\nQuiz Summary:")
print(f"Total Questions Answered: {rounds_played}")
print(f"Correct: {correct_count} | Incorrect: {wrong_count}")

# percentage correct
if rounds_played > 0:
    percentage = (correct_count / rounds_played) * 100
    print(f"Percentage Correct: {percentage:.2f}%")
else:
    print("No questions were answered.")





