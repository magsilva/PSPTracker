import logging
import os 
import sys

debug = logging.getLogger("settings").debug
error = logging.getLogger("settings").error

class Settings(dict):

    def __init__(self, settings=None):
        dict.__init__(self)
        self.filename = settings.filename

        if not filename:
            error("Could not discover the config filename")

        self.loadSettings()
        for k,v in settings.items():
            self.__setitem__( k, v )
        

    def __getitem__(self, k):
        try:
            return dict.__getitem__(self, k)
        except:
            error("Could not locate setting %s", k)
            return ""


    def setFilename(self, filename):
        self.filename = filename


    def loadSettings(self):
        if not os.access(self.filename, os.R_OK):
            self.createInitialSettings()

        fp = None
        try:
            fp = open(self.filename, "r")
            for line in fp:
                line = line.strip()
                if not line or line[0] == '#': continue
                name, value = line.split(':', 1)
                name = name.strip().lower()
                value = value.strip()
                dict.__setitem__(self, name, value)
            fp.close()
            debug("Loaded settings from: %s", self.filename)
        except Exception, e:
            error(e)

        if fp:
            fp.close()    

    
    def saveSettings(self):
        fp = None
        try:
            fp = open(self.filename, "w")
            
            for k,v in self.items():
                fp.write("%s: %s\n" % (k,v))
                
        except Exception, e:
            error("Could not saveSettings", e)

        if fp:
            fp.close()

            
    def createInitialSettings(self):
        try:
            fp = open(self.filename, "w")
        except Exception, e:
            error("Could not write file: %s - %s", self.filename, str(e))
            sys.exit(1)          

        fp.close()
