from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('10.1.9.118',27017)
# client = MongoClient()

database = client.get_database('D4E16')

quiz_collection = database.get_collection('quizzes')

data = [
    {
        'question_from_Nga': 'con chó có mấy chân?',
        'choices': [
            1,
            4,
            3,
            2
        ],
        'rightChoice': 1
    },
    {
        'question': 'con thỏ có mấy chân?',
        'choices': [
            1,
            4,
            3,
            2
        ],
        'rightChoice': 1
    },
        {
        'question': 'con vịt có mấy chân?',
        'choices': [
            1,
            3,
            4,
            2,
        ],
        'rightChoice': 3
    }
]
#CREATE
# quiz_collection.insert_one(data) #data --> dict
# quiz_collection.insert_many(data)  #data --> list

#READ
# quizzes = list(quiz_collection.find())
# print(quizzes)
# for quiz in quizzes:
#     print(quiz)

query = {'rightChoice': {'$gt: 1} }
update = {
    '$set':{
        'updated': 25092002
    }
}
# quiz = list(quiz_collection.find_one((query))
# print(quiz)
# quiz = list(quiz_collection.find({'updated':9999999}))
# quiz_collection.find_one_and_update(query, update)
quiz_collection.find_one_and_update(query, update)
