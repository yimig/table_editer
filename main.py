import sys
from ex_main_form import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainForm = MainForm()
    mainForm.show()
    sys.exit(app.exec_())
