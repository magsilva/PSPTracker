# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created: Sex Nov 12 11:35:59 2004
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class MainForm(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("MainForm")


        MainFormLayout = QGridLayout(self,1,1,11,6,"MainFormLayout")

        layout14 = QGridLayout(None,1,1,0,6,"layout14")

        layout27 = QHBoxLayout(None,0,6,"layout27")

        self.LabelActivity = QLabel(self,"LabelActivity")
        layout27.addWidget(self.LabelActivity)
        spacer46 = QSpacerItem(101,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout27.addItem(spacer46)

        layout14.addLayout(layout27,0,0)

        layout13 = QHBoxLayout(None,0,6,"layout13")

        self.Category = QComboBox(0,self,"Category")
        layout13.addWidget(self.Category)

        self.Activity = QComboBox(0,self,"Activity")
        self.Activity.setSizePolicy(QSizePolicy(1,0,0,0,self.Activity.sizePolicy().hasHeightForWidth()))
        self.Activity.setAutoCompletion(1)
        layout13.addWidget(self.Activity)

        self.ActivityManagement = QToolButton(self,"ActivityManagement")
        self.ActivityManagement.setSizePolicy(QSizePolicy(0,0,0,0,self.ActivityManagement.sizePolicy().hasHeightForWidth()))
        layout13.addWidget(self.ActivityManagement)

        layout14.addLayout(layout13,1,0)

        MainFormLayout.addLayout(layout14,0,0)
        spacer35 = QSpacerItem(21,16,QSizePolicy.Minimum,QSizePolicy.Expanding)
        MainFormLayout.addItem(spacer35,1,0)

        layout24 = QVBoxLayout(None,0,6,"layout24")

        layout23 = QHBoxLayout(None,0,6,"layout23")

        self.LabelDescription = QLabel(self,"LabelDescription")
        layout23.addWidget(self.LabelDescription)
        spacer44 = QSpacerItem(81,21,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout23.addItem(spacer44)
        layout24.addLayout(layout23)

        self.Description = QTextEdit(self,"Description")
        layout24.addWidget(self.Description)

        MainFormLayout.addLayout(layout24,2,0)
        spacer34 = QSpacerItem(20,16,QSizePolicy.Minimum,QSizePolicy.Expanding)
        MainFormLayout.addItem(spacer34,3,0)

        layout5 = QHBoxLayout(None,0,6,"layout5")
        spacer24 = QSpacerItem(40,30,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout5.addItem(spacer24)

        self.Start = QPushButton(self,"Start")
        layout5.addWidget(self.Start)
        spacer4 = QSpacerItem(40,30,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout5.addItem(spacer4)

        self.Pause = QPushButton(self,"Pause")
        self.Pause.setEnabled(0)
        layout5.addWidget(self.Pause)
        spacer5 = QSpacerItem(40,30,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout5.addItem(spacer5)

        self.Stop = QPushButton(self,"Stop")
        self.Stop.setEnabled(0)
        layout5.addWidget(self.Stop)
        spacer25 = QSpacerItem(40,31,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout5.addItem(spacer25)

        MainFormLayout.addLayout(layout5,4,0)
        spacer36 = QSpacerItem(20,16,QSizePolicy.Minimum,QSizePolicy.Expanding)
        MainFormLayout.addItem(spacer36,5,0)

        layout26 = QVBoxLayout(None,0,6,"layout26")

        layout25 = QHBoxLayout(None,0,6,"layout25")

        self.LabelInterruptReason = QLabel(self,"LabelInterruptReason")
        self.LabelInterruptReason.setEnabled(0)
        layout25.addWidget(self.LabelInterruptReason)
        spacer45 = QSpacerItem(91,21,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout25.addItem(spacer45)
        layout26.addLayout(layout25)

        self.InterruptReason = QTextEdit(self,"InterruptReason")
        self.InterruptReason.setEnabled(0)
        layout26.addWidget(self.InterruptReason)

        MainFormLayout.addLayout(layout26,6,0)
        spacer32 = QSpacerItem(20,16,QSizePolicy.Minimum,QSizePolicy.Expanding)
        MainFormLayout.addItem(spacer32,7,0)

        layout22 = QHBoxLayout(None,0,6,"layout22")
        spacer29 = QSpacerItem(60,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout22.addItem(spacer29)

        layout17 = QVBoxLayout(None,0,6,"layout17")

        self.LabelStart = QLabel(self,"LabelStart")
        self.LabelStart.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        layout17.addWidget(self.LabelStart)

        self.LabelEnd = QLabel(self,"LabelEnd")
        self.LabelEnd.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        layout17.addWidget(self.LabelEnd)

        self.LabelTime = QLabel(self,"LabelTime")
        self.LabelTime.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        layout17.addWidget(self.LabelTime)
        layout22.addLayout(layout17)

        layout21 = QVBoxLayout(None,0,6,"layout21")

        self.StartDate = QDateTimeEdit(self,"StartDate")
        layout21.addWidget(self.StartDate)

        self.EndDate = QDateTimeEdit(self,"EndDate")
        layout21.addWidget(self.EndDate)

        layout20 = QHBoxLayout(None,0,6,"layout20")

        self.TotalTime = QTimeEdit(self,"TotalTime")
        layout20.addWidget(self.TotalTime)
        spacer27 = QSpacerItem(71,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout20.addItem(spacer27)
        layout21.addLayout(layout20)
        layout22.addLayout(layout21)
        spacer26 = QSpacerItem(30,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout22.addItem(spacer26)

        MainFormLayout.addLayout(layout22,8,0)
        spacer31 = QSpacerItem(20,16,QSizePolicy.Minimum,QSizePolicy.Expanding)
        MainFormLayout.addItem(spacer31,9,0)

        self.Stress = QProgressBar(self,"Stress")

        MainFormLayout.addWidget(self.Stress,10,0)

        self.languageChange()

        self.resize(QSize(423,580).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.Start,SIGNAL("toggled(bool)"),self.Stop.setEnabled)
        self.connect(self.Start,SIGNAL("toggled(bool)"),self.Pause.setEnabled)
        self.connect(self.Stop,SIGNAL("toggled(bool)"),self.Start.setEnabled)
        self.connect(self.Stop,SIGNAL("toggled(bool)"),self.Pause.setEnabled)
        self.connect(self.Pause,SIGNAL("toggled(bool)"),self.InterruptReason.setEnabled)
        self.connect(self.Pause,SIGNAL("toggled(bool)"),self.LabelInterruptReason.setEnabled)

        self.setTabOrder(self.Category,self.Activity)
        self.setTabOrder(self.Activity,self.Description)
        self.setTabOrder(self.Description,self.Start)
        self.setTabOrder(self.Start,self.Pause)
        self.setTabOrder(self.Pause,self.Stop)
        self.setTabOrder(self.Stop,self.InterruptReason)
        self.setTabOrder(self.InterruptReason,self.StartDate)
        self.setTabOrder(self.StartDate,self.EndDate)
        self.setTabOrder(self.EndDate,self.TotalTime)


    def languageChange(self):
        self.setCaption(self.__tr("PSP - Tracker"))
        self.LabelActivity.setText(self.__tr("Activity"))
        self.ActivityManagement.setText(self.__tr("..."))
        self.LabelDescription.setText(self.__tr("Description"))
        self.Start.setText(self.__tr("Start"))
        self.Pause.setText(self.__tr("Pause"))
        self.Stop.setText(self.__tr("Stop"))
        self.LabelInterruptReason.setText(self.__tr("Interruption reason"))
        self.LabelStart.setText(self.__tr("Start"))
        self.LabelEnd.setText(self.__tr("End"))
        self.LabelTime.setText(self.__tr("Total time"))


    def MainForm_destroyed(self,a0):
        print "MainForm.MainForm_destroyed(QObject*): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("MainForm",s,c)
