import sys
from qt import *

from AbstractMain import AbstractMain
from RealtimeTracker import RealtimeTracker

class Main( AbstractMain ):

	def __init__( self, *args ):
		AbstractMain.__init__( self, *args )
		self.realtimeTracker = RealtimeTracker()
		self.setCentralWidget( self.realtimeTracker )
