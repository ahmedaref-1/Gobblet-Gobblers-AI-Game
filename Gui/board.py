from PyQt5 import QtCore, QtGui, QtWidgets
import Images
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QSound
from Game import *


class boardCurvedButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(boardCurvedButton, self).__init__(parent)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet(
            "QPushButton {"
            "   background-color: transparent;"  # Set a transparent background
            "   border: none;"  # No border
            "   border-radius: 0px;"  # No border-radius for the button
            "   padding: 0px;"  # No padding
            "   background-image: url(:/Images/board_button.png);"  # Use a background image with curved lines
            "}"
        )


class BoardWindow(object):
    def setupUi(self, Gobblet):
        game_instance = Game()

        QSound.play("Images/start_button_sound.wav")
        player1 = "bahaa"
        player2 = "mohamed"
        self.Gobblet = Gobblet  # Store a reference to the main window
        Gobblet.setObjectName("Gobblet")
        Gobblet.resize(1200, 900)
        Gobblet.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(Gobblet)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #D2B48C;")  # Slightly darker beige background
        self.Gobblet.setWindowIcon(QIcon(':/Images/MainLogo.png'))  # Set the window icon

        # adding board background
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(250, 100, 700, 700))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/Images/board_background.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")

        # Adding a re-start button
        self.RestartButton = QtWidgets.QPushButton(self.centralwidget)
        self.RestartButton.setGeometry(QtCore.QRect(500, 810, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Supply Center")
        font.setPointSize(13)
        font.setBold(True)
        self.RestartButton.setFont(font)
        self.RestartButton.setStyleSheet("background-color: rgb(0, 180, 0);"
                                "border: 2px solid Black;"  # Add a white border
                                "border-radius: 10px;")  # Adjust the radius for rounding
        self.RestartButton.setObjectName("RestartButton")
        self.RestartButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        #self.RestartButton.mousePressEvent = self.restart_game
        self.RestartButton.clicked.connect(lambda: self.restart_game(Gobblet))


        # adding label for player turn
        self.playerTurn = QtWidgets.QLabel(self.centralwidget)
        self.playerTurn.setGeometry(QtCore.QRect(440, 25, 330, 60))
        self.playerTurn.setAlignment(QtCore.Qt.AlignCenter)
        self.playerTurn.setStyleSheet("font: 13pt \"Supply Center\";\n"
                                        "color: #ffffff;\n"
                                        "border: 3px solid black;\n"
                                        "border-radius: 10px;\n")
        self.playerTurn.setObjectName("playerTurn")
        self.playerTurn.setText(f"{player1} Turn")

        # Player 1 Name Label
        self.Player1Name = QtWidgets.QLabel(self.centralwidget)
        self.Player1Name.setEnabled(False)
        self.Player1Name.setGeometry(QtCore.QRect(10, 200, 200, 50))
        self.Player1Name.setScaledContents(False)
        self.Player1Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Player1Name.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.Player1Name.setObjectName("Player1Name")

        # Player 2 Name Label
        self.Player2Name = QtWidgets.QLabel(self.centralwidget)
        self.Player2Name.setEnabled(False)
        self.Player2Name.setGeometry(QtCore.QRect(990, 650, 200, 50))
        self.Player2Name.setScaledContents(False)
        self.Player2Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Player2Name.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.Player2Name.setObjectName("Player2Name")

        self.Player1Name.setStyleSheet("font: 10pt \"Supply Center\";\n"
                                       "color: #ffffff;")
        self.Player2Name.setStyleSheet("font: 10pt \"Supply Center\";\n"
                                       "color: #000000;")
        # Set Players Names
        self.Player1Name.setText(player1)
        self.Player2Name.setText(player2)

        # mickey mouse hand
        self.up_finger = QtWidgets.QLabel(self.centralwidget)
        self.up_finger.setGeometry(QtCore.QRect(1040, 710, 100, 100))
        self.up_finger.setText("")
        self.up_finger.setPixmap(QtGui.QPixmap(":/Images/up_finger.png"))
        self.up_finger.setScaledContents(True)
        self.up_finger.setObjectName("label_3")
        self.down_finger = QtWidgets.QLabel(self.centralwidget)
        self.down_finger.setGeometry(QtCore.QRect(60, 90, 100, 100))
        self.down_finger.setText("")
        self.down_finger.setPixmap(QtGui.QPixmap(":/Images/down_finger.png"))
        self.down_finger.setScaledContents(True)
        self.down_finger.setObjectName("label_4")


        # Player 1 Buttons
        self.Player1_Size1_Stack1 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1_Size1_Stack1.setGeometry(QtCore.QRect(90, 310, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1_Size1_Stack1.setFont(font)
        self.Player1_Size1_Stack1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1_Size1_Stack1.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 15px;\n"
            "    background-color: #ffffff;\n"
            "    color: #000000;\n"
            "}"
        )
        self.Player1_Size1_Stack1.setObjectName("Player1_Size1_Stack1")


        self.Player1_Size2_Stack1 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1_Size2_Stack1.setGeometry(QtCore.QRect(80, 300, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1_Size2_Stack1.setFont(font)
        self.Player1_Size2_Stack1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1_Size2_Stack1.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 25px;\n"
            "    background-color: #ffffff;\n"
            "    color: 000000;\n"
            "}"
        )
        self.Player1_Size2_Stack1.setObjectName("Player1_Size2_Stack1")


        self.Player1_Size3_Stack1 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1_Size3_Stack1.setGeometry(QtCore.QRect(70, 290, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1_Size3_Stack1.setFont(font)
        self.Player1_Size3_Stack1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1_Size3_Stack1.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 35px;\n"
            "    background-color: #ffffff;\n"
            "    color: 000000;\n"
            "}"
        )
        self.Player1_Size3_Stack1.setObjectName("Player1_Size3_Stack1")


        self.Player1_Size4_Stack1 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1_Size4_Stack1.setGeometry(QtCore.QRect(60, 280, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1_Size4_Stack1.setFont(font)
        self.Player1_Size4_Stack1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1_Size4_Stack1.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 45px;\n"
            "    background-color: #ffffff;\n"
            "    color: 000000;\n"
            "}"
        )
        self.Player1_Size4_Stack1.setCheckable(False)
        self.Player1_Size4_Stack1.setObjectName("Player1_Size4_Stack1")


        self.Player1_Size1_Stack2 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1_Size1_Stack2.setGeometry(QtCore.QRect(90, 430, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1_Size1_Stack2.setFont(font)
        self.Player1_Size1_Stack2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1_Size1_Stack2.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 15px;\n"
            "    background-color: #ffffff;\n"
            "    color: 000000;\n"
            "}"
        )
        self.Player1_Size1_Stack2.setObjectName("Player1_Size1_Stack2")


        self.Player1_Size2_Stack2 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1_Size2_Stack2.setGeometry(QtCore.QRect(80, 420, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1_Size2_Stack2.setFont(font)
        self.Player1_Size2_Stack2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1_Size2_Stack2.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 25px;\n"
            "    background-color: #ffffff;\n"
            "    color: 000000;\n"
            "}"
        )
        self.Player1_Size2_Stack2.setObjectName("Player1_Size2_Stack2")


        self.Player1_Size3_Stack2 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1_Size3_Stack2.setGeometry(QtCore.QRect(70, 410, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1_Size3_Stack2.setFont(font)
        self.Player1_Size3_Stack2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1_Size3_Stack2.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 35px;\n"
            "    background-color: #ffffff;\n"
            "    color: 000000;\n"
            "}"
        )
        self.Player1_Size3_Stack2.setObjectName("Player1_Size3_Stack2")


        self.Player1_Size4_Stack2 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1_Size4_Stack2.setGeometry(QtCore.QRect(60, 400, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1_Size4_Stack2.setFont(font)
        self.Player1_Size4_Stack2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1_Size4_Stack2.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 45px;\n"
            "    background-color: #ffffff;\n"
            "    color: 000000;\n"
            "}"
        )
        self.Player1_Size4_Stack2.setObjectName("Player1_Size4_Stack2")


        self.Player1_Size1_Stack3 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1_Size1_Stack3.setGeometry(QtCore.QRect(90, 550, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1_Size1_Stack3.setFont(font)
        self.Player1_Size1_Stack3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1_Size1_Stack3.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 15px;\n"
            "    background-color: #ffffff;\n"
            "    color: 000000;\n"
            "}"
        )
        self.Player1_Size1_Stack3.setObjectName("Player1_Size1_Stack3")


        self.Player1_Size2_Stack3 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1_Size2_Stack3.setGeometry(QtCore.QRect(80, 540, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1_Size2_Stack3.setFont(font)
        self.Player1_Size2_Stack3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1_Size2_Stack3.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 25px;\n"
            "    background-color: #ffffff;\n"
            "    color: 000000;\n"
            "}"
        )
        self.Player1_Size2_Stack3.setObjectName("Player1_Size2_Stack3")


        self.Player1_Size3_Stack3 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1_Size3_Stack3.setGeometry(QtCore.QRect(70, 530, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1_Size3_Stack3.setFont(font)
        self.Player1_Size3_Stack3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1_Size3_Stack3.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 35px;\n"
            "    background-color: #ffffff;\n"
            "    color: 000000;\n"
            "}"
        )
        self.Player1_Size3_Stack3.setObjectName("Player1_Size3_Stack3")


        self.Player1_Size4_Stack3 = QtWidgets.QPushButton(self.centralwidget)
        self.Player1_Size4_Stack3.setGeometry(QtCore.QRect(60, 520, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player1_Size4_Stack3.setFont(font)
        self.Player1_Size4_Stack3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player1_Size4_Stack3.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 45px;\n"
            "    background-color: #ffffff;\n"
            "    color: 000000;\n"
            "}"
        )
        self.Player1_Size4_Stack3.setObjectName("Player1_Size4_Stack3")

        #player 2 buttons
        self.Player2_Size1_Stack1 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2_Size1_Stack1.setGeometry(QtCore.QRect(1080, 540, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2_Size1_Stack1.setFont(font)
        self.Player2_Size1_Stack1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2_Size1_Stack1.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 15px;\n"
            "    background-color: #000000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2_Size1_Stack1.setObjectName("Player2_Size1_Stack1")


        self.Player2_Size1_Stack2 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2_Size1_Stack2.setGeometry(QtCore.QRect(1080, 420, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2_Size1_Stack2.setFont(font)
        self.Player2_Size1_Stack2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2_Size1_Stack2.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 15px;\n"
            "    background-color: #000000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2_Size1_Stack2.setObjectName("Player2_Size1_Stack2")


        self.Player2_Size1_Stack3 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2_Size1_Stack3.setGeometry(QtCore.QRect(1080, 300, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2_Size1_Stack3.setFont(font)
        self.Player2_Size1_Stack3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2_Size1_Stack3.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 15px;\n"
            "    background-color: #000000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2_Size1_Stack3.setObjectName("Player2_Size1_Stack3")


        self.Player2_Size2_Stack1 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2_Size2_Stack1.setGeometry(QtCore.QRect(1070, 530, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2_Size2_Stack1.setFont(font)
        self.Player2_Size2_Stack1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2_Size2_Stack1.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 25px;\n"
            "    background-color: #000000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2_Size2_Stack1.setObjectName("Player2_Size2_Stack1")


        self.Player2_Size2_Stack2 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2_Size2_Stack2.setGeometry(QtCore.QRect(1070, 410, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2_Size2_Stack2.setFont(font)
        self.Player2_Size2_Stack2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2_Size2_Stack2.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 25px;\n"
            "    background-color: #000000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2_Size2_Stack2.setObjectName("Player2_Size2_Stack2")


        self.Player2_Size2_Stack3 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2_Size2_Stack3.setGeometry(QtCore.QRect(1070, 290, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2_Size2_Stack3.setFont(font)
        self.Player2_Size2_Stack3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2_Size2_Stack3.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 25px;\n"
            "    background-color: #000000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2_Size2_Stack3.setObjectName("Player2_Size2_Stack3")


        self.Player2_Size3_Stack1 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2_Size3_Stack1.setGeometry(QtCore.QRect(1060, 520, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2_Size3_Stack1.setFont(font)
        self.Player2_Size3_Stack1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2_Size3_Stack1.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 35px;\n"
            "    background-color: #000000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2_Size3_Stack1.setObjectName("Player2_Size3_Stack1")


        self.Player2_Size3_Stack2 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2_Size3_Stack2.setGeometry(QtCore.QRect(1060, 400, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2_Size3_Stack2.setFont(font)
        self.Player2_Size3_Stack2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2_Size3_Stack2.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 35px;\n"
            "    background-color: #000000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2_Size3_Stack2.setObjectName("Player2_Size3_Stack2")


        self.Player2_Size3_Stack3 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2_Size3_Stack3.setGeometry(QtCore.QRect(1060, 280, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2_Size3_Stack3.setFont(font)
        self.Player2_Size3_Stack3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2_Size3_Stack3.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 35px;\n"
            "    background-color: #000000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2_Size3_Stack3.setObjectName("Player2_Size3_Stack3")


        self.Player2_Size4_Stack1 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2_Size4_Stack1.setGeometry(QtCore.QRect(1050, 510, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2_Size4_Stack1.setFont(font)
        self.Player2_Size4_Stack1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2_Size4_Stack1.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 45px;\n"
            "    background-color: #000000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2_Size4_Stack1.setObjectName("Player2_Size4_Stack1")


        self.Player2_Size4_Stack2 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2_Size4_Stack2.setGeometry(QtCore.QRect(1050, 270, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2_Size4_Stack2.setFont(font)
        self.Player2_Size4_Stack2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2_Size4_Stack2.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 45px;\n"
            "    background-color: #000000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2_Size4_Stack2.setObjectName("Player2_Size4_Stack2")


        self.Player2_Size4_Stack3 = QtWidgets.QPushButton(self.centralwidget)
        self.Player2_Size4_Stack3.setGeometry(QtCore.QRect(1050, 390, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Player2_Size4_Stack3.setFont(font)
        self.Player2_Size4_Stack3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Player2_Size4_Stack3.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 45px;\n"
            "    background-color: #000000;\n"
            "    color: #ffffff;\n"
            "}"
        )
        self.Player2_Size4_Stack3.setObjectName("Player2_Size4_Stack3")

        
        # Board Buttons 
        # self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        # self.Button1.setGeometry(QtCore.QRect(250, 90, 150, 150))
        # self.Button1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.Button1.setText("")
        # self.Button1.setObjectName("Button1")
        self.Button1 = boardCurvedButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(300, 140, 150, 150))
        self.Button1.setText("")
        self.Button1.setObjectName("Button1")
        self.Button2 = boardCurvedButton(self.centralwidget)
        self.Button2.setGeometry(QtCore.QRect(450, 140, 150, 150))
        self.Button2.setText("")
        self.Button2.setObjectName("Button2")
        self.Button3 = boardCurvedButton(self.centralwidget)
        self.Button3.setGeometry(QtCore.QRect(600, 140, 150, 150))
        self.Button3.setText("")
        self.Button3.setObjectName("Button3")
        self.Button4 = boardCurvedButton(self.centralwidget)
        self.Button4.setGeometry(QtCore.QRect(750, 140, 150, 150))
        self.Button4.setText("")
        self.Button4.setObjectName("Button4")
        self.Button5 = boardCurvedButton(self.centralwidget)
        self.Button5.setGeometry(QtCore.QRect(300, 290, 150, 150))
        self.Button5.setText("")
        self.Button5.setObjectName("Button5")
        self.Button6 = boardCurvedButton(self.centralwidget)
        self.Button6.setGeometry(QtCore.QRect(450, 290, 150, 150))
        self.Button6.setText("")
        self.Button6.setObjectName("Button6")
        self.Button7 = boardCurvedButton(self.centralwidget)
        self.Button7.setGeometry(QtCore.QRect(600, 290, 150, 150))
        self.Button7.setText("")
        self.Button7.setObjectName("Button7")
        self.Button8 = boardCurvedButton(self.centralwidget)
        self.Button8.setGeometry(QtCore.QRect(750, 290, 150, 150))
        self.Button8.setText("")
        self.Button8.setObjectName("Button8")
        self.Button9 = boardCurvedButton(self.centralwidget)
        self.Button9.setGeometry(QtCore.QRect(300, 440, 150, 150))
        self.Button9.setText("")
        self.Button9.setObjectName("Button9")
        self.Button10 = boardCurvedButton(self.centralwidget)
        self.Button10.setGeometry(QtCore.QRect(450, 440, 150, 150))

        self.Button10.setText("")
        self.Button10.setObjectName("Button10")
        self.Button11 = boardCurvedButton(self.centralwidget)
        self.Button11.setGeometry(QtCore.QRect(600, 440, 150, 150))

        self.Button11.setText("")
        self.Button11.setObjectName("Button11")
        self.Button12 = boardCurvedButton(self.centralwidget)
        self.Button12.setGeometry(QtCore.QRect(750, 440, 150, 150))

        self.Button12.setText("")
        self.Button12.setObjectName("Button12")
        self.Button13 = boardCurvedButton(self.centralwidget)
        self.Button13.setGeometry(QtCore.QRect(300, 590, 150, 150))

        self.Button13.setText("")
        self.Button13.setObjectName("Button13")
        self.Button14 = boardCurvedButton(self.centralwidget)
        self.Button14.setGeometry(QtCore.QRect(450, 590, 150, 150))

        self.Button14.setText("")
        self.Button14.setObjectName("Button14")
        self.Button15 = boardCurvedButton(self.centralwidget)
        self.Button15.setGeometry(QtCore.QRect(600, 590, 150, 150))

        self.Button15.setText("")
        self.Button15.setObjectName("Button15")
        self.Button16 = boardCurvedButton(self.centralwidget)
        self.Button16.setGeometry(QtCore.QRect(750, 590, 150, 150))

        self.Button16.setText("")
        self.Button16.setObjectName("Button16")


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
        # Player1_WhiteButtons = [self.Player1_Size4_Stack1, self.Player1_Size4_Stack2, self.Player1_Size4_Stack3,
        #                         self.Player1_Size3_Stack1, self.Player1_Size3_Stack2, self.Player1_Size3_Stack3,
        #                         self.Player1_Size2_Stack1, self.Player1_Size2_Stack2, self.Player1_Size2_Stack3,
        #                         self.Player1_Size1_Stack1, self.Player1_Size1_Stack2, self.Player1_Size1_Stack3]
        Player1_WhiteButtons= [
                self.Player1_Size4_Stack1, self.Player1_Size3_Stack1, self.Player1_Size2_Stack1, self.Player1_Size1_Stack1,
                self.Player1_Size4_Stack2, self.Player1_Size3_Stack2, self.Player1_Size2_Stack2, self.Player1_Size1_Stack2,
                self.Player1_Size4_Stack3, self.Player1_Size3_Stack3, self.Player1_Size2_Stack3, self.Player1_Size1_Stack3]
        # Set Player 2 Buttons
        # Player2_BlackButtons = [self.Player2_Size4_Stack1, self.Player2_Size4_Stack2, self.Player2_Size4_Stack3,
        #                         self.Player2_Size3_Stack1, self.Player2_Size3_Stack2, self.Player2_Size3_Stack3,
        #                         self.Player2_Size2_Stack1, self.Player2_Size2_Stack2, self.Player2_Size2_Stack3,
        #                         self.Player2_Size1_Stack1, self.Player2_Size1_Stack2, self.Player2_Size1_Stack3]
        
        Player2_BlackButtons = [ 
                self.Player2_Size4_Stack1 , self.Player2_Size3_Stack1 , self.Player2_Size2_Stack1 , self.Player2_Size1_Stack1 ,
                self.Player2_Size4_Stack2 , self.Player2_Size3_Stack2 , self.Player2_Size2_Stack2 , self.Player2_Size1_Stack2 ,
                self.Player2_Size4_Stack3 , self.Player2_Size3_Stack3 , self.Player2_Size2_Stack3 , self.Player2_Size1_Stack3]
        
        
        # Set Board Buttons
        boardButtons = [self.Button1, self.Button2, self.Button3, self.Button4,
                        self.Button5, self.Button6, self.Button7, self.Button8,
                        self.Button9, self.Button10, self.Button11, self.Button12,
                        self.Button13, self.Button14, self.Button15, self.Button16]
        
        # Varaiable to indicate player round 
        playerRound = "player1"

        self.startGame(self, Player1_WhiteButtons, Player2_BlackButtons, boardButtons,playerRound,player1,player2,game_instance)
    
        self.down_finger.show()
        self.up_finger.hide()
    

    def restart_game(self,main_window):
        # Create a new instance of the BoardWindow
        new_window = BoardWindow()
        new_window.setupUi(QtWidgets.QMainWindow(), self.Player1Name.text(), self.Player2Name.text())
        new_window.Gobblet.show()
        # Close the current window
        main_window.close()
        # # Create and show the BoardWindow
        #self.board_window = QtWidgets.QMainWindow()
        #ui = Ui_MainWindow()
        #ui.setupUi(self.board_window)
        #self.board_window.show() 
        #main_entry_point() 
        
    def startGame(self, event, Player1_WhiteButtons, Player2_BlackButtons, boardButtons,playerRound,player1,player2,games_instance):
        for btn in boardButtons:
                btn.setEnabled(False)
        #         btn.setStyleSheet(
        # "QPushButton {\n"
        # "background-color: rgba(0, 0, 0, 10%);\n"  # 50% transparency (adjust as needed)
        # "border: 1px solid black;\n"
        # "}") 
        
        # Enable buttons based on the current player's round and set their event handler
        if(playerRound == "player1"):
                for btn in Player1_WhiteButtons:
                        btn.setEnabled(True)
                for btn in Player2_BlackButtons:
                        btn.setEnabled(False)
                for btn in Player1_WhiteButtons:
                        btn.mousePressEvent = lambda event, button=btn: self.handleButtonPress(event, button, Player1_WhiteButtons, Player2_BlackButtons, boardButtons, playerRound,player1,player2,games_instance)

        elif(playerRound == "player2"):
                for btn in Player2_BlackButtons:
                        btn.setEnabled(True)
                for btn in Player1_WhiteButtons:
                        btn.setEnabled(False)
                for btn in Player2_BlackButtons:
                        btn.mousePressEvent = lambda event, button=btn: self.handleButtonPress(event, button, Player1_WhiteButtons, Player2_BlackButtons, boardButtons, playerRound,player1,player2, games_instance)
        
                
    def handleButtonPress(self, event, button, Player1_WhiteButtons, Player2_BlackButtons, boardButtons, playerRound,player1,player2,games_instance):
        # Enable the clicked button
        for btn in boardButtons:
            btn.setEnabled(True)
            btn.raise_()
            btn.setStyleSheet(
        "QPushButton {"
            "   background-color: transparent;"  # Set a transparent background
            "   border: none;"  # No border
            "   border-radius: 0px;"  # No border-radius for the button
            "   padding: 0px;"  # No padding
            "   background-image: url(:/Images/board_button_transparent.png);"  # Use a background image with curved lines
            "}"
            "QPushButton:hover {"
            "   background-image: url(:/Images/board_button_hover_transparent.png);"  # Use a different image on hover
            "}"
            )
            
        self.background.lower()
            
        # Disable buttons for both players    
        for btn in Player1_WhiteButtons:
            btn.setEnabled(False)
        

        for btn in Player2_BlackButtons:
            btn.setEnabled(False)
        
        for btn in boardButtons:
            btn.mousePressEvent = lambda event, board_button=btn: self.placeButton(event, board_button, Player1_WhiteButtons, Player2_BlackButtons, boardButtons, button, playerRound,player1,player2,games_instance)


    def is_collision(self,board_button, btn, pressedbutton):
        rect1 = board_button.geometry()
        rect2 = btn.geometry()
        # return rect1.intersects(rect2)
        if(rect1.intersects(rect2)):
                if(btn.width() < pressedbutton.width()):
                        return False
                else:
                       return True

    def placeButton(self, event, board_button, Player1_WhiteButtons, Player2_BlackButtons, boardButtons, button, playerRound,player1,player2,games_instance):

         #Check for collisions with other buttons on the board
        for btn in Player1_WhiteButtons + Player2_BlackButtons:
            if self.is_collision(board_button, btn, button):
                return  # Do not place the button if there is a collision

        if(playerRound == "player1"):
            games_instance.make_move(games_instance.FirstPlayerGobbletsArray[Player1_WhiteButtons.index(button)], games_instance.BoardItemsArray[boardButtons.index(board_button)])
        elif(playerRound == "player2"):
            games_instance.make_move(games_instance.SecondPlayerGobbletsArray[Player2_BlackButtons.index(button)], games_instance.BoardItemsArray[boardButtons.index(board_button)])
        # Place the button on the board
        # for btn in boardButtons:
        #        btn.lower()
        # self.background.lower()
        #        btn.setStyleSheet(
        # "QPushButton {\n"
        # "background-color: rgba(0, 0, 0, 10%);\n"  # 50% transparency (adjust as needed)
        # "border: 1px solid black;\n"
        # "}")
        # print(Player1_WhiteButtons.index(button))
        # print(boardButtons.index(board_button))
        
        # Set the position of the button on the board
        buttonWidth = button.width()
        buttonHeight = button.height()
        boardX = board_button.x()
        boardY = board_button.y()
        # board_button.setParent(button)
        button.setGeometry(QtCore.QRect(boardX + int(board_button.width()/2) - int(buttonWidth/2),
                                         boardY+int(board_button.width()/2) - int(buttonHeight/2),
                                           buttonWidth, buttonHeight))
        ################################################################################################################################
        # board_button.setStyleSheet(
        # "QPushButton {\n"
        # "background-color: rgba(0, 0, 0, 10%);\n"  # 50% transparency (adjust as needed)
        # "border: 1px solid black;\n"
        # "}")
        
        # Lower other buttons based on their sizes
        for btn in Player1_WhiteButtons + Player2_BlackButtons:
                if(btn.width() == 90):
                        btn.lower()

        for btn in Player1_WhiteButtons + Player2_BlackButtons:
                if(btn.width() == 70):
                        btn.lower()
        
        for btn in Player1_WhiteButtons + Player2_BlackButtons:
                if(btn.width() == 50):
                        btn.lower()
        
        for btn in Player1_WhiteButtons + Player2_BlackButtons:
                if(btn.width() == 30):
                        btn.lower()
        
        
        # Disable all buttons on the board
        for btn in boardButtons:
               btn.lower()
               btn.setStyleSheet(
                      "QPushButton {"
            "   background-color: transparent;"  # Set a transparent background
            "   border: none;"  # No border
            "   border-radius: 0px;"  # No border-radius for the button
            "   padding: 0px;"  # No padding
            "   background-image: url(:/Images/board_button.png);"  # Use a background image with curved lines
            "}"
               )
        
        self.background.lower()
        #        btn.setStyleSheet(
        # "QPushButton {\n"
        # "background-color: rgba(0, 0, 0, 10%);\n"  # 50% transparency (adjust as needed)
        # "border: 1px solid black;\n"
        # "}")
               

        for btn in boardButtons:
            btn.setEnabled(False)

        # Switch player turns and update button visibility
        if(playerRound == "player1"):
                QSound.play("Images/mario-jump-sound-effect.wav")
                self.down_finger.hide()
                self.up_finger.show()
                playerRound = "player2"
                self.playerTurn.setText(f"{player2} Turn")
                self.playerTurn.setStyleSheet("font: 13pt \"Supply Center\";\n"
                                        "color: #000000;\n"
                                        "border: 3px solid black;\n"
                                        "border-radius: 10px;\n")
                for btn in Player1_WhiteButtons:
                        btn.setEnabled(False)
                for btn in Player2_BlackButtons:
                        btn.setEnabled(True)
                for btn in Player2_BlackButtons:
                        btn.mousePressEvent = lambda event, button=btn: self.handleButtonPress(event, button, Player1_WhiteButtons, Player2_BlackButtons, boardButtons, playerRound,player1,player2, games_instance)
                
        elif(playerRound == "player2"):
                QSound.play("Images/mario-jump-sound-effect.wav")
                self.up_finger.hide()
                self.down_finger.show()
                playerRound = "player1"
                self.playerTurn.setText(f"{player1} Turn")
                self.playerTurn.setStyleSheet("font: 13pt \"Supply Center\";\n"
                                        "color: #ffffff;\n"
                                        "border: 3px solid black;\n"
                                        "border-radius: 10px;\n")
                for btn in Player2_BlackButtons:
                        btn.setEnabled(False)
                for btn in Player1_WhiteButtons:
                        btn.setEnabled(True)
                for btn in Player1_WhiteButtons:
                        btn.mousePressEvent = lambda event, button=btn: self.handleButtonPress(event, button, Player1_WhiteButtons, Player2_BlackButtons, boardButtons, playerRound,player1,player2, games_instance)

    def retranslateUi(self, Gobblet):
        _translate = QtCore.QCoreApplication.translate
        Gobblet.setWindowTitle(_translate("Gobblet", "Gobblet"))
        self.Player1_Size1_Stack1.setText(_translate("Gobblet", "1"))
        self.Player1_Size2_Stack1.setText(_translate("Gobblet", "2"))
        self.Player1_Size3_Stack1.setText(_translate("Gobblet", "3"))
        self.Player1_Size4_Stack1.setText(_translate("Gobblet", "4"))
        self.Player1_Size1_Stack2.setText(_translate("Gobblet", "1"))
        self.Player1_Size2_Stack2.setText(_translate("Gobblet", "2"))
        self.Player1_Size3_Stack2.setText(_translate("Gobblet", "3"))
        self.Player1_Size4_Stack2.setText(_translate("Gobblet", "4"))
        self.Player1_Size1_Stack3.setText(_translate("Gobblet", "1"))
        self.Player1_Size2_Stack3.setText(_translate("Gobblet", "2"))
        self.Player1_Size3_Stack3.setText(_translate("Gobblet", "3"))
        self.Player1_Size4_Stack3.setText(_translate("Gobblet", "4"))
        self.Player2_Size1_Stack1.setText(_translate("Gobblet", "1"))
        self.Player2_Size1_Stack2.setText(_translate("Gobblet", "1"))
        self.Player2_Size1_Stack3.setText(_translate("Gobblet", "1"))
        self.Player2_Size2_Stack1.setText(_translate("Gobblet", "2"))
        self.Player2_Size2_Stack2.setText(_translate("Gobblet", "2"))
        self.Player2_Size2_Stack3.setText(_translate("Gobblet", "2"))
        self.Player2_Size3_Stack1.setText(_translate("Gobblet", "3"))
        self.Player2_Size3_Stack2.setText(_translate("Gobblet", "3"))
        self.Player2_Size3_Stack3.setText(_translate("Gobblet", "3"))
        self.Player2_Size4_Stack1.setText(_translate("Gobblet", "4"))
        self.Player2_Size4_Stack2.setText(_translate("Gobblet", "4"))
        self.Player2_Size4_Stack3.setText(_translate("Gobblet", "4"))
        self.RestartButton.setText(_translate("Gobblet", "Restart"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Gobblet = QtWidgets.QMainWindow()
    ui = BoardWindow()
    ui.setupUi(Gobblet)
    Gobblet.show()
    sys.exit(app.exec_())

