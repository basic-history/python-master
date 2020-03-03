language = ["java", "c", "php"]

for l in language:
    print(l)

language.append("c++")
language.append("python")

print(language)

number = [10, 2, 3]
number2 = [7, 9]

number3 = number + number2

print(number3)  # [10, 2, 3, 7, 9]

print("sort\t\t", sorted(number3))  # [2, 3, 7, 9, 10]
print("sort reverset", sorted(number3, reverse=True))  # [10, 9, 7, 3, 2]

number_list = [number, number2]  # [[10, 2, 3], [7, 9]]

print(number_list)

cp1 = [1, 2, 3]
cp2 = [1, 2, 3]

print("cp1==cp2?", cp1 == cp2)
print("cp1 is cp2?", cp1 is cp2)

empty_list = []
empty_list2 = list()

print("empty_list==empty_list2?", empty_list == empty_list2)
