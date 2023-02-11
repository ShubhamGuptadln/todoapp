import PySimpleGUI as sg
from convert import convert
feet = sg.Text("Enter feet:")
input_text1 = sg.Input(key="feet")
inches = sg.Text("Enter inches:")
input_text2 = sg.Input(key="inches")
con = sg.Button("convert")
output_label = sg.Text("",key="output")

window = sg.Window("Convertor",layout = [[feet,input_text1],[inches,input_text2],[[con,output_label]]])
while True:
    event,values = window.read()
    print(event)
    print(values)
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet,inches)
    window["output"].update(f"value in metre is {result}",text_color="white")

window.read()
window.close()
