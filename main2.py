from PyQt5.QtWidgets import *
import requests

add = QApplication([])
window = QWidget()
window.resize(800, 700)

get = QPushButton("Розрахувати")
menu = QPushButton("Меню")
line = QLineEdit()
line2 = QLineEdit()
line3 = QLineEdit()
line4 = QLineEdit()


main_line = QVBoxLayout()


main_line.addWidget(line)
main_line.addWidget(line2)
main_line.addWidget(line3)
main_line.addWidget(line4)
main_line.addWidget(get)
main_line.addWidget(menu)


add.setStyleSheet("""
        QLineEdit
        {
            border-style: inset;
            border-width: 5px;
            border-radius: 9px   
        }
    """)





def func():
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


get.clicked.connect(func)
window.setLayout(main_line)
window.show()
add.exec()