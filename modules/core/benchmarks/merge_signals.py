"""Size-scaling input generator for merge_signals, used to estimate
empirical time/space complexity. Not part of the task - don't edit."""


def scale_input(n: int) -> tuple:
    return (list(range(n)), list(range(n, 2 * n)))
