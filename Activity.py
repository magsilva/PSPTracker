import time

class Activity(object):

	def __init__( self, description = "" ):
		self.startTime = 0
		self.stopTime = 0 
		self.interruptions = []
		self.state = "stopped"
		self.description = description

	def start( self ):
		if self.state == "stopped":
			self.startTime = time.gmtime()
			self.state = "started"
		else:
			raise Exception( "Activity in execution already (you need to stop it in order to start a new instance" )

	def stop( self ):
		if self.state == "started" or self.state == "paused":
			self.stopTime = time.gmtime()
			self.state = "stopped"
		else:
			raise Exception( "There is no activity running." )

	def pause( self, reason = "" ):
		if self.state == "started":
			interruption = Interruption( reason )
			interruption.startTime = time.gmtime()
			self.interruptions.append( interruption )
			self.state = "paused"
		elif self.state == "paused":
			interruption = self.interruptions[-1]
			interruption.stopTime = time.gmtime()
			self.state = "started"
		else:
			raise Exception( "There is no activity running." )

	def elapsedTime( self ):
		if self.state == "started" or self.state == "paused":
			return time.gmtime() - self.startTime
		else:
			return self.stopTime - self.startTime

	def interruptionTime( self ):
		fruitlessTime = 0
		for i in interruptions[:]:
			fruitlessTime += i.stopTime - i.startTime
		return fruitlessTime

	def netTime( self ):
		return self.elapsedTime() - fruitlessTime
