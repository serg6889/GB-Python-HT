raw_text = input("Enter sentence : ")
text_1= raw_text.split(" ")
for ind, el in enumerate(text_1, 1):
    print(ind, el)
    if len(el) >= 10:
        el = el[:10]
        print(f"{i} - {el}")

