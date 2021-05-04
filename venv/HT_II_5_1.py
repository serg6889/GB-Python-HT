new_number = int(input("Enter new number : "))
my_list = [4, 5, 3, 2, 3 ]
for el in range(len(my_list)):
        if my_list[el] == new_number:
            my_list.insert(el + 1, new_number)
            break

        elif my_list[0] < new_number:
            my_list.insert(0, new_number)
        elif my_list[-1] > new_number:
            my_list.append(new_number)
        elif my_list[el] > new_number and my_list[el + 1] < new_number:
            my_list.insert(el + 1, new_number)
print(f"Current list : {my_list}")