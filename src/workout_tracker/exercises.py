"""Exercise classes for the workout tracker."""

from datetime import datetime


class Exercise:
    """Base class for all exercise types.
    
    Attributes:
        name (str): The name of the exercise
        date (str): The date the exercise was performed (YYYY-MM-DD format)
    """
    
    def __init__(self, name: str, date: str = None):
        """Initialize an Exercise.
        
        Args:
            name: The name of the exercise
            date: The date performed (defaults to today if not provided)
        """
        # TODO: Set self.name
        # TODO: Set self.date (use datetime.now().strftime("%Y-%m-%d") if date is None)
        self.name = name
        self.date = date if date is not None else datetime.now().strftime("%Y-%m-%d")
    
    def calculate_calories(self) -> float:
        """Calculate calories burned for this exercise.
        
        Subclasses must override this method.
        
        Returns:
            float: Estimated calories burned
        """
        # This is a base implementation that subclasses will override
        return 0.0
    
    def get_duration(self) -> float:
        """Get the duration of the exercise in minutes.
        
        Subclasses must override this method.
        
        Returns:
            float: Duration in minutes
        """
        # This is a base implementation that subclasses will override
        return 0.0
    
    def __str__(self) -> str:
        """Return a string representation of the exercise."""
        # TODO: Return a string like "ExerciseName: 100 calories"
        # Use self.calculate_calories() to get the calories
        print(f"ExerciseName: {self.calculate_calories()}")



class CardioExercise(Exercise):
    """Cardio exercise with distance and time tracking.
    
    Attributes:
        name (str): Exercise name
        date (str): Date performed
        distance (float): Distance covered in miles
        duration (float): Time spent in minutes
    """
    
    def __init__(self, name: str, distance: float, duration: float, date: str = None):
        """Initialize a CardioExercise.
        
        Args:
            name: Exercise name (e.g., "Running", "Cycling")
            distance: Distance covered in miles
            duration: Time spent in minutes
            date: Date performed (optional)
        """
        super().__init__(name, date)
        self.distance = distance
        self.duration = duration
    
    def calculate_calories(self) -> float:
        """Calculate calories burned based on distance.
        
        Formula: distance * 100
        
        Returns:
            float: Estimated calories burned
        """
        # TODO: Implement the formula
        self.formula = self.distance * 100
        return self.formula
    
    def get_duration(self) -> float:
        """Get the duration of the cardio exercise.
        
        Returns:
            float: Duration in minutes
        """
        # TODO: Return the duration attribute
        return self.duration
    
    def __str__(self) -> str:
        """Return detailed string representation."""
        # TODO: Return something like "Running (3.5 miles, 30 min): 350 calories"
        # Include self.name, self.distance, self.duration, and self.calculate_calories()
        return f"{self.name} ({self.distance} miles, {self.duration} min): {self.calculate_calories()} calories"


class StrengthExercise(Exercise):
    """Strength exercise with weight, reps, and sets tracking.
    
    Attributes:
        name (str): Exercise name
        date (str): Date performed
        weight (float): Weight lifted in pounds
        reps (int): Repetitions per set
        sets (int): Number of sets
    """
    
    def __init__(self, name: str, weight: float, reps: int, sets: int, date: str = None):
        """Initialize a StrengthExercise.
        
        Args:
            name: Exercise name (e.g., "Bench Press", "Squats")
            weight: Weight lifted in pounds
            reps: Repetitions per set
            sets: Number of sets
            date: Date performed (optional)
        """
        super().__init__(name, date)
        self.weight = weight
        self.reps = reps
        self.sets = sets
    
    def calculate_calories(self) -> float:
        """Calculate calories burned based on weight, reps, and sets.
        
        Formula: (weight * reps * sets) / 500
        
        Returns:
            float: Estimated calories burned
        """
        return (self.weight * self.reps * self.sets) * 0.05

    def __str__(self):
        return f"{self.name} ({self.weight} lbs, {self.reps} reps x {self.sets} sets): {self.calculate_calories()} calories"
    

class FlexibilityExercise(Exercise):
    """Flexibility exercise with duration and intensity tracking.
    
    Attributes:
        name (str): Exercise name
        date (str): Date performed
        duration (float): Time spent in minutes
        intensity (str): Intensity level ("low", "medium", "high")
    """
    
    def __init__(self, name: str, duration: float, intensity: str = "medium", date: str = None):
        """Initialize a FlexibilityExercise.
        
        Args:
            name: Exercise name (e.g., "Yoga", "Stretching")
            duration: Time spent in minutes
            intensity: Intensity level ("low", "medium", "high")
            date: Date performed (optional)
        """
        super().__init__(name, date)
        self.duration = duration
        self.intensity = intensity.lower()
    
    def calculate_calories(self) -> float:
        """Calculate calories burned based on duration and intensity.
        
        Intensity multipliers:
            low: 1 calories/min
            medium: 1.5 calories/min
            high: 2 calories/min
        
        Returns:
            float: Estimated calories burned
        """
        intensity_map = {
            "low": 1.0,
            "medium": 1.5,
            "high": 2
        }
        multiplier = intensity_map.get(self.intensity, 1.0)  # Default to low if unknown
        return self.duration * 2.5 * multiplier
    
    def get_duration(self) -> float:
        """Get the duration of the flexibility exercise.
        
        Returns:
            float: Duration in minutes
        """
        return self.duration
    
    def __str__(self) -> str:
        """Return detailed string representation."""
        return f"{self.name} ({self.duration} min, {self.intensity} intensity): {self.calculate_calories()} calories"