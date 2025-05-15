from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # Vertical Layout
        self.verticalLayout = QVBoxLayout(self.centralwidget)

        # Image Selection Frame
        self.imageFrame = QFrame(self.centralwidget)
        self.imageLayout = QVBoxLayout(self.imageFrame)

        self.imageLabel = QLabel("Choose image:", self.imageFrame)
        self.imagePathLineEdit = QLineEdit(self.imageFrame)
        self.imageBrowseButton = QPushButton("Browse", self.imageFrame)

        self.imageLayout.addWidget(self.imageLabel)
        self.imageLayout.addWidget(self.imagePathLineEdit)
        self.imageLayout.addWidget(self.imageBrowseButton)

        # Image Preview
        self.imagePreview = QLabel("Drop image here", self.centralwidget)
        self.imagePreview.setAlignment(Qt.AlignCenter)
        self.imagePreview.setFrameShape(QFrame.Box)
        self.imagePreview.setStyleSheet("border: 2px dashed #aaa; padding: 20px;")

        # Audio Selection Frame
        self.audioFrame = QFrame(self.centralwidget)
        self.audioLayout = QVBoxLayout(self.audioFrame)

        self.audioLabel = QLabel("Choose audio:", self.audioFrame)
        self.audioPathLineEdit = QLineEdit(self.audioFrame)
        self.audioBrowseButton = QPushButton("Browse", self.audioFrame)

        self.audioLayout.addWidget(self.audioLabel)
        self.audioLayout.addWidget(self.audioPathLineEdit)
        self.audioLayout.addWidget(self.audioBrowseButton)

        # Convert Button
        self.convertButton = QPushButton("Convert to Video", self.centralwidget)

        # Add all to main layout
        self.verticalLayout.addWidget(self.imageFrame)
        self.verticalLayout.addWidget(self.imagePreview)
        self.verticalLayout.addWidget(self.audioFrame)
        self.verticalLayout.addWidget(self.convertButton)

        MainWindow.setCentralWidget(self.centralwidget)