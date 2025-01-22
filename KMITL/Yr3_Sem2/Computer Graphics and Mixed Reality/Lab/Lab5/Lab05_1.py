from pygame.locals import *
from OpenGL.GLU import *
from Cube import *
from LoadMesh import *

pygame.init()

# project settings
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)
 
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Transformations in Python')
cube = Cube(GL_LINE_LOOP)
mesh = LoadMesh("cube.obj", GL_LINE_LOOP)

def initialise():
    glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
    glColor(drawing_color)

    # projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 500.0)

    # modelview
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # glTranslate(0, 0, -5)  # Move the cube back to be visible
    # glTranslate(0, -1, -5)  # Move the cube back to be visible
    glTranslate(-1, 0, -5)  # Move the cube back to be visible
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    mesh.draw()
    glPopMatrix()

done = False
initialise()
# Initialize scaling and rotation values
scale = 1.0
rotation = [0, 0, 0]
position = [0, 0, 0]
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

        display() 
        glPopMatrix()
        pygame.display.flip()  # Swap buffers
        pygame.time.wait(60)  # Wait to control frame rate
pygame.quit()