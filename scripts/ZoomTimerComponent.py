import numpy as np
import opengl_test


class ZoomTimerComponent(opengl_test.PythonComponent):
    def __init__(self):
        self.period = 2.0
        self.amplitude = 10.0
        self.offset = 65.0
        self.theta = 0
        self.camera = None

    def start(self):
        self.camera = self.get_parent().get_component_by_name("cameraComponent")
        if self.camera is None:
            print("Could not find camera component")

    def update(self, delta_time):
        if self.camera is None:
            return

        self.theta = self.theta + (delta_time * (np.pi * 2.0 / self.period))
        while self.theta >= np.pi * 2.0:
            self.theta = self.theta - (np.pi * 2.0)

        new_fov = (np.sin(self.theta) * self.amplitude) + self.offset

        self.camera.fovx = new_fov
