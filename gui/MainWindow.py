from PyQt5.QtWidgets import QMainWindow
from math import (sin, asin, cos, acos, tan, atan,
                  pi, degrees)

from .ui.Ui_MainWindowCalc import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):


    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.init_ui()

        self._expression = ''

        self.base_buttons = [
            self.button_7, self.button_8, self.button_9,
            self.button_4, self.button_5, self.button_6,
            self.button_1, self.button_2, self.button_3,
            self.button_0, self.button_float_point,
            self.button_divide, self.button_multiply, self.button_minus,
            self.button_plus, self.button_left_parentheses, self.button_right_parentheses,
            self.button_pi
        ]

        self.trigonometric_buttons = [
            self.button_sin, self.button_asin,
            self.button_cos, self.button_acos,
            self.button_tan, self.button_atan
        ]

        self.init_signals()


    def init_ui(self):
        self.setupUi(self)


    def init_signals(self):

        for button in self.base_buttons:
            button.clicked.connect(self.on_base_button_clicked)

        for button in self.trigonometric_buttons:
            button.clicked.connect(self.on_trigonometric_button_clicked)

        self.button_equals.clicked.connect(self.on_button_equals_clicked)
        self.button_back.clicked.connect(self.on_button_back_clicked)
        self.button_clear.clicked.connect(self.on_button_clear_clicked)
        self.button_clear_hist.clicked.connect(self.on_button_clear_hist_clicked)


    def on_base_button_clicked(self):
        _sender = self.sender().text()
        self._expression += _sender
        self.expressionLineEdit.setText(self._expression)


    def on_trigonometric_button_clicked(self):
        _sender = self.sender().text()
        self._expression += _sender + '('
        self.expressionLineEdit.setText(self._expression)


    def on_button_back_clicked(self):
        self._expression = self._expression[:-1]
        self.expressionLineEdit.setText(self._expression)


    def on_button_clear_clicked(self):
        self._expression = ''
        self.expressionLineEdit.setText(self._expression)


    def on_button_clear_hist_clicked(self):
        self.historyTextEdit.setText('')


    def on_button_equals_clicked(self):
        try:
            _expression = self.expressionLineEdit.text()
            _result = eval(_expression)
            self.historyTextEdit.append(_expression + '=' + str(_result))
            self._expression = str(_result)
            self.expressionLineEdit.setText(str(_result))
        except SyntaxError:
            self.on_button_clear_clicked()
        except NameError:
            self.on_button_clear_clicked()

