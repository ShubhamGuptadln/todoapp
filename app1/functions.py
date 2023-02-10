FILEPATH = "if.txt"
def readline(filepath=FILEPATH):    #function foe file.writelines
    #filepath = "ih.txt"    #When we do this it will give an error file not found
    """
    This function will read the text file
    and returns the list of to-do items
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def writelines(todos_arg,filepath=FILEPATH ):
    """
    wite the todo items in the textfile
    :param filepath:
    :param todos_arg:
    :return:
    """
    with open(filepath, 'w') as file_local:
        todos_arg = file_local.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")