# Description: The ProgressTracker class tracks the user’s workout completion over time and
# can generate reports on workout progress.
#
# Attributes:
#
#     user: The user whose progress is being tracked.
#
# Methods:
#
#     log_workout(workout): Add a completed workout to the user’s workout history.
#     generate_report(): Generate a report summarizing the user’s workout history and statistics (e.g., number of workouts completed).
from user import User


class ProgressTracker:

    def __init__(self, user: str):
        self.user = user

    def log_workout(self, workout):
        self.user.log_workout(workout)

    def generate_report(self):
        total_workouts = len(self.user.workout_history)
        return f"{self.user.name} has completed {total_workouts} workouts."
