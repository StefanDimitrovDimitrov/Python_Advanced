get_info = lambda name, age, town:f'This is {name} from {town} and he is {age} years old'

print(get_info(**{'name': "Stefan", 'age': 35, 'town': 'Sofia'}))