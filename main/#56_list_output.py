# give number to every name in the list + capitalize them + sort alphabetically, example: '1.Ben'

waiting_list = ["sen", "ben", "john"]
print(waiting_list)
waiting_list.sort()

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)

waiting_list.sort(reverse=True)
print(waiting_list)

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)