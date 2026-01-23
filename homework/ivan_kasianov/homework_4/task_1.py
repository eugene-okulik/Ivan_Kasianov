my_dict = {"tuple": (2, "text", 14, 7.56, 24), "list": [6, "test2", 8.56, 45, 6], "dict": {"one": "value1", "two": "value2", "three": 3, "four": 5.78, "five": True}, "set": {3, 5, "text3", 6.89, False}}
print(my_dict["tuple"][-1])
my_dict["list"].append("add_element")
my_dict["list"].pop(1)
my_dict["dict"]["i'm a tuple"] = 7
my_dict["dict"].pop("two")
my_dict["set"].add(30)
my_dict["set"].remove(5)
print(my_dict)
