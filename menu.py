from PyQt5.QtWidgets import *
import requests

add = QApplication([])
window = QWidget()
window.resize(400, 300)

val = QPushButton("Обмін гривень")
bin = QPushButton("Обмін криптовалют Binance")
Byb = QPushButton("Обмін криптовалют Bybit")

main_line = QVBoxLayout()
main_line.addWidget(val)
main_line.addWidget(bin)
main_line.addWidget(Byb)

def func(val):
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
        print(" Ну ти і лох")

window.setLayout(main_line)
window.show()
add.exec()