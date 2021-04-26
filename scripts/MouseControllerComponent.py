import opengl_test
from opengl_test import glfw
import numpy as np


class MouseControllerComponent(opengl_test.PythonComponent):
    def __init__(self):
        self.sens = (0.25, 0.25)  # degrees per pixel
        self.prev_pos = None
        self.yaw = 0  # degrees
        self.pitch = 0  # degrees
        self.pitch_limits = (-88.0, 88.0)

    def update(self, delta_time):
        cursor_pos = glfw.get_cursor_pos()

        if self.prev_pos is None:
            self.prev_pos = cursor_pos
            return

        delta = (
            (cursor_pos[0] - self.prev_pos[0]) * self.sens[0],
            (cursor_pos[1] - self.prev_pos[1]) * self.sens[1]
        )

        self.prev_pos = cursor_pos

        self.yaw = self.yaw + delta[0]
        while self.yaw < 0:
            self.yaw = self.yaw + 360.0
        while self.yaw >= 360.0:
            self.yaw = self.yaw - 360.0

        self.pitch = self.pitch + delta[1]
        if self.pitch < self.pitch_limits[0]:
            self.pitch = self.pitch_limits[0]
        if self.pitch > self.pitch_limits[1]:
            self.pitch = self.pitch_limits[1]

        new_orientation = (1, 0, 0, 0)
        new_orientation = self._quaternion_mult(new_orientation, self._angle_axis(np.deg2rad(self.yaw), [0.0, -1.0, 0.0]))
        new_orientation = self._quaternion_mult(new_orientation, self._angle_axis(np.deg2rad(self.pitch), [-1.0, 0.0, 0.0]))

        transform = self.get_parent().get_transform()
        transform.set_orientation(*new_orientation)

    def _angle_axis(self, angle, axis):
        sha = np.sin(angle / 2.0)  # Sin Half Angle

        return (
            np.cos(angle / 2.0),
            sha * axis[0],
            sha * axis[1],
            sha * axis[2]
        )

    def _quaternion_mult(self, q, r):
        return [r[0] * q[0] - r[1] * q[1] - r[2] * q[2] - r[3] * q[3],
                r[0] * q[1] + r[1] * q[0] - r[2] * q[3] + r[3] * q[2],
                r[0] * q[2] + r[1] * q[3] + r[2] * q[0] - r[3] * q[1],
                r[0] * q[3] - r[1] * q[2] + r[2] * q[1] + r[3] * q[0]]
