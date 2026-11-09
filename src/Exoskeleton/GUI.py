from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices

from .PianoRoll import PianoRoll


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("VelvetAnt")

        self.init_menubar()

        pianoRoll = PianoRoll(self)
        self.setCentralWidget(pianoRoll)


    def init_menubar(self):
        menuBar = self.menuBar()

        # File
        fileM = menuBar.addMenu('File')
        fileM.addAction('Save (ctrl + s)')
        fileM.addAction('Open')
        fileM.addAction('Export .wav')
        fileM.addAction('Close window (alt + f4)')

        # Edit
        editM = menuBar.addMenu('Edit')
        editM.addAction('Undo (ctrl + z)')
        editM.addAction('Redo (ctrl + shift + z)')
        editM.addAction('Cut (ctrl + x)')
        editM.addAction('Copy (ctrl + c)')
        editM.addAction('Paste (ctrl + v)')

        # Help
        helpM = menuBar.addMenu('Help')
        (
            helpM
            .addAction('Open github repo')
            .triggered
            .connect(lambda: QDesktopServices.openUrl(QUrl("https://github.com/pepeTheSmugMan/VelvetAnt-Music-Sequencer")))
        )

if __name__ == "__main__":
    app = QApplication([])

    widnow = MainWindow()
    widnow.show()
    app.exec()