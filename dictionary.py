dict = {
    'course_name' : 'Python',
    'course_fees' : 5000,
    'course_duration' : '3 months'
}

# print('course_name' in dict.keys())

# print(dict)

# for key in dict:
#     print(key, "->", dict[key])

# print(dict.get('course_name'))
# print(dict.get('course_fees'))

# for key in dict.keys():
#     print(key)

# for value in dict.values():
#     print(value)    

# for a,b in dict.items():
#     print(a, b)

# del(dict['course_duration'])
# print(dict)

# dict.pop('course_fees')
# print(dict)

# dictionary = dict(course_name = 'Python', course_fees = 10000)
# print(dictionary)

# dict.update({'course_name' : 'Java'})
# print(dict)

# dict['course_name'] = 'HTML5 Workshop'
# print(dict)

# dict.clear()
# print(dict)

course = {
    'JAVA' : {'course_duration' : '3 months', 'course_fees' : 10000},
    'PYHTON' : {'course_duration' : '4 months', 'course_fees' : 5000},
    'C++' : {'course_duration' : '2 months', 'course_fees' : 8000}
}

# print(course)

# for k,v in course.items():
#     print(k, "-->")
#     for a,b in v.items():
#         print(a,"->",b)

# course['JAVA']['course_duration'] = '10 months'
# print(course)