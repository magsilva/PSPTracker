PYUIC    = pyuic
PYTHON   = python

SOURCES = main.cpp
OBJECTS = mainform.pyo
FORMS = mainform.ui
DESTDIR  = 
TARGET   = psp

.ui.py:
	$(PYUIC) > $@ $<

.py.pyo:
	$(PYTHON) -O $(CXXFLAGS) $(INCPATH) -o $@ $<

$(TARGET): $(OBJECTS) $(OBJMOC)  
