from PyQt5.QtWidgets import *
import requests



def bybito_window():
    window = QDialog()
    window.resize(800, 700)

    label = QLabel("Технічний перерив!", )

    main_line = QVBoxLayout()

    main_line.addWidget(label)

    window.setStyleSheet("""

            QLabel
            {
                font-size: 150px;
            }
        """)

    window.setLayout(main_line)
    window.show()
    window.exec()

