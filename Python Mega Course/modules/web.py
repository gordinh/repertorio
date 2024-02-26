import streamlit as st
import functions

def add_todo():
  new_todo = st.session_state["new_task"] + '\n'
  todos.append(new_todo)
  functions.add_todos(todos)

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
  checkbox = st.checkbox(todo.capitalize(), key=todo)
  if checkbox:
    todos.pop(index)
    functions.add_todos(todos)
    del st.session_state[todo]
    st.experimental_rerun()


st.text_input(label="", placeholder="Add a new todo", key="new_task", on_change=add_todo)