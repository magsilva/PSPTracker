import sys
import logging

from psptracker import *
from psptracker.trackers import *
from optparse import OptionParser
from psptracker.settings import Settings

def main( args ):
    debug = logging.getLogger( "psptracker" ).debug
    debug("%s v%s starting up..." % APP_NAME, VERSION)
    parser = OptionParser()
    parser.add_option("-c", "--config",
                      dest="configfile",
                      default=DEFAULT_CONF_FILE,
                      metavar=DEFAULT_CONF_FILE,
                      help="Specify the filename for application configuration")
    parser.add_option("-d", "--datadir",
                      dest="datadir",
                      default=DEFAULT_DATA_DIR,
                      metavar=DEFAULT_DATA_DIR,
                      help="Specify the base directory for application data")

    (options, args) = parser.parse_args()

    settings = Settings(options)
    try:
        os.makedirs(settings.get('datadir'))
    except Exception, e:
        if e[0] != 17:
            print e
            sys.exit(1)

    app = QApplication( args )

    trackerUI = psptracker.Main()
    trackerUI = RealtimeTracker()

    app.setMainWidget( trackerUI )
    app.exec_loop()


if __name__ == "__main__":
    main( sys.argv )
