from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('10.1.9.118',27017)

database = client.get_database('D4E16')

quiz_collection = database.get_collection('quizzes')
result_collection = database.get_collection('results')

register = input('Enter your nickname: ')
quizzes = quiz_collection.find()
total_quiz = quiz_collection.count()

score = 0
score = int(score)
for quiz in quizzes:
    question = quiz['question']
    print(question)
    choices = quiz['choices']
    for i in range(len(choices)):
        print(f'{i+1}.{choices[i]}')

    ans = int(input('Your choice: ')) - 1
    if ans == quiz['rightChoice']:
        print('Correct')
        score = score + 1
    else:
        print('Incorrect')

print('Your total score is', score )
percentage = score/ total_quiz *100

result_data = {
    'username': register,
    'score' : percentage,
}
print('Your total percentage of success is: ', percentage,'%' ) 

result_collection.insert_one(result_data)