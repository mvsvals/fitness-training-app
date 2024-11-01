
from user import User

class ProgressTracker:

    def __init__(self, user: str):
        self.user = user

    def log_workout(self, workout):
        self.user.log_workout(workout)

    def generate_report(self):
        total_workouts = len(self.user.workout_history)
        return f"{self.user.name} has completed {total_workouts} workouts."
