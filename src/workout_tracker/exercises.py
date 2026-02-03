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
        self.date = datetime.now().strftime("%Y-%m-%d")
    
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
        super().__init__()
        self.name = name
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
        print(f"{self.name}{self.distance},{self.duration}:{self.calculate_calories}")
