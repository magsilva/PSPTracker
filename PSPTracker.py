import sys
import random
import time
from qt import *

# from Main import Main
# from RealtimeTracker import RealtimeTracker
# from OfflineTracker import OfflineTracker
from TrackerFactory import TrackerFactory
from Tracker import Tracker
from ActivityType import ActivityType
from Activity import Activity

def main( args ):
	app = QApplication( args )
	QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )
	tracker = TrackerFactory.load( "teste" )

	try:
		activityType = tracker.createActivityType( "Teste", "Description for teste" )
	except Exception:
		activityType = tracker.chooseActivityType( "Teste"  )

	random.seed()

	for i in range(0,10):
		activity = activityType.instantiate( "teste" + str( i ) )
		activity.start()
		if random.random() > 0.5:
			print "Lazy guy...\n"
			activity.pause()
			activity.pause()
		activity.stop()

	print tracker.toCSV()
	TrackerFactory.save( "teste", tracker )

#	trackerUI = RealtimeTracker()
#	trackerUI = OfflineTracker()
#	app.setMainWidget( trackerUI )
#	trackerUI.show()
#	app.exec_loop()

if __name__ == "__main__":
	main( sys.argv )
