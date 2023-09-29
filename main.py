# import requests
# from bs4 import BeautifulSoup
#
# response = requests.get("https://morsecode.world/international/morse2.html").text
# bs = BeautifulSoup(response, "html.parser")
#
#
# chars = bs.select(".dotdash span")
# characters = [char.string for char in chars]
# print(characters)
#
# morse = bs.select(".dotdash td")
# morse_code = [m.string for m in morse]
# only_morse = [morse_code[i] for i in range(1, len(morse_code), 2)]
# print(only_morse)

characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '&', "'", '@', ')', '(',
              ':', ',', '=', '!', '.', '-', '×', '%', '+', '"', '?', '/']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
         '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
         '...--', '....-', '.....', '-....', '--...', '---..', '----.', '.-...', '.----.', '.--.-.', '-.--.-', '-.--.',
         '---...', '--..--', '-...-', '-.-.--', '.-.-.-', '-....-', '-..-', '.-.-.', '.-..-.', '..--..', '-..-.',
         '.--.-']


def encode():
    text = input("Type the text you want to encode: ").upper()
    res = []
    for char in text:
        if char == ' ':
            res.append("/ ")
        else:
            res.append(f"{morse[characters.index(char)]} ")
    result = ''.join(res)
    print(result)


def decode():
    code = input("Add the morse code to decode: ").split(' ')
    res = []
    for char in code:
        if char == '/':
            res.append(' ')
        elif char == '':
            continue
        elif char not in morse:
            print("Please type only morse characters.")
        else:
            res.append(characters[morse.index(char)])
    result = ''.join(res)
    print(result)


method = ''
while method.upper() != "EXIT":
    method = input("Do you want to encode(E) or decode(D) morse code (type E/D or type EXIT to leave): ")
    if method.upper() == "E":
        encode()
    elif method.upper() == "D":
        decode()
    elif method.upper() == "EXIT":
        print("Bye!")
    else:
        print("Wrong method!")
