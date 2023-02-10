import PySimpleGUI as sg
feet = sg.Text("Enter feet:")
input_text1 = sg.Input("")
inches = sg.Text("Enter inches:")
input_text2 = sg.Input("")
con = sg.Button("convert")
window = sg.Window("Convertor",layout = [[feet,input_text1],[inches,input_text2],[con]])
window.read()
window.close()
