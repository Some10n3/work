import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import math
import numpy

def init_gl():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, (1, 1, 1, 0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.8, 0.8, 0.8, 1))
    glEnable(GL_COLOR_MATERIAL)

def draw_cube(vertices):
    glBegin(GL_QUADS)
    glNormal3fv((0, 0, -1))
    for vertex in vertices[0]:
        glVertex3fv(vertex)
    glNormal3fv((0, 0, 1))
    for vertex in vertices[1]:
        glVertex3fv(vertex)
    glNormal3fv((-1, 0, 0))
    for vertex in vertices[2]:
        glVertex3fv(vertex)
    glNormal3fv((1, 0, 0))
    for vertex in vertices[3]:
        glVertex3fv(vertex)
    glNormal3fv((0, -1, 0))
    for vertex in vertices[4]:
        glVertex3fv(vertex)
    glNormal3fv((0, 1, 0))
    for vertex in vertices[5]:
        glVertex3fv(vertex)
    glEnd()

def scale_matrix(sx, sy, sz):
    return numpy.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])

def rotate_matrix_z(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    c = math.cos(angle_radians)
    s = math.sin(angle_radians)
    return numpy.array([
        [c, s, 0, 0],
        [-s, c, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def rotate_matrix_y(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    c = math.cos(angle_radians)
    s = math.sin(angle_radians)
    return numpy.array([
        [c, 0, -s, 0],
        [0, 1, 0, 0],
        [s, 0, c, 0],
        [0, 0, 0, 1]
    ])

def rotate_matrix_x(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    c = math.cos(angle_radians)
    s = math.sin(angle_radians)
    return numpy.array([
        [1, 0, 0, 0],
        [0, c, s, 0],
        [0, -s, c, 0],
        [0, 0, 0, 1]
    ])

def transform_vertices(vertices, matrix):
    transformed_vertices = []
    for face in vertices:
        transformed_face = []
        for vertex in face:
            vertex_array = numpy.array([vertex[0], vertex[1], vertex[2], 1])
            transformed_vertex = matrix.dot(vertex_array)
            transformed_face.append((transformed_vertex[0], transformed_vertex[1], transformed_vertex[2]))
        transformed_vertices.append(transformed_face)
    return transformed_vertices

def draw_axes():
    glBegin(GL_LINES)

    glColor3f(1, 0, 0)  # Red for x-axis
    glVertex3f(0, 0, 0)
    glVertex3f(2, 0, 0)
    glVertex3f(1.8, 0.2, 0)  # Letter X
    glVertex3f(2.2, -0.2, 0)
    glVertex3f(1.8, -0.2, 0)  # Letter X
    glVertex3f(2.2, 0.2, 0)

    glColor3f(0, 1, 0)  # Green for y-axis
    glVertex3f(0, 0, 0)
    glVertex3f(0, 2, 0)
    glVertex3f(0.2, 1.8, 0)  # Letter Y
    glVertex3f(0, 2.2, 0)
    glVertex3f(-0.2, 1.8, 0)  # Letter Y
    glVertex3f(0, 2.2, 0)

    glColor3f(0, 0, 1)  # Blue for z-axis
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 2)
    glVertex3f(0.2, 0.2, 1.8)  # Letter Z
    glVertex3f(-0.2, 0.2, 1.8)
    glVertex3f(-0.2, 0.2, 1.8)  # Letter Z
    glVertex3f(0.2, -0.2, 1.8)
    glVertex3f(0.2, -0.2, 1.8)  # Letter Z
    glVertex3f(-0.2, -0.2, 1.8)

    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    pygame.display.set_caption('3D Cube Workshop')

    init_gl()

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    # Adjust camera position and orientation
    glTranslatef(0, 0, -7)  # Move and distance the camera
    glRotatef(0, 0, 0, 0)  # Rotate for a better viewing angle

    vertices = [
        [(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1)],
        [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)],
        [(-1, -1, -1), (-1, 1, -1), (-1, 1, 1), (-1, -1, 1)],
        [(1, -1, -1), (1, 1, -1), (1, 1, 1), (1, -1, 1)],
        [(-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1)],
        [(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1)]
    ]

    scale = 1.0
    angle = 0.0

    clock = pygame.time.Clock()
    fps = 60

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    scale = max(0.1, scale)
                elif event.key == pygame.K_DOWN:
                    scale -= 0.1
                elif event.key == pygame.K_LEFT:
                    angle -= 10
                elif event.key == pygame.K_RIGHT:
                    angle += 10
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # glRotatef(1, 0, 1, 0)  # Rotate around Y-axis
        angle += 1
        scaling_matrix = scale_matrix(scale, scale, scale)
        rotation_matrix = rotate_matrix_y(angle)
        transformation_matrix = rotation_matrix.dot(scaling_matrix)
        transformed_vertices = transform_vertices(vertices, transformation_matrix)

        draw_cube(transformed_vertices)
        draw_axes()  # Draw the axes



        pygame.display.flip()
        clock.tick(fps)

if __name__ == "__main__":
    main()
    