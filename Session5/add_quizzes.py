from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('10.1.9.118',27017)

database = client.get_database('D4E16')

quiz_collection = database.get_collection('quizzes')

input_question = input('Enter question: ')
input_choices = input('Enter choices: ').split(',')
input_right_choices = int(input('Which one is right? ')) - 1

quiz_data = {
    'question': input_question,
    'choices': input_choices,
    'rightChoice': input_right_choices,
}

print(quiz_data)
quiz_collection.insert_one(quiz_data)
