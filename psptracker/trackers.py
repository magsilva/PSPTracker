import sys
from qt import *

from AbstractRealtimeTracker import AbstractRealtimeTracker

class RealtimeTracker( AbstractRealtimeTracker ):
  def __init__( self, tracker, parent = None, name = None, modal = 0, fl = 0):
		AbstractRealtimeTracker.__init__( self, parent, name, modal, fl )
		self.tracker = tracker



from AbstractOfflineTracker import AbstractOfflineTracker

class OfflineTracker( AbstractOfflineTracker ):
  def __init__( self, tracker, parent = None, name = None, modal = 0, fl = 0):
		AbstractOfflineTracker.__init__( self, parent, name, modal, fl )
		self.tracker = tracker
