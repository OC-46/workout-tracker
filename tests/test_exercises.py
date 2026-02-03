"""Unit tests for exercise classes."""

import pytest
from workout_tracker.exercises import (
    Exercise,
    CardioExercise
)


class TestCardioExercise:
    """Tests for CardioExercise class."""
    
    def test_cardio_creation(self):
        """Test creating a cardio exercise."""
        exercise = CardioExercise("Running", distance=3.5, duration=30)
        assert exercise.name == "Running"
        assert exercise.distance == 3.5
        assert exercise.duration == 30
    
    def test_cardio_calories(self):
        """Test calorie calculation for cardio."""
        exercise = CardioExercise("Cycling", distance=10.0, duration=45)
        # Formula: distance * 100
        assert exercise.calculate_calories() == 1000.0
    
    def test_cardio_duration(self):
        """Test getting duration for cardio."""
        exercise = CardioExercise("Swimming", distance=1.0, duration=25)
        assert exercise.get_duration() == 25
    
    def test_cardio_str(self):
        """Test string representation of cardio exercise."""
        exercise = CardioExercise("Running", distance=5.0, duration=40)
        result = str(exercise)
        assert "Running" in result
        assert "5.0 miles" in result
        assert "500" in result  # calories


class TestExerciseInheritance:
    """Tests to verify inheritance works correctly."""
    
    def test_cardio_is_exercise(self):
        """Test that cardio exercise inherits from Exercise."""
        cardio = CardioExercise("Running", distance=5, duration=30)
        assert isinstance(cardio, Exercise)
    
    def test_exercises_have_date(self):
        """Test that exercises have a date attribute."""
        cardio = CardioExercise("Running", distance=5, duration=30)
        assert hasattr(cardio, 'date')
        assert cardio.date is not None
    
    def test_exercise_custom_date(self):
        """Test creating exercise with custom date."""
        exercise = CardioExercise("Running", distance=5, duration=30, date="2024-01-15")
        assert exercise.date == "2024-01-15"
