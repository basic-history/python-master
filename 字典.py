dict = {"key1": "value1", "key2": "value2"}

print("type={}".format(type(dict)), dict)

print(dict["key1"])
print(dict.get("key1"))

print(sorted(dict.keys(), reverse=True))  # ['key2', 'key1']

dict["key1"] = "another key1"

print(dict.values())  # dict_values(['another key1', 'value2'])

dict_items = dict.items()
print(type(dict_items))  # 类型是一个对象

_tuple = tuple(dict_items)
print(_tuple[0])

## {}字典  []list ()元组
