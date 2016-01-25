from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)


thinline = LineStyle(1, black)

ellipse = EllipseAsset(40, 50, thinline, blue)
rectangle = RectangleAsset(200, 604, thinline, red)

Sprite(ellipse, (200, 50))

Sprite(rectangle, (100, 0))
myapp = App()
myapp.run()
