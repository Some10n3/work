from pygame.locals import *
from OpenGL.GLU import *
from LoadMesh import *
from Camera import Camera

pygame.init()

# project settings
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Transformations in Python')
mesh = LoadMesh("teapot.obj", GL_LINE_LOOP)

# Initialize the camera
camera = Camera()

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
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)  

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()

    # Apply camera transformations
    camera.apply_view()

    # Draw the mesh
    mesh.draw()
    
    glPopMatrix()

done = False
initialise()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        camera.move_forward(0.3)
    if keys[pygame.K_DOWN]:
        camera.move_backward(0.3)
    if keys[pygame.K_LEFT]:
        camera.move_left(0.3)
    if keys[pygame.K_RIGHT]:
        camera.move_right(0.3)

    display()
    pygame.display.flip()

pygame.quit()
