from pickle import *
from Tracker import Tracker

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
