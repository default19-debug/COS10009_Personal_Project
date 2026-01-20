class TrainingSession:
    def __init__(self, date, activity, duration, intensity):
        self.date = date
        self.activity = activity
        self.duration = duration
        self.intensity = intensity

    def __str__(self):
        return f"{self.date} | {self.activity} | {self.duration} min | Intensity {self.intensity}"
