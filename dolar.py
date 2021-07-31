from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup
import os
import csv
import matplotlib.pyplot

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(321, 423)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        # self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        # self.graphicsView.setObjectName("graphicsView")
        # self.verticalLayout.addWidget(self.graphicsView)

        self.labelimg = QtWidgets.QLabel(self.centralwidget)
        self.labelimg.setObjectName("img")
        self.verticalLayout.addWidget(self.labelimg)
        self.labelimg.setPixmap(QtGui.QPixmap('grafico.png'))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        from datetime import datetime
        self.search = "dolar"
        url = f"https://www.google.com/search?q={self.search}"
        self.r = requests.get(url)
        self.s = BeautifulSoup(
            self.r.text, "html.parser")
        self.update = self.s.find("div", class_="BNeawe").text
        # print(self.update)
        t = ""
        for i in self.update:
            if i == ",":
                t += "."
            elif i != " ":
                t += i
            else:
                break
        self.t = float(t)
        self.x = 0
        self.valores = []
        self.valoresn = []
        self.rep = 1
        self.dol = []
        self.dia = []
        self.reais = []

        data_e_hora_atuais = datetime.now()
        self.data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.pesquisar)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Digite o valor em dolares para converter em reais:"))
        self.pushButton.setText(_translate("MainWindow", "Converter"))

    def pesquisar(self):
        _translate = QtCore.QCoreApplication.translate
        dig = self.lineEdit.text()
        dig = float(dig)
        mt = self.t * dig
        cs = mt
        mt = str(mt)
        mt = mt.replace(".", ",")
        self.valores.append(f'${self.update} = R${mt}')
        self.valoresn.append(mt)
        self.rep += 1
        self.label.setText(_translate("MainWindow", f'${dig} é igual a R${str(cs)}'))
        # for i in self.valores:
        #     print(i)
        with open('bd.csv', 'a') as f:
            writer = csv.writer(f, lineterminator='\r')
            writer.writerow([self.t] + [dig] + [cs] + [self.data_e_hora_em_texto])


        with open('bd.csv', 'r') as f:
            leitor = csv.reader(f)
            for i in leitor:
                self.dol.append(float(i[0]))
                self.dia.append(i[3])
                self.reais.append(i[2])
        # print(dia)
        # print(dol)
        matplotlib.pyplot.plot(self.dia, self.dol)
        matplotlib.pyplot.xlabel('Data')
        matplotlib.pyplot.ylabel('Valor do Dollar')
        matplotlib.pyplot.savefig('grafico.png')

        # self.verticalLayout.addWidget(self.labelimg)
        self.labelimg.setPixmap(QtGui.QPixmap('grafico.png'))
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())