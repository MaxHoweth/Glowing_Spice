import os


name = "UNKNOWN_NAME"
#counter = 100
#print counter
#wait = input("PRESS ENTER TO CONTINUE.")
#firstTimeRunning()

def testForConfig():
    
    filename = "Glowing_Spice.py"
    path = os.path.realpath(__file__)
    cutpath = path[0:path.index(filename)]
    fullpath = cutpath + "settings.cfg"
    return os.path.exists(fullpath)

def firstTimeRunning():
    name = raw_input("Please enter your preferred user name: ")

if testForConfig() == True:
    print "The file exists"
    i = raw_input()
else:
    firstTimeRunning()


