### Question 1 
- I see a diagonal line when I run the program.
- Probably is part of the cube
- I then move the camera position to see from a farther distance.
- The program creates a cube object and create(import) a mesh (cube) object
- But only displaying the mesh
- change form glTranslated(0, 0,-1) to glTranslated(0, 0,-2) 
  - This change how far the camera is from the center
- Changing x is left / right
- Changing y is up / down

### Question 2
-  The cube is moved
-  From what I searched, openGL transformations like glTranslatef, glRotatef, and glScalef don't actually "move" objects. Instead, they modify the current transformation matrix (CTM), which determines how the scene is projected into view. So, when you translate by (0, 0, -5), you are moving everything except the camera by 5 units along the negative z-axis. Which makes the cube appear smaller on our screen.
-  https://www.ibm.com/docs/en/aix/7.1?topic=subroutines-gltranslate-subroutine
-  https://learn.microsoft.com/en-us/windows/win32/opengl/gltranslatef

### Question 3
- The gluLookAt function sets up the camera's view, but it doesn't move the camera itself. It defines where the camera is looking at and which direction is "up".
- The arguments
  - `Eye position`: (0, 0, 5) - The camera is positioned 5 units above the origin.
  - `Look-at point`: (0, 0, 0) - The camera looks at the origin.
  - `Up vector`: (0, 1, 0) - The camera's "up" direction is along the positive Y-axis.