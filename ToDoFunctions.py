def ToDoView(dict):
    print("------------------")
    print("-------List-------")
    print("------------------")
    for k,v in dict.items():
        print(f"({k}) -  {v}")
    print("------------------")

def ToDoAdd(dict):
    print("------------------")
    print("-----Add Task-----")
    print("------------------")
    tasktoAdd = input("What task would you like to add? ")
    key = len(dict.keys()) + 1

    if tasktoAdd.lower() != 'back':
        dict.update({key:tasktoAdd})
        print(f'task {tasktoAdd} added')
    print("------------------")

def ToDoReorder(dict):
    values = list(dict.values())
    length = len(dict.keys())
    dict.clear()
    for i in range(length):
        index = i + 1
        dict[index] = values[i]
        

def ToDoRm(dict):
    print("------------------")
    print("--- Remove Task ---")
    print("------------------")
    tryRm = True
    while tryRm:
        print("Which task would you like to remove?")
        tasktoRm = input("Please type the task number: ")
        
        try:
            if tasktoRm.lower() != "back":
                dict.pop(int(tasktoRm))
                ToDoReorder(dict)
            tryRm = False
        except:
            print("invalid task entered, try again")

    print("------------------")