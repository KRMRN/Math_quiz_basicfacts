
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

def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list: {valid_ans}"
    while True:
        user_response = input(question).lower()
        for item in valid_ans:
            if item == user_response or user_response == item[0]:
                return item
        print(error)
        print()

print("Welcome to the Math Quiz\n")

# Ask user if they want instructions
if string_checker("Do you want to see the instructions? ") == "yes":
    instructions()