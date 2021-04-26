import opengl_test
from opengl_test import glfw
import numpy as np


class KeyboardControllerComponent(opengl_test.PythonComponent):
    def __init__(self):
        self.speed = 1.0
        self.fast_speed = 5.0
        self.slow_speed = 0.25

    def update(self, delta_time):
        d = {
            'x': 0.0,
            'y': 0.0,
            'z': 0.0
        }

        if glfw.get_key(glfw.GLFW_KEY_W) == glfw.GLFW_PRESS:
            d['z'] = d['z'] - 1.0
        if glfw.get_key(glfw.GLFW_KEY_S) == glfw.GLFW_PRESS:
            d['z'] = d['z'] + 1.0
        if glfw.get_key(glfw.GLFW_KEY_A) == glfw.GLFW_PRESS:
            d['x'] = d['x'] - 1.0
        if glfw.get_key(glfw.GLFW_KEY_D) == glfw.GLFW_PRESS:
            d['x'] = d['x'] + 1.0

        if self._mag(d) < 0.95:
            return

        transform = self.get_parent().get_transform()
        orientation = transform.get_orientation()

        d = self._normalize_vec3(d)
        d = self._rotate_vec(d, orientation)
        d = self._normalize_vec3(d)

        speed = self.speed
        if glfw.get_key(glfw.GLFW_KEY_LEFT_SHIFT) == glfw.GLFW_PRESS:
            speed = self.fast_speed
        elif glfw.get_key(glfw.GLFW_KEY_LEFT_CONTROL) == glfw.GLFW_PRESS:
            speed = self.slow_speed

        d = self._scale_vec3(d, delta_time * speed)

        transform.move(d['x'], d['y'], d['z'])

    def _mag(self, vec):
        return np.sqrt((vec['x'] * vec['x']) + (vec['y'] * vec['y']) + (vec['z'] * vec['z']))

    def _normalize_vec3(self, vec):
        mag = self._mag(vec)

        vec['x'] = vec['x'] / mag
        vec['y'] = vec['y'] / mag
        vec['z'] = vec['z'] / mag

        return vec

    def _rotate_vec(self, p, q):
        r = [0.0, p['x'], p['y'], p['z']]
        q_conj = [q[0], -1*q[1], -1*q[2], -1*q[3]]

        ret = self._quaternion_mult(self._quaternion_mult(q, r), q_conj)

        return {
            'x': ret[1],
            'y': ret[2],
            'z': ret[3]
        }

    def _quaternion_mult(self, q, r):
        return [r[0]*q[0]-r[1]*q[1]-r[2]*q[2]-r[3]*q[3],
                r[0]*q[1]+r[1]*q[0]-r[2]*q[3]+r[3]*q[2],
                r[0]*q[2]+r[1]*q[3]+r[2]*q[0]-r[3]*q[1],
                r[0]*q[3]-r[1]*q[2]+r[2]*q[1]+r[3]*q[0]]

    def _scale_vec3(self, v, s):
        return {
            'x': v['x'] * s,
            'y': v['y'] * s,
            'z': v['z'] * s
        }