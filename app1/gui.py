import functions
import PySimpleGUI as sg
import time
sg.theme("Black")
clock = sg.Text("",key="Clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo",key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.readline(),
                      key="todos",
                      enable_events=True,
                      size = [45,10])
list_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
close = sg.Button("close")
window = sg.Window("My To -Do App",
                   layout=[[clock],[label],[input_box,add_button],[list_box,list_button,complete_button],[close]],
                   font = ("Helvetica",20))
while True:
    event,values = window.read(timeout=10)
    window["Clock"].update(time.strftime("%b-%d-%Y  %H:%M:%S"))
    print(1,event)
    print(2,values)

    match event:
        case "Add":
            todos = functions.readline()
            newtodo = values['todo']+"\n"
            todos.append(newtodo)
            functions.writelines(todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                newtodo = values['todo']+"\n"

                todos = functions.readline()
                index = todos.index(todo_to_edit)
                todos[index]=newtodo
                functions.writelines(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first")
        case "Complete":
            todo_to_delete = values['todos'][0]
            todos = functions.readline()
            todos.remove(todo_to_delete)
            functions.writelines(todos)
            window['todos'].update(values=todos)
            window['todo'].update("")
        case "close":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break




window.close()