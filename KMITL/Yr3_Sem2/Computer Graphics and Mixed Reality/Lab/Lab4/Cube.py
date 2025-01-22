### Cube.py ###
from OpenGL.GL import *
from Mesh import *

class Cube(Mesh):
    """
    Represents a 3D cube using vertices and triangle indices.
    Inherits from the Mesh class to utilize the draw method.
    """

    def __init__(self, draw_type):
        """
        Initializes the Cube with specific vertices and triangles.

        :param draw_type: OpenGL draw type (e.g., GL_LINE_LOOP, GL_TRIANGLES)
        """

        self.vertices = [
            (0.5, -0.5, 0.5),  
            (-0.5, -0.5, 0.5), 
            (0.5, 0.5, 0.5),   
            (-0.5, 0.5, 0.5),  
            (0.5, 0.5, -0.5),  
            (-0.5, 0.5, -0.5), 
            (0.5, -0.5, -0.5), 
            (-0.5, -0.5, -0.5) 
        ]


        self.triangles = [
            0, 1, 3, 0, 3, 2,
            6, 7, 5, 6, 5, 4,
            1, 7, 5, 1, 5, 3,
            0, 2, 4, 0, 4, 6,
            2, 3, 5, 2, 5, 4,
            0, 6, 7, 0, 7, 1
        ]

        # Pass initialization to parent class
        super().__init__(self.vertices, self.triangles, draw_type)
