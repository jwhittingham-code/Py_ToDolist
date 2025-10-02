#ToDoList
#Goal - Add, Remove, View and exit program
import ToDoFunctions
#Variables
toDo = {1:"Create to Do list", 2:"add add function"}
Running = True

#functions



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
            #Create function to remove items.
            continue
        case _:
            print('Please select a valid input')

    
