import requests
from bs4 import BeautifulSoup
import os
import csv
import matplotlib.pyplot
from datetime import datetime

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
valores = []
valoresn = []
rep = 1
dol = []
dia = []
reais = []
while x == 0:
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
    try:
        dig = input(f"Digite um valor a ser convertido em {search}: R$")

        if dig == "":
            x += 1
            print("\nGoodBye!!!")
        else:
            dig = float(dig)
            mt = t * dig
            cs = mt
            mt = str(mt)
            mt = mt.replace(".", ",")
            valores.append(f'${update} = R${mt}')
            valoresn.append(mt)
            rep += 1
            for i in valores:
                print(i)
            with open('bd.csv', 'a') as f:
                writer = csv.writer(f, lineterminator='\r')
                writer.writerow([t] + [dig] + [cs] + [data_e_hora_em_texto])

    except ValueError:
        print("Valor inválido")
with open('bd.csv', 'r') as f:
    leitor = csv.reader(f)
    for i in leitor:
        dol.append(i[0])
        dia.append(i[3])
        reais.append(i[2])
matplotlib.pyplot.plot(dia, dol)
matplotlib.pyplot.xlabel('Data')
matplotlib.pyplot.ylabel('Valor do Dollar')
matplotlib.pyplot.show()