from edit_form import *
from PyQt5.QtWidgets import QMessageBox, QMainWindow
import re


class EditForm(QMainWindow, Ui_edit_form):

    def __init__(self, parent=None):
        super(EditForm, self).__init__(parent)
        #禁用最大化、不允许手动改变大小
        self.setFixedSize(self.width(), self.height())
        self.setupUi(self)
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        self.btn_save.clicked.connect(self.btn_save_clicked)
        self.list = ["", "", "", "", "", ""]
        self.is_edit = False
        self.target_row = 0
        self.parent = parent

    def btn_cancel_clicked(self):
        self.close()

    def btn_save_clicked(self):
        if self.check_info():
            self.close()
            self.list[0] = self.le_school_id.text()
            self.list[1] = self.le_name.text()
            self.list[2] = "男" if self.cb_gender.currentIndex() == 0 else "女"
            self.list[3] = self.le_age.text()
            self.list[4] = self.le_phone.text()
            self.list[5] = self.le_address.text()
            if self.is_edit:
                self.parent.edit_row(self.target_row, self.list)
            else:
                self.parent.add_one_row(self.list)

    def init_list(self):
        self.le_school_id.setText(self.list[0])
        self.le_name.setText(self.list[1])
        self.cb_gender.setCurrentIndex(1 if self.list[2] == "女" else 0)
        self.le_age.setText(self.list[3])
        self.le_phone.setText(self.list[4])
        self.le_address.setText(self.list[5])

    def check_info(self):
        is_pass = False
        if not re.match("\\d{10}", self.le_school_id.text()):
            QMessageBox.information(self, "提示", "学号格式不正确")
            self.le_school_id.setFocus()
        elif len(self.le_name.text()) == 0:
            QMessageBox.information(self, "提示", "姓名不能为空")
            self.le_name.setFocus()
        elif not re.match("\\d{2}", self.le_age.text()):
            QMessageBox.information(self, "提示", "年龄格式不正确")
            self.le_age.setFocus()
        elif not re.match("^[1]([3-9])[0-9]{9}$", self.le_phone.text()):
            QMessageBox.information(self, "提示", "联系电话格式不正确")
            self.le_phone.setFocus()
        elif len(self.le_address.text()) == 0:
            QMessageBox.information(self, "提示", "家庭住址不能为空")
            self.le_address.setFocus()
        else:
            is_pass = True
        return is_pass
