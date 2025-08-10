todos = []

while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")+ '\n'

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
                #file = open('todos.txt', 'r')
                #todos = file.readlines()
                #file.close()

            todos.append(todo.title())

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
                #file = open('todos.txt', 'w')
                #file.writelines(todos)
                #file.close()
        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
                #file = open('todos.txt', 'r')
                #todos = file.readlines()
                #file.close()
            if not todos:
               print("You don't have anything to do! Congrats!")
            else:
                #new_todos = [item.strip('\n') for item in todos]
                for index, item in enumerate(todos):
                    item = item.strip('\n')
                    print(f'{index + 1}. {item}')
        case 'edit':
            number = int(input("Which number would you like to edit? "))
            number -= 1

            with open('todos.txt','r') as file:
                todos = file.readlines()

            new_todo = input("Change the todo: ")
            todos[number] = new_todo.title() + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)


        case 'complete':
            completed_number = int(input('Which number would you like to complete?'))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            completed_number -= 1
            todo_to_remove = todos[completed_number].strip('\n')
            todos.pop(completed_number)

            with open('todos.txt','w') as file:
                file.writelines(todos)
            message = f'Todo {todo_to_remove} was completed! Good job!'
            print(message)
        case 'exit':
            break
print("Bye!")