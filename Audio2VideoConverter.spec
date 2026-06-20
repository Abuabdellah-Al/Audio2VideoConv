# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[
        # Bundle FFmpeg
        ('ffmpeg/bin/ffmpeg.exe', 'ffmpeg/bin'),
    ],
    datas=[
        ('assets/icon3.ico', 'assets'),   # Icon for runtime
    ],
    hiddenimports=[
        'moviepy',
        'moviepy.audio',
        'imageio',
        'imageio_ffmpeg',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Remove other Qt bindings
        'PyQt5', 'PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets', 'PyQt5.sip',
        'PyQt6', 'PyQt6.QtCore', 'PyQt6.QtGui', 'PyQt6.QtWidgets', 'PyQt6.sip',
        # Remove unused PySide6 modules (saves ~30-50 MB)
        'PySide6.QtWebEngine',
        'PySide6.QtWebEngineCore',
        'PySide6.QtWebEngineWidgets',
        'PySide6.QtMultimedia',
        'PySide6.QtMultimediaWidgets',
        'PySide6.QtCharts',
        'PySide6.QtDataVisualization',
        'PySide6.Qt3D',
        'PySide6.QtBluetooth',
        'PySide6.QtNfc',
        'PySide6.QtPositioning',
        'PySide6.QtSerialPort',
        'PySide6.QtSql',
        'PySide6.QtSvg',
        'PySide6.QtXml',
        'PySide6.QtXmlPatterns',
    ],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Audio2VideoConverter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,          # Remove debug symbols
    upx=True,            # Compress with UPX
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,       # No console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets/icon3.ico'],
)

# Create a one-folder bundle (not one-file)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=True,
    upx=True,
    upx_exclude=[],
    name='Audio2VideoConverter',
)