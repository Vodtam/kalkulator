from PyQt5.QtWidgets import *
import requests

add = QApplication([])
window = QWidget()
window.resize(800, 700)

get = QPushButton("Отримати курс валют")
line = QLineEdit()
line2 = QLineEdit()
line3 = QLineEdit()


main_line = QVBoxLayout()


main_line.addWidget(get)
main_line.addWidget(line)
main_line.addWidget(line2)
main_line.addWidget(line3)




def func():
    val = line.text()
    date = line2.text()
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={val}&date={date}&json"
    p = requests.get(url)
    if p.status_code == 200:
        data = p.json()
        print(data)
        line3.setText(str(data[0]["rate"]))
    else:
        print(" Ну ти і лох")


get.clicked.connect(func)
window.setLayout(main_line)
window.show()
add.exec()