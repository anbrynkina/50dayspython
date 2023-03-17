todos = []

while True:
    user_action = input("Type add or show, or exit: ")
    user_action = user_action.strip()
    # to get clean command without spaces and save it for future use in the program

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            # prints each item without [] ''
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        case anything_else:
            print("Hey, you have entered an unknown command!")

print("Bye!")

