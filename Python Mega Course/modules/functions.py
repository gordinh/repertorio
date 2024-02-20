FILEPATH = './todos.txt'

def get_todos(filepath=FILEPATH):
  """Return the todos from a file."""
  with open(filepath, 'r') as f:
    tasks = f.readlines()
  return tasks

def add_todos(tasks, filepath=FILEPATH):
  """ Write a list of todos to a file. """
  with open(filepath, 'w') as f:
    f.writelines(tasks)

if __name__ == '__main__':
  print("Hello")
  print(get_todos())