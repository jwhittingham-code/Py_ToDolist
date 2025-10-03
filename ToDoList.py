#ToDoList
#Goal - Add, Remove, View and exit program
#functions
import ToDoFunctions

#Variables
toDo = {1:"Create to Do list", 2:"add add function"}
Running = True

#Prgram loop
while Running:
    print("------------------")
    print("----To Do List----")
    print("------------------")
    
    Menu = input("Add,View,Remove or Exit: ")
    Menu = Menu.lower()
    
    match Menu: 
        case "exit":
            Running = False
        case "view":
            ToDoFunctions.ToDoView(toDo)    
        case "add":
            ToDoFunctions.ToDoAdd(toDo)
        case "remove":
            ToDoFunctions.ToDoRm(toDo)
           
        case _:
            print('Please select a valid input')

    
