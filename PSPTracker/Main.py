import AbstractMain

class Main( AbstractMain ):
	def __init__( self ):
		AbstractMain.__init__( self )
		self.realtimeTracker = RealtimeTracker()
		self.setCentralWidget( self.realtimeTracker )
