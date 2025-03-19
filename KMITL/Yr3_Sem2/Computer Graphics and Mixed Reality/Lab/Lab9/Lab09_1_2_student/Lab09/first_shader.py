from glApp.PyOGApp import *
import numpy as np
from glApp.Utils import *
from OpenGL.arrays.vbo import VBO
from glApp.Graphics_Data import *
from glApp.Square import *
from glApp.Triangle import *

vertex_shader = r'''
#version 330 core

in vec3 position;
in vec3 vertex_color;
uniform vec3 translation;
out vec3 color;

void main() {

    vec3 pos = position + translation;
   gl_Position = vec4(pos, 1.0);
   color = vertex_color;
}
'''

fragment_shader = r'''
#version 330 core

in vec3 color;
out vec4 FragColor;
void main() {

    FragColor = vec4(color, 1.0f);
}
'''

class MyFirstShader(PyOGApp):
    def __init__(self):
        super().__init__(850, 200, 1000, 800)
        # self.vao_ref = None
        # self.vertex_count = 0
        self.square = None
        self.triangle = None

    def initialise(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.square = Square(self.program_id, pygame.Vector3(-0.5, 0.5, 0.0))
        self.triangle = Triangle(self.program_id, pygame.Vector3(0.5, -0.5, 0.0))


    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        self.square.draw()
        self.triangle.draw()

MyFirstShader().mainloop()