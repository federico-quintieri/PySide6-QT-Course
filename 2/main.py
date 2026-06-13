# Importo il modulo sys per accedere agli argomenti passati da riga di comando
import sys

# Importo le classi Qt necessarie:
# QApplication = gestisce l'intera applicazione GUI
# QWidget = finestra/widget base di Qt
from PySide6.QtWidgets import QApplication, QWidget

# Creo l'oggetto applicazione.
# Deve esistere una sola QApplication per processo.
# sys.argv permette a Qt di leggere eventuali parametri passati da terminale.
app = QApplication(sys.argv)


# Creo una finestra vuota.
# QWidget è il widget base da cui derivano quasi tutti i controlli Qt.
window = QWidget()

# Rende visibile la finestra.
# Senza questa chiamata la finestra esiste ma rimane nascosta.
window.show()


# Avvia l'event loop di Qt.
# Da questo momento il programma resta in attesa di eventi:
# - click del mouse
# - pressione tasti
# - ridimensionamento finestra
# - timer
# - segnali dei widget
#
# Quando l'utente chiude l'applicazione,
# app.exec() termina e il programma si chiude.
app.exec()
