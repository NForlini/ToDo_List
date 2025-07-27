todos = []

while True:
    user_prompt = "Enter Todo:"
    todo = input(user_prompt)
    todos.append(todo.title())
    print(todos)
    print("Next...")