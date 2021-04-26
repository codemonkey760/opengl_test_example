import opengl_test


class CameraComponent(opengl_test.PythonComponent):
    def __init__(self):
        self.type = "perspective"
        self.fovx = 65.0
        self.near = 0.05
        self.far = 100.0
        self.width = 640
        self.height = 480
