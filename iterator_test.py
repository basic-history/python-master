string = 'abcd'

for c in string:
    print(c)

for c in iter(string):
    print(c)

print("*" * 8)
string_list = ['java', 'c', 'php']
iterator = iter(string_list)

for i in range(0, len(string_list)):
    item = next(iterator)
    print(item)
