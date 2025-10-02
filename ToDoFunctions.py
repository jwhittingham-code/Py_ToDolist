def ToDoView(dict):
    for k,v in dict.items():
        print(f"({k}) -  {v}")

def ToDoAdd(dict):
    tasktoAdd = input("What task would you like to add? ")
    key = len(dict.keys()) + 1
    
    dict.update({key:tasktoAdd})
    print(dict[key])

def ToDoRm(dict):
    print("Which task would you like to remove?")
    tasktoRm = input("Please type the task number: ")

    dict.pop(int(tasktoRm))
    