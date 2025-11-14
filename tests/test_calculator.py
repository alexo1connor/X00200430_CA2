import pytest
from src.calculator import add, subtract, multiply, divide

class TestCalculator:
    def test_add(self):
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(-1, -1) == -2
    
    