PYUIC    = pyuic
PYTHON   = python

FORMS = AbstractMain.py AbstractRealtimeTracker.py AbstractOfflineTracker.py
DESTDIR  = 
TARGET = PSPTracker.py

%.py: PSPTracker/forms/%.ui
	$(PYUIC) $< -o PSPTracker/$@ 

all: $(FORMS)


clean:
	rm -f *~ *.pyc *.pyo Abstract*.py
	rm -f PSPTracker/*~ PSPTracker/*.pyc PSPTracker/*.pyo PSPTracker/Abstract*.py
	rm -f docs/*.bak.*
