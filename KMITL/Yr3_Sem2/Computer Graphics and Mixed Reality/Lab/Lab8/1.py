import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def bresenham_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    
    glBegin(GL_POINTS)
    while True:
        glVertex2i(x0, y0)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    screen = pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    gluOrtho2D(0, 800, 600, 0)
    clock = pygame.time.Clock()
    running = True
    points = []
    
    while running:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                points.append(event.pos)
        
        for i in range(0, len(points) - 1, 2):
            bresenham_line(points[i][0], points[i][1], points[i + 1][0], points[i + 1][1])
        
        print(points)  # Print all stored pairs of points every loop
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()