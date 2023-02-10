# from functions import readline, writelines    # first method way of importing files
import functions  # second way of importing the modules
import time

#print(help(functions.readline))
day = time.strftime("%b-%d-%Y %H:%M:%S")
print(day)

while True:
    do = input("Enter add or show or complete or edit or exit")
    if 'add' in do:
        todo = do[4:] + '\n'
        #with open("if.txt", 'r') as file:
         #   todos = file.readlines()

        todos = functions.readline("if.txt")
        todos.append(todo)

        #with open("if.txt", 'w') as file:
         #   todos = file.writelines(todos)
        functions.writelines("if.txt", todos)

    elif 'show' in do:
        #with open("if.txt", 'r') as file:
         #   todos = file.readlines()
        todos = functions.readline("if.txt")
        for index, item in enumerate(todos):
            index = index+1
            item = item.strip("\n")
            print(f"{index}.{item}")

    elif 'edit' in do:
        try:
            index = int(do[5:])-1
            new_item = input("Enter the new item") + "\n"
            #with open("if.txt", 'r') as file:
             #   todos = file.readlines()
            todos = functions.readline("if.txt")
            todos[index] = new_item

            with open("if.txt", 'w') as file:
                todos = file.writelines(todos)
        except IndexError:
            print("Invalid command")
            continue
    elif 'complete' in do:
        try:
            index = int(do[9:])-1
            #with open("if.txt", 'r') as file:
             #   todos = file.readlines()
            todos = functions.readline("if.txt")

            todos.pop(index)

            #with open("if.txt", 'w') as file:
             #   todos = file.writelines(todos)

            functions.writelines("if.txt", todos)

        except IndexError:
            print("Invalid index")
            continue
    elif 'exit' in do:
        break

    else:
        print("Invalid entry")
