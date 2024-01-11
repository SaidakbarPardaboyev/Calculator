import PyQt5.QtWidgets as qtw
# class for Window_Icon
import PyQt5.QtGui as qtg

# Create main Window
class Calculator(qtw.QTabWidget):
    def __init__(self):
        super().__init__()

        self.essignments = ['−','+','÷','×']
        self.OtherAmallar = []

        # Set Title to the app
        self.setWindowTitle("Calculator")
        # Set Icon to the app
        self.setWindowIcon(qtg.QIcon("C:/Users/user/Desktop/Calculator Icon.ico"))
        # To give size to the app by our hand
        self.resize(405, 700)
        # Make the window unchangable
        self.setMinimumSize(405, 700)
        self.setMaximumSize(405, 700)
        # Give the position for the app when run it, it should be the position
        self.move(0, 0)

        # Give black color to the background of the app
        self.setStyleSheet("background-color: black;")

        # Create a Entry Label
        self.Entry_Label = qtw.QLabel("0", self)
        # Give a size and a position for the entry label
        self.Entry_Label.setGeometry(35, 145, 335, 40)
        # Give a size for the entry label
        self.Entry_Label.setFont(qtg.QFont("Arial", 35))
        # Set font color to white
        self.Entry_Label.setStyleSheet("color: white")


        # Create AC buttom to clear the screen of the Calculator
        self.AC_Buttom = qtw.QPushButton("AC", self, clicked= lambda: self.EnterAC())
        # Give a size for AC bottom by our hand and give a position for it
        self.AC_Buttom.setGeometry(20, 200, 80, 80)
        # Give color to the AC bottom and make it circular shape
        self.AC_Buttom.setStyleSheet("background-color: #A5A5A5; border-radius: 40px;")
        # Change size of the bottom's name shrift and make shrift Thin
        self.AC_Buttom.setFont(qtg.QFont("Arial", 18, weight=100))

        # Create buttom to change number into minus of it or pilus of it
        self.PulMin = qtw.QPushButton("+/-", self, clicked= lambda: self.EnterPulMin())
        # Give a size of the buttom by hand and give position for it
        self.PulMin.setGeometry(115, 200, 80, 80)
        # Give a color and circular shape to the buttom
        self.PulMin.setStyleSheet("background-color: #A5A5A5; border-radius: 40px;")
        # Change size of the bottom's name shirft and make shrift Thin
        self.PulMin.setFont(qtg.QFont("Arial", 18, weight=80))

        # Create Percentage buttom
        self.Percentage = qtw.QPushButton("%", self, clicked= lambda: self.EnterPersentage())
        # Give a size and a position for the buttom
        self.Percentage.setGeometry(210, 200, 80, 80)
        # Change the color of the Buttom and make it circular
        self.Percentage.setStyleSheet("background-color: #A5A5A5; border-radius: 40px;")
        # Change the Buttom name shrift and make it Thin
        self.Percentage.setFont(qtg.QFont("Arial", 18, weight=90))

        # Create Diviser Button
        self.Divisor = qtw.QPushButton("÷", self, clicked= lambda: self.Adder('÷'))
        # Give a size and a position for the Button
        self.Divisor.setGeometry(305, 200, 80, 80)
        # Give a color to the back and name of the Button and make the Button circular shape
        self.Divisor.setStyleSheet("background-color: orange; color: white; border-radius: 40px;")
        # Give a size for the Button name and make it Thin
        self.Divisor.setFont(qtg.QFont("Arial", 27, weight=80))

        # Create Seven Button
        self.Seven = qtw.QPushButton("7", self, clicked= lambda: self.Adder(7))
        # Give a size and a position for the Button
        self.Seven.setGeometry(20, 295, 80, 80)
        # Give a color to the back and name of the Button and make the button circular shape
        self.Seven.setStyleSheet("color: white; background-color: #3D3D3D; border-radius: 40px;")
        # Give a size for the button name and make it Thin
        self.Seven.setFont(qtg.QFont("Calibri", 25, weight=60))

        # Create Eight Button
        self.Eight = qtw.QPushButton("8", self, clicked= lambda: self.Adder(8))
        # Give a size and a position for the Button
        self.Eight.setGeometry(115, 295, 80, 80)
        # Give a color to the back and name of the Button and make the button circular shape
        self.Eight.setStyleSheet("color: white; background-color: #3D3D3D; border-radius: 40px;")
        # Give a size for the Button name and make it Thin
        self.Eight.setFont(qtg.QFont("Calibri", 25, weight=60))

        # Create Nine Button
        self.Nine = qtw.QPushButton("9", self, clicked= lambda: self.Adder(9))
        # Give a size and a position for the Button
        self.Nine.setGeometry(210, 295, 80, 80)
        # Give a color to the back and name of the Button and make the button circular shape
        self.Nine.setStyleSheet("color: white; background-color: #3D3D3D; border-radius: 40px")
        # Give a size for the Button name and make it Thin
        self.Nine.setFont(qtg.QFont("Calibri", 25, weight=60))

        # Create Multiply Button
        self.Multipy = qtw.QPushButton("×", self, clicked= lambda: self.Adder('×'))
        # Give a size and a position for the Button
        self.Multipy.setGeometry(305, 295, 80, 80)
        # Give a color for the background and name of the Button and make the Button circular shape
        self.Multipy.setStyleSheet("color: white; background-color: orange; border-radius: 40px;")
        # Give a size to the Button name and make it Thin
        self.Multipy.setFont(qtg.QFont("Arial", 27, weight=80))
        
        # Create four Button
        self.Four = qtw.QPushButton("4", self, clicked= lambda: self.Adder(4))
        # Give a size and a position for the Button
        self.Four.setGeometry(20, 390, 80, 80)
        # give color to the back and name of the Button and make the Button circular shape
        self.Four.setStyleSheet("color: white; background-color: #3D3D3D; border-radius: 40px")
        # give a size to the Button name and make it Thin
        self.Four.setFont(qtg.QFont("Calibri", 25, weight=60))

        # Create four Button
        self.Five = qtw.QPushButton("5", self, clicked= lambda: self.Adder(5))
        # Give a size and a position for the Button
        self.Five.setGeometry(115, 390, 80, 80)
        # give color to the back and name of the Button and make the Button circular shape
        self.Five.setStyleSheet("color: white; background-color: #3D3D3D; border-radius: 40px")
        # give a size to the Button name and make it Thin
        self.Five.setFont(qtg.QFont("Calibri", 25, weight=60))

        # Create four Button
        self.Six = qtw.QPushButton("6", self, clicked= lambda: self.Adder(6))
        # Give a size and a position for the Button
        self.Six.setGeometry(210, 390, 80, 80)
        # give color to the back and name of the Button and make the Button circular shape
        self.Six.setStyleSheet("color: white; background-color: #3D3D3D; border-radius: 40px")
        # give a size to the Button name and make it Thin
        self.Six.setFont(qtg.QFont("Calibri", 25, weight=60))

        # Create four Button
        self.Minus = qtw.QPushButton("−", self, clicked= lambda: self.Adder('−'))
        # Give a size and a position for the Button
        self.Minus.setGeometry(305, 390, 80, 80)
        # give color to the back and name of the Button and make the Button circular shape
        self.Minus.setStyleSheet("color: white; background-color: orange; border-radius: 40px")
        # give a size to the Button name and make it Thin
        self.Minus.setFont(qtg.QFont("Arial", 27, weight=80))

        # Create four Button
        self.One = qtw.QPushButton("1", self, clicked= lambda: self.Adder(1))
        # Give a size and a position for the Button
        self.One.setGeometry(20, 485, 80, 80)
        # give color to the back and name of the Button and make the Button circular shape
        self.One.setStyleSheet("color: white; background-color: #3D3D3D; border-radius: 40px")
        # give a size to the Button name and make it Thin
        self.One.setFont(qtg.QFont("Calibri", 25, weight=60))

        # Create four Button
        self.Two = qtw.QPushButton("2", self, clicked= lambda: self.Adder(2))
        # Give a size and a position for the Button
        self.Two.setGeometry(115, 485, 80, 80)
        # give color to the back and name of the Button and make the Button circular shape
        self.Two.setStyleSheet("color: white; background-color: #3D3D3D; border-radius: 40px")
        # give a size to the Button name and make it Thin
        self.Two.setFont(qtg.QFont("Calibri", 25, weight=60))

        # Create four Button
        self.Three = qtw.QPushButton("3", self, clicked= lambda: self.Adder(3))
        # Give a size and a position for the Button
        self.Three.setGeometry(210, 485, 80, 80)
        # give color to the back and name of the Button and make the Button circular shape
        self.Three.setStyleSheet("color: white; background-color: #3D3D3D; border-radius: 40px")
        # give a size to the Button name and make it Thin
        self.Three.setFont(qtg.QFont("Calibri", 25, weight=60))

        # Create four Button
        self.Pilus = qtw.QPushButton("+", self, clicked= lambda: self.Adder('+'))
        # Give a size and a position for the Button
        self.Pilus.setGeometry(305, 485, 80, 80)
        # give color to the back and name of the Button and make the Button circular shape
        self.Pilus.setStyleSheet("color: white; background-color: orange; border-radius: 40px")
        # give a size to the Button name and make it Thin
        self.Pilus.setFont(qtg.QFont("Arial", 27, weight=80))

        # Create four Button
        self.Zero = qtw.QPushButton("0", self, clicked= lambda: self.Adder(0))
        # Give a size and a position for the Button
        self.Zero.setGeometry(20, 580, 175, 80)
        # give color to the back and name of the Button and make the Button circular shape
        self.Zero.setStyleSheet("color: white; background-color: #3D3D3D; border-radius: 40px")
        # give a size to the Button name and make it Thin
        self.Zero.setFont(qtg.QFont("Calibri", 25, weight=60))

        # Create four Button
        self.Vergul = qtw.QPushButton(",", self, clicked= lambda: self.Adder('.'))
        # Give a size and a position for the Button
        self.Vergul.setGeometry(210, 580, 80, 80)
        # give color to the back and name of the Button and make the Button circular shape
        self.Vergul.setStyleSheet("color: white; background-color: #3D3D3D; border-radius: 40px")
        # give a size to the Button name and make it Thin
        self.Vergul.setFont(qtg.QFont("Calibri", 25, weight=60))

        # Create four Button
        self.Equal = qtw.QPushButton("=", self, clicked= lambda: self.EnterEqual())
        # Give a size and a position for the Button
        self.Equal.setGeometry(305, 580, 80, 80)
        # give color to the back and name of the Button and make the Button circular shape
        self.Equal.setStyleSheet("color: white; background-color: orange; border-radius: 40px")
        # give a size to the Button name and make it Thin
        self.Equal.setFont(qtg.QFont("Arial", 27, weight=80))

        # Show the app
        self.show()

    def EnterAC(self):
        self.Entry_Label.setText("0")

    def EnterPulMin(self):
        if self.Entry_Label.text() != '0':
            try:
                self.Entry_Label.setText(str(int(self.Entry_Label.text()) * (-1)))
            except:
                try:
                    self.Entry_Label.setText(str(float(self.Entry_Label.text()) * (-1)))
                except:
                    pass

    def EnterPersentage(self):
        if self.Entry_Label.text() != '0':
            try:
                self.Entry_Label.setText(str(int(self.Entry_Label.text().strip()) / 100))
            except:
                try:
                    self.Entry_Label.setText(str(float(self.Entry_Label.text().strip()) / 100))
                except:
                    pass

    def Adder(self, number):
        if self.Entry_Label.text() == '0':
            if number not in self.essignments:
                self.Entry_Label.setText(str(number))
        else:
            if number in self.essignments and self.Entry_Label.text()[-1] in self.essignments:
                self.Entry_Label.setText(str((self.Entry_Label.text().strip())[:-1] + str(number)))
            else:
                self.Entry_Label.setText(str((self.Entry_Label.text().strip()) + str(number)))

    def EnterEqual(self):
        res = self.Entry_Label.text()
        res = res.replace('−', '-')
        res = res.replace('+', '+')
        res = res.replace('÷', '/')
        res = res.replace('×', '*')
        self.Entry_Label.setText(str(eval(res)))
        

app = qtw.QApplication([])
mainWind = Calculator()

# Run the app
app.exec_()