from PySide import QtGui
from QtGui import QWidget

class DiagnosticToolWidget(QWidget):
  
    def __init__(self):
        super(DiagnosticToolWidget, self).__init__()
        self.setObjectName('DiagnosticToolWidget')
	getDataBtn = QtGui.QPushButton('Quit', self) 
