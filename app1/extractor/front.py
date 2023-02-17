import PySimpleGUI as sg
from backend import extractor
label1 = sg.Text("Select archive")
input1 = sg.Input("")
filebrowser = sg.FilesBrowse("choose",key="archive")

label2 = sg.Text("Select destination folder")
input2 = sg.Input("")
folderbrowser = sg.FolderBrowse("choose",key="dest")
extract = sg.Button("Extract")
outputlabel = sg.Text(key="output",text_color="green")
window = sg.Window("Archive Extractor",
                   layout=[[label1,input1,filebrowser],
                            [label2,input2,folderbrowser],
                           [extract,outputlabel]]

                  )
while True:
    event,values = window.read()
    print(event)
    print(values)
    arc = values["archive"]
    des = values["dest"]
    extractor(arc,des)
    window["output"].update("Extracted successfully")


window.read()
window.close()

