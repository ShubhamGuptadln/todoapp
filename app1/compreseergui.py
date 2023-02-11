from zipcreator import make_archive
import PySimpleGUI as sg
file_select = sg.Text("Select file to compress")
input1 =sg.Input("")
choose1= sg.FilesBrowse("Choose",key="files")

folder_select = sg.Text("Select destination folder")
input2 =sg.Input("")
choose2= sg.FolderBrowse("Choose",key="folder")
compress = sg.Button("Compress")
output_label = sg.Text("",key="output")
window = sg.Window("File Compressor", layout=[[file_select, input1, choose1],
                   [folder_select, input2, choose2], [compress],[output_label]])

while True:
    event,values = window.read()
    print(event)
    print(values)
    filepath = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepath,folder)
    window["output"].update("Compressed successfully")

window.close()

