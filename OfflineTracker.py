import sys
from qt import *

from AbstractOfflineTracker import AbstractOfflineTracker

class OfflineTracker( AbstractOfflineTracker ):
  def __init__( self, parent = None, name = None, modal = 0, fl = 0):
		AbstractOfflineTracker.__init__( self, parent, name, modal, fl )
