todos = []

while True:
    user_action = input("Type add or show, edit, complete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index + 1}--{item}"
                print(row)
        case 'exit':
            break
        case 'edit':
            number = int(input("Enter the number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case anything_else:
            print("Hey, you have entered an unknown command!")

print("Bye!")

