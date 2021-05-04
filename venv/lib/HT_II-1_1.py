my_int = 42
my_float = 4.7
my_str = "Python is the best  language"
my_list = [3, True, "str", 4]
my_tuple = ('a', 'b', 'c', 56)

common_list = [my_int, my_float, my_str, my_list, my_tuple]
for i in common_list:
    print(f"Element {i} is {type(i)}")
