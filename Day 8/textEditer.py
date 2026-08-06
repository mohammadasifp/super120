stack=[]
text=""
while True:
    print("====== text Editer =====")
    print("1.Add text")
    print("2.Display text")
    print("3.Undo")
    print("4.Exit")
    
    choice=int(input("Enter your choice :"))
    
    if choice == 1:
        stack.append(text)
        new_text=input("Enter text :")
        text+=new_text
        print("Text Added Successfuly")
    elif choice==2:
        print("Current Text")
        print("text is :",text)
    elif choice==3:
        if len(stack)==0:
            print("Nothing to Undo")
        else:
            text=stack.pop
            print("Undo Successfully")
    elif choice==4:
        print("Thank you")
        break
    else:
        print("Invalid choice")