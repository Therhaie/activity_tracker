class Activity:
    def __init__(self, name, start_time, end_time = None):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

    def duration(self):
        if self.end_time:
            return self.end_time - self.start_time
        return None
