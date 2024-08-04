# bridge_pattern.py

from abc import ABC, abstractmethod

# Implementor
class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius):
        pass

    @abstractmethod
    def render_square(self, side):
        pass

# Concrete Implementors
class VectorRenderer(Renderer):
    def render_circle(self, radius):
        return f"Drawing a circle of radius {radius} using vector graphics"

    def render_square(self, side):
        return f"Drawing a square of side {side} using vector graphics"

class RasterRenderer(Renderer):
    def render_circle(self, radius):
        return f"Drawing a circle of radius {radius} using raster graphics"

    def render_square(self, side):
        return f"Drawing a square of side {side} using raster graphics"

# Abstraction
class Shape(ABC):
    def __init__(self, renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass

# Refined Abstractions
class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        return self.renderer.render_circle(self.radius)

class Square(Shape):
    def __init__(self, renderer, side):
        super().__init__(renderer)
        self.side = side

    def draw(self):
        return self.renderer.render_square(self.side)

# Client code
if __name__ == "__main__":
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()

    circle1 = Circle(vector_renderer, 5)
    circle2 = Circle(raster_renderer, 7)
    square1 = Square(vector_renderer, 4)
    square2 = Square(raster_renderer, 6)

    shapes = [circle1, circle2, square1, square2]

    for shape in shapes:
        print(shape.draw())
