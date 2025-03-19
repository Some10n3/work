import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

def parametric_line(t, A, B):
    """Compute point on the line at parameter t."""
    return A + t * (B - A)

def find_intersection(A, B, sphere_center, radius):
    """Find intersection points of the line AB with the sphere."""
    C = sphere_center
    r = radius
    
    d = B - A  # Direction vector
    f = A - C  # Vector from sphere center to A
    
    a = np.dot(d, d)
    b = 2 * np.dot(f, d)
    c = np.dot(f, f) - r**2
    
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []  # No intersection
    elif discriminant == 0:
        t = -b / (2*a)
        return [parametric_line(t, A, B)]  # One intersection
    else:
        sqrt_disc = np.sqrt(discriminant)
        t1 = (-b + sqrt_disc) / (2*a)
        t2 = (-b - sqrt_disc) / (2*a)
        return [parametric_line(t1, A, B), parametric_line(t2, A, B)]  # Two intersections

def print_parametric_equation(A, B):
    """Print the parametric equation of the line passing through A and B."""
    d = B - A
    print(f"Parametric Equation of the Line:")
    print(f"x = {A[0]} + {d[0]}t")
    print(f"y = {A[1]} + {d[1]}t")
    print(f"z = {A[2]} + {d[2]}t")

def print_intersection_points(A, B, sphere_center, radius):
    """Print intersection points of the line with the sphere."""
    intersections = find_intersection(A, B, sphere_center, radius)
    if not intersections:
        print("No intersection points found.")
    else:
        print("Intersection Points:")
        for point in intersections:
            print(f"({point[0]:.2f}, {point[1]:.2f}, {point[2]:.2f})")

def draw_sphere(center, radius, slices=20, stacks=20):
    """Draw a wireframe sphere using OpenGL."""
    glPushMatrix()
    glTranslatef(*center)
    for i in range(slices):
        lat0 = np.pi * (-0.5 + float(i) / slices)
        z0 = np.sin(lat0)
        zr0 = np.cos(lat0)

        lat1 = np.pi * (-0.5 + float(i + 1) / slices)
        z1 = np.sin(lat1)
        zr1 = np.cos(lat1)

        glBegin(GL_LINE_LOOP)
        for j in range(stacks):
            lng = 2 * np.pi * float(j) / stacks
            x = np.cos(lng)
            y = np.sin(lng)

            glVertex3f(x * zr0 * radius, y * zr0 * radius, z0 * radius)
            glVertex3f(x * zr1 * radius, y * zr1 * radius, z1 * radius)
        glEnd()
    glPopMatrix()

def draw_line(A, B):
    """Draw the line passing through points A and B."""
    glBegin(GL_LINES)
    glVertex3fv(A)
    glVertex3fv(B)
    glEnd()

def draw_point(point, color=(1, 0, 0)):
    """Draw a small point at the given position."""
    glColor3f(*color)
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex3fv(point)
    glEnd()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Sphere-Line Intersection")
    
    gluPerspective(45, (800 / 600), 1, 100)
    glTranslatef(0, 0, -50)
    
    A = np.array([1, 2, 3])
    B = np.array([5, 4, 6])
    sphere_center = np.array([12.5, 0, 0])
    radius = 12.5

    # Print parametric equation of the line
    print_parametric_equation(A, B)

    # Print intersection points
    print_intersection_points(A, B, sphere_center, radius)

    # print sphere location
    print(f"Sphere Center: ({sphere_center[0]}, {sphere_center[1]}, {sphere_center[2]})")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(0, 1, 0)
        draw_sphere(sphere_center, radius)
        
        glColor3f(1, 1, 1)
        draw_line(A, B)
        
        intersections = find_intersection(A, B, sphere_center, radius)
        for point in intersections:
            draw_point(point)
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
