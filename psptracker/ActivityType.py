from Activity import Activity
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
