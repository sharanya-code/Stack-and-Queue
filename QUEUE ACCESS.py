Queue = [] 
choice = 0

while True:

    print("\nQ U E U E - O P E R A T I O N S")
    print(" 1. Add an element")
    print(" 2. Delete an element ")
    print(" 3. Display the Queue")
    print(" 4. Exit")
    
    choice = int(input("ENTER YOUR CHOICE (1-4): "))
    
    #Add an element
    if choice == 1:
        element = int(input("Enter the element to be added: "))
        Queue.append(element)
        print("The element has been added\n")


    #Delete an existing element 
    elif choice == 2:
        L =len(Queue)
        if L>0:
            element = Queue.pop(0)#Delete the first element of the list
            print("The element",element,"has been deleted\n")
        else:
            print("\nUnderflow!!\n")

            
    #display the Queue
    elif choice == 3:
        print("\nThe Queue is:")
        print(Queue)
        

    #exit from the menu
    elif choice == 4:
        break

    else:
        print("Choice is not valid")
        print("\n\nPress any key to continue..............")
        ch = input()
