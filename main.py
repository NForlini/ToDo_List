todos = []

while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")+ '\n'

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo.title())

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            if not todos:
               print("You don't have anything to do! Congrats!")
            else:
                for index, item in enumerate(todos):
                   print(f'{index + 1}. {item}')
        case 'edit':
            number = int(input("Which number would you like to edit? "))
            number -= 1
            new_todo = input("Change the todo: ")
            todos[number] = new_todo.title()
        case 'complete':
            completed_number = int(input('Which number would you like to complete?'))
            completed_number -= 1
            todos.pop(completed_number)
        case 'exit':
            break
print("Bye!")