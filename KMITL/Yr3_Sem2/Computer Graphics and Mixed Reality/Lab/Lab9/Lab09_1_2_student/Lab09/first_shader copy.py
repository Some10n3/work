from glApp.PyOGApp import *
import numpy as np
from glApp.Utils import *
from OpenGL.arrays.vbo import VBO
from glApp.Graphics_Data import *
from OpenGL.GL import *
import pygame

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
        self.vertex_count = 5
        self.vao_ref = None

    def initialise(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        
        position_data = np.array([
            [ 0.0, -0.9, 0.0],  # Bottom point
            [-0.6,  0.8, 0.0],  # Upper left
            [ 0.9, -0.2, 0.0],  # Right
            [-0.9, -0.2, 0.0],  # Left
            [ 0.6,  0.8, 0.0]   # Upper right
        ], dtype=np.float32)

        color_data = np.array([
            [1.0, 0.0, 0.0],  # Red
            [0.0, 1.0, 0.0],  # Green
            [0.0, 0.0, 1.0],  # Blue
            [1.0, 1.0, 0.0],  # Yellow
            [1.0, 0.0, 1.0]   # Purple
        ], dtype=np.float32)

        self.vao_ref = glGenVertexArrays(1)
        glBindVertexArray(self.vao_ref)

        vbo_ref = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo_ref)
        glBufferData(GL_ARRAY_BUFFER, position_data.nbytes + color_data.nbytes, None, GL_STATIC_DRAW)
        glBufferSubData(GL_ARRAY_BUFFER, 0, position_data.nbytes, position_data)
        glBufferSubData(GL_ARRAY_BUFFER, position_data.nbytes, color_data.nbytes, color_data)

        position_loc = glGetAttribLocation(self.program_id, 'position')
        glEnableVertexAttribArray(position_loc)
        glVertexAttribPointer(position_loc, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        color_loc = glGetAttribLocation(self.program_id, 'vertex_color')
        glEnableVertexAttribArray(color_loc)
        glVertexAttribPointer(color_loc, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(position_data.nbytes))

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        glBindVertexArray(self.vao_ref)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertex_count)

MyFirstShader().mainloop()