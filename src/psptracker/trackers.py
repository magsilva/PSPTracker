import sys
from qt import *

from AbstractRealtimeTracker import AbstractRealtimeTracker
from AbstractOfflineTracker import AbstractOfflineTracker
from AbstractCategoryManager import AbstractCategoryManager

class CategoryManager(AbstractCategoryManager):
  def __init__(self, tracker, parent = None, name = None, modal = 0, fl = 0):
		AbstractCategoryManager.__init__(self, parent, name, modal, fl)
		self.tracker = tracker

#	widget = QtGui.QWidget()
#	widget.resize(250, 150)
#	widget.setWindowTitle('simple')
#	widget.show()

class RealtimeTracker(AbstractRealtimeTracker):
  def __init__(self, tracker, parent = None, name = None, modal = 0, fl = 0):
		AbstractRealtimeTracker.__init__(self, parent, name, modal, fl)
		self.tracker = tracker
		self.categoryManager = CategoryManager(tracker, parent = self)


class OfflineTracker(AbstractOfflineTracker):
  def __init__(self, tracker, parent = None, name = None, modal = 0, fl = 0):
		AbstractOfflineTracker.__init__(self, parent, name, modal, fl)
		self.tracker = tracker
