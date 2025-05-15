from typing import List


def select_minimal_test_cases(test_cases: List[List[int]]) -> List[int]:
    """
    In software testing, it's often required to select a minimal set of test cases that cover all the requirements.
    You are given a set of test cases and their associated covered requirements.
    Your task is to select the minimal subset of test cases such that all requirements are covered.

    For example, you have the following test cases and requirements they cover:

    test_cases = [
        [1, 2, 3],   # Test case 0 covers requirements 1, 2, 3
        [1, 4],      # Test case 1 covers requirements 1, 4
        [2, 3, 4],   # Test case 2 covers requirements 2, 3, 4
        [1, 5],      # Test case 3 covers requirements 1, 5
        [3, 5]       # Test case 4 covers requirements 3, 5
    ]

    Args:
        test_cases: a list of test cases, where each test case is a list of requirements it covers.
                    Assume each requirement is covered by at least one test case.

    Returns:
        A list of indices of the minimal subset of test cases that covers all requirements
    """

    def generate_combinations(n: int, r: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, path: List[int]):
            if len(path) == r:
                result.append(path[:])
                return
            for i in range(start, n):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result

    # Step 1: gather all requirements
    all_requirements = set()
    for tc in test_cases:
        all_requirements.update(tc)

    n = len(test_cases)

    # Step 2: try combinations of increasing size
    for r in range(1, n + 1):
        for combo in generate_combinations(n, r):
            combined = set()
            for i in combo:
                combined.update(test_cases[i])
            if combined == all_requirements:
                return combo

    return []


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],
        [1, 4],
        [2, 3, 4],
        [1, 5],
        [3, 5]
    ]

    result = select_minimal_test_cases(test_cases)
    print(result)  # Expected output: [2, 3]
