PYUIC    = pyuic4
PYTHON   = python

FORMS = AbstractRealtimeTracker.py AbstractOfflineTracker.py AbstractCategoryManager.py AbstractActivityManager.py
DESTDIR  = 
TARGET = psptracker.py

%.py: src/psptracker/forms/%.ui
	$(PYUIC) $< -o src/psptracker/$@ 

all: $(FORMS)


clean:
	rm -f *~ *.pyc *.pyo Abstract*.py
	rm -f psptracker/*~ psptracker/*.pyc psptracker/*.pyo psptracker/Abstract*.py
	rm -f docs/*.bak.*
