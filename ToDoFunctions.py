def ToDoView(dict):
    for k,v in dict.items():
        print(f"({k}) -  {v}")

def ToDoAdd(dict):
    tasktoAdd = input("What task would you like to add? ")
    key = len(dict.keys()) + 1

    dict.update({key:tasktoAdd})
    print(dict[key])

def ToDoReorder(dict):
    values = list(dict.values())
    length = len(dict.keys())
    dict.clear()
    for i in range(length):
        index = i + 1
        dict[index] = values[i]
        

def ToDoRm(dict):
    print("Which task would you like to remove?")
    tasktoRm = input("Please type the task number: ")
    dict.pop(int(tasktoRm))
    ToDoReorder(dict)
    

    