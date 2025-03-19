from .Mesh import *

class Pentagon(Mesh):
    def __init__(self, program_id, location):
        vertices = [
            [ 0.0,  0.5, 0.0],  # Top
            [ 0.5,  0.2, 0.0],  # Upper right
            [ 0.3, -0.5, 0.0],  # Lower right
            [-0.3, -0.5, 0.0],  # Lower left
            [-0.5,  0.2, 0.0]   # Upper left
        ]

        colors = [
            [1.0, 0.0, 0.0],  # Red
            [0.0, 1.0, 0.0],  # Green
            [0.0, 0.0, 1.0],  # Blue
            [1.0, 1.0, 0.0],  # Yellow
            [1.0, 0.0, 1.0]   # Purple
        ]
        super().__init__(program_id, vertices, colors, GL_TRIANGLE_FAN, location)