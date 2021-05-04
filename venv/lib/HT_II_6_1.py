new_goods_list = []
new_goods1 = int(input("Enter total items number: "))
item_num = 1
while item_num <= new_goods1:
    new_goods2 = input("Enter title of item : ")
    new_goods3 = float(input("Enter item's price: "))
    new_goods4 = int(input("Enter item's quantity: "))
    new_goods5 = input("Enter item's unit measure: ")
    new_goods_dict = {
                      'title': new_goods2, 'price': new_goods3, 'quantity': new_goods4, 'unit measure': new_goods5}
    new_goods_list.append((item_num, new_goods_dict))
    item_num += 1

    statistics = {}

    for (id, properties) in new_goods_list:
        for key in properties:
            if key not in statistics:
                statistics[key] = set()
            value = properties[key]
            statistics[key].add(value)

    print(statistics)


