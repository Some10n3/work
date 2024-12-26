import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Corrected vertices and edges
vertices = [
    [-0.5, -0.5, -0.5],  # Vertex 0 back down left 
    [ 0.5, -0.5, -0.5],  # Vertex 1 back down right
    [ 0.5,  0.5, -0.5],  # Vertex 2 back up right
    [-0.5,  0.5, -0.5],  # Vertex 3 back up left
    [-0.5, -0.5,  0.5],  # Vertex 4 front down left
    [ 0.5, -0.5,  0.5],  # Vertex 5 front down right
    [ 0.5,  0.5,  0.5],  # Vertex 6 front up right
    [-0.5,  0.5,  0.5],  # Vertex 7 front up left
]

edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],
    [4, 5], [5, 6], [6, 7], [7, 4],
    [0, 4], [1, 5], [2, 6], [3, 7]
]

# Draw cube
def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Main program
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glRotatef(1, 0, 1, 0)  # Rotate around Y-axis

        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()
