from time import *


class ActivityType(object):

	def __init__( self, name = "", description = "" ):
		self.logs = []
		self.name = name
		self.description = description

	def elapsedTime( self ):
		totalTime = 0
		for i in self.logs:
			totalTime += i.elapsedTime()
		return totalTime

	def interruptionTime( self ):
		totalTime = 0
		for i in self.logs:
			totalTime += i.interruptionTime()
		return totalTime

	def netTime( self ):
		return self.elapsedTime() - self.interruptionTime()

	def instantiate( self, description = "" ):
		activity = Activity( description )
		self.logs.append( activity )
		return activity

	def cancel( self, activity ):
		try:
			self.logs.remove( activity )
		except ValueError:
			raise Exception( "Activity not found" )

	def toCSV( self ):
		csv = ""
		csv = self.name + "," + self.description + "," + str( self.elapsedTime() ) + "," + str( self.interruptionTime() )
		return csv


class Interruption(object):

	def __init__( self, reason = "" ):
		self.reason =  reason
		self.startTime = 0
		self.stopTime = 0




class Activity(object):

	def __init__( self, description = "" ):
		self.startTime = 0
		self.stopTime = 0
		self.interruptions = []
		self.state = "stopped"
		self.description = description
		print self.description

	def start( self ):
		if self.state == "stopped":
			self.startTime = time()
			self.state = "started"
		else:
			raise Exception( "Activity in execution already (you need to stop it in order to start a new instance" )

	def stop( self ):
		if self.state == "started" or self.state == "paused":
			self.stopTime = time()
			self.state = "stopped"
		else:
			raise Exception( "There is no activity running." )

	def pause( self, reason = "" ):
		if self.state == "started":
			interruption = Interruption( reason )
			interruption.startTime = time()
			self.interruptions.append( interruption )
			self.state = "paused"
		elif self.state == "paused":
			interruption = self.interruptions[ -1 ]
			interruption.stopTime = time()
			self.state = "started"
		else:
			raise Exception( "There is no activity running." )

	def elapsedTime( self ):
		if self.state == "started" or self.state == "paused":
			return time() - self.startTime
		else:
			return self.stopTime - self.startTime

	def interruptionTime( self ):
		fruitlessTime = 0
		for i in self.interruptions[:]:
			fruitlessTime += i.stopTime - i.startTime
		return fruitlessTime

	def netTime( self ):
		return self.elapsedTime() - self.interruptionTime()

	def toCSV( self ):
		csv = ""
		csv = self.description + "," + str( self.elapsedTime() ) + "," + str( self.interruptionTime() )
		return csv
