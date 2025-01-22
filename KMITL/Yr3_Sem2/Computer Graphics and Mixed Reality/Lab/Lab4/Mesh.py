### Mesh.py ###
from OpenGL.GL import *

class Mesh:

    def __init__(self, vertices=None, triangles=None, draw_type=GL_LINE_LOOP):

        # Allow overriding defaults
        self.vertices = vertices or []
        self.triangles = triangles or []
        self.draw_type = draw_type

    def draw(self):

        if not self.vertices or not self.triangles:
            print("Mesh has no vertices or triangles defined.")
            return
        
        glBegin(self.draw_type)
        for t in range(0, len(self.triangles), 3):
            glVertex3fv(self.vertices[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
        glEnd()