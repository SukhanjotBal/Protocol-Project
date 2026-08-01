def Encode(Text_Inputted):
    Binary_string =' '.join(format(ord(char), '08b') for char in Text_Inputted)
    return Binary_string
        