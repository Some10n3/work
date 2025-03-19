from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_triangle():
    glBegin(GL_TRIANGLES)
    
    # Vertex 1: Red
    # glColor3f(1.0, 0.0, 0.0)
    glColor3f(1.0, 0.7, 0.0)
    glVertex2f(-0.5, -0.5)
    
    # Vertex 2: Green
    # glColor3f(0.0, 1.0, 0.0)
    glColor3f(0.0, 1.0, 0.7)
    glVertex2f(0.5, -0.5)
    
    # Vertex 3: Blue
    # glColor3f(0.0, 0.0, 1.0)
    glColor3f(0.0, 0.7, 1.0)
    glVertex2f(0.0, 0.5)
    
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_triangle()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Gouraud Shaded Triangle")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
