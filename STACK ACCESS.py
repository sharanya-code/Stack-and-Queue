Stack = [] 
choice = 0

while True:

    print("\nS T A C K - O P E R A T I O N S")
    print(" 1. PUSH an element")
    print(" 2. POP an element ")
    print(" 3. Display the Stack")
    print(" 4. Exit")
    
    choice = int(input("ENTER YOUR CHOICE (1-4): "))
    
    #PUSH an element
    if choice == 1:
        element = int(input("Enter the element to be pushed: "))
        Stack.append(element)
        print("The element has been pushed\n")


    #POP an existing element 
    elif choice == 2:
        L =len(Stack)
        if L>0:
            element = Stack.pop()
            print("The element",element,"has been deleted\n")
        else:
            print("\nUnderflow!!\n")

            
    #display the list
    elif choice == 3:
        print("\nThe Stack is:")
        for i in range(len(Stack)-1,-1,-1):
            print(Stack[i])
        

    #exit from the menu
    elif choice == 4:
        break

    else:
        print("Choice is not valid")
        print("\n\nPress any key to continue..............")
        ch = input()
