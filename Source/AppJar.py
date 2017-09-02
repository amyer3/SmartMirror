import Source.MirrorData as md
from appJar import *


newsarr = md.news()
app = gui()
app.setBg("black")
#app.setExpand("both")

app.setSticky("ne")
app.addLabel("wthr", md.weather(), 0, 2)

app.setSticky("nw")
app.addLabel("time", md.times(), 0, 0, 1)

app.setSticky("s")
app.addLabel("news", newsarr[1], 4, 1, 1)

app.setFg("white")
app.setGeometry("fullscreen")
app.go()
