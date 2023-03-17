todos = []

while True:
    user_action = input("Type add or show, edit or exit: ")
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
        case 'edit':
            number = int(input("Enter the number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case anything_else:
            print("Hey, you have entered an unknown command!")

print("Bye!")

