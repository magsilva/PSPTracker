import os

APP_NAME = "PSPTracker"
VERSION = "1.0.0"
DEFAULT_TRACKER = "default"
DEFAULT_DATA_DIR = os.path.join( os.path.abspath( os.path.expanduser( "~" ) ), "." + APP_NAME.lower() )
DEFAULT_CONF_FILE = os.path.join( os.path.abspath( os.path.expanduser( "~" ) ), "." + APP_NAME.lower() + "rc" );
