while True:
    Text_Input = str(input("Enter the text to be encoded: "))

    Binary_str = ' '.join(format(ord(char), '08b') for char in Text_Input)

    print(f"Text: {Text_Input} has been encoded")
    print(Binary_str)
    
    Quit = input("Quit? (Yes/No)")
    
    if Quit == "Yes":
        break
    elif Quit == "No":
        pass
    else:
        print("Invalid Input")
        

    

