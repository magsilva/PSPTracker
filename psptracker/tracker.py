from activity import ActivityType
from time import *
from pickle import *


class Tracker(object):

	def __init__( self ):
		self.activities = {}
		self.categories = {}

	def listCategories( self ):
		return self.categories.keys()

	def categorizeActivityType( self, activityType, category ):
		if not self.categories.has_key( category ):
			self.categories[ category ] = []
		if not self.categories[ category ].index( activityType ):
			self.categories[ category ].append( activityType )

	def uncategorizeActivityType( self, activityType, category ):
		if not self.categories.has_key( category ):
			raise Exception( "The category " + category + " doesn't exist." )
		try:
			self.categories[ category ].remove( activityType )
		except ValueError:
			raise Exception( "The activity type " + activityType + " doesn't belog to the category " + category + "." )

	def listActivityTypes( self, category = "" ):
		if category == "":
			return self.activities.keys()
		else:
			return self.categories[ category ].keys()

	def chooseActivityType( self, type = "" ):
		try:
			return self.activities[ type ]
		except ValueError:
			raise Exception( "Activity type could not be found." )

	def createActivityType( self, name, description = "" ):
		if self.activities.has_key( name ):
			raise Exception( "This activity type already exists." )
		else:
			activityType = ActivityType( name, description )
			self.activities[ name ] = activityType
			return activityType

	def deleteActivityType( self ):
		del( self.activities[ name ] )

	def toCSV( self ):
		csv = ""
		for i in self.activities:
			csv += self.activities[ i ].toCSV() + "\n"
		return csv




class TrackerFactory( object ):

	trackers = {}

	def __init__( self ):
		pass


	def load( cls, trackerName ):
		if not cls.trackers.has_key( trackerName ):
			try:
				file = open( trackerName, "r" )
				unpickler = Unpickler( file )
				cls.trackers[ trackerName ] = unpickler.load()
			except IOError:
				tracker = Tracker()
				cls.save( trackerName, tracker )
				cls.trackers[ trackerName ] = tracker

		return cls.trackers[ trackerName ]

	load = classmethod( load )


	def save( cls, trackerName, tracker ):
		file = open( trackerName, "w+" )
		pickler = Pickler( file, HIGHEST_PROTOCOL )
		return pickler.dump( tracker )

	save = classmethod( save )
