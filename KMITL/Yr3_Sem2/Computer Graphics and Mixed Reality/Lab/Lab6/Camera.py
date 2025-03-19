import numpy as np
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

class Camera:
    def __init__(self):
        # Initialize camera position and orientation
        self.eye = np.array([0.0, 0.0, 0.0])  # Camera position
        self.look = np.array([0.0, 0.0, 1.0])  # Point the camera is looking at
        self.up = np.array([0.0, 1.0, 0.0])  # Up direction
        self.forward = np.array([0.0, 0.0, 1.0])  # Forward vector
        self.right = np.cross(self.forward, self.up)  # Right vector
        self.yaw = 0.0
        self.pitch = 0.0
        self.last_mouse_pos = pygame.mouse.get_pos()

    def move_forward(self, distance):
        self.eye += self.forward * distance
        self.look += self.forward * distance

    def move_backward(self, distance):
        self.eye -= self.forward * distance
        self.look -= self.forward * distance

    def move_left(self, distance):
        self.eye -= self.right * distance
        self.look -= self.right * distance

    def move_right(self, distance):
        self.eye += self.right * distance
        self.look += self.right * distance

    def update_orientation(self):
        mouse_pos = pygame.mouse.get_pos()
        dx = mouse_pos[0] - self.last_mouse_pos[0]
        dy = mouse_pos[1] - self.last_mouse_pos[1]
        self.last_mouse_pos = mouse_pos

        sensitivity = 0.1
        self.yaw += dx * sensitivity
        self.pitch -= dy * sensitivity

        # Limit pitch to avoid gimbal lock
        self.pitch = max(-89.0, min(89.0, self.pitch))

        # Calculate new forward vector
        yaw_radians = np.radians(self.yaw)
        pitch_radians = np.radians(self.pitch)
        self.forward = np.array([
            np.cos(pitch_radians) * np.cos(yaw_radians),
            np.sin(pitch_radians),
            np.cos(pitch_radians) * np.sin(yaw_radians)
        ])
        self.forward = self.forward / np.linalg.norm(self.forward)

        # Recalculate right and up vectors
        self.right = np.cross(self.forward, np.array([0.0, 1.0, 0.0]))
        self.right = self.right / np.linalg.norm(self.right)
        self.up = np.cross(self.right, self.forward)
        self.up = self.up / np.linalg.norm(self.up)

    def apply_view(self):
        self.update_orientation()
        gluLookAt(
            self.eye[0], self.eye[1], self.eye[2],
            self.eye[0] + self.forward[0], self.eye[1] + self.forward[1], self.eye[2] + self.forward[2],
            self.up[0], self.up[1], self.up[2]
        )