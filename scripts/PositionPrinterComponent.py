import opengl_test


class PositionPrinterComponent(opengl_test.PythonComponent):
    def __init__(self):
        self.timer = 0.0
        self.time_out = 1.0

    def update(self, delta_time):
        self.timer = self.timer + delta_time
        if self.timer < self.time_out:
            return

        while self.timer >= self.time_out:
            self.timer = self.timer - self.time_out

        parent = self.get_parent()
        transform = parent.get_transform()
        name = parent.get_name()
        position = transform.get_position()

        print('{} is at ({:.2f}, {:.2f}, {:.2f})'.format(name, *position))
