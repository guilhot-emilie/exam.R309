from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QLabel, QLineEdit, QPushButton
import sys
import socket

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)


        lab = QLabel("Serveur")
        lab2 = QLabel("Port")
        lab3 = QLabel("Message :")
        textserv = QLineEdit("")
        textport = QLineEdit("")
        textmess = QLineEdit("")
        envoyer = QPushButton("Envoyer")
        connexion = QPushButton("Connexion")
        effacer = QPushButton("Effacer")
        quitter = QPushButton("Quitter")
        text = QLineEdit("")


        # Constructeur
        self.__lab = lab
        self.__text = text
        self.__lab2 = lab2
        self.__lab3 = lab3
        self.__textmess = textmess
        self.__textserv = textserv
        self.__textport = textport
        self.__envoyer = envoyer
        self.__connexion = connexion
        self.__effacer = effacer
        self.__quitter= quitter

        # Affichage
        grid.addWidget(self.__lab, 0, 0)
        grid.addWidget(self.__lab2, 1, 0)
        grid.addWidget(self.__textserv, 0, 1)
        grid.addWidget(self.__textport, 1, 1)
        grid.addWidget(self.__envoyer, 5, 1)
        grid.addWidget(self.__connexion, 2, 1)
        grid.addWidget(self.__text, 3, 1)
        grid.addWidget(self.__lab3, 4, 0)
        grid.addWidget(self.__textmess, 4, 1)
        grid.addWidget(self.__effacer, 6, 0)
        grid.addWidget(self.__quitter, 6, 1)


        connexion.clicked.connect(self._actionconn)
        #envoyer.clicked.connect(self._actionmess())
        #quitter.clicked.connect(self._actionQuitter)
        self.setWindowTitle("Un logiciel de tchat")

    #def _actionQuitter(self):
    #    QCoreApplication.exit(0)


    def _actionconn(self):
        host = self.__textserv
        port = self.__textport
        print(host, port)
        client_socket = socket.socket()
        client_socket.connect(())

    #def _actionmess(self):
    #    a = self.__textmess
    #    socket.socket().send(a.encode())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
