#ToDoList
#Goal - Add, Remove, View and exit program
#Variables
toDo = {1:"Create to Do list"}
Running = True

#functions


#Prgram loop

while Running:
    
    Menu = input("Add,View,Remove or Exit:")
    Menu = Menu.lower()
    print(Menu)

    if Menu == "exit":
        Running = False
        
    
