#ToDoList
#Goal - Add, Remove, View and exit program
import ToDoFunctions
#Variables
toDo = {1:"Create to Do list"}
Running = True

#functions



#Prgram loop

while Running:
    
    Menu = input("Add,View,Remove or Exit:")
    Menu = Menu.lower()
    
    match Menu: 
        case "exit":
            Running = False
        case "view":
            ToDoFunctions.ToDoView(toDo)
            
        case "add":
            #Create function to Add items.
            continue
        case "remove":
            #Create function to remove items.
            continue

    
