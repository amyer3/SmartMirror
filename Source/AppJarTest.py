from appJar import gui
import Source.MirrorData as md


app = gui()
app.addLabel("w", md.weather())
app.setLabelFg("w", "white")
app.addLabel("t", md.times())
app.setLabelFg("t", "white")
app.addLabel("s", md.stocks())
app.setLabelFg("s", "white")
app.setBg("black")
app.go()
