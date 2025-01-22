### main.py ###
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import *

# Initialize Pygame and OpenGL
pygame.init()

# Screen settings
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)  # RGBA

# Create Pygame screen
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')

# Create a Cube instance
cube = Cube(GL_LINE_LOOP)

def initialise():
    """
    Set up OpenGL context, viewport, and projection settings.
    """
    glClearColor(*background_color)  # Background color

    # Projection matrix setup
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)

    # Modelview matrix setup
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslate(0, 0, -5)  # Move the cube back to be visible

    glViewport(0, 0, screen_width, screen_height)  # Viewport settings
    glEnable(GL_DEPTH_TEST)  # Enable depth testing for 3D rendering

def display():
    """
    Render the scene by clearing buffers, applying transformations, and drawing the cube.
    """
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear color and depth buffers
    glRotatef(1, 10, 2, 1)  # Rotate the cube slightly
    cube.draw()  # Draw the cube

def main():
    """
    Main game loop to handle events and update the display.
    """
    initialise()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        display()  # Render the scene
        pygame.display.flip()  # Swap buffers
        pygame.time.wait(60)  # Wait to control frame rate

    pygame.quit()  # Clean up resources

if __name__ == "__main__":
    main()
