PYUIC    = pyuic
PYTHON   = python

FORMS = AbstractRealtimeTracker.py AbstractOfflineTracker.py
DESTDIR  = 
TARGET = PSPTracker.py

.ui.py:
	$(PYUIC) -o $@ $<

all: $(TARGET)

$(TARGET): $(FORMS)

clean:
	rm -f *~ *.pyc *.pyo
	rm -f Documentation/Project/*.bak.*
