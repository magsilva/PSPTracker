PYUIC    = pyuic
PYTHON   = python

FORMS = AbstractMain.py AbstractRealtimeTracker.py AbstractOfflineTracker.py
DESTDIR  = 
TARGET = PSPTracker.py

%.py: psptracker/forms/%.ui
	$(PYUIC) $< -o psptracker/$@ 

all: $(FORMS)


clean:
	rm -f *~ *.pyc *.pyo Abstract*.py
	rm -f psptracker/*~ psptracker/*.pyc psptracker/*.pyo psptracker/Abstract*.py
	rm -f docs/*.bak.*
