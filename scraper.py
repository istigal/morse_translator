import requests
from bs4 import BeautifulSoup

response = requests.get("https://morsecode.world/international/morse2.html").text
bs = BeautifulSoup(response, "html.parser")


chars = bs.select(".dotdash span")
characters = [char.string for char in chars]
print(characters)

morse = bs.select(".dotdash td")
morse_code = [m.string for m in morse]
only_morse = [morse_code[i] for i in range(1, len(morse_code), 2)]
print(only_morse)