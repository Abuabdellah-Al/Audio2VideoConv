import sys
import os
os.environ["IMAGEIO_FFMPEG_EXE"] = os.path.join(os.path.dirname(__file__), "ffmpeg")
# Disable high contrast adaptation
os.environ["QT_QPA_PLATFORM"] = "windows:darkmode=2:nohighcontrast"
from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QMouseEvent
from moviepy import ImageClip, AudioFileClip
from ui_main_window3 import Ui_MainWindow
from PySide6.QtCore import QStandardPaths
from PySide6.QtGui import QIcon
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QStyleFactory

class AudioToVideoConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("app_icon.ico"))  # or .png

        def set_windows_dark_theme(self):
            """Full Windows 11 dark theme implementation"""
            # 1. Force Windows native style
            self.setStyle(QStyleFactory.create("windowsvista"))

            # 2. Windows 11 dark palette
            palette = self.palette()
            palette.setColor(QPalette.Window, QColor(32, 32, 32))  # #202020
            palette.setColor(QPalette.WindowText, QColor(240, 240, 240))  # #F0F0F0
            palette.setColor(QPalette.Base, QColor(25, 25, 25))  # #191919
            palette.setColor(QPalette.Text, QColor(240, 240, 240))
            palette.setColor(QPalette.Button, QColor(51, 51, 51))  # #333333
            palette.setColor(QPalette.Highlight, QColor(0, 120, 215))  # Windows blue
            self.setPalette(palette)

            # 3. Windows 11 style controls
            self.setStyleSheet("""
                /* Windows 11 styled push buttons */
                QPushButton {
                    background-color: #333333;
                    border: 1px solid #4A4A4A;
                    border-radius: 4px;
                    padding: 5px 16px;
                    min-width: 80px;
                    font: 12px 'Segoe UI Variable';
                }
                QPushButton:hover {
                    background-color: #404040;
                }
                QPushButton:pressed {
                    background-color: #2A2A2A;
                }

                /* Windows 11 styled inputs */
                QLineEdit, QComboBox {
                    background-color: #252525;
                    border: 1px solid #3E3E3E;
                    padding: 5px;
                    selection-background-color: #0078D7;
                }

                /* Image drop zone */
                QLabel#imagePreview {
                    background-color: #252525;
                    color: #A0A0A0;
                    border: 2px dashed #404040;
                    font: 14px 'Segoe UI Variable';
                }
            """)

            # 4. Force dark window frame (Windows 10/11)
            self.enable_dark_title_bar()

        def enable_dark_title_bar(self):
            """Windows 10/11 dark title bar"""
            try:
                from ctypes import windll, byref, sizeof, c_int
                HWND = int(self.winId())
                DWMWA_USE_IMMERSIVE_DARK_MODE = 20
                windll.dwmapi.DwmSetWindowAttribute(
                    HWND,
                    DWMWA_USE_IMMERSIVE_DARK_MODE,
                    byref(c_int(1)),
                    sizeof(c_int))
            except Exception as e:
                print(f"Couldn't set dark title bar: {e}")






        # Setup drag-drop
        self.ui.imagePreview.setAcceptDrops(True)
        self.ui.imagePreview.mouseDoubleClickEvent = self.on_image_preview_double_click
        # Connect buttons
        self.ui.imageBrowseButton.clicked.connect(self.browse_image)
        self.ui.audioBrowseButton.clicked.connect(self.browse_audio)
        self.ui.convertButton.clicked.connect(self.convert)

    def on_image_preview_double_click(self, event: QMouseEvent):
        """Handle double-click on image preview"""
        if event.button() == Qt.LeftButton:
            self.browse_image()


    def browse_image(self):
        pictures_dir = QStandardPaths.writableLocation(QStandardPaths.PicturesLocation)
        path, _ = QFileDialog.getOpenFileName(self, "Select Image", pictures_dir, "Images (*.png *.jpg *.jpeg)")
        if path:
            self.ui.imagePathLineEdit.setText(path)
            self.show_image(path)

    def browse_audio(self):
        music_dir = QStandardPaths.writableLocation(QStandardPaths.MusicLocation)
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Audio File",
            music_dir,
            "Audio Files (*.mp3 *.wav *.ogg *.flac *.aac *.m4a *.wma);;All Files (*)"
        )
        if path:
            self.ui.audioPathLineEdit.setText(path)

    def show_image(self, path):
        pixmap = QPixmap(path)
        if not pixmap.isNull():
            # Scale while maintaining aspect ratio
            scaled = pixmap.scaled(
                self.ui.imagePreview.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.ui.imagePreview.setPixmap(scaled)
            self.ui.imagePreview.setProperty("hasImage", "true")
            self.ui.imagePreview.style().polish(self.ui.imagePreview)  # Refresh style
        else:
            self.clear_image_preview()

    def clear_image_preview(self):
        self.ui.imagePreview.clear()
        self.ui.imagePreview.setText("Drop image here!")
        self.ui.imagePreview.setProperty("hasImage", "false")
        self.ui.imagePreview.style().polish(self.ui.imagePreview)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            self.ui.imagePreview.setStyleSheet("border: 2px dashed #0078d7;")
            event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        self.ui.imagePreview.setStyleSheet("border: 2px dashed #555;")



    def dropEvent(self, event):
        for url in event.mimeData().urls():
            path = url.toLocalFile()
            if path.lower().endswith(('.png', '.jpg', '.jpeg')):
                self.ui.imagePathLineEdit.setText(path)
                self.show_image(path)
            elif path.lower().endswith(('.mp3', '.wav')):
                self.ui.audioPathLineEdit.setText(path)

    def show_message(self, title, message, is_error=False):
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(message)
        if is_error:
            msg.setIcon(QMessageBox.Critical)
        else:
            msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def resizeEvent(self, event):
        if hasattr(self, 'current_image_path'):
            self.show_image(self.current_image_path)
        super().resizeEvent(event)

    def convert(self):
        image_path = self.ui.imagePathLineEdit.text()
        audio_path = self.ui.audioPathLineEdit.text()

        if not all([image_path, audio_path]):
            self.show_message("Error", "Please select both image and audio files!", True)
            return

        output_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Video",
            "",
            "MP4 Files (*.mp4);;AVI Files (*.avi)"
        )

        if not output_path:
            return

        try:
            # Ensure .mp4 extension
            if not output_path.lower().endswith('.mp4'):
                output_path += '.mp4'

            # Verify files exist
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"Image file not found: {image_path}")
            if not os.path.exists(audio_path):
                raise FileNotFoundError(f"Audio file not found: {audio_path}")

            # Update UI
            self.ui.convertButton.setEnabled(False)
            self.ui.convertButton.setText("Converting...")
            QApplication.processEvents()

            # Load clips (CORRECTED VERSION)
            audio_clip = AudioFileClip(audio_path)
            image_clip = ImageClip(image_path)

            # Set image duration to match audio
            image_clip = image_clip.with_duration(audio_clip.duration)

            # Combine clips (CORRECTED METHOD)
            video_clip = image_clip.with_audio(audio_clip)

            # Write video file
            video_clip.write_videofile(
                output_path,
                fps=24,
                codec='libx264',
                audio_codec='aac',
                threads=4,
                ffmpeg_params=['-crf', '18']  # Better quality
            )

            # Verify output
            if os.path.exists(output_path):
                self.show_message("Success", f"Video created successfully!\n{output_path}")
            else:
                raise Exception("Conversion completed but no file was created")

        except Exception as e:
            self.show_message("Error", f"Conversion failed:\n{str(e)}", True)

        finally:
            self.ui.convertButton.setEnabled(True)
            self.ui.convertButton.setText("Convert to Video")
            QApplication.processEvents()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioToVideoConverter()
    window.show()
    sys.exit(app.exec())