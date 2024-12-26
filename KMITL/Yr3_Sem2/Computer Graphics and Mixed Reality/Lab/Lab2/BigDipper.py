import pygame 
from pygame.locals import * 
from OpenGL.GL import *
from OpenGL.GLU import *
pygame.init()
screen_width = 1000 
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL) 
pygame.display.set_caption("OpenGL in Python")

def init_ortho():
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480)
done = False 
init_ortho()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity() 

    # glBegin(GL_POINTS) 
    # glVertex2i(100, 50) 
    # glVertex2i(600, 450) 
    # glEnd()
    glPointSize(15)
    glBegin(GL_POINTS)
    glVertex2i(68, 192)  #1
    glVertex2i(205, 240) #3
    glVertex2i(342, 192) #5
    glEnd()

    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2i(136, 240) #2
    glVertex2i(410, 336) #6
    glVertex2i(478, 240) #7
    glEnd()

    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2i(273, 240) #4
    glEnd()


    pygame.display.flip() 
    pygame.time.wait(100)

pygame.quit()