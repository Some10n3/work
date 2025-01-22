from OpenGL.GL import *
from Mesh import Mesh  # Inherit from the original Mesh class

class LoadMesh(Mesh):
    """
    A class to load and store 3D mesh data from .obj files.
    """

    def __init__(self, filename, draw_type):
        self.filename = filename
        self.draw_type = draw_type
        super().__init__()  # Initialize the Mesh parent class
        self.load_drawing()  # Load vertices and triangles from the .obj file

    def load_drawing(self):
        """
        Parses the .obj file and populates vertices and triangles.
        """
        with open(self.filename) as fp:
            for line in fp:
                if line.startswith("v "):  # Vertex definition
                    vx, vy, vz = map(float, line[2:].split())
                    self.vertices.append((vx, vy, vz))
                elif line.startswith("f "):  # Face definition
                    face = [int(value.split('/')[0]) - 1 for value in line[2:].split()]
                    self.triangles.extend(face)
        print(f"Loaded {len(self.vertices)} vertices and {len(self.triangles) // 3} faces.")
