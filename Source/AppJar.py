import Source.MirrorData as md
from appJar import *


app = gui()
app.addLabel("l1", "Simple Demo")
app.addEntry("text")
app.addButton("OK")
app.addEmptyLabel("l2")
app.go()