import sys
from qt import *

def main( args ):
    app = QApplication( args )
		trackerUI = TrackerUI()
		app.setMainWidget( trackerUI )
    trackerUI.show()
    app.exec_loop()

if __name__=="__main__":
    main( sys.argv )
