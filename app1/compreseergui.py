import PySimpleGUI as sg
file_select = sg.Text("Select file to compress")
input1 =sg.Input("")
choose1= sg.FilesBrowse("Choose")

folder_select = sg.Text("Select destination folder")
input2 =sg.Input("")
choose2= sg.FolderBrowse("Choose")
compress = sg.Button("Compress")
window = sg.Window("File Compressor", layout=[[file_select, input1, choose1],
                   [folder_select, input2, choose2], [compress]])
window.read()
window.close()

