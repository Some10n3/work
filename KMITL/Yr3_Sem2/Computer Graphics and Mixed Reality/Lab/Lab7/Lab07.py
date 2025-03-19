import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image

# Camera variables
camera_pos = [0.0, -1.5, -15.0]
camera_pan = [0.0, 0.0]
zoom_level = 1.0
mouse_last_pos = None
mouse_panning = False
mouse_zooming = False

# Light position
light_pos = [0.0, 5.0, 0.0, 1.0]

def load_texture(image_path):
    """Load an image as a texture."""
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    image = Image.open(image_path)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    img_data = image.convert("RGB").tobytes()
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.width, image.height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    return texture_id

def draw_textured_floor(texture_id):
    """Draw a floor with the applied texture."""
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    for x in range(-10, 10):
        for z in range(-10, 10):
            glTexCoord2f(0, 0)
            glVertex3f(x, 0, z)
            glTexCoord2f(1, 0)
            glVertex3f(x + 1, 0, z)
            glTexCoord2f(1, 1)
            glVertex3f(x + 1, 0, z + 1)
            glTexCoord2f(0, 1)
            glVertex3f(x, 0, z + 1)
    glEnd()
    glDisable(GL_TEXTURE_2D)

def draw_sphere(x, y, z, radius, transparent=False):
    """Draw a sphere at the specified position."""
    if transparent:
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glColor4f(0.7, 0.7, 1, 0.3)  # Light blue with transparency
    else:
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [0, 1, 1, 1])  # Cyan
        glMaterialfv(GL_FRONT, GL_SPECULAR, [1, 1, 1, 1])  # White specular highlight
        glMaterialf(GL_FRONT, GL_SHININESS, 50.0)  # Shiny surface
    glPushMatrix()
    glTranslatef(x, y, z)
    quad = gluNewQuadric()
    gluSphere(quad, radius, 64, 64)
    glPopMatrix()
    if transparent:
        glDisable(GL_BLEND)

def setup_lighting():
    """Set up lighting for the scene."""
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    
    # Light position (dynamic)
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    
    # Adjusted white diffuse light for more natural shadows
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 0.8, 0.8, 1])
    
    # Increased ambient light for softer shadows
    # glLightfv(GL_LIGHT0, GL_AMBIENT, [0.3, 0.3, 0.3, 1])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.1, 0.1, 0.1, 1])

    
    # Adjusted specular highlights for enhanced realism
    glLightfv(GL_LIGHT0, GL_SPECULAR, [0.9, 0.9, 0.9, 1])

def setup_scene():
    """Initialize the scene settings."""
    glClearColor(0.5, 0.5, 0.5, 1)  # Light gray background
    glEnable(GL_DEPTH_TEST)  # Enable depth testing for 3D rendering
    glEnable(GL_COLOR_MATERIAL)  # Enable color tracking

def handle_mouse_events():
    """Handle mouse controls for panning and zooming."""
    global mouse_last_pos, mouse_panning, mouse_zooming, camera_pan, zoom_level

    mouse_buttons = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    # Left button for panning
    if mouse_buttons[0]:
        if mouse_last_pos is not None and mouse_panning:
            dx = (mouse_pos[0] - mouse_last_pos[0]) * 0.01
            dy = (mouse_pos[1] - mouse_last_pos[1]) * 0.01
            camera_pan[0] += dx
            camera_pan[1] -= dy
        mouse_panning = True
    else:
        mouse_panning = False

    # Right button for zooming
    if mouse_buttons[2]:
        if mouse_last_pos is not None and mouse_zooming:
            dy = mouse_pos[1] - mouse_last_pos[1]
            zoom_level -= dy * 0.01
            zoom_level = max(0.1, min(5.0, zoom_level))  # Limit zoom range
        mouse_zooming = True
    else:
        mouse_zooming = False

    mouse_last_pos = mouse_pos

def handle_keyboard_events():
    """Handle keyboard events to move the light source."""
    global light_pos
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:  # Move light left
        light_pos[0] -= 0.2
    if keys[pygame.K_d]:  # Move light right
        light_pos[0] += 0.2
    if keys[pygame.K_w]:  # Move light forward
        light_pos[2] -= 0.2
    if keys[pygame.K_s]:  # Move light backward
        light_pos[2] += 0.2
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)  # Update light position

def update_camera():
    """Update the camera view based on panning and zooming."""
    glLoadIdentity()
    gluPerspective(45 * zoom_level, 800 / 600, 0.1, 50.0)
    glTranslatef(camera_pan[0], camera_pan[1], camera_pos[2])

def main():
    """Main program loop."""
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(*camera_pos)  # Initialize camera position

    setup_scene()
    setup_lighting()

    # Load the chess texture
    texture_id = load_texture("chess.png")  # Load your chessboard pattern

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Handle mouse input
        handle_mouse_events()

        # Handle keyboard input
        handle_keyboard_events()

        # Update the camera view
        update_camera()

        # Render the scene
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_textured_floor(texture_id)
        draw_sphere(-3, 2, 0, 2)  # Opaque sphere (moved up)
        draw_sphere(3, 2, 0, 2, transparent=True)  # Transparent sphere (moved up)
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
