# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/psptracker/forms/AbstractRealtimeTracker.ui'
#
# Created: Sat Sep 12 19:13:31 2009
#      by: PyQt4 UI code generator 4.5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AbstractRealtimeTracker(object):
    def setupUi(self, AbstractRealtimeTracker):
        AbstractRealtimeTracker.setObjectName("AbstractRealtimeTracker")
        AbstractRealtimeTracker.resize(423, 580)
        self.gridlayout = QtGui.QGridLayout(AbstractRealtimeTracker)
        self.gridlayout.setObjectName("gridlayout")
        spacerItem = QtGui.QSpacerItem(20, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 5, 0, 1, 1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem1 = QtGui.QSpacerItem(40, 30, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.Start = QtGui.QPushButton(AbstractRealtimeTracker)
        self.Start.setObjectName("Start")
        self.hboxlayout.addWidget(self.Start)
        spacerItem2 = QtGui.QSpacerItem(40, 30, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem2)
        self.Pause = QtGui.QPushButton(AbstractRealtimeTracker)
        self.Pause.setEnabled(False)
        self.Pause.setObjectName("Pause")
        self.hboxlayout.addWidget(self.Pause)
        spacerItem3 = QtGui.QSpacerItem(40, 30, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem3)
        self.Stop = QtGui.QPushButton(AbstractRealtimeTracker)
        self.Stop.setEnabled(False)
        self.Stop.setObjectName("Stop")
        self.hboxlayout.addWidget(self.Stop)
        spacerItem4 = QtGui.QSpacerItem(40, 31, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem4)
        self.gridlayout.addLayout(self.hboxlayout, 6, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem5, 7, 0, 1, 1)
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.LabelInterruptReason = QtGui.QLabel(AbstractRealtimeTracker)
        self.LabelInterruptReason.setEnabled(False)
        self.LabelInterruptReason.setWordWrap(False)
        self.LabelInterruptReason.setObjectName("LabelInterruptReason")
        self.hboxlayout1.addWidget(self.LabelInterruptReason)
        spacerItem6 = QtGui.QSpacerItem(91, 21, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem6)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.gridlayout.addLayout(self.vboxlayout, 8, 0, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem7, 10, 0, 1, 1)
        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")
        spacerItem8 = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem8)
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.LabelStart = QtGui.QLabel(AbstractRealtimeTracker)
        self.LabelStart.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LabelStart.setWordWrap(False)
        self.LabelStart.setObjectName("LabelStart")
        self.vboxlayout1.addWidget(self.LabelStart)
        self.LabelTime = QtGui.QLabel(AbstractRealtimeTracker)
        self.LabelTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LabelTime.setWordWrap(False)
        self.LabelTime.setObjectName("LabelTime")
        self.vboxlayout1.addWidget(self.LabelTime)
        self.hboxlayout2.addLayout(self.vboxlayout1)
        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.dateTimeStart = QtGui.QDateTimeEdit(AbstractRealtimeTracker)
        self.dateTimeStart.setObjectName("dateTimeStart")
        self.vboxlayout2.addWidget(self.dateTimeStart)
        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setObjectName("hboxlayout3")
        self.timeTotal = QtGui.QTimeEdit(AbstractRealtimeTracker)
        self.timeTotal.setObjectName("timeTotal")
        self.hboxlayout3.addWidget(self.timeTotal)
        spacerItem9 = QtGui.QSpacerItem(71, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem9)
        self.vboxlayout2.addLayout(self.hboxlayout3)
        self.hboxlayout2.addLayout(self.vboxlayout2)
        spacerItem10 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem10)
        self.gridlayout.addLayout(self.hboxlayout2, 11, 0, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(20, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem11, 12, 0, 1, 1)
        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setObjectName("hboxlayout4")
        self.LabelActivity = QtGui.QLabel(AbstractRealtimeTracker)
        self.LabelActivity.setWordWrap(False)
        self.LabelActivity.setObjectName("LabelActivity")
        self.hboxlayout4.addWidget(self.LabelActivity)
        spacerItem12 = QtGui.QSpacerItem(101, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout4.addItem(spacerItem12)
        self.gridlayout.addLayout(self.hboxlayout4, 0, 0, 1, 1)
        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setObjectName("vboxlayout3")
        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setObjectName("hboxlayout5")
        self.LabelDescription = QtGui.QLabel(AbstractRealtimeTracker)
        self.LabelDescription.setWordWrap(False)
        self.LabelDescription.setObjectName("LabelDescription")
        self.hboxlayout5.addWidget(self.LabelDescription)
        spacerItem13 = QtGui.QSpacerItem(81, 21, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout5.addItem(spacerItem13)
        self.vboxlayout3.addLayout(self.hboxlayout5)
        self.gridlayout.addLayout(self.vboxlayout3, 3, 0, 1, 1)
        spacerItem14 = QtGui.QSpacerItem(21, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem14, 2, 0, 1, 1)
        self.hboxlayout6 = QtGui.QHBoxLayout()
        self.hboxlayout6.setObjectName("hboxlayout6")
        self.Category = QtGui.QComboBox(AbstractRealtimeTracker)
        self.Category.setAutoCompletion(True)
        self.Category.setDuplicatesEnabled(False)
        self.Category.setObjectName("Category")
        self.hboxlayout6.addWidget(self.Category)
        self.CategoryManagement = QtGui.QToolButton(AbstractRealtimeTracker)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CategoryManagement.sizePolicy().hasHeightForWidth())
        self.CategoryManagement.setSizePolicy(sizePolicy)
        self.CategoryManagement.setObjectName("CategoryManagement")
        self.hboxlayout6.addWidget(self.CategoryManagement)
        self.Activity = QtGui.QComboBox(AbstractRealtimeTracker)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Activity.sizePolicy().hasHeightForWidth())
        self.Activity.setSizePolicy(sizePolicy)
        self.Activity.setAutoCompletion(True)
        self.Activity.setDuplicatesEnabled(False)
        self.Activity.setObjectName("Activity")
        self.hboxlayout6.addWidget(self.Activity)
        self.ActivityManagement = QtGui.QToolButton(AbstractRealtimeTracker)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ActivityManagement.sizePolicy().hasHeightForWidth())
        self.ActivityManagement.setSizePolicy(sizePolicy)
        self.ActivityManagement.setObjectName("ActivityManagement")
        self.hboxlayout6.addWidget(self.ActivityManagement)
        self.gridlayout.addLayout(self.hboxlayout6, 1, 0, 1, 1)
        self.textDescription = QtGui.QTextEdit(AbstractRealtimeTracker)
        self.textDescription.setObjectName("textDescription")
        self.gridlayout.addWidget(self.textDescription, 4, 0, 1, 1)
        self.textInterruptionReason = QtGui.QTextEdit(AbstractRealtimeTracker)
        self.textInterruptionReason.setObjectName("textInterruptionReason")
        self.gridlayout.addWidget(self.textInterruptionReason, 9, 0, 1, 1)
        self.progressBarStress = QtGui.QProgressBar(AbstractRealtimeTracker)
        self.progressBarStress.setProperty("value", QtCore.QVariant(24))
        self.progressBarStress.setObjectName("progressBarStress")
        self.gridlayout.addWidget(self.progressBarStress, 13, 0, 1, 1)

        self.retranslateUi(AbstractRealtimeTracker)
        QtCore.QObject.connect(self.Start, QtCore.SIGNAL("toggled(bool)"), self.Stop.setEnabled)
        QtCore.QObject.connect(self.Start, QtCore.SIGNAL("toggled(bool)"), self.Pause.setEnabled)
        QtCore.QObject.connect(self.Stop, QtCore.SIGNAL("toggled(bool)"), self.Start.setEnabled)
        QtCore.QObject.connect(self.Stop, QtCore.SIGNAL("toggled(bool)"), self.Pause.setEnabled)
        QtCore.QObject.connect(self.Pause, QtCore.SIGNAL("toggled(bool)"), self.LabelInterruptReason.setEnabled)
        QtCore.QObject.connect(self.ActivityManagement, QtCore.SIGNAL("clicked()"), AbstractRealtimeTracker.ActivityManagement_clicked)
        QtCore.QObject.connect(self.Start, QtCore.SIGNAL("toggled(bool)"), AbstractRealtimeTracker.Start_toggled)
        QtCore.QObject.connect(self.Pause, QtCore.SIGNAL("toggled(bool)"), AbstractRealtimeTracker.Pause_toggled)
        QtCore.QObject.connect(self.Stop, QtCore.SIGNAL("toggled(bool)"), AbstractRealtimeTracker.Stop_toggled)
        QtCore.QObject.connect(AbstractRealtimeTracker, QtCore.SIGNAL("destroyed(QObject*)"), AbstractRealtimeTracker.AbstractRealtimeTracker_destroyed)
        QtCore.QObject.connect(self.Start, QtCore.SIGNAL("clicked()"), AbstractRealtimeTracker.Start_clicked)
        QtCore.QObject.connect(self.CategoryManagement, QtCore.SIGNAL("clicked()"), AbstractRealtimeTracker.CategoryManagement_clicked)
        QtCore.QMetaObject.connectSlotsByName(AbstractRealtimeTracker)
        AbstractRealtimeTracker.setTabOrder(self.Category, self.Activity)
        AbstractRealtimeTracker.setTabOrder(self.Activity, self.Start)
        AbstractRealtimeTracker.setTabOrder(self.Start, self.Pause)
        AbstractRealtimeTracker.setTabOrder(self.Pause, self.Stop)

    def retranslateUi(self, AbstractRealtimeTracker):
        AbstractRealtimeTracker.setWindowTitle(QtGui.QApplication.translate("AbstractRealtimeTracker", "Realtime Tracker", None, QtGui.QApplication.UnicodeUTF8))
        self.Start.setText(QtGui.QApplication.translate("AbstractRealtimeTracker", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.Pause.setText(QtGui.QApplication.translate("AbstractRealtimeTracker", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.Stop.setText(QtGui.QApplication.translate("AbstractRealtimeTracker", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelInterruptReason.setText(QtGui.QApplication.translate("AbstractRealtimeTracker", "Interruption reason", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelStart.setText(QtGui.QApplication.translate("AbstractRealtimeTracker", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelTime.setText(QtGui.QApplication.translate("AbstractRealtimeTracker", "Total time", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelActivity.setText(QtGui.QApplication.translate("AbstractRealtimeTracker", "Activity", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelDescription.setText(QtGui.QApplication.translate("AbstractRealtimeTracker", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.CategoryManagement.setText(QtGui.QApplication.translate("AbstractRealtimeTracker", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.ActivityManagement.setText(QtGui.QApplication.translate("AbstractRealtimeTracker", "...", None, QtGui.QApplication.UnicodeUTF8))

