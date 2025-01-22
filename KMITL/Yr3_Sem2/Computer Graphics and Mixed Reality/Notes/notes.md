> `anti aliasing` : make object sharp, even with lower screen resolution

> `voxel` : 3d equivalent of pixel

> `Rastering` : convert 3d object into 2d view plane for calculations


# Lecture 2

## Sets in Com graphics
![alt text]({34398224-C86C-4579-B49E-636A51FCD9BE}.png)

### Properties of set
![alt text]({DC214EB3-DE0A-4F3E-AFF5-BD4C745B5251}.png)
![alt text]({B7064CDF-6EDA-4B1C-925A-FA922D53A311}.png)

# Skipping lots of basic math shits

### Global and local frame
![alt text]({D99D0101-F412-4EEC-BDA9-691A5FB51C67}.png)
![alt text]({CEF5244F-3144-444C-BD3E-FC2DDDCF7962}.png)
- Basically just position based on entire scene or individual object.

# Lecture 3
## Opengl
![alt text]({C09F8B4F-DB35-4C7C-8042-3ABDE86F9882}.png)
- GLUT
  - Windowing toolkit (key, mouse handler, window events)
- GLU
  - Viewing –perspective/orthographic
  - Image scaling, polygon tessellation
  - Sphere, cylinders, quadratic surfaces
- GL
  - Primitives - points, line, polygons
  - Shading and Colour
  - Translation, rotation, scalingViewing, Clipping, Texture
  - Hidden surface removal

### Command format
![alt text]({6A35814B-FA3A-4334-9118-FDE3C69C4A48}.png)
![alt text]({FC1B5D6D-905C-436E-A927-80445FAB089D}.png)

### Creating objects
![alt text]({7E503001-75A1-4D6E-BAFD-980508C94F70}.png)
- glBegin(object type) with points inside
  - GL_POINTS Each vertex is displayed as one pixel
  - GL_LINES Takes successive pair of vertices(lines are disconnected)
  - GL_LINE_STRIP Successive vertices are connected
  - GL_LINE_LOOP Polyline are closed

### Simple, Convex
- ![alt text]({6B9F893B-33F8-41DD-9A5A-AB313C7594B1}.png)
  - edge(line) cross each other, not simple (last one)
- ![alt text]({A0A7702F-0945-4B00-8693-64D9FC54F560}.png)
  - GL_POLYGON only works correctly with convex shapes.
  - Non-convex shapes need to be broken down into triangles.

### Tessellation
![alt text]({653528FA-E0FE-44A3-AF47-FB4160652C78}.png)
- Break objects into smaller shapes (mostly triangles in com graphics because triangle has the lowest vertice count, so it's the most optimal shape)

### Commands
Here's a concise summary of the GLUT and OpenGL commands you shared:

### **GLUT Initialization and Window Management Commands**
1. **`glutInit(int *argc, char **argv)`**  
   - Initializes GLUT and processes command-line arguments.  
   - Must be called before any other GLUT functions.  
   - Example: `glutInit(&argc, argv)`

2. **`glutInitDisplayMode(unsigned int mode)`**  
   - Specifies display mode: color model (RGBA or color-index), single/double buffer, and optional buffers (depth, stencil, accumulation).  
   - Examples:  
     - Double-buffered RGBA with depth: `glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)`  
     - Single-buffered RGB: `glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)`

3. **`glutInitWindowPosition(int x, int y)`**  
   - Sets the position of the upper-left corner of the window on the screen (in pixels).  
   - Example: `glutInitWindowPosition(0, 0);`

4. **`glutInitWindowSize(int width, int height)`**  
   - Sets the size of the window (in pixels).  
   - Example: `glutInitWindowSize(500, 500);`

5. **`glutCreateWindow(char *title)`**  
   - Creates a window with the specified title and an OpenGL context.  
   - Returns a unique identifier for the window.  
   - Example: `glutCreateWindow("Sierpinski Gasket");`

6. **`glutDisplayFunc(void (*func)(void))`**  
   - Registers the display callback function to redraw the window content.  
   - Example: `glutDisplayFunc(displayCallbackFunction);`

7. **`glutMainLoop(void)`**  
   - Starts the event processing loop.  
   - Once entered, it does not exit, and all windows created are rendered.

### **OpenGL Rendering and Buffer Commands**
1. **`glViewport(GLint x, GLint y, GLsizei w, GLsizei h)`**  
   - Sets the viewport rectangle (in pixels) for rendering.  
   - `(x, y)` specifies the lower-left corner, and `w:h` defines the aspect ratio.  
   - Example: `glViewport(0, 0, 500, 500);`

2. **`glFlush()`**  
   - Ensures all OpenGL commands in buffers are executed immediately.  
   - Especially useful for single-buffered windows to force drawing.

### **Key Notes**
- **Buffers:**  
  - Single-buffering: Draws directly to the screen.  
  - Double-buffering: Uses a back buffer for rendering to reduce flickering.  

- **Callback Functions:**  
  - Registered with GLUT (like `glutDisplayFunc`) to handle specific events (e.g., window updates).

### OpenGL syntax
- Functions:
glFunction: glBegin, glClear, glVertex, …
- Constants:
GL_CONSTANT: GL_2D, GL_LINE
- Datatypes:
GLtype: GLbyte, GLint, GLfloat

#### Example
```
glClearColor(1.0,1.0,1.0,0.0);                     // Background color
glMatrixMode(GL_PROJECTION);                      // Set transformation
glLoadIdentity;
gluOrtho2D(0, 200, 0, 150);
glClear(GL_COLOR_BUFFER_BIT);                      // Clear background
glColor3f(1.0, 0.0, 0.0);                      // Set color to red

glBegin(GL_LINES);                      // Draw line
  glVertex2i(180, 15);                      // - first point
  glVertex2i(10, 145);                      // - second point
glEnd;                      // Ready with line
glFlush;                      // Send
```

## Orthogonal view
![alt text](image-2.png)
![alt text](image.png)
![alt text](image-1.png)

## Matrix meaning in different operation
![alt text](image-3.png)
![alt text](image-4.png)

## Bezier curve and spline

### Curve
![alt text](image-5.png)

### Creating curve with a Spline
```
A spline is a smooth curve that is constructed by interpolating or approximating a set of points called control points. The purpose of using splines is to create a smooth, flexible curve that can pass through or near a set of specified points, or even be influenced by them to form a desired shape.
```
- Specified by a few control points
  - Good for UI
  - Good for storage
- ![alt text](image-7.png)

### Control point
- user specified points to guide the curve
- ![alt text](image-6.png)

### Tessalation
-  It is easy to rasterize mathematical line segments
into pixels
- OpenGL and the graphics hardware can do it for you
   - But polynomials and other parametric functions are harder
- ![alt text](image-8.png)
- ![alt text](image-9.png)

### Interpolation vs Approximation
![alt text](image-10.png)
![alt text](image-11.png)

### Cubic bezier curve
![alt text](image-12.png)
- Interpolate first and last one, while approximate the others
  - ![alt text](image-16.png)

![alt text](image-13.png)
![alt text](image-14.png)
- verify t = 0 and t = 1

![alt text](image-17.png)
![alt text](image-18.png)
- B shows how much weight, each point has on the real curve at time t
- P1 and P4 was very influential, it solely was taken as the value of the curve at the start and end. 
- P2 and P3 only influence a bit but the value at the time was not exactly.

> It is a linear combination of basis polynomials.
> The opposite perspective, control points are the weights of polynomials!!!

#### Cubic Polynomial
![alt text](image-19.png)
![alt text](image-20.png)
![alt text](image-21.png)
![alt text](image-25.png)
![alt text](image-24.png)
![alt text](image-23.png)

### Matrix vector notation
![alt text](image-26.png)

### Bernstein polynomial
![alt text](image-27.png)
![alt text](image-28.png)
- Sum of all B at time t is 1

![alt text](image-29.png)
- Already understand from before but this is the `definition` one

### How to convert Bernstein to canonical
[4x4 Matrix inversion youtube link](https://youtu.be/95dYWsZEXmM)
![alt text](image-30.png)
![alt text](image-31.png)

### Snap back to reality
![ ](image-34.png)
![alt text](image-32.png)
![alt text](image-33.png)

### more than 4 control points
![alt text](image-35.png)
- **you will not need this in this class**

### Subdivision of a bezier curve
![alt text](image-36.png)
- This is useful for adding detail
- It avoids using nasty higher-order curves

![alt text](image-37.png)
![alt text](image-38.png)

![alt text](image-39.png)
- Works on not 0.5 too

## Recap of lecture 3`
![alt text](image-40.png)


# Lecture 4

## Raster image
- Raster data is a matrix of pixels
- pixel is picture elements
- ![alt text](image-41.png)
- ![alt text](image-42.png)

### Gamma color correction
- ![alt text](image-43.png)

### Colors
- RGB color
- ![alt text](image-44.png)
- Alpha
- ![alt text](image-45.png)
  
**Important formula**
> The formula c = αcf + (1 - α)cb is used for blending, where cf is the foreground color and cb is the background color. 

### Image storage formats
![alt text](image-46.png)

### Bayer mosaic pattern
- ![alt text](image-47.png)

## Ray Tracing
- Ray tracing is an image-order algorithm for rendering 3D scenes.
- It works by generating rays from a viewpoint through each pixel of an image plane and finding the nearest object that intersects each ray.
- The color of the pixel is then determined by the object's material properties and the lighting in the scene.
- Ray tracing can be used to create realistic images of 3D scenes,including effects such as shadows, reflections, and refractions