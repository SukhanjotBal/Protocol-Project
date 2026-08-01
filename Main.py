import Def_function_Encode
from Def_function_Encode import Encode

while True:
    Text_Input = input("Input Text to be encoded: ")

    Binary_str = Encode(Text_Input)
    print(Binary_str)
    
    print(f'Your input has been encoded as {Binary_str}')
    
    Quit = input("Quit? (Yes/No)")
    
    if Quit == "Yes":
        break
    elif Quit == "No":
        pass
    else:
        print("Invalid Input")
        