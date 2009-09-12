# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/psptracker/forms/AbstractCategoryManager.ui'
#
# Created: Sat Sep 12 19:13:31 2009
#      by: PyQt4 UI code generator 4.5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AbstractCategoryManager(object):
    def setupUi(self, AbstractCategoryManager):
        AbstractCategoryManager.setObjectName("AbstractCategoryManager")
        AbstractCategoryManager.resize(384, 243)
        AbstractCategoryManager.setModal(True)
        self.gridlayout = QtGui.QGridLayout(AbstractCategoryManager)
        self.gridlayout.setObjectName("gridlayout")
        self.labelCategory = QtGui.QLabel(AbstractCategoryManager)
        self.labelCategory.setWordWrap(False)
        self.labelCategory.setObjectName("labelCategory")
        self.gridlayout.addWidget(self.labelCategory, 0, 0, 1, 1)
        self.editCategory = QtGui.QLineEdit(AbstractCategoryManager)
        self.editCategory.setObjectName("editCategory")
        self.gridlayout.addWidget(self.editCategory, 1, 0, 1, 1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.buttonAdd = QtGui.QPushButton(AbstractCategoryManager)
        self.buttonAdd.setObjectName("buttonAdd")
        self.hboxlayout.addWidget(self.buttonAdd)
        spacerItem = QtGui.QSpacerItem(51, 31, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.pushRename = QtGui.QPushButton(AbstractCategoryManager)
        self.pushRename.setObjectName("pushRename")
        self.hboxlayout.addWidget(self.pushRename)
        spacerItem1 = QtGui.QSpacerItem(51, 30, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.buttonDelete = QtGui.QPushButton(AbstractCategoryManager)
        self.buttonDelete.setObjectName("buttonDelete")
        self.hboxlayout.addWidget(self.buttonDelete)
        self.gridlayout.addLayout(self.hboxlayout, 2, 0, 1, 1)
        self.listCategory = QtGui.QListWidget(AbstractCategoryManager)
        self.listCategory.setObjectName("listCategory")
        self.gridlayout.addWidget(self.listCategory, 3, 0, 1, 1)

        self.retranslateUi(AbstractCategoryManager)
        QtCore.QObject.connect(AbstractCategoryManager, QtCore.SIGNAL("destroyed(QObject*)"), AbstractCategoryManager.AbstractCategoryManager_destroyed)
        QtCore.QObject.connect(self.buttonAdd, QtCore.SIGNAL("clicked()"), AbstractCategoryManager.buttonAdd_clicked)
        QtCore.QObject.connect(self.buttonDelete, QtCore.SIGNAL("clicked()"), AbstractCategoryManager.buttonDelete_clicked)
        QtCore.QObject.connect(self.pushRename, QtCore.SIGNAL("clicked()"), AbstractCategoryManager.pushRename_clicked)
        QtCore.QMetaObject.connectSlotsByName(AbstractCategoryManager)

    def retranslateUi(self, AbstractCategoryManager):
        AbstractCategoryManager.setWindowTitle(QtGui.QApplication.translate("AbstractCategoryManager", "Category Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCategory.setText(QtGui.QApplication.translate("AbstractCategoryManager", "Category", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAdd.setText(QtGui.QApplication.translate("AbstractCategoryManager", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushRename.setText(QtGui.QApplication.translate("AbstractCategoryManager", "Rename", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonDelete.setText(QtGui.QApplication.translate("AbstractCategoryManager", "Delete", None, QtGui.QApplication.UnicodeUTF8))

