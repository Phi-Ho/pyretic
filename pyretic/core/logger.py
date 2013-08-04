import datetime
import os

class simpleLogger(object):
  def __init__(self, baseName=None, logLevel=0, timeStamped=True):
  
    logFile = None
    LOGLEVEL        = int(os.environ["PYRETICLOGLEVEL"])
    doLog = logLevel >= LOGLEVEL
    self.doLog = doLog
    
    if baseName != None:
      
      if not doLog:
        return
        
      datetimeNow = datetime.datetime.now()
      timeNow     = datetimeNow.strftime("%H:%M:%S.%f")

      logDirPathName  = os.environ["PYRETICLOGDIR"].split(".")[0]  
      logFileName = baseName
      
      if timeStamped:
        logFileName = "%s-%s" % (timeNow, baseName)
              
      logFilePathName = "%s/%s" % (logDirPathName, logFileName)
      
      logFile = open(logFilePathName, 'w', 1)
      logFile.write("Created: %s\n" % timeNow)
      
    self.logFile = logFile
   
  def write(self, logLine, timeStamped=False):
  
    if not self.doLog:
      return
      
    if self.logFile == None:
      from time import sleep
      sleep(0.1)
      print(logLine)
      
    else:
      if timeStamped:
        timeNow = datetime.datetime.now().strftime("%H:%M:%S.%f")
        thisLine = "\n%s: %s" % (timeNow, logLine)
      
      else:
        thisLine = "\n%s" % logLine
        
      self.logFile.write(thisLine)
      
     
