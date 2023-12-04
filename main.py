import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTextEdit
from PyQt5.QtCore import Qt
from datetime import datetime
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def generate_sql_script(start_date, end_date):
    sql_script = f"""
    SELECT
    o.fTax, o.Source, o.dReceievedDate, o.Town, o.Region, o.Subtotal, o.PostageCostExTax, o.cFullName, nOrderId, o.TotalCharge, fTotalCharge
    FROM
    [Order] o
    WHERE
    dReceievedDate <= '{end_date}'
    AND 
    dReceievedDate >= '{start_date}'
    """
    return sql_script

class SQLScriptGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('SQL Script Generator')
        self.setGeometry(100, 100, 600, 400)

        self.label_start_date = QLabel('Enter the start date (YYYY-MM-DD):')
        self.edit_start_date = QLineEdit(self)

        self.label_end_date = QLabel('Enter the end date (YYYY-MM-DD):')
        self.edit_end_date = QLineEdit(self)

        self.btn_generate = QPushButton('Generate SQL Script', self)
        self.btn_generate.clicked.connect(self.generate_sql_script)

        self.text_output = QTextEdit(self)
        self.text_output.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.label_start_date)
        layout.addWidget(self.edit_start_date)
        layout.addWidget(self.label_end_date)
