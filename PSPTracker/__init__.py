import os

app_name = "PSPTracker"
version = '1.0.0'

home_dir = os.path.basename( os.path.abspath( os.path.expanduser( "~" ) ) )
base_dir = os.path.join( home_dir, "." + app_name.lower() )

__all__ = [
	"AbstractMain",
	"AbstractOfflineTracker",
	"AbstractRealtimeTracker",
	"Activity",
	"ActivityType",
	"Main",
	"OfflineTracker",
	"RealtimeTracker",
	"Tracker",
	"TrackerFactory"
]
