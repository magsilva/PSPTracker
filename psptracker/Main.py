from AbstractMain import AbstractMain

class Main( AbstractMain ):
	def __init__( self, *args ):
		AbstractMain.__init__( self, *args )
		self.realtimeTracker = RealtimeTracker()
		self.setCentralWidget( self.realtimeTracker )
