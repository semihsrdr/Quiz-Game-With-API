import requests
from question_model import Question
import html
url="https://opentdb.com/api.php"
parameters={
    "type":"boolean",
    "amount":11,
    "difficulty":"easy"
}

def create_questions():
    question_objects = []
    respond=requests.get(url,params=parameters)
    respond.raise_for_status()
    data=respond.json()

    for i in range(11):
        question=html.unescape(data["results"][i]["question"])
        answer=data["results"][i]["correct_answer"]
        question_objects.append(Question(question,answer))
    return question_objects


def check_answer(user_answer,question_number,question_objects):
    if user_answer==question_objects[question_number].answer:
        return True






