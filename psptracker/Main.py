from PSPTracker import *
import AbstractMain
import RealtimeTracker

__all__ = [ "Main" ]

class Main( PSPTracker.AbstractMain ):
	def __init__( self ):
		AbstractMain.__init__( self )
		self.realtimeTracker = RealtimeTracker()
		self.setCentralWidget( self.realtimeTracker )
