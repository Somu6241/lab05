import requests
import json

url = "https://michaelgathara.com/api/python-challenge"



print('Name : Somanath Reddy')
print('Blazer id : Srpalle')

# Send a GET request to the URL
response = requests.get(url)
challenges = response.json()


for problem in challenges:
    problem_id = problem.get("id")
    problem_statement = problem.get("problem")

    # Remove the question mark from the problem statement
    problem_statement = problem_statement.replace("?", "")

    # Evaluate the problem
    operands = problem_statement.split(" ")
    operator = operands[1]
    num1 = int(operands[0])
    num2 = int(operands[2])

    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    elif operator == "*":
        answer = num1 * num2
    elif operator == "/":
        answer = num1 / num2

    # Print the problem and its answer
    print(f"Problem {problem_id}: {problem_statement} = {answer}")
