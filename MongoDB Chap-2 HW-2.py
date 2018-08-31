import pymongo

conn = pymongo.MongoClient()
db = conn.students.grades
result = db.find({'type':'homework'}).sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)])
saveVar = 0


for doc in result:
    if doc['student_id'] !=saveVar:
        db.delete_one({'_id':doc['_id']})
        saveVar = doc['student_id']

result = db.find({'type':'homework'}).sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)])
for doc in result:
    print(doc)