import requests
from bs4 import BeautifulSoup

search = "dollar"
url = f"https://www.google.com/search?q={search}"
r = requests.get(url)
s = BeautifulSoup(r.text, "html.parser")
update = s.find("div", class_="BNeawe").text
print(update)
t = ""
for i in update:
    if i == ",":
        t += "."
    elif i != " ":
        t += i
    else:
        break
t = float(t)
x = 0
while x == 0:
    try:
        dig = input("Digite um valor a ser convertido em dollar:")
        if dig == "":
            x += 1
            print("\nGoodBye!!!")
        else:
            dig = float(dig)
            mt = t * dig
            mt = str(mt)
            mt = mt.replace(".", ",")
            print(f"Receberá R${mt} reais")

    except ValueError:
        print("Valor inválido")
# sal = t * 500
# sal = str(sal)
# sal = sal.replace(".", ",")
# print(f"Receberá R${sal} reais")