from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
import numpy as np

class Camera:
    def __init__(self):
        # Initialize camera position and orientation
        self.eye = np.array([0.0, 0.0, 0.0])  # Camera position
        self.look = np.array([0.0, 0.0, 1.0])  # Point the camera is looking at
        self.up = np.array([0.0, 1.0, 0.0])  # Up direction
        self.forward = np.array([0.0, 0.0, 1.0])  # Forward vector
        self.right = np.cross(self.forward, self.up)  # Right vector

    def move_forward(self, distance):
        # Move the camera forward relative to its current orientation
        self.eye += self.forward * distance
        self.look += self.forward * distance

    def move_backward(self, distance):
        # Move the camera backward relative to its current orientation
        self.eye -= self.forward * distance
        self.look -= self.forward * distance

    def move_left(self, distance):
        # Move the camera left relative to its current orientation
        self.eye -= self.right * distance
        self.look -= self.right * distance

    def move_right(self, distance):
        # Move the camera right relative to its current orientation
        self.eye += self.right * distance
        self.look += self.right * distance

    def apply_view(self):
        # Apply the view transformation using gluLookAt
        gluLookAt(
            self.eye[0], self.eye[1], self.eye[2],
            self.look[0], self.look[1], self.look[2],
            self.up[0], self.up[1], self.up[2]
        )