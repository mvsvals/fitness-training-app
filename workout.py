
class Workout:

    def __init__(self, name: str):
        self.name = name
        self.exercises = []

    def add_exercise(self, exercise: str, sets: int, reps: int, rest_time: int, silent_mode=False):
        for current_exercise in self.exercises:
            if current_exercise['exercise'] == exercise:
                print(f'Exercise {exercise} is already included in the workout')
                return None
        self.exercises.append({'exercise': exercise, 'sets': sets, 'reps': reps, 'rest_time': rest_time})
        if not silent_mode:
            print(f'Exercise {exercise} has been added to Workout {self.name}.')

    def remove_exercise(self, exercise_name: str):
        self.exercises = list(filter(lambda x: x['exercise'] != exercise_name, self.exercises))
        print(f'Exercise {exercise_name} has been removed from the workout.')

    def view_workout(self):
        print(f'Workout: {self.name}')
        for index, exercise in enumerate(self.exercises, 1):
            print(f"{index}. Exercise: {exercise['exercise']} Sets: {exercise['sets']} Reps: {exercise['reps']} Rest: {exercise['rest_time']} sec")