characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '&', "'", '@', ')', '(', ':', ',', '=', '!', '.', '-', '×', '%', '+', '"', '?', '/']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '.-...', '.----.', '.--.-.', '-.--.-', '-.--.', '---...', '--..--', '-...-', '-.-.--', '.-.-.-', '-....-', '-..-', '.-.-.', '.-..-.', '..--..', '-..-.', '.--.-']


def encode():
    text = input("Type the text you want to encode: ").upper()
    res = []
    for char in text:
        if char == ' ':
            res.append("/ ")
        else:
            res.append(f"{morse[characters.index(char)]} ")
    result = ''.join(res)
    print("The morse text is:\n\n"+result)


def decode():
    code = input("Add the morse code to decode: ").split(' ')
    res = []
    for char in code:
        if char not in morse:
            print("Please type only morse code!")
            return
        elif char == '/':
            res.append(' ')
        elif char == '':
            continue
        else:
            res.append(characters[morse.index(char)])
    result = ''.join(res)
    print(f"The translated text is:\n\n{result}")


method = ''
while method.upper() != "EXIT":
    method = input("\nDo you want to encode(E) or decode(D) text? (type E/D or type EXIT to leave): ")
    if method.upper() == "E":
        encode()
    elif method.upper() == "D":
        decode()
    elif method.upper() == "EXIT":
        print("Bye!")
    else:
        print("Wrong method!")
