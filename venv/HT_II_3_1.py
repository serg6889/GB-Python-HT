seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
input_val = int(input("Enter month as a number:  "))

if input_val > 12:
    print("Your input is incorrect")
elif 0 < input_val <= 2:
    print(f'Your input month {input_val}  is in {seasons_list[0]} season')
    print(f'Your input month {input_val}  is in {seasons_dict.get(1)} season')
elif  2 < input_val <= 5:
    print(f'Your input month {input_val}  is in {seasons_list[1]} season')
    print(f'Your input month {input_val}  is in {seasons_dict.get(2)} season')
elif 5 < input_val <= 8:
    print(f'Your input month {input_val}  is in {seasons_list[2]} season')
    print(f'Your input month {input_val}  is in {seasons_dict.get(3)} season')
elif 8 < input_val < 12:
    print(f'Your input month {input_val}  is in {seasons_list[3]} season')
    print(f'Your input month {input_val}  is in {seasons_dict.get(4)} season')


