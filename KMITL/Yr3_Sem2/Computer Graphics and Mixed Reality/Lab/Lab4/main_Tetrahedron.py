### main.py ###
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Tetrahedron import *

# Initialize Pygame and OpenGL
pygame.init()

# Screen settings
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)  # RGBA

# Create Pygame screen
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')

# Create a Tetrahedron instance
tetrahedron = Tetrahedron(GL_LINE_LOOP)

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
    glTranslate(0, 0, -5)  # Move the tetrahedron back to be visible

    glViewport(0, 0, screen_width, screen_height)  # Viewport settings
    glEnable(GL_DEPTH_TEST)  # Enable depth testing for 3D rendering

def main():
    """
    Main game loop to handle events and update the display.
    """

    # Initialize scaling and rotation values
    scale = 1.0
    rotation = [0, 0, 0]
    position = [0, 0, 0]

    # Initialize pygame and OpenGL
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, display[0] / display[1], 0.1, 50.0)
    # glTranslatef(0.0, 0.0, -10)

    initialise()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                print(event.key)
                # key w is pressed
                if event.key == pygame.K_w:
                    rotation[0] -= 5
                elif event.key == pygame.K_s:
                    rotation[0] += 5
                elif event.key == pygame.K_a:
                    rotation[1] -= 5
                elif event.key == pygame.K_d:
                    rotation[1] += 5
                elif event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                    scale += 0.1
                elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                    scale -= 0.1
                elif event.key == pygame.K_LEFT:
                    position[0] -= 0.1
                elif event.key == pygame.K_RIGHT:
                    position[0] += 0.1
                elif event.key == pygame.K_UP:
                    position[1] += 0.1
                elif event.key == pygame.K_DOWN:
                    position[1] -= 0.1
                elif event.key == pygame.K_q:
                    rotation[2] += 5
                elif event.key == pygame.K_e:
                    rotation[2] -= 5

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear color and depth buffers
        
        # Apply transformations
        glPushMatrix()
        glScalef(scale, scale, scale)
        glRotatef(rotation[0], 1, 0, 0)
        glRotatef(rotation[1], 0, 1, 0)
        glRotatef(rotation[2], 0, 0, 1)
        glTranslatef(position[0], position[1], position[2])

        tetrahedron.draw()  # Draw the tetrahedron
        glPopMatrix()
        pygame.display.flip()  # Swap buffers
        pygame.time.wait(60)  # Wait to control frame rate

    pygame.quit()  # Clean up resources

if __name__ == "__main__":
    main()
