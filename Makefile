PYUIC    = pyuic
PYTHON   = python

FORMS = AbstractMain.py AbstractRealtimeTracker.py AbstractOfflineTracker.py
DESTDIR  = 
TARGET = PSPTracker.py

%.py: %.ui
	$(PYUIC) $< -o $@ 

all: $(FORMS)


clean:
	rm -f *~ *.pyc *.pyo
	rm -f Documentation/Project/*.bak.*
