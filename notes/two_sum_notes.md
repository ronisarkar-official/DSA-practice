# Two Sum Notes

## Problem
Find two indices in an array that add up to a target value.

## Approach
Use a hashmap to store seen numbers and their indices. For each number, check if the complement (target - num) is in the map.

## Time Complexity
O(n) - Single pass through the array.

## Space Complexity
O(n) - For the hashmap storing up to n elements.

## Edge Cases
- No solution: Return empty list
- Duplicate numbers: Works as long as indices are different
- Negative numbers: Hashmap handles negatives fine

## Alternative Approaches
- Brute force: O(n^2) nested loops
- Sort and two pointers: O(n log n) time, O(1) extra space if allowed to modify array

## Lessons Learned
- Hashmaps are powerful for O(1) lookups
- Always consider edge cases in tests