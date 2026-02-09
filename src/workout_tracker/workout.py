from typing import List
from workout_tracker.exercises import Exercise

class Workout:
    _exercises = List[Exercise]

    def __init__(self):
        self._exercises = []

    def add_exercise(self, exercise: Exercise) -> None:
        #Add an exercise to the workout
        if not isinstance(exercise, Exercise):
            raise TypeError("Only Exercise objects can be added to a workout.")
        self._exercises.append(exercise)

    def get_exercises(self) -> List[Exercise]:
        #Get the list of exercises in the workout
        return self._exercises.copy()

    def total_calories(self) -> float:
        #Calculate total calories burned in the workout
        return sum(exercise.calculate_calories() for exercise in self._exercises)
    
    def total_duration(self) -> float:
        #Calculate total duration of the workout in minutes.
        return sum(exercise.get_duration() for exercise in self._exercises)
    
    def exercise_count(self) -> int:
        #Get the total number of exercises in the workout.
        return len(self._exercises)
    
    def __len__(self) -> int:
        #Return the number of exercises in the workout.
        return len(self._exercises)
    
    def __str__(self) -> str:
        #Get a string representation of the workout, including total exercises and calories.
        count = self.exercise_count()
        exercise_word = "exercise" if count == 1 else "exercises"
        calories = self.total_calories()
        return f"{count} {exercise_word}, {calories} calories"
    
    def get_summary(self) -> str:
        #Get a summary of the workout
        if self.exercise_count() == 0:
            return "Empty workout - no exercises added."
        
        summary_lines = ["=== Workout Summary ==="]
        
        for idx, exercise in enumerate(self._exercises, 1):
            summary_lines.append(f"{idx}. {exercise}")
        
        summary_lines.append("-" * 40)
        
        total_calories = self.total_calories()
        total_duration = self.total_duration()
        summary_lines.append(f"Total: {total_calories} calories, {int(total_duration)} minutes")
        
        return "\n".join(summary_lines)