from .Mesh import *

class Hexagon(Mesh):
    def __init__(self, program_id, location):
        # Create hexagon vertices (in 3D space)
        vertices = [
            [ 0.0,  0.5, -1.0],    # Top
            [ 0.43, 0.25, -1.0],   # Upper right
            [ 0.43, -0.25, -1.0],  # Lower right
            [ 0.0, -0.5, -1.0],    # Bottom
            [-0.43, -0.25, -1.0],  # Lower left
            [-0.43, 0.25, -1.0]    # Upper left
        ]

        # Define colors for each vertex
        colors = [
            [1.0, 0.0, 0.0],  # Red
            [1.0, 1.0, 0.0],  # Yellow
            [0.0, 1.0, 0.0],  # Green
            [0.0, 1.0, 1.0],  # Cyan
            [0.0, 0.0, 1.0],  # Blue
            [1.0, 0.0, 1.0]   # Magenta
        ]
        
        super().__init__(program_id, vertices, colors, GL_TRIANGLE_FAN, location)