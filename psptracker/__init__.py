import os

APP_NAME = "PSPTracker"
VERSION = "1.0.0"
DEFAULT_DATA_DIR = os.path.join( os.path.abspath( os.path.expanduser( "~" ) ), "." + APP_NAME.lower() )
DEFAULT_CONF_FILE = os.path.join( os.path.abspath( os.path.expanduser( "~" ) ), "." + APP_NAME.lower() + "rc" );

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
