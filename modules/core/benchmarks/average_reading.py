"""Size-scaling input generator for average_reading, used to estimate
empirical time/space complexity. Not part of the task - don't edit."""


def scale_input(n: int) -> tuple:
    return ([float(i) for i in range(1, n + 1)],)
