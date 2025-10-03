#ToDoList
#Goal - Add, Remove, View and exit program
#functions
import ToDoFunctions

#Variables
toDo = {1:"Create to Do list", 2:"add add function"}
Running = True

#Prgram loop
print("------------------")
while Running:
    print("----To Do List----")
    print("------ Menu ------")
    print("------------------")
    
    Menu = input("Add,View,Remove or Exit: ")
    Menu = Menu.lower()
    
    match Menu: 
        case "exit":
            print("Thank you for using this to do list app")
            print("------------------")
            Running = False
        case "view":
            ToDoFunctions.ToDoView(toDo)    
        case "add":
            ToDoFunctions.ToDoAdd(toDo)
        case "remove":
            ToDoFunctions.ToDoRm(toDo)
        case _:
            print('Please select a valid input')
            
