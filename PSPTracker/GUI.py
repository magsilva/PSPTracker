import qt
import psptracker.Main

def main( args ):
	app = qt.QApplication( args )
	qt.QObject.connect( app, qt.SIGNAL( 'lastWindowClosed()' ), app, qt.SLOT( 'quit()' ) )

	trackerUI = psptracker.Main()
	app.setMainWidget( trackerUI )
	trackerUI.show()
	app.exec_loop()
