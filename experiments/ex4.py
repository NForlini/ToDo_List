todos = []

while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo.title())
        case 'show':
            for index,item in enumerate(todos):
                print(f'{index+1}. {item}')
                print(len(todos))
            print("hello",index,item) #<---------------------

        case 'edit':
            number = int(input("Which number would you like to edit? "))
            number -= 1
            new_todo = input("Change the todo: ")
            todos[number] = new_todo
        case 'complete':
            completed_number = int(input('Which number would you like to complete?'))
            completed_number -= 1
            todos.pop(completed_number)
        case 'exit':
            break
print("Bye!")