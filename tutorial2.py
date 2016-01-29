from ggame import App, Color, LineStyle, Sprite
from ggame import CircleAsset

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, black)
circleb = CircleAsset(5, thinline, blue)
circler = CircleAsset(5, thinline, red)
xcoordinates = range(100, 600, 10)

# Generate a list of sprites that form a line!
sprites = [Sprite(circleb, (x, x*.001 + 100)) for x in xcoordinates]
sprites = [Sprite(circler, (x, x*2 + 20)) for x in xcoordinates]

myapp = App()
myapp.run()
