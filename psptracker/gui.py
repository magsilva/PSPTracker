from qt import QApplication
import psptracker.Main

def main( args ):
	app = QApplication( args )

	trackerUI = psptracker.Main()
	app.setMainWidget( trackerUI )
	app.exec_loop()
