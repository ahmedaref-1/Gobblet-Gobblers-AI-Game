from PyQt5 import QtCore, QtGui, QtWidgets
import Images


class BoardWindow(object):
    def setupUi(self, Gobblet):
        Gobblet.setObjectName("Gobblet")
        Gobblet.resize(1083, 838)
        Gobblet.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(Gobblet)
        self.centralwidget.setObjectName("centralwidget")

        # Player 1 Name Label
        self.Player1Name = QtWidgets.QLabel(self.centralwidget)
        self.Player1Name.setEnabled(False)
        self.Player1Name.setGeometry(QtCore.QRect(10, 50, 200, 51))
        self.Player1Name.setScaledContents(False)
        self.Player1Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Player1Name.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.Player1Name.setObjectName("Player1Name")

        # Player 2 Name Label
        self.Player2Name = QtWidgets.QLabel(self.centralwidget)
        self.Player2Name.setEnabled(False)
        self.Player2Name.setGeometry(QtCore.QRect(850, 700, 200, 51))
        self.Player2Name.setScaledContents(False)
        self.Player2Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Player2Name.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.Player2Name.setObjectName("Player2Name")
        self.Player1Name.setStyleSheet("font: 10pt \"Supply Center\";\n"
                                       "color: rgb(0, 0, 255);")
        self.Player2Name.setStyleSheet("font: 10pt \"Supply Center\";\n"
                                       "color: rgb(255, 0, 0);")
        # Set Players Names
        self.Player1Name.setText(f"player1")
        self.Player2Name.setText(f"player2")


        # Player 1 Buttons
        self.Player1G4_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1G4_1.setGeometry(QtCore.QRect(90, 160, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1G4_1.setFont(font)
        self.Player1G4_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1G4_1.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 15px;\n"
            "    background-color: #0000FF;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player1G4_1.setObjectName("Player1G4_1")


        self.Player1G3_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1G3_1.setGeometry(QtCore.QRect(80, 150, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1G3_1.setFont(font)
        self.Player1G3_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1G3_1.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 25px;\n"
            "    background-color: #0000FF;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player1G3_1.setObjectName("Player1G3_1")


        self.Player1G2_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1G2_1.setGeometry(QtCore.QRect(70, 140, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1G2_1.setFont(font)
        self.Player1G2_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1G2_1.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 35px;\n"
            "    background-color: #0000FF;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player1G2_1.setObjectName("Player1G2_1")


        self.Player1G1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1G1_1.setGeometry(QtCore.QRect(60, 130, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1G1_1.setFont(font)
        self.Player1G1_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1G1_1.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 45px;\n"
            "    background-color: #0000FF;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player1G1_1.setCheckable(False)
        self.Player1G1_1.setObjectName("Player1G1_1")


        self.Player1G4_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1G4_2.setGeometry(QtCore.QRect(90, 280, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1G4_2.setFont(font)
        self.Player1G4_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1G4_2.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 15px;\n"
            "    background-color: #0000FF;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player1G4_2.setObjectName("Player1G4_2")


        self.Player1G3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1G3_2.setGeometry(QtCore.QRect(80, 270, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1G3_2.setFont(font)
        self.Player1G3_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1G3_2.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 25px;\n"
            "    background-color: #0000FF;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player1G3_2.setObjectName("Player1G3_2")


        self.Player1G2_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1G2_2.setGeometry(QtCore.QRect(70, 260, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1G2_2.setFont(font)
        self.Player1G2_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1G2_2.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 35px;\n"
            "    background-color: #0000FF;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player1G2_2.setObjectName("Player1G2_2")


        self.Player1G1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1G1_2.setGeometry(QtCore.QRect(60, 250, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1G1_2.setFont(font)
        self.Player1G1_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1G1_2.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 45px;\n"
            "    background-color: #0000FF;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player1G1_2.setCheckable(False)
        self.Player1G1_2.setObjectName("Player1G1_2")


        self.Player1G4_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1G4_3.setGeometry(QtCore.QRect(90, 400, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1G4_3.setFont(font)
        self.Player1G4_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1G4_3.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 15px;\n"
            "    background-color: #0000FF;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player1G4_3.setObjectName("Player1G4_3")


        self.Player1G3_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1G3_3.setGeometry(QtCore.QRect(80, 390, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1G3_3.setFont(font)
        self.Player1G3_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1G3_3.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 25px;\n"
            "    background-color: #0000FF;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player1G3_3.setObjectName("Player1G3_3")


        self.Player1G2_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1G2_3.setGeometry(QtCore.QRect(70, 380, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1G2_3.setFont(font)
        self.Player1G2_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1G2_3.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 35px;\n"
            "    background-color: #0000FF;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player1G2_3.setObjectName("Player1G2_3")


        self.Player1G1_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1G1_3.setGeometry(QtCore.QRect(60, 370, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1G1_3.setFont(font)
        self.Player1G1_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1G1_3.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 45px;\n"
            "    background-color: #0000FF;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player1G1_3.setCheckable(False)
        self.Player1G1_3.setObjectName("Player1G1_3")


        self.Player2G4_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2G4_1.setGeometry(QtCore.QRect(940, 590, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2G4_1.setFont(font)
        self.Player2G4_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2G4_1.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 15px;\n"
            "    background-color: #FF0000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2G4_1.setObjectName("Player2G4_1")


        self.Player2G4_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2G4_2.setGeometry(QtCore.QRect(940, 470, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2G4_2.setFont(font)
        self.Player2G4_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2G4_2.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 15px;\n"
            "    background-color: #FF0000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2G4_2.setObjectName("Player2G4_2")


        self.Player2G4_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2G4_3.setGeometry(QtCore.QRect(940, 350, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2G4_3.setFont(font)
        self.Player2G4_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2G4_3.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 15px;\n"
            "    background-color: #ff0000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2G4_3.setObjectName("Player2G4_3")


        self.Player2G3_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2G3_1.setGeometry(QtCore.QRect(930, 580, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2G3_1.setFont(font)
        self.Player2G3_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2G3_1.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 25px;\n"
            "    background-color: #ff0000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2G3_1.setObjectName("Player2G3_1")


        self.Player2G3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2G3_2.setGeometry(QtCore.QRect(930, 460, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2G3_2.setFont(font)
        self.Player2G3_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2G3_2.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 25px;\n"
            "    background-color: #ff0000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2G3_2.setObjectName("Player2G3_2")


        self.Player2G3_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2G3_3.setGeometry(QtCore.QRect(930, 340, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2G3_3.setFont(font)
        self.Player2G3_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2G3_3.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 25px;\n"
            "    background-color: #ff0000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2G3_3.setObjectName("Player2G3_3")


        self.Player2G2_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2G2_1.setGeometry(QtCore.QRect(920, 570, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2G2_1.setFont(font)
        self.Player2G2_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2G2_1.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 35px;\n"
            "    background-color: #ff0000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2G2_1.setObjectName("Player2G2_1")


        self.Player2G2_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2G2_2.setGeometry(QtCore.QRect(920, 450, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2G2_2.setFont(font)
        self.Player2G2_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2G2_2.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 35px;\n"
            "    background-color: #ff0000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2G2_2.setObjectName("Player2G2_2")


        self.Player2G2_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2G2_3.setGeometry(QtCore.QRect(920, 330, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2G2_3.setFont(font)
        self.Player2G2_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2G2_3.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 35px;\n"
            "    background-color: #ff0000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2G2_3.setObjectName("Player2G2_3")


        self.Player2G1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2G1_1.setGeometry(QtCore.QRect(910, 560, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2G1_1.setFont(font)
        self.Player2G1_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2G1_1.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 45px;\n"
            "    background-color: #ff0000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2G1_1.setCheckable(False)
        self.Player2G1_1.setObjectName("Player2G1_1")


        self.Player2G1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2G1_2.setGeometry(QtCore.QRect(910, 320, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2G1_2.setFont(font)
        self.Player2G1_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2G1_2.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 45px;\n"
            "    background-color: #ff0000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2G1_2.setCheckable(False)
        self.Player2G1_2.setObjectName("Player2G1_2")


        self.Player2G1_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2G1_3.setGeometry(QtCore.QRect(910, 440, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2G1_3.setFont(font)
        self.Player2G1_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2G1_3.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 45px;\n"
            "    background-color: #ff0000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2G1_3.setCheckable(False)
        self.Player2G1_3.setObjectName("Player2G1_3")

        
        # Board Buttons 
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(250, 90, 150, 150))
        self.Button1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button1.setText("")
        self.Button1.setObjectName("Button1")
        self.Button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2.setGeometry(QtCore.QRect(400, 90, 150, 150))
        self.Button2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button2.setText("")
        self.Button2.setObjectName("Button2")
        self.Button3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button3.setGeometry(QtCore.QRect(550, 90, 150, 150))
        self.Button3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button3.setText("")
        self.Button3.setObjectName("Button3")
        self.Button4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button4.setGeometry(QtCore.QRect(700, 90, 150, 150))
        self.Button4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button4.setText("")
        self.Button4.setObjectName("Button4")
        self.Button5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button5.setGeometry(QtCore.QRect(250, 240, 150, 150))
        self.Button5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button5.setText("")
        self.Button5.setObjectName("Button5")
        self.Button6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button6.setGeometry(QtCore.QRect(400, 240, 150, 150))
        self.Button6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button6.setText("")
        self.Button6.setObjectName("Button6")
        self.Button7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button7.setGeometry(QtCore.QRect(550, 240, 150, 150))
        self.Button7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button7.setText("")
        self.Button7.setObjectName("Button7")
        self.Button8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button8.setGeometry(QtCore.QRect(700, 240, 150, 150))
        self.Button8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button8.setText("")
        self.Button8.setObjectName("Button8")
        self.Button9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button9.setGeometry(QtCore.QRect(250, 390, 150, 150))
        self.Button9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button9.setText("")
        self.Button9.setObjectName("Button9")
        self.Button10 = QtWidgets.QPushButton(self.centralwidget)
        self.Button10.setGeometry(QtCore.QRect(400, 390, 150, 150))
        self.Button10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button10.setText("")
        self.Button10.setObjectName("Button10")
        self.Button11 = QtWidgets.QPushButton(self.centralwidget)
        self.Button11.setGeometry(QtCore.QRect(550, 390, 150, 150))
        self.Button11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button11.setText("")
        self.Button11.setObjectName("Button11")
        self.Button12 = QtWidgets.QPushButton(self.centralwidget)
        self.Button12.setGeometry(QtCore.QRect(700, 390, 150, 150))
        self.Button12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button12.setText("")
        self.Button12.setObjectName("Button12")
        self.Button13 = QtWidgets.QPushButton(self.centralwidget)
        self.Button13.setGeometry(QtCore.QRect(250, 540, 150, 150))
        self.Button13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button13.setText("")
        self.Button13.setObjectName("Button13")
        self.Button14 = QtWidgets.QPushButton(self.centralwidget)
        self.Button14.setGeometry(QtCore.QRect(400, 540, 150, 150))
        self.Button14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button14.setText("")
        self.Button14.setObjectName("Button14")
        self.Button15 = QtWidgets.QPushButton(self.centralwidget)
        self.Button15.setGeometry(QtCore.QRect(550, 540, 150, 150))
        self.Button15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button15.setText("")
        self.Button15.setObjectName("Button15")
        self.Button16 = QtWidgets.QPushButton(self.centralwidget)
        self.Button16.setGeometry(QtCore.QRect(700, 540, 150, 150))
        self.Button16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button16.setText("")
        self.Button16.setObjectName("Button16")


        self.up_finger = QtWidgets.QLabel(self.centralwidget)
        self.up_finger.setGeometry(QtCore.QRect(50, 470, 100, 100))
        self.up_finger.setText("")
        self.up_finger.setPixmap(QtGui.QPixmap("Images/up_finger.png"))
        self.up_finger.setScaledContents(True)
        self.up_finger.setObjectName("label_3")
        self.down_finger = QtWidgets.QLabel(self.centralwidget)
        self.down_finger.setGeometry(QtCore.QRect(900, 210, 100, 100))
        self.down_finger.setText("")
        self.down_finger.setPixmap(QtGui.QPixmap("Images/down_finger.png"))
        self.down_finger.setScaledContents(True)
        self.down_finger.setObjectName("label_4")
        Gobblet.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Gobblet)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1083, 26))
        self.menubar.setObjectName("menubar")
        Gobblet.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Gobblet)
        self.statusbar.setObjectName("statusbar")
        Gobblet.setStatusBar(self.statusbar)
        

        # Setting the central widget for the main window
        Gobblet.setCentralWidget(self.centralwidget)

        # Translating user interface texts
        self.retranslateUi(Gobblet)
        QtCore.QMetaObject.connectSlotsByName(Gobblet)

        # Set Player 1 Buttons
        P1BlueButtons = [self.Player1G1_1, self.Player1G1_2, self.Player1G1_3,
                       self.Player1G2_1, self.Player1G2_2, self.Player1G2_3,
                       self.Player1G3_1, self.Player1G3_2, self.Player1G3_3,
                       self.Player1G4_1, self.Player1G4_2, self.Player1G4_3]
        
        # Set Player 2 Buttons
        P2RedButtons = [self.Player2G1_1, self.Player2G1_2, self.Player2G1_3,
                        self.Player2G2_1, self.Player2G2_2, self.Player2G2_3,
                        self.Player2G3_1, self.Player2G3_2, self.Player2G3_3,
                        self.Player2G4_1, self.Player2G4_2, self.Player2G4_3]
        
        # Set Board Buttons
        boardButtons = [self.Button1, self.Button2, self.Button3, self.Button4,
                        self.Button5, self.Button6, self.Button7, self.Button8,
                        self.Button9, self.Button10, self.Button11, self.Button12,
                        self.Button13, self.Button14, self.Button15, self.Button16]
        
        # Varaiable to indicate player round 
        playerRound = "player1"

        self.startGame(self, P1BlueButtons, P2RedButtons, boardButtons,playerRound)
    
        self.down_finger.hide()
    
        
    def startGame(self, event, P1BlueButtons, P2RedButtons, boardButtons,playerRound):
        for btn in boardButtons:
                btn.setEnabled(False)
                btn.setStyleSheet(
        "QPushButton {\n"
        "background-color: rgba(0, 0, 0, 10%);\n"  # 50% transparency (adjust as needed)
        "border: 1px solid black;\n"
        "}") 
        
        # Enable buttons based on the current player's round and set their event handler
        if(playerRound == "player1"):
                for btn in P1BlueButtons:
                        btn.setEnabled(True)
                for btn in P2RedButtons:
                        btn.setEnabled(False)
                for btn in P1BlueButtons:
                        btn.mousePressEvent = lambda event, button=btn: self.handleButtonPress(event, button, P1BlueButtons, P2RedButtons, boardButtons, playerRound)

        elif(playerRound == "player2"):
                for btn in P2RedButtons:
                        btn.setEnabled(True)
                for btn in P1BlueButtons:
                        btn.setEnabled(False)
                for btn in P2RedButtons:
                        btn.mousePressEvent = lambda event, button=btn: self.handleButtonPress(event, button, P1BlueButtons, P2RedButtons, boardButtons, playerRound)
        
                
    def handleButtonPress(self, event, button, P1BlueButtons, P2RedButtons, boardButtons, playerRound):
        # Enable the clicked button
        for btn in boardButtons:
            btn.setEnabled(True)
            btn.raise_()
            btn.setStyleSheet(
        "QPushButton {\n"
        "background-color: rgba(0, 0, 0, 10%);\n"  # 50% transparency (adjust as needed)
        "border: 1px solid black;\n"
        "}")
            
        # Disable buttons for both players    
        for btn in P1BlueButtons:
            btn.setEnabled(False)
        

        for btn in P2RedButtons:
            btn.setEnabled(False)
        
        for btn in boardButtons:
            btn.mousePressEvent = lambda event, board_button=btn: self.placeButton(event, board_button, P1BlueButtons, P2RedButtons, boardButtons, button, playerRound)


    def is_collision(self,board_button, btn, pressedbutton):
        rect1 = board_button.geometry()
        rect2 = btn.geometry()
        # return rect1.intersects(rect2)
        if(rect1.intersects(rect2)):
                if(btn.width() < pressedbutton.width()):
                        return False
                else:
                        return True

    def placeButton(self, event, board_button, P1BlueButtons, P2RedButtons, boardButtons, button, playerRound):

        # Check for collisions with other buttons on the board
        for btn in P1BlueButtons + P2RedButtons:
            if self.is_collision(board_button, btn, button):
                return  # Do not place the button if there is a collision

        # Place the button on the board
        for btn in boardButtons:
            #    btn.lower()
               btn.setStyleSheet(
        "QPushButton {\n"
        "background-color: rgba(0, 0, 0, 10%);\n"  # 50% transparency (adjust as needed)
        "border: 1px solid black;\n"
        "}")
        
        # Set the position of the button on the board
        buttonWidth = button.width()
        buttonHeight = button.height()
        boardX = board_button.x()
        boardY = board_button.y()
        # board_button.setParent(button)
        button.setGeometry(QtCore.QRect(boardX + int(board_button.width()/2) - int(buttonWidth/2),
                                         boardY+int(board_button.width()/2) - int(buttonHeight/2),
                                           buttonWidth, buttonHeight))
        board_button.setStyleSheet(
        "QPushButton {\n"
        "background-color: rgba(0, 0, 0, 10%);\n"  # 50% transparency (adjust as needed)
        "border: 1px solid black;\n"
        "}")
        
        # Lower other buttons based on their sizes
        for btn in P1BlueButtons + P2RedButtons:
                if(btn.width() == 90):
                        btn.lower()

        for btn in P1BlueButtons + P2RedButtons:
                if(btn.width() == 70):
                        btn.lower()
        
        for btn in P1BlueButtons + P2RedButtons:
                if(btn.width() == 50):
                        btn.lower()

        for btn in P1BlueButtons + P2RedButtons:
                if(btn.width() == 30):
                        btn.lower()
        
        # Disable all buttons on the board
        for btn in boardButtons:
               btn.lower()
               btn.setStyleSheet(
        "QPushButton {\n"
        "background-color: rgba(0, 0, 0, 10%);\n"  # 50% transparency (adjust as needed)
        "border: 1px solid black;\n"
        "}")
               

        for btn in boardButtons:
            btn.setEnabled(False)

        # Switch player turns and update button visibility
        if(playerRound == "player1"):
                self.down_finger.show()
                self.up_finger.hide()
                playerRound = "player2"
                for btn in P1BlueButtons:
                        btn.setEnabled(False)
                for btn in P2RedButtons:
                        btn.setEnabled(True)
                for btn in P2RedButtons:
                        btn.mousePressEvent = lambda event, button=btn: self.handleButtonPress(event, button, P1BlueButtons, P2RedButtons, boardButtons, playerRound)
                
        elif(playerRound == "player2"):
                self.up_finger.show()
                self.down_finger.hide()
                playerRound = "player1"
                for btn in P2RedButtons:
                        btn.setEnabled(False)
                for btn in P1BlueButtons:
                        btn.setEnabled(True)
                for btn in P1BlueButtons:
                        btn.mousePressEvent = lambda event, button=btn: self.handleButtonPress(event, button, P1BlueButtons, P2RedButtons, boardButtons, playerRound)

    def retranslateUi(self, Gobblet):
        _translate = QtCore.QCoreApplication.translate
        Gobblet.setWindowTitle(_translate("Gobblet", "Gobblet"))
        self.Player1G4_1.setText(_translate("Gobblet", "4"))
        self.Player1G3_1.setText(_translate("Gobblet", "3"))
        self.Player1G2_1.setText(_translate("Gobblet", "2"))
        self.Player1G1_1.setText(_translate("Gobblet", "1"))
        self.Player1G4_2.setText(_translate("Gobblet", "4"))
        self.Player1G3_2.setText(_translate("Gobblet", "3"))
        self.Player1G2_2.setText(_translate("Gobblet", "2"))
        self.Player1G1_2.setText(_translate("Gobblet", "1"))
        self.Player1G4_3.setText(_translate("Gobblet", "4"))
        self.Player1G3_3.setText(_translate("Gobblet", "3"))
        self.Player1G2_3.setText(_translate("Gobblet", "2"))
        self.Player1G1_3.setText(_translate("Gobblet", "1"))
        self.Player2G4_1.setText(_translate("Gobblet", "4"))
        self.Player2G4_2.setText(_translate("Gobblet", "4"))
        self.Player2G4_3.setText(_translate("Gobblet", "4"))
        self.Player2G3_1.setText(_translate("Gobblet", "3"))
        self.Player2G3_2.setText(_translate("Gobblet", "3"))
        self.Player2G3_3.setText(_translate("Gobblet", "3"))
        self.Player2G2_1.setText(_translate("Gobblet", "2"))
        self.Player2G2_2.setText(_translate("Gobblet", "2"))
        self.Player2G2_3.setText(_translate("Gobblet", "2"))
        self.Player2G1_1.setText(_translate("Gobblet", "1"))
        self.Player2G1_2.setText(_translate("Gobblet", "1"))
        self.Player2G1_3.setText(_translate("Gobblet", "1"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Gobblet = QtWidgets.QMainWindow()
    ui = BoardWindow()
    ui.setupUi(Gobblet)
    Gobblet.show()
    sys.exit(app.exec_())
