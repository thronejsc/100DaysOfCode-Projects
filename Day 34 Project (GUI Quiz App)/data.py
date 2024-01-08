import requests
from random import choice

parameters = {
    "amount": 10,
    "type": "boolean",
    "category" : 18,
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
questions = response.json()


question_data = [{"question": i['question'], "correct_answer": i['correct_answer']} for i in questions['results']]

