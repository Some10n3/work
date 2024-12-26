import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np

def bezier_curve(control_points, t):
    """Generate points along a Bezier curve defined by control points."""
    n = len(control_points) - 1
    curve = []
    for i in range(n + 1):
        bernstein = binomial_coefficient(n, i)
        point = sum(bernstein * cp for cp in control_points[i])
        curve.append(point)
    return np.array(curve)

def binomial_coefficient(n, k):
    result = 1
    for i in range(1, k + 1):
        result *= (n - i + 1) / i
    return result

def generate_cylinder_body(radius=0.5, length=4.0, segments=20):
    control_points = [
        [0, 0, -length/2],
        [radius, 0, -length/4],
        [radius, 0, length/4],
        [0, 0, length/2]
    ]
    side_profile = bezier_curve(control_points[:4], t=np.linspace(0, 1, segments))
    
    
    vertices = []
    for i in range(segments):
        x = side_profile[i][0] * np.cos(2 * np.pi * i / segments)
        y = side_profile[i][1] * np.sin(2 * np.pi * i / segments)
        z = side_profile[i][2]
        vertices.append([x, y, z])
    
    return vertices

def generate_faces(vertices, segments):
    faces = []
    n = len(vertices)
    for i in range(0, n - segments, segments):
        for j in range(segments - 1):
            faces.append([i + j, i + j + 1, i + j + segments])
            faces.append([i + j + 1, i + j + segments, i + j + segments + 1])
        faces.append([i + segments - 1, i, i + 2*segments - 1])
        faces.append([i, i + segments - 1, i + segments])
    return faces

def draw_cylinder(vertices, faces):
    glBegin(GL_TRIANGLES)
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

# Initialize scaling and rotation values
scale = 1.0
rotation = [0, 0]

def main():
    global scale, rotation

    # Initialize pygame and OpenGL
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, display[0] / display[1], 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)

    # Generate the cylinder body
    segments = 20
    cylinder_vertices = generate_cylinder_body(radius=0.5, length=4.0, segments=segments)
    cylinder_faces = generate_faces(cylinder_vertices, segments)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rotation[0] -= 5
                elif event.key == pygame.K_DOWN:
                    rotation[0] += 5
                elif event.key == pygame.K_LEFT:
                    rotation[1] -= 5
                elif event.key == pygame.K_RIGHT:
                    rotation[1] += 5
                elif event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                    scale += 0.1
                elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                    scale -= 0.1

        # Clear screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Apply transformations
        glPushMatrix()
        glScalef(scale, scale, scale)
        glRotatef(rotation[0], 1, 0, 0)
        glRotatef(rotation[1], 0, 1, 0)

        # Draw the airplane body as a cylinder
        draw_cylinder(cylinder_vertices, cylinder_faces)

        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
