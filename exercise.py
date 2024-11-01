
class Exercise:

    def __init__(self, name: str, description: str, difficulty: str):
        self.name = name
        self.description = description
        self.difficulty = difficulty

    def display_exercise(self):
        return f'{self.name} ({self.difficulty}): {self.description}'
