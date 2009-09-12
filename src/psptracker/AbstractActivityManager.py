# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/psptracker/forms/AbstractActivityManager.ui'
#
# Created: Sat Sep 12 19:13:31 2009
#      by: PyQt4 UI code generator 4.5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AbstractActivityManager(object):
    def setupUi(self, AbstractActivityManager):
        AbstractActivityManager.setObjectName("AbstractActivityManager")
        AbstractActivityManager.resize(378, 305)
        AbstractActivityManager.setModal(True)
        self.gridlayout = QtGui.QGridLayout(AbstractActivityManager)
        self.gridlayout.setObjectName("gridlayout")
        self.editActivity = QtGui.QLineEdit(AbstractActivityManager)
        self.editActivity.setObjectName("editActivity")
        self.gridlayout.addWidget(self.editActivity, 3, 0, 1, 2)
        self.labelActivity = QtGui.QLabel(AbstractActivityManager)
        self.labelActivity.setWordWrap(False)
        self.labelActivity.setObjectName("labelActivity")
        self.gridlayout.addWidget(self.labelActivity, 2, 0, 1, 2)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.buttonAdd = QtGui.QPushButton(AbstractActivityManager)
        self.buttonAdd.setObjectName("buttonAdd")
        self.hboxlayout.addWidget(self.buttonAdd)
        spacerItem = QtGui.QSpacerItem(51, 31, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.pushRename = QtGui.QPushButton(AbstractActivityManager)
        self.pushRename.setObjectName("pushRename")
        self.hboxlayout.addWidget(self.pushRename)
        spacerItem1 = QtGui.QSpacerItem(51, 30, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.buttonDelete = QtGui.QPushButton(AbstractActivityManager)
        self.buttonDelete.setObjectName("buttonDelete")
        self.hboxlayout.addWidget(self.buttonDelete)
        self.gridlayout.addLayout(self.hboxlayout, 4, 0, 1, 2)
        self.comboCategory = QtGui.QComboBox(AbstractActivityManager)
        self.comboCategory.setObjectName("comboCategory")
        self.gridlayout.addWidget(self.comboCategory, 1, 0, 1, 1)
        self.CategoryManagement = QtGui.QToolButton(AbstractActivityManager)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CategoryManagement.sizePolicy().hasHeightForWidth())
        self.CategoryManagement.setSizePolicy(sizePolicy)
        self.CategoryManagement.setObjectName("CategoryManagement")
        self.gridlayout.addWidget(self.CategoryManagement, 1, 1, 1, 1)
        self.labelCategory = QtGui.QLabel(AbstractActivityManager)
        self.labelCategory.setWordWrap(False)
        self.labelCategory.setObjectName("labelCategory")
        self.gridlayout.addWidget(self.labelCategory, 0, 0, 1, 2)
        self.listActivity = QtGui.QListWidget(AbstractActivityManager)
        self.listActivity.setObjectName("listActivity")
        self.gridlayout.addWidget(self.listActivity, 5, 0, 1, 2)

        self.retranslateUi(AbstractActivityManager)
        QtCore.QMetaObject.connectSlotsByName(AbstractActivityManager)

    def retranslateUi(self, AbstractActivityManager):
        AbstractActivityManager.setWindowTitle(QtGui.QApplication.translate("AbstractActivityManager", "Activity Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.labelActivity.setText(QtGui.QApplication.translate("AbstractActivityManager", "Activity", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAdd.setText(QtGui.QApplication.translate("AbstractActivityManager", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushRename.setText(QtGui.QApplication.translate("AbstractActivityManager", "Rename", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonDelete.setText(QtGui.QApplication.translate("AbstractActivityManager", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.CategoryManagement.setText(QtGui.QApplication.translate("AbstractActivityManager", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCategory.setText(QtGui.QApplication.translate("AbstractActivityManager", "Category", None, QtGui.QApplication.UnicodeUTF8))

