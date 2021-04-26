import numpy as np
import opengl_test


class RotationComponent(opengl_test.PythonComponent):
    def __init__(self):
        self.rot_rate = 45.0  # degrees per second

    def update(self, delta_time):
        theta = np.radians(self.rot_rate * delta_time)

        transform = self.get_parent().get_transform()
        transform.rotate(
            np.cos(theta / 2.0),
            0.0,
            0.0,
            np.sin(theta / 2.0)
        )
