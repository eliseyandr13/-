from PyQt5.QtCore import QUrl, QFileInfo
from PyQt5.QtWidgets import QApplication
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import PyQt5.QtWidgets as qtw
import sys
import PyQt5

"""
Если кликнул на q, то это до
на w - ре
на e - ми
на r - фа
на t - соль
на y - ля
на u - си
на i - до
"""


class Piano(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Фортепиано')
        self.setupUI()

    def setupUI(self):
        self.lst = {'do_1': 'До', 're': 'Ре', 'mi': 'Ми', 'fa': 'Фа', 'salt': 'Соль', 'la': 'Ля', 'ci': 'Си', 'do_2': 'До'}
        # widgets
        self.do_1 = qtw.QPushButton('До первой', self)
        self.re = qtw.QPushButton('Ре', self)
        self.mi = qtw.QPushButton('Ми', self)
        self.fa = qtw.QPushButton('Фа', self)
        self.salt = qtw.QPushButton('Соль', self)
        self.la = qtw.QPushButton('Ля', self)
        self.ci = qtw.QPushButton('Си', self)
        self.do_2 = qtw.QPushButton('До второй', self)

        self.player = QMediaPlayer()

        # layouts
        self.main_layout = qtw.QHBoxLayout()
        self.main_layout.addWidget(self.do_1)
        self.main_layout.addWidget(self.re)
        self.main_layout.addWidget(self.mi)
        self.main_layout.addWidget(self.fa)
        self.main_layout.addWidget(self.salt)
        self.main_layout.addWidget(self.la)
        self.main_layout.addWidget(self.ci)
        self.main_layout.addWidget(self.do_2)
        self.setLayout(self.main_layout)
        
        self.do_1.clicked.connect(self.was_clicked)
        self.re.clicked.connect(self.was_clicked)
        self.mi.clicked.connect(self.was_clicked)
        self.fa.clicked.connect(self.was_clicked)
        self.salt.clicked.connect(self.was_clicked)
        self.la.clicked.connect(self.was_clicked)
        self.ci.clicked.connect(self.was_clicked)
        self.do_2.clicked.connect(self.was_clicked)
    
    def was_clicked(self):
        if self.sender().text() == 'До первой':
            file_info = QFileInfo(r"some_note-do.wav")
        elif self.sender().text() == 'Ре':
            file_info = QFileInfo(r"re-note-sound.wav")
        elif self.sender().text() == 'Ми':
            file_info = QFileInfo(r"some_note-mi.wav")
        elif self.sender().text() == 'Фа':
            file_info = QFileInfo(r"fa-note-sound.wav")
        elif self.sender().text() == 'Соль':
            file_info = QFileInfo(r"salt-note-sound.wav")
        elif self.sender().text() == 'Ля':
            file_info = QFileInfo(r"some_note-la.wav")
        elif self.sender().text() == 'Си':
            file_info = QFileInfo(r"c-note-sound.wav")
        else:
            file_info = QFileInfo(r"some_note-do-in-the-second-octave.wav")
        url = QUrl.fromLocalFile(file_info.absoluteFilePath())
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()
    
    def keyPressEvent(self, e):
        if e.key() == PyQt5.QtCore.Qt.Key_Q:
            file_info = QFileInfo(r"some_note-do.wav")
        elif e.key() == PyQt5.QtCore.Qt.Key_W:
            file_info = QFileInfo(r"re-note-sound.wav")
        elif e.key() == PyQt5.QtCore.Qt.Key_E:
            file_info = QFileInfo(r"some_note-mi.wav")
        elif e.key() == PyQt5.QtCore.Qt.Key_R:
            file_info = QFileInfo(r"fa-note-sound.wav")
        elif e.key() == PyQt5.QtCore.Qt.Key_T:
            file_info = QFileInfo(r"salt-note-sound.wav")
        elif e.key() == PyQt5.QtCore.Qt.Key_Y:
            file_info = QFileInfo(r"some_note-la.wav")
        elif e.key() == PyQt5.QtCore.Qt.Key_U:
            file_info = QFileInfo(r"c-note-sound.wav")
        elif e.key() == PyQt5.QtCore.Qt.Key_I:
            file_info = QFileInfo(r"some_note-do-in-the-second-octave.wav")
        url = QUrl.fromLocalFile(file_info.absoluteFilePath())
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()
    
if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    copy = Piano()
    copy.show()
    sys.exit(app.exec())