from modules import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is:  ", now)
while True:
  user_action = input("Type add, show, edit, complete or exit: ")
  user_action = user_action.strip()

  if user_action.startswith('add'):
    todo = user_action[4:] + "\n"
    
    todos = functions.get_todos()

    todos.append(todo)

    functions.add_todos(tasks=todos)
  elif user_action.startswith('show'):
    todos = functions.get_todos()

    for index, item in enumerate(todos):
      item = item.strip('\n')
      row = f"{index + 1}-{item}"
      print(row)
  elif user_action.startswith('edit'):
    try:

      number = int(user_action[5:])
      number -= 1
      todos = functions.get_todos()
      print('Here are the existing todos: ', todos)
      
      new_todo = input("Enter new todo:  ")
      todos[number] = new_todo + '\n'
      print(todos)
      
      functions.add_todos(tasks=todos)

    except ValueError:
      print("Your command is not valid.")
      continue


  elif user_action.startswith('complete'):
    try:
      number = int(user_action[9:])

      
      todos = functions.get_todos()
      
      todo_to_remove = todos[number - 1].strip('\n')

      todos.pop(number - 1)

      functions.add_todos(tasks=todos)


      message = f"Todo {todo_to_remove} was removed from the lsit."
      print(message)
    except IndexError:
      print("There is no item with that number.")
      continue
  elif user_action.startswith('exit'):
    break
  
  else:
    print("Command not supported")