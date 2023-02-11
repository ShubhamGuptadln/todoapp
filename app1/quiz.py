import PySimpleGUI as sg
button_labels =("Add","Edit","Apply","End",
                 "Cancel","Undo","Redo")
layout = []
for label in button_labels:
    layout.append([sg.Button(label)])
window = sg.Window("My To - do App",layout= layout)
window.read()
window.close()
