import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state.new_todo = ""


st.title("My To-do app")
st.subheader("Be your best self")
st.write("Enter and manage your tasks :")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

inputbox = st.text_input(label="Enter a to-do:", placeholder="Add a new to-do...", on_change=add_todo, key='new_todo')