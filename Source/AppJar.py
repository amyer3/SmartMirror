import MirrorData as md
from appJar import *


newsarr = md.news()
font = 50
app = gui()
app.setGeometry("fullscreen")
#app.hideTitleBar()
app.setBg("black")
#app.setExpand("both")

app.setSticky("ne")
app.addLabel("wthr", md.weather(), 0, 2)

app.setSticky("nw")
app.addLabel("time", md.times(), 0, 0, 1)

app.setSticky("s")
app.addLabel("news", newsarr[1], 4, 0, 4)

app.setFg("white")
app.setLabelFont(font)
app.go()
