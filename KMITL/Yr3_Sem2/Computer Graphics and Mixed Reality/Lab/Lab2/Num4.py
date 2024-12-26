import pygame
from pygame.locals import * 
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init() 
screen_width = 1000 
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL) 
pygame.display.set_caption("Mouse Click Coordinates")
pos_clicked = []

def init_ortho():
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480)

def screen_to_opengl(x, y):
    """Convert screen coordinates to OpenGL coordinates""" 
    return (x * 640 // screen_width, 480 - (y * 480 // screen_height)) # Flip Y coordinate

def plot_pos(x, y):
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()

done = False 
init_ortho()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left mouse button
                # Get mouse position and convert to OpenGL coordinates 
                mouse_x, mouse_y = pygame.mouse.get_pos()
                opengl_x, opengl_y = screen_to_opengl(mouse_x, mouse_y) 
                print(f"Screen coordinates: ({mouse_x}, {mouse_y})") 
                print(f"OpenGL coordinates: ({opengl_x}, {opengl_y})") 
                print("---")
                pos_clicked.append((opengl_x, opengl_y))

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    for pos in pos_clicked:
        plot_pos(pos[0], pos[1])



    pygame.display.flip() 
    pygame.time.wait(10)
pygame.quit()