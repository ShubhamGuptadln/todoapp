import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo",key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.readline(),
                      key="todos",
                      enable_events=True,
                      size = [45,10])
list_button = sg.Button("Edit")
window = sg.Window("My To -Do App",
                   layout=[[label],[input_box,add_button],[list_box,list_button]],
                   font = ("Helvetica",20))
while True:
    event,values = window.read()
    print(1,event)
    print(2,values)
    print(3,values['todos'])
    match event:
        case "Add":
            todos = functions.readline()
            newtodo = values['todo']+"\n"
            todos.append(newtodo)
            functions.writelines(todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            newtodo = values['todo']+"\n"

            todos = functions.readline()
            index = todos.index(todo_to_edit)
            todos[index]=newtodo
            functions.writelines(todos)
            window['todos'].update(values=todos)
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break




window.close()