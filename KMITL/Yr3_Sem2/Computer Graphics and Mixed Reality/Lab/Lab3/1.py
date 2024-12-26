import pygame
from OpenGL.GL import * 
from OpenGL.GLU import * 
from pygame.locals import *

def init_gl():
    glEnable(GL_DEPTH_TEST) 
    glClearColor(0.0, 0.0, 0.0, 1.0)

def draw_polygon(vertices, color):
    glBegin(GL_POLYGON)  # Start defining the polygon
    glColor3fv(color)    # Set the color for the polygon
    for vertex in vertices:
        glVertex3fv(vertex)  # Add each vertex to the polygon
    glEnd()  # End defining the polygon

def main():
    pygame.init() 
    display = (800, 600) 
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL) 
    pygame.display.set_caption('OpenGL Shapes Workshop')
    init_gl()
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()
    gluOrtho2D(-1, 1, -1, 1) 
    glMatrixMode(GL_MODELVIEW)
    current_shape = 'triangle' 
    clock = pygame.time.Clock() 
    fps = 60
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    current_shape = 'triangle' 
                elif event.key == pygame.K_s:
                    current_shape = 'square'
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                    
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        if current_shape == 'triangle': 
            draw_polygon([(-0.6, -0.4, 0.0), (0.6, -0.4, 0.0), (0.0, 0.6, 0.0)], (1.0, 0.0, 0.0)) 
        elif current_shape == 'square':
            draw_polygon([(-0.4, -0.4, 0.0), (0.4, -0.4, 0.0), (0.4, 0.4, 0.0), (-0.4, 0.4, 0.0)], (1.0, 1.0, 0.0))
        pygame.display.flip() 
        clock.tick(fps)

if __name__ == "__main__":
    main()
