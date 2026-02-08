from shutil import copy
from typing import List
from workout_tracker.exercises import Exercise

class Workout:
    _exercises = List[Exercise]

    def __init__(self):
        self._exercises = []

    def add_exercise(self, exercise: Exercise) -> None:
        """Add an exercise to the workout."""
        if not isinstance(exercise, Exercise):
            raise TypeError("Only Exercise objects can be added to a workout.")
        self._exercises.append(exercise)

    def get_exercises(self) -> List[Exercise]:
        """Get the list of exercises in the workout."""
        return copy.copy(self._exercises)

    def total_calories(self) -> float:
        """Calculate total calories burned in the workout."""
        return sum(exercise.calculate_calories() for exercise in self._exercises)
    
    def total_duration(self) -> float:
        """Calculate total duration of the workout in minutes."""
        return sum(exercise.get_duration() for exercise in self._exercises)
    
    def exercise_count(self) -> int:
        """Get the total number of exercises in the workout."""
        return len(self._exercises)
    
    def get_summary(self) -> str:
        """Get a summary of the workout."""
        summary_lines = [
            f"Total Exercises: {self.exercise_count()}",
            f"Total Duration: {self.total_duration()} minutes",
            f"Total Calories Burned: {self.total_calories()} calories"
        ]
        if self.exercise_count() == 0:
            summary_lines.append("Empty workout - no exercises added.")
        return "\n".join(summary_lines)