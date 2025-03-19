import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import time

# Define triangles (Vertices with RGBA Colors)
triangles = [
    # Red triangle (closer)
    [[-1, -1, -2], [1, -1, -2], [0, 1, -2], [1, 0, 0, 0.8]], 
    # Green triangle (mid)
    [[-1, -1, -4], [1, -1, -4], [0, 1, -4], [0, 1, 0, 0.8]],  
    # Blue triangle (farther)
    [[-1, -1, -6], [1, -1, -6], [0, 1, -6], [0, 0, 1, 0.8]],  
]

def draw_triangles():
    """ Draws the three triangles with colors and depth. """
    glBegin(GL_TRIANGLES)
    for tri in triangles:
        color = tri[3]
        for vertex in tri[:3]:
            glColor4fv(color)  # Set color with transparency
            glVertex3fv(vertex)  # Set vertex position
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Set up perspective projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0] / display[1]), 1, 50)
    glMatrixMode(GL_MODELVIEW)
    
    # Enable depth testing (Z-buffer)
    glEnable(GL_DEPTH_TEST)
    
    # Set up camera view
    gluLookAt(0, 2, 10, 0, 0, 0, 0, 1, 0)  # Camera at (0,2,10) looking at origin

    clock = pygame.time.Clock()
    rotation_angle = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear screen and depth buffer

        # Apply rotation to the scene
        glLoadIdentity()
        gluLookAt(0, 2, 10, 0, 0, 0, 0, 1, 0)
        glRotatef(rotation_angle, 1, 1, 0)  # Rotate around X and Y axis

        draw_triangles()  # Draw the triangles

        pygame.display.flip()  # Update display
        clock.tick(60)  # Limit FPS to 60

        rotation_angle += 1  # Increment rotation angle

    pygame.quit()

if __name__ == "__main__":
    main()