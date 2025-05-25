import random


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
    question = f"{num1} {operation} {num2}"
    answer = round(eval(question))
    return question, answer


mode = "regular"
score = 0
correct_count = 0
wrong_count = 0
rounds_played = 0
quiz_history = []

selected_ops = get_operations()

# quiz loop

question, correct_answer = generate_question(selected_ops)
print(f"What is {question}? (Type 'xxx' to quit)")
user_input = input("Your answer: ")


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