"""Size-scaling input generator for merge_counts, used to estimate empirical
time/space complexity. Not part of the task - don't edit."""


def scale_input(n: int) -> tuple:
    half = max(n // 2, 1)
    a = {f"k{i}": i for i in range(n)}
    b = {f"k{i}": i for i in range(half, half + n)}
    return (a, b)
