import sys
sys.path.append('..')
from solutions.two_sum import two_sum

def test_two_sum():
    # Test example 1
    result = two_sum([2, 7, 11, 15], 9)
    assert sorted(result) == [0, 1], f"Expected [0, 1], got {result}"
    
    # Test example 2
    result = two_sum([3, 2, 4], 6)
    assert sorted(result) == [1, 2], f"Expected [1, 2], got {result}"
    
    # Test example 3
    result = two_sum([3, 3], 6)
    assert sorted(result) == [0, 1], f"Expected [0, 1], got {result}"
    
    # Test no solution
    result = two_sum([1, 2, 3], 10)
    assert result == [], f"Expected [], got {result}"
    
    # Test negative numbers
    result = two_sum([-1, -2, -3, -4, -5], -8)
    assert sorted(result) == [2, 4], f"Expected [2, 4], got {result}"
    
    print("All tests passed!")

if __name__ == "__main__":
    test_two_sum()