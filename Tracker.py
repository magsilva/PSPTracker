class Tracker(object):

	def __init__( self, filename = "" ):
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

	def exportCSV( self ):
		csv = ""
		for i in self.activities:
			csv += i.name + "," + i.description + ","  + i.elapsedTime() + "," + i.interruptionTime() + "," + i.netTime() + "\n"
		return csv
