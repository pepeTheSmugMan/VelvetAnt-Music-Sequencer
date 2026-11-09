from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from .Note import Note
from .GridScene import GridScene

from Antennae import Data
from Chrysalis import Mixer
from Chirp import Presets
import sounddevice

class PianoRoll(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # initialise scene and view for it
        self.scene = GridScene(self)
        self.view = QGraphicsView(self.scene)

        # set scrollbars (we dont know final measurements yet)
        self.view.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOn
        )
        self.view.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOn
        )
        self.view.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )

        # automatically resize margin
        # scrollbar = self.view.horizontalScrollBar()
        # def extend_scene(value):
        #     scrollbar = self.view.horizontalScrollBar()

        #     if value >= scrollbar.maximum() - 100:
        #         rect = self.scene.sceneRect()

        #         self.scene.setSceneRect(
        #             rect.x(),
        #             rect.y(),
        #             rect.width() + 2000,
        #             rect.height()
        #         )
        # scrollbar.valueChanged.connect(extend_scene)

        # create layout for view to be visible
        layout = QVBoxLayout(self)
        layout.addWidget(self.view)

        button = QPushButton('Notes')
        button.clicked.connect(lambda _ : print(self.scene.items()))
        layout.addWidget(button)

        button2 = QPushButton('Play')
        button2.clicked.connect(self.play)
        layout.addWidget(button2)

    def mousePressEvent(self, event):

        if (event.button() == Qt.MouseButton.LeftButton):
            note = Note()
            self.scene.addItem(note)

            #! BUG: coordinates respond more to the grid than spaces between them,
            #! which makes it unintuitive
            pos = self.view.mapToScene(event.position().toPoint())
            note.setPos(pos)

    def play(self):

        gridUnitLengthSec = 0.125
        segment = Data.Segment(0.0, 30.0, [])
        
        for note in self.scene.items():
            
            newNote = Data.Note(
                start=note.pos().x() / self.scene.grid_size * gridUnitLengthSec,
                duration=note.rect().width() / self.scene.grid_size * gridUnitLengthSec,
                pitch=1200 - (note.pos().y() + 100.0)
            )
            segment.notes.append(newNote)
            print(note)
        
        print(segment, segment.notes)

        sound = Mixer.segment_to_melody(Presets.sine, segment)
        sounddevice.play(sound)

        return