from PyQt5.QtWidgets import *
import requests

import binancito
import bybitor
import main2

add = QApplication([])
window = QWidget()
window.resize(400, 300)

valbtn = QPushButton("Обмін гривень")
bino = QPushButton("Обмін криптовалют Binance")
Bybo = QPushButton("Обмін криптовалют Bybit")



main_line = QVBoxLayout()
main_line.addWidget(valbtn)
main_line.addWidget(bino)
main_line.addWidget(Bybo)

def func(val):
    window.setStyleSheet("""
            QPushButton
                   {
                       background-color: #0021c5;  
                   }

           
                    QPushButton
                   {
                       font-size: 35px;  
                   }


               """)

    val = line.text()
    date = line2.text()
    kilka = int(line3.text())



    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={val}&date={date}&json"
    p = requests.get(url)
    if p.status_code == 200:
        data = p.json()
        print(data)
        line4.setText(str(data[0]["rate"] * kilka))
    else:
        print(" Ні")

valbtn.clicked.connect(main2.menu_window)
bino.clicked.connect(binancito.binanco_window)
Bybo.clicked.connect(bybitor.bybito_window)
window.setLayout(main_line)
window.show()
add.exec()
