# bezier_editor.py
import pygame
from pygame.locals import *
from OpenGL.GL import *
import numpy as np

def bezier_curve(t, p0, p1, p2, p3):
    """Calculate a point on a cubic Bézier curve."""
    return (1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3

def draw_curve():
    """Draw the cubic Bézier curve using OpenGL."""
    glColor3f(1, 1, 1)
    glBegin(GL_LINE_STRIP)
    for t in np.linspace(0, 1, 100):
        x, y = bezier_curve(t, *control_points)
        glVertex2f(x, y)
    glEnd()

def draw_control_points():
    """Draw control points as small squares."""
    glColor3f(1, 0, 0)
    for x, y in control_points:
        glBegin(GL_QUADS)
        glVertex2f(x - 5, y - 5)
        glVertex2f(x + 5, y - 5)
        glVertex2f(x + 5, y + 5)
        glVertex2f(x - 5, y + 5)
        glEnd()

def draw_control_polygon():
    """Draw lines connecting control points to visualize the control polygon."""
    glColor3f(0, 1, 0)
    glBegin(GL_LINE_STRIP)
    for x, y in control_points:
        glVertex2f(x, y)
    glEnd()

def find_selected_point(mouse_pos):
    """Check if a control point is clicked."""
    mx, my = mouse_pos
    for i, (x, y) in enumerate(control_points):
        if abs(mx - x) < 10 and abs(my - y) < 10:
            return i
    return None

pygame.init()
screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Bézier Curve Editor")
glOrtho(0, 800, 600, 0, -1, 1)

# Initial control points
control_points = [
    np.array([100, 500]),
    np.array([250, 100]),
    np.array([550, 100]),
    np.array([700, 500])
]

selected_point = None
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            selected_point = find_selected_point(event.pos)
        elif event.type == MOUSEBUTTONUP:
            selected_point = None
        elif event.type == MOUSEMOTION and selected_point is not None:
            control_points[selected_point] = np.array(event.pos)
    
    glClear(GL_COLOR_BUFFER_BIT)
    draw_curve()
    draw_control_points()
    draw_control_polygon()
    pygame.display.flip()

pygame.quit()
