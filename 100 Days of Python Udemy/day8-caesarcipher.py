alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction=direction, text=text, shift=shift):
    cypher = []
    for letter in text:
        number = alphabet.index(letter)
        if direction == 'encode':
            cypher.append(alphabet[number + shift])        
        elif direction == 'decode':
            cypher.append(alphabet[number - shift])
            
    if direction == 'encode':
        print(f"The encoded text is {''.join(cypher)}")
    else:
        print(f"The decoded text is {''.join(cypher)}")
        

    
caesar()

# def encrypt(text=text, shift=shift):
#     cypher = []
#     for i in text:
#         number = alphabet.index(i)
#         cypher.append(alphabet[number + shift])
#         encode = ''.join(cypher)

#     return print(f"The encoded text is {encode}")

# def decrypt(text=text, shift=shift):
#     cypher = []
#     for i in text:
#         number = alphabet.index(i)
#         cypher.append(alphabet[number - shift])
#         encode = ''.join(cypher)

#     return print(f"The decoded text is {encode}") 

# if direction == 'encode':
#     encrypt()
# else:
#     decrypt() 


