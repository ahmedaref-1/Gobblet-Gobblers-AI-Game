from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
# Importing image resources
import Images
from board import BoardWindow



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Setting up the main window properties
        self.MainWindow = MainWindow  # Store MainWindow as an instance variable
        MainWindow.setObjectName("Gobblet")
        MainWindow.resize(1083, 838)
        MainWindow.setStyleSheet("background-color: #D2B48C;")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.MainWindow.setWindowIcon(QIcon(':/Images/MainLogo.png'))  # Set the window icon

        # Setting up the game mode
        mode = ""

        # Set board window to None
        self.board_window = None

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
        self.PVPImage.setGeometry(QtCore.QRect(80, 170, 221, 151))
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
        # Player 1 Name
        self.Player1Name = QtWidgets.QTextEdit(self.centralwidget)
        self.Player1Name.setGeometry(QtCore.QRect(490, 310, 231, 30))
        self.Player1Name.setStyleSheet("font: 10pt \"Supply Center\";\n"
                                       "color: #ffffff;"
                                       "border: none;"
                                       "background-color: #DEC29D;"
                                       "border-radius: 10px;")
        self.Player1Name.setObjectName("Player1Name")
        self.Player1Name.setPlaceholderText("Player 1 Name")  # Set the placeholder text
        self.Player1Name.hide()

        # Player 2 Name
        self.Player2Name = QtWidgets.QTextEdit(self.centralwidget)
        self.Player2Name.setGeometry(QtCore.QRect(730, 310, 231, 30))
        self.Player2Name.setStyleSheet("font: 10pt \"Supply Center\";\n"
                                       "color: #000000;"
                                       "border: none;"
                                       "background-color: #DEC29D;"
                                       "border-radius: 10px;"
                                       "alignment: center;")
        self.Player2Name.setObjectName("Player2Name")
        self.Player2Name.setPlaceholderText("Player 1 Name")  # Set the placeholder text
        self.Player2Name.hide()


        # Adding a start button
        # Start Button
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(590, 510, 291, 81))
        font = QtGui.QFont()
        font.setFamily("Supply Center")
        font.setPointSize(16)
        font.setBold(True)
        self.StartButton.setFont(font)
        self.StartButton.setStyleSheet("background-color: rgb(0, 180, 0);"
                                "border: 5px solid black;"  # Add a white border
                                "border-radius: 40px;")  # Adjust the radius for rounding
        self.StartButton.setObjectName("StartButton")
        self.StartButton.hide()
        self.StartButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


        #Adding Diffculty lables and List
        # Adding a label for the list view 
        self.difficultyLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.difficultyLabel1.setGeometry(QtCore.QRect(730, 310, 231, 30))
        self.difficultyLabel1.setStyleSheet("font: 10pt \"Supply Center\";\n"
                                           "color: #000000;"
                                           "border: none;"
                                           "background-color: #DEC29D;"
                                           "border-radius: 10px;")
        self.difficultyLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.difficultyLabel1.setText("Computer Level")
        # Hide lable 1
        self.difficultyLabel1.hide()

        # Difficulty List 1
        self.difficultyListWidget1 = QtWidgets.QListWidget(self.centralwidget)
        self.difficultyListWidget1.setGeometry(QtCore.QRect(730, 350, 231, 90))
        
        # Adding items to the QListWidget
        self.difficultyListWidget1.addItems(['EASY', 'MEDIUM', 'HARD'])
        
        # Set text style to be the same as the label
        self.difficultyListWidget1.setStyleSheet("font: 10pt \"Supply Center\";\n"
                                          "color: #FFFF36  ;"
                                          "border: none;")
        # Set Item color
        self.difficultyListWidget1.item(0).setForeground(QtGui.QColor("#4CAF50"))
        self.difficultyListWidget1.item(1).setForeground(QtGui.QColor("#FF9800"))
        self.difficultyListWidget1.item(2).setForeground(QtGui.QColor("#D32F2F"))

        # Prevent text from being changed in the list widget
        self.difficultyListWidget1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # Hide it
        self.difficultyListWidget1.hide()

        # Adding a label for the list view
        self.difficultyLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.difficultyLabel2.setGeometry(QtCore.QRect(490, 310, 231, 30))
        self.difficultyLabel2.setStyleSheet("font: 10pt \"Supply Center\";\n"
                                           "color: #ffffff;"
                                           "border: none;"
                                           "background-color: #DEC29D;"
                                           "border-radius: 10px;")
        self.difficultyLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.difficultyLabel2.setText("Computer Level")
        self.difficultyLabel2.hide()
        
        # Difficulty List 2
        self.difficultyListWidget2 = QtWidgets.QListWidget(self.centralwidget)
        self.difficultyListWidget2.setGeometry(QtCore.QRect(490, 350, 231, 90))
        
        # Adding items to the QListWidget
        self.difficultyListWidget2.addItems(['EASY', 'MEDIUM', 'HARD'])

        
        # Set text style to be the same as the label
        self.difficultyListWidget2.setStyleSheet("font: 10pt \"Supply Center\";\n"
                                      "color: #00FF36  ;"
                                      "border: none;")

        # Set Item color
        self.difficultyListWidget2.item(0).setForeground(QtGui.QColor("#4CAF50"))
        self.difficultyListWidget2.item(1).setForeground(QtGui.QColor("#FF9800"))
        self.difficultyListWidget2.item(2).setForeground(QtGui.QColor("#D32F2F"))
        # Prevent text from being changed in the list view
        self.difficultyListWidget2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Hide it
        self.difficultyListWidget2.hide()

        # Connect itemClicked signals to a method that checks for selections
        self.difficultyListWidget1.itemClicked.connect(self.checkSelectionPVC)
        self.difficultyListWidget2.itemClicked.connect(self.checkSelectionCVC)

        # Connecting mouse press events to show player names and start button
        self.PVPImage.mousePressEvent = lambda event : self.showPlayersNames(event)
        self.PVCImage.mousePressEvent = lambda event : self.showPlayerName(event)
        self.CVCImage.mousePressEvent = lambda event : self.showComputerName(event)
        self.StartButton.mousePressEvent = lambda event : self.showBoardWindow(event)

        # Setting the central widget for the main window
        MainWindow.setCentralWidget(self.centralwidget)

        # Translating user interface texts
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
     
    # Methods for showing and hiding player names and start button 
    def showPlayersNames(self, event):
        # Show player names and start button when PVP label is clicked
        # Hide everything first
        self.Player1Name.hide()
        self.Player2Name.hide()
        self.StartButton.hide()
        self.difficultyListWidget1.hide()
        self.difficultyLabel1.hide()
        self.difficultyListWidget2.hide()
        self.difficultyLabel2.hide()
        self.Player1Name.setText("")
        self.Player2Name.setText("")
         
        # Show player names and start button 
        self.mode = "PVP" 
        self.Player1Name.show()
        self.Player2Name.show() 
        self.StartButton.show()
        

    def showPlayerName(self, event):
        # Show player names and start button when PVC label is clicked
        # Hide everything first
        self.Player1Name.hide()
        self.Player2Name.hide()
        self.StartButton.hide()
        self.difficultyListWidget1.hide()
        self.difficultyLabel1.hide()
        self.difficultyListWidget2.hide()
        self.difficultyLabel2.hide()
        self.Player1Name.setText("")
        self.Player2Name.setText("Computer")


        # Show player names and start button
        self.mode = "PVC"
        self.Player1Name.show()
        self.difficultyListWidget1.show()
        self.difficultyLabel1.show()

    def showComputerName(self, event):
        # Show start button when CVC label is clicked
        # Adding a label for the list view
        self.Player1Name.hide()
        self.Player2Name.hide()
        self.StartButton.hide()
        self.difficultyListWidget1.hide()
        self.difficultyLabel1.hide()
        self.difficultyListWidget2.hide()
        self.difficultyLabel2.hide()
        self.Player1Name.setText("Computer1")
        self.Player2Name.setText("Computer2")
   
        # Show player names and start button
        self.mode = "CVC" 
        self.difficultyListWidget1.show()
        self.difficultyLabel1.show()
        self.difficultyListWidget2.show()
        self.difficultyLabel2.show()


    def checkSelectionCVC(self):
        # Check if an item is selected in both list widgets
        if self.difficultyListWidget1.currentItem() is not None and self.difficultyListWidget2.currentItem() is not None:
            self.StartButton.show()
        else:
            self.StartButton.hide()

    def checkSelectionPVC(self):
        # Check if an item is selected in both list widgets
        if self.difficultyListWidget1.currentItem() is not None:
            self.StartButton.show()
        else:
            self.StartButton.hide()        

    # Show the board window
    def showBoardWindow(self, event):
         if self.board_window is None or not self.board_window.isVisible():
            # Create and show the BoardWindow
            self.board_window = QtWidgets.QMainWindow()
            ui = BoardWindow()

            if self.difficultyListWidget1.currentItem() is not None and self.difficultyListWidget2.currentItem() is None:
                difficulty2 = self.difficultyListWidget1.currentItem().text()
                ui.setupUi(self.board_window, self.Player1Name.toPlainText(), self.Player2Name.toPlainText(),self.mode,"",difficulty2)
            
            elif self.difficultyListWidget1.currentItem() is not None and self.difficultyListWidget2.currentItem() is not None:
                difficulty2 = self.difficultyListWidget1.currentItem().text()
                difficulty1 = self.difficultyListWidget2.currentItem().text()
                ui.setupUi(self.board_window, self.Player1Name.toPlainText(), self.Player2Name.toPlainText(),self.mode,difficulty1,difficulty2)
            
            else : 
                ui.setupUi(self.board_window, self.Player1Name.toPlainText(), self.Player2Name.toPlainText(),self.mode,"","")
                
            self.board_window.show()
            self.MainWindow.close()    

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
                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.Player2Name.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                "p, li { white-space: pre-wrap; }\n"
                                "hr { height: 1px; border-width: 0; }\n"
                                "li.unchecked::marker { content: \"\\2610\"; }\n"
                                "li.checked::marker { content: \"\\2612\"; }\n"
                                "</style></head><body style=\" font-family:\'Supply Center\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.StartButton.setText(_translate("MainWindow", "Start"))


def main_entry_point():
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# Application entry point
if __name__ == "__main__":
    import sys
    main_entry_point()
