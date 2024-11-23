select = str()
generalTodo = []
while select != "End":
    print("Tap 'End' to stop.")
    print("1- Add.\n2- Show list.")
    select = input("Select one of those: ")
    if select == "1":
        item = input("Add item: ")
        time = input("Add time: ")
        toDo = item,time
        generalTodo += [toDo]
        if generalTodo:
            print("Item added successfully!.")
    elif select == "2":
        if generalTodo != []:
            print(generalTodo)
        else:
            print("You have nothing!.")
    elif select == "End":
        print("See you later!.")
    else: 
        print("There are only two options, choose betwen them.")
 