"""
3Sum implementations for Assignment 1.

This module contains different implementations of the 3Sum problem:
1. Brute Force - O(N^3) time complexity
2. Optimized with sorting and two pointers - O(N^2) time complexity
"""

import random
import time


def three_sum_brute_force(
    nums: list[int], target: int = 0, return_values: bool = False
) -> list[tuple[int, int, int]]:
    """
    Brute force implementation of 3Sum problem.

    Time Complexity: O(N^3)
    Space Complexity: O(1)

    Args:
        nums: List of integers
        target: Target sum (default: 0)
        return_values: If True, return unique value triplets; if False, return index

    Returns:
        List of tuples (i, j, k) where nums[i] + nums[j] + nums[k] = target
        or value triplets if return_values=True
    """
    n = len(nums)

    if return_values:
        # For value-based deduplication, use a set to track unique triplets
        result_set = set()

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == target:
                        # Create sorted triplet of values for deduplication
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        result_set.add(triplet)

        return list(result_set)
    else:
        result = []

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == target:
                        result.append((i, j, k))

        return result


def _three_sum_values(nums: list[int], target: int) -> list[tuple[int, int, int]]:
    """Helper function for value-based 3Sum using two pointers."""
    n = len(nums)
    sorted_nums = sorted(nums)
    result = []

    for i in range(n - 2):
        if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            current_sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]

            if current_sum == target:
                result.append((sorted_nums[i], sorted_nums[left], sorted_nums[right]))

                # Skip duplicates for second and third elements
                while left < right and sorted_nums[left] == sorted_nums[left + 1]:
                    left += 1
                while left < right and sorted_nums[right] == sorted_nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result


def _three_sum_indices(nums: list[int], target: int) -> list[tuple[int, int, int]]:
    """Helper function for index-based 3Sum using two pointers."""
    n = len(nums)
    indexed_nums = [(nums[i], i) for i in range(n)]
    indexed_nums.sort(key=lambda x: x[0])
    result = []

    for i in range(n - 2):
        if i > 0 and indexed_nums[i][0] == indexed_nums[i - 1][0]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            current_sum = (
                indexed_nums[i][0] + indexed_nums[left][0] + indexed_nums[right][0]
            )

            if current_sum == target:
                original_indices = (
                    indexed_nums[i][1],
                    indexed_nums[left][1],
                    indexed_nums[right][1],
                )
                result.append(original_indices)

                # Skip duplicates for second and third elements
                while (
                    left < right and indexed_nums[left][0] == indexed_nums[left + 1][0]
                ):
                    left += 1
                while (
                    left < right
                    and indexed_nums[right][0] == indexed_nums[right - 1][0]
                ):
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result


def three_sum_optimized(
    nums: list[int], target: int = 0, return_values: bool = False
) -> list[tuple[int, int, int]]:
    """
    Optimized implementation of 3Sum problem using sorting and two pointers.

    Time Complexity: O(N^2)
    Space Complexity: O(1) excluding output

    Args:
        nums: List of integers
        target: Target sum (default: 0)
        return_values: If True, return unique value triplets; if False, return index

    Returns:
        List of tuples (i, j, k) where nums[i] + nums[j] + nums[k] = target
        or value triplets if return_values=True
    """
    if return_values:
        return _three_sum_values(nums, target)
    else:
        return _three_sum_indices(nums, target)


def three_sum_optimized_with_hash(
    nums: list[int], target: int = 0, return_values: bool = False
) -> list[tuple[int, int, int]]:
    """
    Alternative optimized implementation using hash set for the third element.

    Time Complexity: O(N^2)
    Space Complexity: O(N)

    Args:
        nums: List of integers
        target: Target sum (default: 0)
        return_values: If True, return unique value triplets; if False, return index

    Returns:
        List of tuples (i, j, k) where nums[i] + nums[j] + nums[k] = target
        or value triplets if return_values=True
    """
    n = len(nums)

    if return_values:
        # For value-based deduplication, use a set to track unique triplets
        result_set = set()

        for i in range(n - 2):
            seen = set()
            for j in range(i + 1, n):
                complement = target - nums[i] - nums[j]
                if complement in seen:
                    # Create sorted triplet of values for deduplication
                    triplet = tuple(sorted([nums[i], nums[j], complement]))
                    result_set.add(triplet)
                seen.add(nums[j])

        return list(result_set)
    else:
        # For index-based results with value deduplication
        seen_triplets = set()
        result = []

        for i in range(n - 2):
            seen = {}
            for j in range(i + 1, n):
                complement = target - nums[i] - nums[j]
                if complement in seen:
                    k = seen[complement]
                    # Create sorted triplet of values for deduplication check
                    value_triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    if value_triplet not in seen_triplets:
                        seen_triplets.add(value_triplet)
                        result.append((i, k, j))

                # Only store the first occurrence of each value
                if nums[j] not in seen:
                    seen[nums[j]] = j

        return result


def generate_test_data(n: int, min_val: int = -1000, max_val: int = 1000) -> list[int]:
    """
    Generate random test data for 3Sum algorithms.

    Args:
        n: Number of elements
        min_val: Minimum value
        max_val: Maximum value

    Returns:
        List of random integers
    """
    return [random.randint(min_val, max_val) for _ in range(n)]


def measure_time(func, *args, **kwargs):
    """
    Measure execution time of a function.

    Args:
        func: Function to measure
        *args: Positional arguments for the function
        **kwargs: Keyword arguments for the function

    Returns:
        Tuple of (result, execution_time_in_seconds)
    """
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    return result, end_time - start_time


def test_three_sum():
    """Test function to verify 3Sum implementations work correctly."""
    print("Testing 3Sum implementations...")

    # Test cases
    test_cases = [
        [0, 1, 2, -1, -2],
        [1, 2, 3, 4, 5],
        [-1, 0, 1, 2, -1, -4],
        [0, 0, 0],
        [1, 1, 1],
        [],
    ]

    implementations = [
        ("Brute Force", three_sum_brute_force),
        ("Optimized (Two Pointers)", three_sum_optimized),
        ("Optimized (Hash Set)", three_sum_optimized_with_hash),
    ]

    for test_case in test_cases:
        print(f"\nTest case: {test_case}")

        for name, func in implementations:
            try:
                result, exec_time = measure_time(func, test_case)
                print(f"{name}: {len(result)} triplets found in {exec_time:.6f}s")
                max_display_results = 10
                # Only show results for small cases
                if len(result) <= max_display_results:
                    print(f"  Results: {result}")
            except (ValueError, TypeError, MemoryError) as e:
                print(f"{name}: Error - {e}")


def performance_comparison():
    """Compare performance of different 3Sum implementations."""
    print("\nPerformance Comparison:")
    print("Size\tBrute Force\tOptimized (2P)\tOptimized (Hash)")
    print("-" * 60)

    sizes = [10, 20, 50, 100, 200]
    implementations = [
        ("Brute Force", three_sum_brute_force),
        ("Optimized (Two Pointers)", three_sum_optimized),
        ("Optimized (Hash Set)", three_sum_optimized_with_hash),
    ]

    for size in sizes:
        test_data = generate_test_data(size)
        times = []

        for _name, func in implementations:
            try:
                _result, exec_time = measure_time(func, test_data)
                times.append(exec_time)
            except (ValueError, TypeError, MemoryError):
                times.append(float("inf"))

        print(f"{size}\t{times[0]:.6f}\t{times[1]:.6f}\t{times[2]:.6f}")


if __name__ == "__main__":
    # Set random seed for reproducible results
    random.seed(42)

    test_three_sum()
    performance_comparison()
