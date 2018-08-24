"""A dictionary is a python data structure that matches KEYS with VALUES.
You can look up a value using its key. KEYS must be unique,
but values can be the same."""

"""Example is the English Dictionary. Key = the word
value = the definition."""

#Declare a dictionary with known VALUES
spanish_english = {
    'hola':"hello",
    'gato':'cat',
    'mujer':'women'
}

first_value = spanish_english['hola']

bikes = []  #empty List
users = {}  #empty Dictionary
users['Lila'] = 20
# if print users: users= {'Lila': 20}

friends_family = {
    'Amber': 4,
    'Grace': 7,
    'Haona': 16
}

friends_family2 = {}
friends_family['Amber'] = 16

dictTest = {}
dictTest['Haona'] = [16]
dictTest['Haona'].append("Junior")
dictTest['Amber'] = [4]
dictTest['Amber'].append("preschool")
dictTest['Grace'] = [6]
dictTest['Grace'].append("elementary")


print(dictTest)
