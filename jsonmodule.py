import json

obj = {'courses' : ['Python', 'Java', 'Javascript'], 'course_duration' : '6 months', 'course_fees' : 10000.50}

# print(type(obj))
# print(obj)

# Convert python object into a json object

# jsonObj = json.dumps(obj)
# print(type(jsonObj))
# print(jsonObj)


# Convert json object into a python object

# pythonObj = json.loads(jsonObj)
# print(type(pythonObj))
# print(pythonObj)


# file = open('demo.json','r')
# jsonObject = json.loads(file.read())
# print(jsonObject)

# file = open('demo.json','w')
# json.dump(obj, file, indent=4)

simpleObj = {
    'course_name' : 'Java workshop',
    'course_duration' : '3 months',
    'course_fees' : 3000
}

# jsonObj = json.dumps(simpleObj)
# print(type(jsonObj))
# print(jsonObj)

# plainObj = json.loads(jsonObj)
# print(type(plainObj))
# print(plainObj)

# file = open('demo.json','r')
# plainObj = json.load(file)
# print(type(plainObj))
# print(plainObj)
# for o in plainObj:
#     print(o)
#     print()

# file = open('demo.json','w')
# json.dump(simpleObj, file)