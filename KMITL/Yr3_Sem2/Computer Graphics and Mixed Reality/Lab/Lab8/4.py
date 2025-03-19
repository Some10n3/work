import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pywavefront
import math

# Load the 3D model
model = pywavefront.Wavefront('myphone2.obj', collect_faces=True)

def draw_model():
    """Render the 3D model."""
    glBegin(GL_TRIANGLES)
    for face in model.mesh_list[0].faces:
        for vertex_index in face:
            glVertex3fv(model.vertices[vertex_index])
    glEnd()

def main():
    # Initialize PyGame
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Set up OpenGL perspective
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, -2.0, -7)  # Move object into view
    glEnable(GL_DEPTH_TEST)  # Enable depth testing for proper 3D rendering

    angle = 0  # Rotation angle

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Rotate object
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glRotatef(angle, 0, 1, 0)  # Rotate around Y-axis
        draw_model()
        glPopMatrix()
        
        pygame.display.flip()
        pygame.time.wait(10)
        
        angle += 1  # Increase rotation angle

if __name__ == "__main__":
    main()
