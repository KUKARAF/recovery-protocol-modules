"""Size-scaling input generator for is_palindrome_code, used to estimate
empirical time/space complexity. Not part of the task - don't edit."""


def scale_input(n: int) -> tuple:
    half = "A" * max(n // 2, 1)
    return (half + half[::-1],)
