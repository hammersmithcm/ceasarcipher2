
message = input("Please enter a sentence:")
message = message.lower()

sub_dict = {
    "a": "f",
    "b": "g",
    "c": "h",
    "d": "i",
    "e": "j",
    "f": "k",
    "g": "l",
    "h": "m",
    "i": "n",
    "j": "o",
    "k": "p",
    "l": "q",
    "m": "r",
    "n": "s",
    "o": "t",
    "p": "u",
    "q": "v",
    "r": "w",
    "s": "x",
    "t": "y",
    "u": "z",
    "v": "a",
    "w": "b",
    "x": "c",
    "y": "d",
    "z": "e",
}

new_message = ''
for char in message:
    if char in sub_dict:
        char = sub_dict[char]
    new_message += char
print(new_message)



# more fun cipher with you entering the number of letters to shift by :)
alphabet = ("abcdefghijklmnopqrstuvwxyz")
change = int(input("Please enter how much your want to shift your letters? "))
another_message = input ("Please enter a sentence: ")
another_message = another_message.lower()
 
encripted_message = ''

for letter in another_message:
    if letter in alphabet:
        position = alphabet.find(letter)
        new_position = (position + change) % 26
        new_letter = alphabet[new_position]
        encripted_message += new_letter
    else:
        encripted_message += letter
print("Your encripted message is" , encripted_message)

#Unencript the  message giving how much the shift was
alphabet = ("abcdefghijklmnopqrstuvwxyz")
unchange = int(input("Please enter how much your letters were shifted: "))
en_message = input("Please enter your encripted sentence, with spaces: ")

unencripted_message = ''
for let in en_message:
    if let in alphabet:
        pos = alphabet.find(let)
        new_pos = (pos - unchange) % 26
        new_let = alphabet[new_pos]
        unencripted_message += new_let
    else:
        unencripted_message += let
print ("Your unencripted message is" , unencripted_message)

