import opengl_test


class FPSCounterComponent(opengl_test.PythonComponent):
    def __init__(self):
        self.timer = 0.0
        self.time_out = 1.0
        self.frames = 0

    def update(self, delta_time):
        self.frames = self.frames + 1
        self.timer = self.timer + delta_time
        if self.timer < self.time_out:
            return

        while self.timer >= self.time_out:
            self.timer = self.timer - self.time_out

        print('FPS: {}'.format(self.frames))
        self.frames = 0
