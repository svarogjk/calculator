from PyQt5.QtWidgets import QMainWindow

from .ui.Ui_MainWindowCalc import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):


    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.init_ui()

        self._expression = ''

        self.buttons = [
            self.button_7, self.button_8, self.button_9, self.button_divide,
            self.button_4, self.button_5, self.button_6, self.button_multiply,
            self.button_1, self.button_2, self.button_3, self.button_minus,
            self.button_0, self.button_float_point, self.button_equals, self.button_plus
        ]

        self.init_signals()


    def init_ui(self):
        self.setupUi(self)


    def init_signals(self):

        for button in self.buttons:
            button.clicked.connect(self.on_button_clicked)


    def on_button_clicked(self):
        _sender =self.sender().text()
        if _sender == '=':
            self._result = eval(self._expression)
            self.historyTextEdit.append(str(self._expression) + '=' + str(self._result) + '\n')
            self._expression = ''
            self.expressionLineEdit.setText(self._expression)
        else:
            self._expression += _sender
            self.expressionLineEdit.setText(self._expression)







