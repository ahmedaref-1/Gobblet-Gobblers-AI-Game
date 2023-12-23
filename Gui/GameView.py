from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
# Importing image resources
import Images
from board import BoardWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Setting up the main window properties
        MainWindow.setObjectName("Gobblet")
        MainWindow.resize(1083, 838)
        MainWindow.setStyleSheet("background-color:rgb(255, 255, 255)")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)


        # Creating the central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Adding a logo image label
        self.gameLogo = QtWidgets.QLabel(self.centralwidget)
        self.gameLogo.setGeometry(QtCore.QRect(390, 60, 361, 191))
        self.gameLogo.setText("")
        self.gameLogo.setPixmap(QtGui.QPixmap(":/Images/Logo.png"))
        self.gameLogo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gameLogo.setObjectName("gameLogo")

        # Adding labels for different game modes with images
        # Player versus Player Mode
        self.PVPImage = QtWidgets.QLabel(self.centralwidget)
        self.PVPImage.setGeometry(QtCore.QRect(60, 170, 221, 151))
        self.PVPImage.setStyleSheet("image: url(:/Images/PVP.png);")
        self.PVPImage.setText("")
        self.PVPImage.setObjectName("PVPImage")
        self.PVPImage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # Player Versus Computer Mode
        self.PVCImage = QtWidgets.QLabel(self.centralwidget)
        self.PVCImage.setGeometry(QtCore.QRect(90, 350, 231, 151))
        self.PVCImage.setStyleSheet("image: url(:/Images/PVC.png);")
        self.PVCImage.setText("")
        self.PVCImage.setObjectName("PVCImage")
        self.PVCImage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # Computer Versus Computer Mode
        self.CVCImage = QtWidgets.QLabel(self.centralwidget)
        self.CVCImage.setGeometry(QtCore.QRect(30, 510, 301, 231))
        self.CVCImage.setStyleSheet("image: url(:/Images/CVC.png);")
        self.CVCImage.setText("")
        self.CVCImage.setObjectName("CVCImage")
        self.CVCImage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # Adding text edits for player names
        self.Player1Name = QtWidgets.QTextEdit(self.centralwidget)
        self.Player1Name.setGeometry(QtCore.QRect(490, 310, 231, 41))
        self.Player1Name.setStyleSheet("font: 10pt \"Supply Center\";\n"
                                       "color: rgb(0, 0, 255);")
        self.Player1Name.setObjectName("Player1Name")
        self.Player1Name.hide()

        self.Player2Name = QtWidgets.QTextEdit(self.centralwidget)
        self.Player2Name.setGeometry(QtCore.QRect(730, 310, 231, 41))
        self.Player2Name.setStyleSheet("font: 10pt \"Supply Center\";\n"
                                       "color: rgb(255, 0, 0);")
        self.Player2Name.setObjectName("Player2Name")
        self.Player2Name.hide()


        # Adding a start button
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(590, 510, 291, 81))
        font = QtGui.QFont()
        font.setFamily("Supply Center")
        font.setPointSize(16)
        font.setBold(True)
        self.StartButton.setFont(font)
        self.StartButton.setStyleSheet("background-color: rgb(0, 220, 0);")
        self.StartButton.setObjectName("StartButton")
        self.StartButton.hide()
        self.StartButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


        # Connecting mouse press events to show player names and start button
        self.PVPImage.mousePressEvent = self.showPlayersNames
        self.PVCImage.mousePressEvent = self.showPlayerName
        self.CVCImage.mousePressEvent = self.showComputerName
        self.StartButton.mousePressEvent = self.showBoardWindow

        # Set board window to None
        self.board_window = None

        # Setting the central widget for the main window
        MainWindow.setCentralWidget(self.centralwidget)

        # Translating user interface texts
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
     
    def showPlayersNames(self, event):
        # Show player names and start button when PVP label is clicked
        self.Player1Name.show()
        self.Player2Name.show()   
        self.StartButton.show()

    def showPlayerName(self, event):
        # Show player names and start button when PVC label is clicked
        self.Player1Name.show()
        self.Player2Name.setText("Computer")
        self.StartButton.show()

    def showComputerName(self, event):
        # Show start button when CVC label is clicked
        self.Player1Name.setText("Computer-1")
        self.Player2Name.setText("Computer-2")
        self.StartButton.show()

    def showBoardWindow(self, event):
         if self.board_window is None or not self.board_window.isVisible():
            # Create and show the BoardWindow
            self.board_window = QtWidgets.QMainWindow()
            ui = BoardWindow()
            ui.setupUi(self.board_window, self.Player1Name.toPlainText(), self.Player2Name.toPlainText())
            self.board_window.show()
            MainWindow.close()    

    def retranslateUi(self, MainWindow):
        # Translating window title and setting initial text for player names
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gobblet"))
        self.Player1Name.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                "p, li { white-space: pre-wrap; }\n"
                                "hr { height: 1px; border-width: 0; }\n"
                                "li.unchecked::marker { content: \"\\2610\"; }\n"
                                "li.checked::marker { content: \"\\2612\"; }\n"
                                "</style></head><body style=\" font-family:\'Supply Center\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Player 1 NAME</p></body></html>"))
        self.Player2Name.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                "p, li { white-space: pre-wrap; }\n"
                                "hr { height: 1px; border-width: 0; }\n"
                                "li.unchecked::marker { content: \"\\2610\"; }\n"
                                "li.checked::marker { content: \"\\2612\"; }\n"
                                "</style></head><body style=\" font-family:\'Supply Center\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Player 1 NAME</p></body></html>"))
        self.StartButton.setText(_translate("MainWindow", "Start"))


# Application entry point
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
