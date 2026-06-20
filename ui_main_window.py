from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                           QMetaObject, QObject, QPoint, QRect,
                           QSize, QTime, QUrl, Qt)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QMainWindow, QFileDialog, QMessageBox,
                              QMenuBar, QStatusBar)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QWidget,
                               QVBoxLayout, QHBoxLayout, QSizePolicy)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(628, 900)  # Increased height to accommodate new header

        # Central Widget with Layout
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_layout = QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(15)  # Increased spacing between widgets

        # ========== NEW HEADER SECTION ==========
        self.header_frame = QFrame()
        self.header_frame.setObjectName(u"header_frame")
        self.header_layout = QVBoxLayout(self.header_frame)
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(5)

        # Main title "Audio2Video Converter"
        self.title_label = QLabel("Audio2Video Converter")
        self.title_label.setObjectName(u"title_label")
        title_font = QFont()
        title_font.setPointSize(24)
        title_font.setBold(True)
        self.title_label.setFont(title_font)
        self.title_label.setStyleSheet("color: dodgerblue;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Subtitle "Powered by DeepSeek℗"
        self.subtitle_label = QLabel("Powered by DeepSeek℗")
        self.subtitle_label.setObjectName(u"subtitle_label")
        subtitle_font = QFont()
        subtitle_font.setPointSize(10)
        subtitle_font.setItalic(True)
        self.subtitle_label.setFont(subtitle_font)
        self.subtitle_label.setStyleSheet("color: gray;")
        self.subtitle_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Add to header layout
        self.header_layout.addWidget(self.title_label)
        self.header_layout.addWidget(self.subtitle_label)
        self.main_layout.addWidget(self.header_frame)

        # Image Selection Frame
        self.image_frame = QFrame()
        self.image_frame.setObjectName(u"image_frame")
        self.image_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.image_layout = QHBoxLayout(self.image_frame)
        self.image_layout.setContentsMargins(5, 5, 5, 5)

        self.label = QLabel("Choose Image:")
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(16)
        self.label.setFont(font1)

        self.imagePathLineEdit = QLineEdit()
        self.imagePathLineEdit.setObjectName(u"imagePathLineEdit")

        self.imageBrowseButton = QPushButton("Browse")
        self.imageBrowseButton.setObjectName(u"imageBrowseButton")
        font = QFont()
        font.setPointSize(14)

        fontSmall = QFont()
        fontSmall.setPointSize(10)
        self.imageBrowseButton.setFont(font)

        self.image_layout.addWidget(self.label)
        self.image_layout.addWidget(self.imagePathLineEdit)
        self.image_layout.addWidget(self.imageBrowseButton)

        # Image Preview Area - Now Dynamic
        self.preview_frame = QFrame()
        self.preview_frame.setObjectName(u"preview_frame")
        self.preview_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.preview_layout = QVBoxLayout(self.preview_frame)
        self.preview_layout.setContentsMargins(0, 0, 0, 0)

        # Modified imagePreview setup
        self.imagePreview = QLabel("Drop image here",self.preview_frame)
        self.imagePreview.setObjectName(u"imagePreview")
        self.imagePreview.setGeometry(QRect(80, 10, 450, 450))
        # Remove font settings that might conflict
        self.imagePreview.setStyleSheet(u"""
            QLabel {
                border: 2px solid #666;
                border-radius: 5px;
                padding: 20px;
                background-color: #f0f0f0;
                color: #333;  /* Text color */
                font-size: 16px;
                font-weight: bold;
            }
            QLabel:hover {
                background-color: #e0e0e0;
            }
        """)
        self.imagePreview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.imagePreview.setScaledContents(False)  # Changed from True

        self.preview_layout.addWidget(self.imagePreview)

        # Audio Selection Frame
        self.audio_frame = QFrame()
        self.audio_frame.setObjectName(u"audio_frame")
        self.audio_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.audio_layout = QHBoxLayout(self.audio_frame)
        self.audio_layout.setContentsMargins(5, 5, 5, 5)

        self.label_3 = QLabel("Choose Audio file:")
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.audioPathLineEdit = QLineEdit()
        self.audioPathLineEdit.setObjectName(u"audioPathLineEdit")

        self.audioBrowseButton = QPushButton("Browse")
        self.audioBrowseButton.setObjectName(u"audioBrowseButton")
        self.audioBrowseButton.setFont(font)

        self.audio_layout.addWidget(self.label_3)
        self.audio_layout.addWidget(self.audioPathLineEdit)
        self.audio_layout.addWidget(self.audioBrowseButton)

        # Convert Button
        self.convertButton = QPushButton("Convert")
        self.convertButton.setObjectName(u"convertButton")
        font3 = QFont()
        font3.setPointSize(24)
        self.convertButton.setFont(font3)
        self.convertButton.setStyleSheet("padding: 10px;")

        # Footer Label
        self.label_2 = QLabel("This application uses FFmpeg. FFmpeg is licensed under the LGPL/GPL.\nThe source code for the FFmpeg build used in this release can be found at: https://www.gyan.dev/ffmpeg/builds/ ")

        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(fontSmall)

        # Add all to main layout
        self.main_layout.addWidget(self.image_frame)
        self.main_layout.addWidget(self.preview_frame, 1)  # Priority stretch
        self.main_layout.addWidget(self.audio_frame)
        self.main_layout.addWidget(self.convertButton)
        self.main_layout.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        # Menu and Status Bars
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 628, 33))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # Update retranslateUi with new labels
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Audio2VideoConverter", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Audio2Video Converter", None))
        self.subtitle_label.setText(QCoreApplication.translate("MainWindow", u"Powered by DeepSeek℗", None))