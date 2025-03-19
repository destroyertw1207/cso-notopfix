import os
import sys
import time
import ctypes

from pywinauto import Application
from pywinauto.win32functions import SetWindowLong
import win32gui
import win32con
import win32api
import win32clipboard
from screeninfo import get_monitors

import uiautomation as auto
import pygetwindow as gw

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QMessageBox, QDialog
from PyQt6.QtGui import QPixmap, QMovie
from PyQt6.QtCore import Qt, QMetaObject, Q_ARG

# 獲取所有顯示器資訊
monitors = get_monitors()
monitor = monitors[0]

def run_as_admin():
    # 檢查是否以管理員身份運行
    if not ctypes.windll.shell32.IsUserAnAdmin():
        # 如果不是，重新啟動腳本以管理員身份運行
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
        sys.exit(0)

run_as_admin()

window_titles = [
      "Counter-Strike Online"
    , "Counter-Strike Nexon"
]

for window_title in window_titles:
    if gw.getWindowsWithTitle(window_title):
        hwnd = gw.getWindowsWithTitle(window_title)[0]._hWnd
        
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                          win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        print(f"視窗 '{window_title}' 已取消置頂")