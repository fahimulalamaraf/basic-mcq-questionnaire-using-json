import json
import random

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

random.shuffle(data)

score = 0
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index+1,"-", alternative)
    user_choice = int(input("Enter your choice: "))
    question["user_choice"] = user_choice


for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score += 1
        result = "Correct Answer"
    else:
        result = "Incorrect Answer"

    message = f"{result}, {index+1}- Your answer: {question['user_choice']}"\
    f" Correct Answer: {question['correct_answer']}"
    print(message)


print(score, "/", len(data))