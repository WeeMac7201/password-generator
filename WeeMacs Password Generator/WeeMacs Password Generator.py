#Basic Password Generator

import random
import string
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QGroupBox, QSpinBox, QCheckBox, QBoxLayout, QWidget, QHBoxLayout
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt



# Defining the password variables and style/contents
def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters 
    required_chars = []

    if numbers:
        characters += digits
        required_chars.append(random.choice(digits))
    if special_characters:
        characters += special
        required_chars.append(random.choice(special))

    remaning_length = max(min_length - len(required_chars), 0)
    pwd = required_chars + [random.choice(characters) for _ in range(remaning_length)]

    random.shuffle(pwd)

    return "".join(pwd) 


#Constructing window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Graphical Stuff 
        self.setWindowTitle("Custom Password Generator")
        self.setGeometry(1000, 500, 500, 500)
        self.setWindowIcon(QIcon("\WeeMacs Password Generator\padlock.png"))
        self.initUI()
        
    def initUI(self):
                        # Background Image
        background_frame = QLabel(self)
        background_frame.setGeometry(0, 0, self.width(), self.height())

        pixmap_background = QPixmap("\WeeMacs Password Generator\Background.jpg")
        background_frame.setPixmap(pixmap_background)
        background_frame.setScaledContents(True)
        background_frame.setGeometry(0, 0, self.width(), self.height())  # Full window
        background_frame.lower()  # Ensure it's behind other widgets
        if pixmap_background.isNull():
            print("Failed to load image!")

        #Title Text
        self.text = QLabel("WeeMac's Password Generator", self)
        self.text.setFont(QFont("Arial", 25))
        self.text.setGeometry(0, 0, 500, 100)
        self.text.setStyleSheet("color: black;" 
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        self.text.setAlignment(Qt.AlignCenter)   #Center and Center
      
        #Dynamic Text
        self.dtext = QLabel("Password Pending...", self)
        self.dtext.setFont(QFont("Arial", 20))
        self.dtext.setGeometry(0, 250, 500, 100)
        self.dtext.setStyleSheet("color: black;" 
                            "font-weight: bold;")
        self.dtext.setAlignment(Qt.AlignCenter)   #Center and Center

        # Password Option Selection Box

        self.options_group = QGroupBox("Password Options", self)
        self.options_group.setAlignment(Qt.AlignCenter) 
        self.options_group.setFont(QFont("Arial", 18))
        self.options_group.setStyleSheet("color: black;"
                                         "font-weight: bold;")
        self.options_group.setGeometry(50, 100, 400, 100)
        self.options_group.raise_

        layout = QHBoxLayout()

        # Length Selector 

        self.length_spin = QSpinBox()
        self.length_spin.setMinimum(10)
        self.length_spin.setMaximum(24)
        self.length_spin.setValue(14)
        layout.addWidget(QLabel("Length:"))
        layout.addWidget(self.length_spin)

        # Numbers Toggle 

        self.numbers_checkbox = QCheckBox("Include Numbers")
        self.numbers_checkbox.setChecked(True)
        layout.addWidget(self.numbers_checkbox)

        # Special Chars Toggle

        self.special_checkbox = QCheckBox("Include Special Characters")
        self.special_checkbox.setChecked(True)
        layout.addWidget(self.special_checkbox)
        
        # Key to displaying the selection boxes to the Password Option Selection Box
        self.options_group.setLayout(layout)

        

        # Start Button Settings

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click to Generate")
        self.b1.setFont(QFont("arial" ,15))
        self.b1.setGeometry(160, 200, 180, 50)
        self.b1.clicked.connect(self.clicked)

          # Copy Button Settings
        self.b2 = QPushButton("Copy to Clipboard", self)
        self.b2.setGeometry(175, 370, 150, 40)
        self.b2.clicked.connect(self.cp_clipboard)
        self.b2.setEnabled(False) #Disables Button by default

        self.statusBar()

    def clicked(self):
        length = self.length_spin.value()
        use_numbers = self.numbers_checkbox.isChecked()
        use_special = self.special_checkbox.isChecked()

        password = generate_password(min_length = length, 
                                     numbers=use_numbers,
                                      special_characters=use_special)
        self.dtext.setText(password)
        self.b2.setEnabled(True) #Enables the Copy Button


     # Copy Button Settings
    
    def cp_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.dtext.text())
        self.statusBar().showMessage("Password copied to clipboard!", 2000)

        



#Showing the window
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



