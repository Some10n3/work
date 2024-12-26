import pygame 
from pygame.locals import * 
from OpenGL.GL import * 
from OpenGL.GLU import * 
 
pygame.init() 
display = (800, 600) 
pygame.display.set_mode(display, DOUBLEBUF|OPENGL) 
     
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0) 
glTranslatef(0.0, 0.0, -5) 
 
x_position = 0.0 
move_direction = 0.01 
 
while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            quit() 
 
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) 
     
    glBegin(GL_LINES) 
    # Changed starting positions to center the line 
    glVertex3fv([0.5 + x_position, 0.0, 0.0])    # Moved right by 0.5 
    glVertex3fv([-0.5 + x_position, -1.0, 0.0])  # Moved right by 0.5 
    glEnd() 
     
    x_position += move_direction 
     
    # Adjusted boundaries for centered line 
    if x_position > 1.5 or x_position < -1.5: 
        move_direction = -move_direction 
     
    pygame.display.flip() 
    pygame.time.wait(10)