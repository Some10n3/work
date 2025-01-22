### Tetrahedron.py ###
from OpenGL.GL import *
from Mesh import *

class Tetrahedron(Mesh):
    """
    Represents a 3D tetrahedron using vertices and triangle indices.
    Inherits from the Mesh class to utilize the draw method.
    """

    def __init__(self, draw_type):
        """
        Initializes the Tetrahedron with specific vertices and triangles.

        :param draw_type: OpenGL draw type (e.g., GL_LINE_LOOP, GL_TRIANGLES)
        """

        self.vertices = [
            (0.0, 1.0, 0.0),  
            (0.0, 0.0, 1.0),  
            (1.0, 0.0, 0.0),  
            (0.0, 0.0, -1.0)  
        ]

        self.triangles = [
            0, 1, 2,
            0, 2, 3,
            0, 3, 1,
            1, 3, 2
        ]

        # Pass initialization to parent class
        super().__init__(self.vertices, self.triangles, draw_type)