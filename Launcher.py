import json

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from main import main_game

app = QApplication([])
settings = {}
def read_data():
    global settings
    with open("settings.json", "r", encoding="utf-8") as file:
        settings = json.load(file)
def write_data():
    global settings
    with open("settings.json", "w", encoding="utf-8") as file:
        json.dump(settings, file)
window = QWidget()

read_data()
print(settings)

start_btn = QPushButton("Старт")
change_btn = QPushButton("Change")
skin_1 = QLabel("Картинка")
skin_1_img = QPixmap("asteroid.png")
skin_1_img = skin_1_img.scaledToWidth(64)
skin_1.setPixmap(skin_1_img)
line_edit = QLineEdit(settings["skin"])

main_line = QVBoxLayout()
main_line.addWidget(line_edit)
main_line.addWidget(change_btn)
main_line.addWidget(start_btn)
main_line.addWidget(skin_1)
main_line.addWidget(buy_skin_1_bth)
window.setLayout(main_line)


def buy_skin_1():
    if settings["money"] >= 7:
        settings["skin"] = "asteroid.png"
        write_data()
    else:
        print("Грошей не хватає!!")

        buy_skin_1_btn.clicked.connect(buy_skin_1)
        def change_data():
            settings["skin"] = line_edit.text()
            write_data()
def change_data():
    settings["skin"] = line_edit.text()
    write_data()


def change_data():
    settings["skin"] = line_edit.text()
    write_data()

change_btn.clicked.connect(change_data)

start_btn.clicked.connect(main_game)

window.show()
app.exec()
