import sys

from qt import QApplication
from psptracker import *

def main( args ):
	app = QApplication( args )
	QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )

	trackerUI = Main()
	app.setMainWidget( trackerUI )
	trackerUI.show()
	app.exec_loop()


if __name__ == "__main__":
	main( sys.argv )
