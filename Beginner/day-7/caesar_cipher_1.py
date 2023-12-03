alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text_string, shift_amount):
    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    
    if shift_amount <= 0:
        print("Nothing to shift")
        return
    # create an empty list for cipher text
    encode = []
    
    for letter in text_string:
        # get index of letter from alphabet list
        index = alphabet.index(letter)
        # shift index forward based on shift value
        new_index = (index + shift_amount) % 26
        # after shifting, store the shifted text into a list
        encode.append(alphabet[new_index])
    # at the end, join list to become a string
    cipher_text = "".join(encode)
    # print the cipher text
    print(f"The encoded text is {cipher_text}")
        
    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(text, shift)