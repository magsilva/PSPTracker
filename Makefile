PYUIC    = pyuic
PYTHON   = python

FORMS = AbstractRealtimeTracker.py AbstractOfflineTracker.py AbstractCategoryManager.py AbstractActivityManager.py
DESTDIR  = 
TARGET = psptracker.py

%.py: psptracker/forms/%.ui
	$(PYUIC) $< -o psptracker/$@ 

all: $(FORMS)


clean:
	rm -f *~ *.pyc *.pyo Abstract*.py
	rm -f psptracker/*~ psptracker/*.pyc psptracker/*.pyo psptracker/Abstract*.py
	rm -f docs/*.bak.*
