# A Global Variable
total_items = list()

#The starting Function.
def select():
    user_input = str()
    while user_input != "End":
        print("Tap 'End' to stop.")
        user_input = input("select one of these: \n1- Add item.\n2- remove item.\n3- see list.\n")
        if user_input == '1':
            Add_item()
        elif user_input == '2':
            remove_item()
        elif user_input == '3' :
            see_list() 
        else:
            print("Please select one of the above!") if user_input != "End" else ""
    print("See you later!.")

#Add Items function.
def Add_item():
    item = str()

    #if the user input was EMPTY, the program will ask Him again.  
    while item == '':
        item = input("Enter an item: ")
        total_items.append(item) if item != '' else print("Please enter an item!")

    #check if the item was added 
    if total_items:
        print("Item added successfuly!")

#Remove Items Function
def remove_item():
    #check if the list is EMPTY or NOT
    if total_items != []:
        print(total_items)
        print("To remove an Item, Please Enter it's name.")
        select_user = input("Enter the item you want to remove: ")
        for i in total_items:
            if i == select_user:
                total_items.remove(i)
                print("Item removed successfuly!")
    else:
        print("Your list is already Empty!")

#show list function
def see_list():
    #check if the list is EMPTY or NOT again.
    if total_items != []:
        print("Your list is:")
        for x in total_items:
            print(x)
    else: 
        print("Your list is Empty!") 

#The starting Function.
select()