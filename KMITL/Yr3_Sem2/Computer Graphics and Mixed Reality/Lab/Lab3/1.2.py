import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import math

# Initialize transformation variables
current_shape = 'triangle'
current_color = [1.0, 0.0, 0.0]  # RGB
scale = 1.0
rotation_angle = 0.0
color_increasing = True  # Toggle for color adjustment

# Shape vertices
shapes = {
    'triangle': [(-0.6, -0.4, 0.0), (0.6, -0.4, 0.0), (0.0, 0.6, 0.0)],
    'square': [(-0.4, -0.4, 0.0), (0.4, -0.4, 0.0), (0.4, 0.4, 0.0), (-0.4, 0.4, 0.0)],
    'pentagon': [
        (0.0, 0.6, 0.0), (-0.5, 0.2, 0.0), (-0.3, -0.5, 0.0),
        (0.3, -0.5, 0.0), (0.5, 0.2, 0.0)
    ]
}

# Matrix transformations
def apply_scale(vertices, factor):
    scaled_vertices = []
    for x, y, z in vertices:
        scaled_vertices.append((x * factor, y * factor, z))
    return scaled_vertices

def apply_rotation(vertices, angle):
    rotated_vertices = []
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    for x, y, z in vertices:
        rotated_vertices.append((
            x * cos_theta - y * sin_theta,
            x * sin_theta + y * cos_theta,
            z
        ))
    return rotated_vertices

def draw_polygon(vertices, color):
    glBegin(GL_POLYGON)
    glColor3fv(color)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()

def handle_input():
    global current_shape, current_color, scale, rotation_angle, color_increasing
    keys = pygame.key.get_pressed()

    # Shape Selection
    if keys[pygame.K_t]:
        current_shape = 'triangle'
    elif keys[pygame.K_s]:
        current_shape = 'square'
    elif keys[pygame.K_p]:
        current_shape = 'pentagon'

    # Toggle color adjustment mode
    if keys[pygame.K_c]:  # Press 'C' to toggle
        color_increasing = not color_increasing
        pygame.time.wait(200)  # Prevent rapid toggling

    # Color Modification
    adjustment = 0.01 if color_increasing else -0.01
    if keys[pygame.K_r]:
        current_color[0] = max(0.0, min(current_color[0] + adjustment, 1.0))
    if keys[pygame.K_g]:
        current_color[1] = max(0.0, min(current_color[1] + adjustment, 1.0))
    if keys[pygame.K_b]:
        current_color[2] = max(0.0, min(current_color[2] + adjustment, 1.0))

    # Size Control
    if keys[pygame.K_UP]:
        scale += 0.01
    if keys[pygame.K_DOWN]:
        scale = max(0.01, scale - 0.01)

    # Rotation
    if keys[pygame.K_LEFT]:
        rotation_angle -= 0.05  # Counterclockwise
    if keys[pygame.K_RIGHT]:
        rotation_angle += 0.05  # Clockwise

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Enhanced OpenGL Shapes Workshop')
    gluOrtho2D(-1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)

    clock = pygame.time.Clock()
    fps = 60

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        handle_input()

        # Clear screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Transform and draw shape
        vertices = shapes[current_shape]
        transformed_vertices = apply_scale(vertices, scale)
        transformed_vertices = apply_rotation(transformed_vertices, rotation_angle)
        draw_polygon(transformed_vertices, current_color)

        # Refresh display
        pygame.display.flip()
        clock.tick(fps)

if __name__ == "__main__":
    main()
