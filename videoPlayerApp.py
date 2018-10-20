from PyQt4 import QtGui
from PyQt4 import phonon


from ui import main


class VideoPlayerClass(main.Ui_MainWindow, QtGui.QMainWindow):
    def __init__(self):
        super(VideoPlayerClass, self).__init__()
        self.setupUi(self)
        self.play_PB.clicked.connect(lambda: self.videoPlayer.play())
        self.pause_PB.clicked.connect(lambda: self.videoPlayer.pause())
        self.stop_PB.clicked.connect(lambda: self.videoPlayer.stop())
        self.actionOpen.triggered.connect(self.select_video)

    def select_video(self):
        filepath = QtGui.QFileDialog.getOpenFileName(self, 'Select Video')
        self.load_video(filepath)

    def load_video(self, filepath):
        media = phonon.Phonon.MediaSource(filepath)
        self.videoPlayer.load(media)
        self.seekSlider.setMediaObject(self.videoPlayer.mediaObject())
        self.volumeSlider.setAudioOutput(self.videoPlayer.audioOutput())
        self.videoPlayer.play()


if __name__ == '__main__':
    app = QtGui.QApplication([])
    vp = VideoPlayerClass()
    vp.show()
    app.exec_()

